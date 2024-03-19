import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latex_gen_3000",
    version="0.0.2",
    author="AlexandrBon",
    author_email="bon527870@mail.ru",
    description="A small latex generator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexandrBon/latex_gen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)