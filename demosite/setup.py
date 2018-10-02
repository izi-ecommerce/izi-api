"""
A demosite with iziapi for demo and documentation purposes
"""
from setuptools import setup, find_packages
import os

__version__ = "0.0.1"

setup(
    name='iziapi-demosite',
    version=__version__,
    description="Oscar API Demosite",
    long_description=__doc__,
    classifiers=[],
    keywords='',
    author='Martijn Jacobs',
    author_email='martijn@devopsconsulting.nl',
    url='https://github.com/izi-ecommerce/izi-api/demosite',
    license='Copyright',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'izi-api',
        'django>=1.11, <2.1',
        'izi-core>=1.5.1'
    ],
)
