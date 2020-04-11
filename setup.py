from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

VERSION = '0.0.9'

setup(
    name="mkdocs-rebalance-theme",
    version=VERSION,
    url='https://github.com/kubilus1/mkdocs-rebalance-theme',
    license='GPL',
    description='Rebalance theme for mkdocs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Matt Kubilus',
    author_email='mattkubilus@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'rebalance = rebalance',
        ]
    },
    zip_safe=False
)
