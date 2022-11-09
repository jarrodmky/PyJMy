@cls
@echo off

py -m pip install -U pip
py -m pip install -U mypy
py -m mypy --disallow-incomplete-defs --no-incremental --cache-dir=nul .
