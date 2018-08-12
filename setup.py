import codecs, os, re

from setuptools import find_packages, setup

def read(*rnames):
    return codecs.open(os.path.join(os.path.dirname(__file__), *rnames), 'r', 'utf-8').read()


setup(
    name='d3-italy',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=read('requirements.txt'),
    author='Michael Sarfati',
    author_email='michael.sarfati@utoronto.ca',
    url='geopolitik.io',
)
