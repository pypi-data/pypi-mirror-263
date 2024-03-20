import setuptools

with open("README.md", 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fibermat",
    version="1.0",
    author="François Mahé",
    author_email="francois.mahe@ens-rennes.fr",
    description="A mechanical solver to simulate fiber packing and perform statistical analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fmahe/fibermat",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.8"
)
