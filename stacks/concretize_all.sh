#!/bin/bash
set -e
set -x

if [[ -d $1 ]]; then
  pushd $1
  shift
fi


os
target

stacks=(
  "hpc-libs"
  "gpu"
  # "tools"
  "ml"
  # "data-vis-sdk
)

if [ -z $SPACK_CONCRETE_ENV_DIR ]; then
  export SPACK_CONCRETE_ENV_DIR=$(realpath $PWD/../../)
fi

# Concretize the base
# This provides all compilers and toolchains needed for other stacks
spack -e $PWD/base concretize $@

spack isolate --path $PWD
for stack in ${stacks[@]}; do
  spack -e $PWD/$stack concretize $@
done

popd
