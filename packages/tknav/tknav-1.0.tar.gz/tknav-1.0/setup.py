from distutils.core import setup

with open("./README.md", "r", encoding="UTF8") as f:
  long_description = f.read()

setup(
    name="tknav",
    packages=["tknav"],
    version="1.0",  # Ideally should be same as your github release tag varsion
    description="Simple navigation API for tkinter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Adarsh Ravikumar",
    author_email="azracstudios@gmail.com",
    url="https://www.github.com/AzracStudios/tknav",
    download_url="https://github.com/AzracStudios/tknav/releases/download/release/tknav-0.1.0.tar.gz",
    keywords=["tkinter", "nav", "navigation", "tknav"],
    classifiers=[],
)
