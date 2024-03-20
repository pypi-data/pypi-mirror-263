from setuptools import setup, find_packages

setup(
    name="PyIPe",
    version="0.1",
    description="A library for retrieving public IP addresses",
    author="twinsszi",
    author_email="adhm90879@email.com",
    packages=find_packages(),
    install_requires=["requests"],
    keywords='ip'
)
