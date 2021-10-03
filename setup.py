
from setuptools import setup

setup(name='street_address_parser_api',
      version='0.1',
      description='Street Address Parser API for QGIS plugin',
      url='https://github.com/tamos/qgis-street-address-parser-api/blob/main/api.py',
      author='Tyler Amos',
      author_email='tyler.amos@alumni.carleton.ca',
      license='GPLv3',
      zip_safe=False,
      install_requires=['torch', 'deepparse', 'flask', 'flask_restful'],
      entry_points = {
          'console_scripts': ['street_address_parser_api=street_address_parser_api.api:main'],
      })
