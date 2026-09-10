# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWaterdynamics(PythonPackage):
    """
    Analysis of water dynamics in molecular dynamics trajectories and water
    interactions with other molecules.
    """

    homepage = "https://github.com/MDAnalysis/waterdynamics"
    pypi = "waterdynamics/waterdynamics-1.2.0.tar.gz"

    maintainers("LydDeb")

    license("LGPL-2.1-only", checked_by="LydDeb")

    version("1.2.0", sha256="ab87ca22c46db71cf72b2c5534fbd062fd853d999cee9c10587932217cd40c96")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@40.9.0:", type="build")
    depends_on("py-versioningit", type="build")
    depends_on("py-mdanalysis@2.1.0:", type=("build", "run"))
    depends_on("py-numpy@1.22.3:", type=("build", "run"))
