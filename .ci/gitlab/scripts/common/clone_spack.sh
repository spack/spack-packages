#!/bin/sh -e

if [ -d .ci/tmp/spack ]; then
  exit 0
fi

mkdir -p .ci/tmp/spack
cd .ci/tmp/spack
git init
git remote add origin "https://github.com/${SPACK_CHECKOUT_REPO}.git"
git fetch --depth 1 origin "${SPACK_CHECKOUT_VERSION}"
git checkout FETCH_HEAD
