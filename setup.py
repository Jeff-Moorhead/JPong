from setuptools import setup, find_packages

setup(
    name="PyPong",
    description="A simple Pong game written with Pygame",
    packages=find_packages(),
    author="Jeff Moorhead",
    author_email="Jeff.Moorhead1@gmail.com",
    entry_points = {
        "console_scripts": [
            "pong=pong.pong:main"
            ]
        }
)
