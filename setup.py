# ./setup.py

from setuptools import setup, find_packages

setup(
    name="vectara-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        
    ],
    extras_require={
        "advanced": [
            torch, transformers, accelerate
        ],
    },
)