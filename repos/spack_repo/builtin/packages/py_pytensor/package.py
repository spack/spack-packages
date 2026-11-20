# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytensor(PythonPackage):
    """Optimizing compiler for evaluating mathematical expressions on CPUs and
    GPUs."""

    homepage = "https://github.com/pymc-devs/pytensor"
    pypi = "pytensor/pytensor-3.3.2.tar.gz"

    license("BSD-3-Clause")

    version("3.3.2", sha256="6d340a333ff6bfb2f7962a1d7647ab64225518073b9f49f53590db763ed81fa2")
    version("2.31.7", sha256="0af99e240c95bc0223886eefb4343b0e9dc6fba349b70b107b3a6fbb9cb66409")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("py-cython")
        depends_on("py-versioneer+toml@0.29")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:3.14", when="@3.3.2")
        depends_on("python@3.10:3.13", when="@2.31.7")

        depends_on("py-setuptools@59:")
        depends_on("py-scipy@1")
        depends_on("py-filelock@3.15:")

        depends_on("py-numpy@2:", when="@3.3.2")
        depends_on("py-numba@0.58:0.67", when="@3.3.2")

        depends_on("py-cons", when="@2.31.7")
        depends_on("py-etuples", when="@2.31.7")
        depends_on("py-logical-unification", when="@2.31.7")
        depends_on("py-minikanren", when="@2.31.7")
        depends_on("py-numpy@1.17:", when="@2.31.7")
