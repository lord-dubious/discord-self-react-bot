from setuptools import setup, find_packages



# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    
    name="discord-self-react-bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="chukwudubem chukwurah",
    author_email="chukwurahdavid@gmail.com",
    description="discord reaction bot",
    url="https://github.com/dubious-senpai/discord-self-react-bot",
      # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown'
)
