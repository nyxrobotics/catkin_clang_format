#! /usr/bin/env python
# -*- encoding: utf-8 -*-
import sys

def prepare_arguments(parser):
    parser.description = """\
Format one or more packages in a catkin workspace.
"""
    add = parser.add_argument
    # What packages to build
    pkg_group = parser.add_argument_group('Packages', 'Control which packages get built.')
    add = pkg_group.add_argument
    add('packages', metavar='PKGNAME', nargs='*',
        help='Workspace packages to build, package dependencies are built as well unless --no-deps is used. '
             'If no packages are given, then all the packages are built.')
    add('--this', dest='build_this', action='store_true', default=False,
        help='Build the package containing the current working directory.')
    add('--no-deps', action='store_true', default=False,
        help='Only build specified packages, not their dependencies.')
    add('--unbuilt', action='store_true', default=False,
        help='Build packages which have yet to be built.')
    add('packages', nargs='*',
        help='Workspace packages to build, package dependencies are built as well unless --no-deps is used. '
             'If no packages are given, then all the packages are built.')
    add('--no-deps', action='store_true', default=False,
        help='Only build specified packages, not their dependencies.')
    return parser

def main(opts):
    # Load the context
    ctx = Context.load(opts.workspace, opts.profile, load_env=False)
    if not ctx:
        sys.exit(clr("@{rf}ERROR: Could not determine workspace.@|"))

    log("[format] Start Catkin Format")
    return 0
