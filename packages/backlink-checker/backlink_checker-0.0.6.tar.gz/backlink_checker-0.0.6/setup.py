import os
from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='backlink_checker',
  version='0.0.6',
  description='backlink checker',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='',  
  author='mr11robot',
  author_email='taha.youssef.fares@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='backlinks', 
  packages=find_packages(),
  install_requires=['openpyxl','pandas','beautifulsoup4','requests','google-oauth2-tool','google-api-python-client'], 
)
