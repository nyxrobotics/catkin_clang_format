#! /usr/bin/env python
# -*- encoding: utf-8 -*-  
# from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup
setup_args = generate_distutils_setup(
    packages=['catkin_format'],
    # scripts=['bin/__init__.py'],
    package_dir={'': 'src'},
    entry_points={
        'catkin_tools.commands.catkin.verbs': [
            # Example from catkin_tools' setup.py:
            # 'list = catkin_tools.verbs.catkin_list:description',
            'format = catkin_format.scripts.catkin_format:description',
        ],
    }
)
setup(**setup_args)

# setup(
#     name = "catkin_format",
#     version = "0.0.1",
#     package_dir = {'': 'src',},
#     scripts=['scripts/catkin_format/__init__.py'],
#     entry_points={
#         'catkin_tools.commands.catkin.verbs': [
#             # Example from catkin_tools' setup.py:
#             # 'list = catkin_tools.verbs.catkin_list:description',
#             'format = catkin_format.scripts.catkin_format:description',
#         ],
#     }
# )
