# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHighspy(PythonPackage):
    """A thin set of pybind11 wrappers to HiGHS"""

    homepage = "https://github.com/ERGO-Code/HiGHS"
    pypi = "highspy/highspy-1.13.1.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("1.13.1", sha256="7888873501c6ca3e0fa19fee960c8b3cb1c64132c5a9b514903cc7e259b5b0c7")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("cmake@3.15:3.27", type="build")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-scikit-build-core@0.3.3:", type="build")
    depends_on("py-pybind11", type="build")
    depends_on("py-numpy", type=("build", "run"))
