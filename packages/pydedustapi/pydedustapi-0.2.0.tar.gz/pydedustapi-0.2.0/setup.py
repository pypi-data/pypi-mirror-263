from setuptools import setup, find_packages

setup(
    name='pydedustapi',
    version='0.2.0',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/labfunny/py-dedust-api',
    license='MIT',
    author='Max',
    description='A Python library for interacting with the DeDust API',
    classifiers = ['Programming Language :: Python :: 3.6']
)