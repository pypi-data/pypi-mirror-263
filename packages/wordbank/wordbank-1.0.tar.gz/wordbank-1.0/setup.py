from setuptools import setup, find_packages

setup(
    name="wordbank",
    version='1.0',
    packages=find_packages(),
    package_data={
    },
    install_requires=[
        'nltk',
    ],
)