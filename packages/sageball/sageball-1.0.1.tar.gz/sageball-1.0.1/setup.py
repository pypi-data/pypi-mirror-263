from distutils.core import setup
from setuptools import find_packages
with open("README.rst", "r") as f:
  long_description = f.read()
setup(name='sageball',
      version='1.0.1',
      description='A small extension package for SageMath',
      long_description=long_description,
      author='pikaball',
      author_email='whitesworder@gmail.com',
      url='https://github.com/pikaball/Sageball',
      install_requires=[],
      license='BSD License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3'
      ],
      )