# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

with open('README.md') as readme:
    long_description = readme.read()

INSTALL_REQUIRES = [
    'django',
    'django-extensions',
    'six',
]

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
]

setup(
    name='vpms',
    version='XXX',
    author='Moshe Nahmias',
    author_email='Moshe Nahmias <moshegrey@gmail.com>',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/moshe742/vpms',
    license='AGPLv3+',
    description='XXX',
    long_description=long_description,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
)
