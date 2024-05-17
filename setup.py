from setuptools import setup
from setuptools import find_packages
import sys

version = '2.3.dev0'

if sys.version_info < (3, 2):
    extra = {
            'z3cform': ['z3c.form',
                        'zope.interface',
                        'zope.component',
                        'zope.schema',
                       ],
      }
else:
    extra = {}

setup(name='htmllaundry',
      version=version,
      description='Simple HTML cleanup utilities',
      long_description=open('README.rst').read() + '\n\n' +
                       open('CHANGES.rst').read(),
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing :: Markup :: HTML',
          ],
      keywords='html clean',
      author='Wichert Akkerman',
      author_email='wichert@wiggy.net',
      url='',
      license='BSD',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'lxml',
          'six',
      ],
      extras_require=extra,
      tests_require='nose>=0.10.0b1',
      test_suite='nose.collector',
      )
