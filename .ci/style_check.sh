#!/bin/sh -e
ref="${1:-develop}"
if [ ! -d "spack-core" ]; then
  printf "No 'spack-core' dir found, should be a symlink or clone of 'spack/spack'\n" >&2
  exit 1
fi
python_files() { git diff --name-only --diff-filter=ACMR -z "$ref" | grep -zE '\.pyi?$'; }
python_files > /dev/null || exit 0
python_files | xargs -0 printf "%s\n"
python_files | xargs -0 -n 100 flake8
python_files | xargs -0 -n 100 isort --check --diff
python_files | xargs -0 -n 100 black --check --diff --color
