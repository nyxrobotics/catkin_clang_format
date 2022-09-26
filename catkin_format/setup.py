#! /usr/bin/env python
# -*- encoding: utf-8 -*-  
# from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup
setup(
    name='catkin_format',
    version="0.0.1",
    author='nyxrobotics',
    author_email='nyxrobotics01@gmail.com',
    description='Run clang-format and clang-tidy on catkin packages',

    # package_dir={'': 'src'},
    packages=['catkin_format'],

    install_requires=['catkin-pkg'],

    entry_points={
        'catkin_tools.commands.catkin.verbs': [
            'format = src.catkin_format:description'
        ]
    }
)

