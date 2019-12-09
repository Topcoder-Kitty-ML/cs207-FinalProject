import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="genericdiff-topcoderkitty", # Replace with your own username
    version="0.0.1",
    author="Top Coder Kitty ML",
    author_email="mark.y.lock@gmail.com",
    description="Package for automatic differentiation",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Topcoder-Kitty-ML/cs207-FinalProject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)