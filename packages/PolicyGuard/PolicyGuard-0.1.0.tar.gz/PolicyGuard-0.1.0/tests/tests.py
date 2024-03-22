import unittest
from unittest.mock import patch, MagicMock, AsyncMock
from policyguard import PolicyGuard
from aiohttp import ClientResponse
import asyncio


class TestPolicyGuard(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.pg = PolicyGuard()

    async def test_send_policy_request_network(self):
        # Create a mock response object with the expected properties
        mock_response = MagicMock(spec=ClientResponse)  # Use spec to ensure it behaves like a ClientResponse
        mock_response.status = 200
        mock_response.json = MagicMock(return_value=asyncio.Future())
        mock_response.json.return_value.set_result({"result": True})
        
        # Patch the post method to return a context manager that mimics the actual behavior
        with patch('policyguard.policyguard.aiohttp.ClientSession.post', return_value=AsyncMock(return_value=mock_response)) as mocked_post:
            input_json = {
                "source_ip": "127.0.0.1",
                "headers": [["Authorization", "My Token"], ["Content-Type", "application/json"]],
                "method": "POST"
            }
            result = await self.pg.send_policy_request("network", {"input": input_json})

            self.assertEqual(result, {"result": True})
            # Ensure the mock was awaited and called with the correct arguments
            mocked_post.assert_awaited_with(url, json=input_json)

if __name__ == '__main__':
    unittest.main()
