from setuptools import setup, find_packages

VERSION = "0.0.3"
DESCRIPTION = "sample package"

setup(
    name="samplepypackagexxx",
    version=VERSION,
    author="Julian Amin",
    author_email="julian.amin@infor.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=["samplepackage"],
    # classifiers=[
    #     "sample :: sample"
    # ]
)