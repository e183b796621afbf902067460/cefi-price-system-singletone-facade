from setuptools import setup


with open('README.md', 'r') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

setup(
    name="defi-traders-composite",
    version="1.0",
    author="e183b796621afbf902067460",
    author_email="606d18446a06fe9738fd@gmail.com",
    url="https://github.com/e183b796621afbf902067460/defi-traders-composite",
    packages=['traders'],
    long_description=long_description,
    install_requires=required,
)
