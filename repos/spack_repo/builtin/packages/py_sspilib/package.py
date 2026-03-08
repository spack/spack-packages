# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySspilib(PythonPackage):
    """SSPI API bindings for Python."""

    homepage = "https://github.com/jborean93/sspilibi"
    pypi = "sspilib/sspilib-0.1.0.tar.gz"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("0.5.0", sha256="b62f7f2602aa1add0505eee2417e2df24421224cb411e53bf3ae42a71b62fe98")
    version("0.4.0", sha256="b482b3be8dc30e086f89e13831139129c022f90f6e7c0603b3c60209d9a4561d")
    version("0.3.1", sha256="6df074ee54e3bd9c1bccc84233b1ceb846367ba1397dc52b5fae2846f373b154")
    version("0.2.0", sha256="4d6cd4290ca82f40705efeb5e9107f7abcd5e647cb201a3d04371305938615b8")
    version("0.1.0", sha256="58b5291553cf6220549c0f855e0e6973f4977375d8236ce47bb581efb3e9b1cf")

    depends_on("py-setuptools@61:", type="build")
    depends_on("py-cython@3", type=("build", "run"))
