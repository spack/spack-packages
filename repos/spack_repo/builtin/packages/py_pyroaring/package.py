# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyroaring(PythonPackage):
    """An efficient and light-weight ordered set of integers.
    This is a Python wrapper for the C library CRoaring."""

    homepage = "https://github.com/Ezibenroc/PyRoaringBitMap"
    pypi = "pyroaring/pyroaring-1.0.3.tar.gz"

    license("MIT", checked_by="Chrismarsh")

    version("1.0.3", sha256="cd7392d1c010c9e41c11c62cd0610c8852e7e9698b1f7f6c2fcdefe50e7ef6da")

    depends_on("py-setuptools", type="build")
    depends_on("cxx", type="build")
    depends_on("py-cython@3.0.2:", type="build")
