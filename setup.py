import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="firecat",
    version="0.1.0a",
    description="Mess with files like a cat.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sayonarahash-bye/firecat",
    author="sayonarahash-bye",
    author_email="miguelmocje@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8"
    ],
    packages=[],
    include_package_data=True,
    install_requires=[]
)