#!/bin/sh
ref="${1:-develop}"
if [ ! -d "spack-core" ]; then
  printf "No 'spack-core' dir found, should be a symlink or clone of 'spack/spack'\n" >&2
  exit 1
fi
all_commands_successful=true
check_command() {
  cmd_status=$?
  if [ $cmd_status -ne 0 ]; then
    all_commands_successful=false
  fi
}
python_files() { git diff --name-only --diff-filter=ACMR -z "$ref" | grep -zE '\.pyi?$'; }
python_files > /dev/null || exit 0
python_files | xargs -0 printf "%s\n"
python_files | xargs -0 -n 100 flake8
check_command
python_files | xargs -0 -n 100 isort --check --diff
check_command
python_files | xargs -0 -n 100 black --check --diff --color
check_command
if $all_commands_successful; then
  exit 0
else
  exit 1
fi