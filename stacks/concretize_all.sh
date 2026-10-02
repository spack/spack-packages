#!/bin/bash
set -e
set -x

if [[ -d $1 ]]; then
  pushd $1
  shift
fi

stacks=(
  "base"
  "gpu"
  "hpc-libs"
  # "tools"
  "ml"
  # "data-vis-sdk
)

export SPACK_CONCRETE_ENV_DIR=$(realpath $PWD/../../)

for stack in ${stacks[@]}; do
  spack -e $PWD/$stack concretize $@
done

popd
