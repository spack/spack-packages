#!/bin/sh -e
info() { printf "%b%s\n" "\033[1;34m==> \033[0m" "$1"; }
die() { printf "%b%s%b\n" "\033[31;1m==> " "$1" "\033[0m" >&2; exit 1; }
python_files() { git diff --name-only --diff-filter=ACMR -z "$ref" | grep -zE '\.pyi?$'; }

ref="develop"
format_flags="--diff"
check_flags="--no-fix"

while [ $# -gt 0 ]; do
  case "$1" in
    --help|-h)
      echo "$0 [--help] [--fix] [ref]"
      exit 0
      ;;
    --fix)
      format_flags=""
      check_flags="--fix"
      ;;
    -*) die "unknown option: $1" ;;
    *) ref="$1" ;;
  esac
  shift
done

# Ref should always be the merge-base to avoid picking up extra files
ref=$(git merge-base $ref HEAD)

if ! python_files > /dev/null; then
  info "skipping style checks: no Python files changed"
  exit 0
fi
python_files | xargs -0 printf "%s\n"
info "running ruff format"
python_files | xargs -0 -n 100 ruff format $format_flags || error=1
info "running ruff check"
python_files | xargs -0 -n 100 ruff check $check_flags || error=1
[ "$error" = "1" ] && die "style checks failed"
info "style checks passed"
