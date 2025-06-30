#!/bin/bash
set -e

changed_files="$(git diff --name-only --diff-filter=ACMR HEAD^1 | grep ".*\.pyi\?")"
if [ -n "$changed_files" ]; then
  echo "Detected changed..."
  for f in "${changed_files[@]}"; do
    echo "  $f"
  done
  echo ""

  #echo "Running mypy checks..."
  #mypy "${changed_files[@]}"
  #echo ""

  echo "Running black checks..."
  black --check "${changed_files[@]}"
else
  exit 0  # no changed files
fi
