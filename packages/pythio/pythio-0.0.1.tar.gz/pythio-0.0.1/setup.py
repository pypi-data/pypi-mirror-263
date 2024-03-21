from distutils.core import setup
from setuptools import find_packages


setup(
    name='pythio',
    packages=find_packages(),
    version='0.0.1',
    license='MIT',
    description='python library',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_context_type='text/x-rst',
    author='amirali irvany',
    author_email='dev.amirali.irvany@gmail.com',
    url='https://github.com/metect/pythio',
    keywords=['api', 'telegram'],
    install_requires=['requests'],
)
