# -----------------------------------------------------------------------------
# PantryPy
# Copyright (c) 2023 Felipe Amaral dos Santos
# Licensed under the MIT License (see LICENSE file)
# -----------------------------------------------------------------------------

from setuptools import setup
import yaml

with open('requirements.txt', 'r') as file:
    requirements = file.readlines()

with open('metadata.yaml', 'r') as file:
    metadata = yaml.safe_load(file)

setup(
    name=metadata['name'],
    version=metadata['version'],
    description=metadata['description'],
    long_description=metadata['long_description'],
    author=metadata['author'],
    author_email=metadata['author_email'],
    license=metadata['license'],
    keywords=metadata['keywords'],
    packages=['pantrypy']
)
