# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCasadi(PythonPackage):
    """CasADi -- framework for algorithmic differentiation and numeric optimization"""

    homepage = "https://web.casadi.org/"
    pypi = "casadi/casadi-3.6.4.tar.gz"

    license("LGPL")

    version("3.6.7", sha256="21cde87288afebb32a2a035bf6b6a91a025e24ee14aba7a0ae5515707b9887c1")
    version("3.6.4", sha256="affdca1a99c14580992cdf34d247754b7d851080b712c2922ad2e92442eeaa35")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
