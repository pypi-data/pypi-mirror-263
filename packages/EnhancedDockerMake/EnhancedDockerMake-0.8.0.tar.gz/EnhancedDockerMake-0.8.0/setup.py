from setuptools import setup
from dockermake import __version__

with open("requirements.txt", "r") as reqfile:
    requirements = [x.strip() for x in reqfile if x.strip()]

setup(
    name="EnhancedDockerMake",
    version=__version__,
    packages=["dockermake"],
    license="Apache 2.0",
    author="b32147",
    python_requires=">=3.9",
    author_email="avirshup@gmail.com",
    description="Build manager for docker images",
    url="https://github.com/b32147/dockermake",
    entry_points={"console_scripts": ["docker-make = dockermake.__main__:main"]},
    install_requires=["termcolor", "docker>=4", "pyyaml>=5", "jinja2"],
)
