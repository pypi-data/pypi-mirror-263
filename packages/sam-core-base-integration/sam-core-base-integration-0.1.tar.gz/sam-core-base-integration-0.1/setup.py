from setuptools import setup, find_packages

print('Paquetes:',find_packages())

setup(
    name='sam-core-base-integration',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ]
)
