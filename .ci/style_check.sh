#!/bin/bash
set -x
set -e

if [ ! changed_files=$(git diff --name-only --diff-filter=ACMR HEAD^1 | grep ".*\.pyi\?") ]; then
    exit 0  # no changed files
fi

if [ ! -z "$changed_files" ]; then
  echo "Detected changed..."
  for f in ${changed_files[@]}; do
    echo "  $f"
  done
  echo ""

  echo "Running mypy checks..."
  mypy ${changed_files[@]}
  echo ""

  echo "Running black checks..."
  black --check ${changed_files[@]}
fi
