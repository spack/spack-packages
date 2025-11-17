# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGpawData(PythonPackage):
    """Data package for PAW files and other data files for the GPAW DFT code."""

    homepage = "https://gpaw.readthedocs.io/"
    pypi = "gpaw_data/gpaw_data-1.0.1.tar.gz"

    maintainers("alikhamze")

    license("GPL-3.0-or-later", checked_by="alikhamze")

    version("1.0.1", sha256="28212110aa04daae333ef1260b281d70b818ad9cf4282078624ee3fc7a8fc05c")
    with default_args(deprecated=True):
        version("1.0.0", sha256="dabcdc4bb29450b37ed8bece6161d42da4ff609f05e0067a35c7811849e64223")

    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-setuptools", type="build")
