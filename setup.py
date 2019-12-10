import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rnavelocity-genericdiff",
    version="0.1.0",
    author="Top Coder Kitty ML",
    author_email="mark.y.lock@gmail.com",
    description="Package for RNA velocity, cell ordering and automatic differentiation",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Topcoder-Kitty-ML/cs207-FinalProject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "pytest",
        "matplotlib"
        ],
    python_requires='>=3.6',
)