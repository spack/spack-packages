# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFortdepend(PythonPackage):
    """Automatically generate Fortran dependencies"""

    homepage = "https://github.com/ZedThree/fort_depend.py"
    pypi = "fortdepend/fortdepend-2.3.2.tar.gz"

    license("MIT")

    maintainers("pearzt")

    version("2.3.2", sha256="dfd165659315c284ecff4669e8b84471c6a1580cf42f165bdb3b837ecd6e105c")

    depends_on("py-setuptools", type="build")
    depends_on("py-colorama@0.3.9:", type=("build", "run"))
    depends_on("py-pcpp@1.1.0:", type=("build", "run"))
