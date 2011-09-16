import os
from setuptools import setup, find_packages

setup(
    name='plustoys',
    description='Django app to create Google+ user-badges as embeddable web widgets',
    keywords='django, django project, website',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    version="0.1",
    author="Matteo Scotuzzi",
    author_email="matteo.scotuzzi@gmail.com",
    classifiers = ['Framework :: Django',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                   ],
    url="https://github.com/scotu/plustoys_powazord_com",
    license="MIT",
    platforms=["all"],
)
