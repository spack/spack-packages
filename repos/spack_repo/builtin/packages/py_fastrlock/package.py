# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFastrlock(PythonPackage):
    """This is a C-level implementation of a fast, re-entrant,
    optimistic lock for CPython."""

    homepage = "https://github.com/scoder/fastrlock"
    pypi = "fastrlock/fastrlock-0.5.tar.gz"

    license("MIT")

    version("0.8.3", sha256="4af6734d92eaa3ab4373e6c9a1dd0d5ad1304e172b1521733c6c3b3d73c8fa5d")
    version("0.8.1", sha256="8a5f2f00021c4ac72e4dab910dc1863c0e008a2e7fb5c843933ae9bcfc3d0802")

    depends_on("c", type="build")  # generated

    depends_on("py-setuptools", type="build")
    depends_on("py-cython", type="build")
    depends_on("py-cython@3.0.11:3.0", when="@0.8.3", type="build")
    depends_on("py-cython@3.0.0:3.0", when="@0.8.1", type="build")
    # in newer pip versions --install-option does not exist
    depends_on("py-pip", type="build")
    depends_on("py-pip@:23.0", when="@:0.8.1", type="build")

    def install_options(self, spec, prefix):
        if self.spec.satisfies("^py-pip@:23.0"):
            return ["--with-cython"]
        else:
            return []

    def config_settings(self, spec, prefix):
        # pip deprecated --install-option, suggests using --global-option instead
        # in https://github.com/pypa/pip/issues/11859#issuecomment-1741867145
        if self.spec.satisfies("^py-pip@23.1:"):
            return {"--global-option": "--with-cython"}
        else:
            return {}
