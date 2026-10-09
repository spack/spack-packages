# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTensorstore(PythonPackage):
    """Read and write large, multi-dimensional arrays."""

    homepage = "https://github.com/google/tensorstore"
    pypi = "tensorstore/tensorstore-0.1.54.tar.gz"

    license("Apache-2.0")

    version("0.1.85", sha256="26698bded0278e98e0988eb8f7d76ad248762afc5f55a38b9122ffd1474e505f")
    version("0.1.76", sha256="ed0d565e7a038a84b1b5b5d9f7397caec200b53941d8889f44b7f63dd6abffe7")
    version("0.1.54", sha256="e1a9dcb0be7c828f752375409537d4b39c658dd6c6a0873fe21a24a556ec0e2a")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")

        depends_on("py-setuptools@64:", when="@0.1.70:")
        depends_on("py-setuptools@30.3:")
        depends_on("py-setuptools-scm@8.1:", when="@0.1.63:")
        depends_on("py-setuptools-scm")

        # Bazel tends to be backwards-compatible within major versions
        # .bazelversion
        depends_on("bazel@8.5.1:8", when="@0.1.82:")
        depends_on("bazel@7.6.1.0:7", when="@0.1.76")
        depends_on("bazel@6.4.0:6", when="@:0.1.67")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:", when="@0.1.79:")
        depends_on("python@3.9:")

        depends_on("py-numpy@1.22:", when="@0.1.61:")
        depends_on("py-numpy@1.16:")
        depends_on("py-ml-dtypes@0.5:", when="@0.1.75:")
        depends_on("py-ml-dtypes@0.3.1:")

    def patch(self):
        # Trick bazelisk into using the Spack-installed copy of bazel
        symlink(bazel.path, join_path("tools", "bazel"))

    def flag_handler(self, name, flags):
        if name == "cflags" and self.spec.satisfies("@:0.1.76 %gcc@15:"):
            flags.append("-std=gnu18")
        return (flags, None, None)
