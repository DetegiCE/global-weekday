import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="global-weekday-DetegiCE", # Replace with your own username
    version="1.0.0",
    author="DetegiCe",
    author_email="martino1103@gmail.com",
    description="Convert date to weekday in global languages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DetegiCE/global-weekday",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)