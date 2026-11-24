# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyevtk(PythonPackage):
    """EVTK (Export VTK) package allows exporting data to binary VTK files for visualization
    and data analysis."""

    homepage = "https://github.com/pyscience-projects/pyevtk"
    pypi = "pyevtk/pyevtk-1.6.0.tar.gz"

    maintainers("tpadioleau", "xylar")

    license("MIT", checked_by="tpadioleau")

    version("1.6.0", sha256="1f6be7876a3a005c8258861551da4fe7e44ff1a2e7ff2a93d6dc51deedfda5f4")

    depends_on("py-setuptools@42:", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-versioneer", type=("build", "run"))
