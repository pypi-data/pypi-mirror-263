from setuptools import setup, find_packages

with open("README.md") as fh:
    longdescription = fh.read()

setup(
    name="Promethee",
    version="0.4",
    author="Eduardo Teles, Wilson Freita, Vinícius Oliveira, Gabriel Monteiro, Josef Jaeger",
    description="Promethee algorithm",
    long_description=longdescription,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=['pandas',]
)
