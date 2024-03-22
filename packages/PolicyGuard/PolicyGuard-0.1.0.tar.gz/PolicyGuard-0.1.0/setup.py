from setuptools import setup, find_packages

setup(
    name='PolicyGuard',
    version='0.1.0',
    author='Apratim Shukla',
    author_email='apratimshukla6@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/apratimshukla6/PolicyGuard',
    license='Apache',
    description='An automated tool for managing OPA policies.',
    long_description=open('README.md').read(),
    install_requires=[
        'aiohttp',
        'docker'
    ],
    entry_points={
        'console_scripts': [
            'policyguard=policyguard.policyguard:main_wrapper',
        ],
    },
    package_data={'policyguard': ['default/*', 'Dockerfile']},
)