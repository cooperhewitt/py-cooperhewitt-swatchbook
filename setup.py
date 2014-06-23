#!/usr/bin/env python

from distutils.core import setup

setup(name='cooperhewitt-swatchbook',
      version='0.1',
      description='Cooper Hewitt's Python tools for wrangling colours',
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/py-cooperhewitt-swatchbook',
      requires=['colorsys', 'webcolors'],
      packages=[
          'cooperhewitt'
      ],
      scripts=[],
      download_url='https://github.com/cooperhewitt/py-cooperhewitt-swatchbook/releases/tag/v0.1',
      license='BSD')
