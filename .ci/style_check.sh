#!/bin/sh -e
ref="${1:-develop}"

python_files() { git diff --name-only --diff-filter=ACMR -z "$ref" | grep -zE '\.pyi?$'; }
python_files > /dev/null || exit 0
python_files | xargs -0 printf "%s\n"
echo "Running flake8 check"
python_files | xargs -0 -n 100 flake8 || flake_err=1
echo "Running isort check"
python_files | xargs -0 -n 100 isort --check --diff || isort_err=1
echo "Running black check"
python_files | xargs -0 -n 100 black --check --diff --color || black_err=1

if [ $flake_err ] || [ $isort_err ] || [ $black_err ]; then
  exit 1
fi
