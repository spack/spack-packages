# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPy2bit(PythonPackage):
    """A package for accessing 2bit files using lib2bit."""

    pypi = "py2bit/py2bit-0.2.1.tar.gz"

    license("MIT")

    version("0.3.3", sha256="264f5bfc39d729f1acad54c760ac04fa8a20d4184f4b505d9c333d2e03253770")
    version("0.3.0", sha256="450555c40cba66957ac8c9a4b6afb625fb34c4bb41638de78c87661ff8b682ef")
    version("0.2.1", sha256="34f7ac22be0eb4b5493063826bcc2016a78eb216bb7130890b50f3572926aeb1")

    depends_on("c", type="build")  # generated

    patch("https://salsa.debian.org/med-team/python-py2bit/-/commit/fefc9d02c2a1a81f5cfe9c05e55f0fbf9a8b398a.patch", sha256="09039112ae2ca3e344b4dbb93e79e786a5c6dcfd9a22d46505b78459c7954f0f", when="@0.3:0.3.1 %gcc@14:")

    depends_on("py-setuptools", type="build")
