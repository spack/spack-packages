# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySspilib(PythonPackage):
    """SSPI API bindings for Python."""

    homepage = "https://github.com/jborean93/sspilib"
    pypi = "sspilib/sspilib-0.1.0.tar.gz"
    git = "https://github.com/jborean93/sspilib.git"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("0.5.0", sha256="b62f7f2602aa1add0505eee2417e2df24421224cb411e53bf3ae42a71b62fe98")
    version("0.1.0", sha256="58b5291553cf6220549c0f855e0e6973f4977375d8236ce47bb581efb3e9b1cf")

    depends_on("python@3.9:", type=("build", "run"), when="@0.3:")
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-setuptools@77:", type="build", when="@0.3.1:")
    depends_on("py-setuptools@77.0.3:", type="build", when="@0.4:")
    depends_on("py-cython@3", type="build")
    depends_on("py-cython@3.1.3", type="build", when="@0.4")
    depends_on("py-cython@3.2.1", type="build", when="@0.5")
