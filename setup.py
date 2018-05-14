#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()

setup(name='cooperhewitt-swatchbook',
      version='0.3',
      description='Cooper Hewitt\'s Python tools for wrangling colours',
      long_description=desc,
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/py-cooperhewitt-swatchbook',
      requires=['colorsys', 'webcolors', 'colormath (<2.0)'],
      install_requires=['webcolors', 'colormath<2.0'],
      packages=packages,
      scripts=[],
      download_url='https://github.com/cooperhewitt/py-cooperhewitt-swatchbook/releases/tag/v0.3',
      license='BSD')
