from setuptools import setup, find_packages

with open("README.md") as file:
    description = file.read()

setup(
    name="area-calculator-dci_einherer",
    version="0.0.1",
    author="einherer",
    packages=find_packages(),
    install_requires=[],
    long_description=description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
