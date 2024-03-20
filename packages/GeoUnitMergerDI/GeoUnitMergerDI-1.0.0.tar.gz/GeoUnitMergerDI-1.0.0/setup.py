#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='GeoUnitMergerDI',
    version='1.0.0',
    url='https://github.com/dataintmx/RiskIndex-GeoMerger',
    description=(
        "DataInt module for merging graph nodes with their neighbors based on their weights. intended for merging geolocations."),
    license='BSD',
    platforms=['linux', 'windows'],
    packages=find_packages(exclude=['Noteboooks*', 'Tests*']),
    #package_dir={'': 'GeoMergerDI'},  # This line tells setuptools where to find packages
    include_package_data=True,
    install_requires=[
       'numpy==1.24.1',
    ],
   
    classifiers=[
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Other/Nonlisted Topic'
    ],
)