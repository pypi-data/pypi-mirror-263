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
  version='0.0.1',
  description='backlink checker',
  long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read() + '\n\n' + open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.txt')).read(),
  url='',  
  author='mr11robot',
  author_email='taha.youssef.fares@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='backlinks', 
  packages=find_packages(),
  install_requires=['openpyxl','pandas','beautifulsoup4','requests','google-oauth2-tool','google-api-python-client'] 
)
