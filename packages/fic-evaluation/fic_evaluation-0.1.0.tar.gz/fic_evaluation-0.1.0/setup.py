from io import open

from setuptools import find_packages, setup

setup(
    name="fic_evaluation",
    version="0.1.0",
    author="Aviv Slobodkin, Ori Shapira, Ran Levy, Ido Dagan",
    author_email="lovodkin93@gmail.com",
    description="PyTorch implementation of the highlights faithfulness and coverage metrics for the Fusion-in-Context task",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="fusion NLP deep learning metric",
    license="Apache License (2.0)",
    url="https://github.com/fusereviews/fic_evaluation",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "torch>=2.1.0",
        "tqdm>=4.66.1",
        "transformers>=4.34.1",
        "numpy",
        "requests",
        "tqdm>=4.31.1",
        "spacy>=3.7.2",
        "accelerate>=0.24.0",
        "packaging>=20.9"
    ],
    include_package_data=True,
    python_requires=">=3.11",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)