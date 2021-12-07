#! /usr/bin/env python
# -*- encoding: utf-8 -*-
from .cli import main
from .cli import prepare_arguments

description = dict(
    verb='format',
    description="Format files with Clang-Tidy and ClangFormat",
    main=main,
    prepare_arguments=prepare_arguments,
)
