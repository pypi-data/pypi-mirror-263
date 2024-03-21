from setuptools import setup, find_packages

setup(
  name='VLoDVP',
  version='1.0.8',
  description='Validating Licenses on Discord Validating Package',
  url='https://github.com/t-a-g-o/vlod',  
  author='tago',
  license='MIT',
  packages=find_packages(),
  install_requires= ['cryptography', 'requests']
)