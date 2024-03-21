from setuptools import setup, find_packages

setup(
    name='kpisQueryGeneration',
    version='0.1.6',
    packages=find_packages(),
    install_requires=[
        'jinjasql==0.1.7',
        'Jinja2==3.0.2',
    ],)

