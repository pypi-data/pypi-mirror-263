import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsbix",
    version="0.1",
    author="veoh",
    author_email="zfq@tuta.io",
    description="API für DSBMobile via tesseract.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zfqtim/dsbix",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)