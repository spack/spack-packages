# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTensorstore(PythonPackage):
    """Read and write large, multi-dimensional arrays."""

    homepage = "https://github.com/google/tensorstore"
    pypi = "tensorstore/tensorstore-0.1.84.tar.gz"

    license("Apache-2.0")

    version("0.1.84", sha256="3cb091dfde68600e6d8f03a389ccc92ffa7c0798a0c600d1013c0138d7163e6b")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # .bazelversion specifies the minimum required version of Bazel.
    # To not have to bump this every time the minimum required version of
    # Bazel is increased and minimize the amount of bazel version churn,
    # we depend on the most recent version which we can support in spack.
    depends_on("bazel@8.7.0:", type="build")

    with default_args(type="build"):
        depends_on("py-setuptools@30.3:")
        depends_on("py-setuptools-scm")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:")
        depends_on("py-numpy@1.16:")
        depends_on("py-ml-dtypes@0.3.1:")

    def patch(self):
        # Trick bazelisk into using the Spack-installed copy of bazel
        symlink(bazel.path, join_path("tools", "bazel"))
