
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(name="pdf_scrap",
version = "1.3",
description="This package extracts important keywords from a pdf document!!!",
long_description =long_description,
long_description_content_type="text/markdown",
author="Poorvi Prajapati",
packages=['pdf_scrap'],
install_requires=["nltk","scikit-learn","PyPDF2"])