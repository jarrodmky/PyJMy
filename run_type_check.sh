#!/bin/sh

python3.10 -m pip install -U pip
python3.10 -m pip install -U mypy
python3.10 -m mypy --disallow-incomplete-defs --no-incremental --cache-dir=/dev/null .
