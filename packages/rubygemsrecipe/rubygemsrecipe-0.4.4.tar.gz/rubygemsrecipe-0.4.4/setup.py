#!/usr/bin/env python

import os
import sys

from setuptools import setup

version = '0.4.4'
name = 'rubygemsrecipe'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

test_requires=['mock']
if sys.version_info < (3,4):
    test_requires.append('pathlib')

setup(name=name,
      version=version,
      description="zc.buildout recipe for installing ruby gems.",
      long_description=(read('README.rst') + '\n' + read('CHANGES.rst')),
      author='Mantas Zimnickas',
      author_email='sirexas@gmail.com',
      url='https://lab.nexedi.com/nexedi/rubygemsrecipe',
      license='GPL',
      py_modules=['rubygems'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'six',
          'zc.buildout',
          'setuptools',
          'slapos.recipe.build>=0.57',
      ],
      extras_require={
          'test': test_requires
      },
      entry_points={
          'zc.buildout': ['default = rubygems:Recipe']
      },
      classifiers=[
          'Framework :: Buildout',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Topic :: Software Development :: Libraries :: Ruby Modules',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ])
