from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="mkdocs-rebalance-theme",
    version=VERSION,
    url='https://github.com/kubilus1/mkdocs-rebalance-theme',
    license='GPL',
    description='Rebalance theme for mkdocs',
    author='Matt Kubilus',
    author_email='mattkubilus@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'themename = rebalance',
        ]
    },
    zip_safe=False
)
