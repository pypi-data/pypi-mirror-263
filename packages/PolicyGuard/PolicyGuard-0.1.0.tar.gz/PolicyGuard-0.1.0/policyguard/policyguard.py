import argparse
import aiohttp
import asyncio
import logging
import docker
import os
from zipfile import ZipFile
from io import BytesIO
import json
from importlib.resources import files
from asyncio import get_event_loop

logger = logging.getLogger("PolicyGuard")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

async def async_log_info(message):
    loop = get_event_loop()
    await loop.run_in_executor(None, logger.info, message)

async def async_log_error(message):
    loop = get_event_loop()
    await loop.run_in_executor(None, logger.error, message)

class PolicyGuard:
    def __init__(self):
        self.client = docker.from_env()

    async def send_policy_request(self, policy_name, input_json):
        url = f"http://localhost:8181/v1/data/policyguard/{policy_name}/{policy_name}_enforced"
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=input_json) as response:
                if response.status == 200:
                    response_json = await response.json()
                    await async_log_info(f"Response from {policy_name} policy: {json.dumps(response_json['result'], indent=2)}")
                    return response_json
                else:
                    await async_log_error(f"Failed to get response for {policy_name} policy. HTTP Status: {response.status}")
                    return None

    async def download_and_extract_policies(self, url, extract_to='policies'):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.read()
                    zip_file = ZipFile(BytesIO(data))
                    zip_file.extractall(extract_to)
                    await async_log_info(f"Policies extracted to {extract_to}/")
                else:
                    await async_log_error("Failed to download the policies.")

    def image_exists(self, image_tag):
        images = self.client.images.list(name=image_tag)
        return len(images) > 0

    def get_container(self, image_tag):
        containers = self.client.containers.list(all=True, filters={"ancestor": image_tag})
        if containers:
            return containers[0]
        return None

    def policies_directory_to_use(self):
        policies_dir = os.path.join(os.getcwd(), 'policies')
        default_policies_dir = files('policyguard').joinpath('default').as_posix()

        if os.path.isdir(policies_dir) and os.listdir(policies_dir):
            return policies_dir, False
        else:
            return default_policies_dir, True

    async def start_opa_container_with_policies(self, image_tag="opa_policy_image", host_port=8181):
        policies_dir, used_default = self.policies_directory_to_use()

        if used_default:
            await async_log_info("No downloaded policies found. Using default policies.")

        if not self.image_exists(image_tag):
            await async_log_info(f"Building Docker image {image_tag}...")
            self.client.images.build(path='.', tag=image_tag)
        else:
            await async_log_info(f"Docker image {image_tag} already exists. Skipping build.")

        existing_container = self.get_container(image_tag)

        if existing_container:
            if existing_container.status == 'running':
                await async_log_info(f"Stopping existing PolicyGuard OPA container (ID: {existing_container.id}) to update configuration...")
                existing_container.stop()
                existing_container.remove()
                await async_log_info("Existing container stopped and removed.")

        await async_log_info("Starting PolicyGuard OPA container with updated configuration...")
        container = self.client.containers.run(image_tag, ports={'8181/tcp': host_port}, detach=True, volumes={os.path.abspath(policies_dir): {'bind': '/app/policies', 'mode': 'rw'}}, restart_policy={"Name": "no"})

        start_opa_cmd = "opa run --server --log-level=info /app/policies"
        container.exec_run(start_opa_cmd, detach=True)

        await async_log_info(f"Container {container.id} restarted. PolicyGuard OPA server is accessible on port {host_port}")

async def main():
    pg = PolicyGuard()
    parser = argparse.ArgumentParser(description="Manage OPA policies and container")
    parser.add_argument("command", choices=["download", "start", "send"], help="Command to execute")
    parser.add_argument("--url", help="URL for downloading policies (required for download)")
    parser.add_argument("--policy", help="Policy name for request (use 'all' for all policies)")
    parser.add_argument("--input", help="JSON input file for policy request")

    args = parser.parse_args()

    if args.command == "download" and args.url:
        await pg.download_and_extract_policies(args.url)
    elif args.command == "start":
        await pg.start_opa_container_with_policies()
    elif args.command == "send" and args.policy and args.input:
        with open(args.input, 'r') as input_file:
            input_json = json.load(input_file)
            if args.policy.lower() == 'all':
                for policy_name in input_json:
                    await pg.send_policy_request(policy_name, input_json[policy_name])
            else:
                await pg.send_policy_request(args.policy, input_json[args.policy])

def main_wrapper():
    asyncio.run(main())

if __name__ == "__main__":
    main_wrapper()
