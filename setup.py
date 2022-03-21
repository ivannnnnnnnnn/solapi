from setuptools import find_packages, setup

setup(
    name='solapi',
    packages=find_packages(),
    version='0.0.5',
    description='Python wrap for solana NFT marketplaces such as MagicEden and Solanart',
    author='ivan.srshtn.crypto@gmail.com',
    license='MIT',
    install_requires=[
        'requests==2.26.0'
    ]
)
