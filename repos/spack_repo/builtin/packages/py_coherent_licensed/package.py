# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCoherentLicensed(PythonPackage):
    """License management tooling for Coherent System and skeleton projects."""

    homepage = "https://github.com/coherent-oss/coherent.licensed"
    pypi = "coherent_licensed/coherent_licensed-0.5.2.tar.gz"

    license("MIT")

    version("0.5.2", sha256="d8071403ce742d3ac3592ddc4fb7057a46caffb415b928b4d52802e5f208416d")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-flit-core@3.11:3", type="build")
