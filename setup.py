"""
install:
$ python setup.py install pkg_temp

uninstall
$ pip uninstall pkg_temp
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pkg_temp",  # Replace with your own username
    version="0.1.0",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/", # github repo for your package
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    dependency_links=[],  # httpl inks where package can be downloaded
    install_requires=[],  # package names that is available in pip
)