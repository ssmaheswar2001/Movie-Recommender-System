from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

AUTHOR_NAME = "Surya Sai Maheswar Budidi"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_NAME,
    author_email="ssmaheswar2001@gmail.com",
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package =[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)