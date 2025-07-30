#!/bin/sh -e
info() { printf "%b%s\n" "\033[1;34m==> \033[0m" "$1"; }
die() { printf "%b%s%b\n" "\033[31;1m==> " "$1" "\033[0m" >&2; exit 1; }
python_files() { git diff --name-only --diff-filter=ACMR -z "$ref" | grep -zE '\.pyi?$'; }

ref="develop"
flags="--check --diff"

while [ $# -gt 0 ]; do
  case "$1" in
    --help|-h)
      echo "$0 [--help] [--fix] [ref]"
      exit 0
      ;;
    --fix) flags= ;;
    -*) die "unknown option: $1" ;;
    *) ref="$1" ;;
  esac
  shift
done
if ! python_files > /dev/null; then
  info "skipping style checks: no Python files changed"
  exit 0
fi
[ -d "spack-core" ] ||  die "no 'spack-core' dir found: should be a clone of 'spack/spack'"
python_files | xargs -0 printf "%s\n"
info "running flake8"
python_files | xargs -0 -n 100 flake8 || error=1
info "running isort"
python_files | xargs -0 -n 100 isort $flags || error=1
info "running black"
python_files | xargs -0 -n 100 black --color $flags || error=1
[ "$error" = "1" ] && die "style checks failed"
info "style checks passed"
