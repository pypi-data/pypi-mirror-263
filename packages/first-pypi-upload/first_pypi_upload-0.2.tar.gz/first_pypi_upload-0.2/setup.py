from setuptools import setup, find_packages

setup(
    name="first_pypi_upload",
    version="0.2",
    description="A simple password generator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nick Koscinski",
    author_email="ndkoscinski@gmail.com",
    url="https://github.com/nkoscinski/basic-pwd-generator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
