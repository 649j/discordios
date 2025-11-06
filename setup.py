"""Setup file for DiscordiOS"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="discordios",
    version="1.0.0",
    author="B3nderServices",
    author_email="",
    description="Make your Discord bot appear as a mobile device",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/B3nderServices/DiscordiOS",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "discord.py>=2.0.0",
    ],
    keywords="discord bot mobile ios android",
)
