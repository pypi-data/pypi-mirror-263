from setuptools import setup, find_packages

setup(
    name='kalamari-cli',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kalamari=main:main',
        ],
    },
    author='Sentou Technologies',
    author_email='eito@sentou.tech',
    description='Kalamari CLI tool for smart contract management and development.',
    install_requires=[
        'argparse',
        'sys',
    ],
)