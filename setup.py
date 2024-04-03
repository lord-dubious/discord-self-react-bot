from setuptools import setup, find_packages

setup(
    with open("README.md", "r") as fh:
    long_description = fh.read()
    name="discord-self-react-bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="chukwudubem chukwurah",
    author_email="chukwurahdavid@gmail.com",
    description="discord reaction bot",
    url="https://github.com/dubious-senpai/discord-self-react-bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
