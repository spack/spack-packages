# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPathsimanalysis(PythonPackage):
    """
    Calculates the geometric similarity of molecular dynamics trajectories using
    path metrics such as the Hausdorff and Fréchet distances.
    """

    homepage = "https://github.com/MDAnalysis/pathsimanalysis"
    pypi = "pathsimanalysis/pathsimanalysis-1.2.0.tar.gz"

    maintainers("LydDeb")

    license("LGPL-2.1-only", checked_by="LydDeb")

    version("1.2.0", sha256="afd63ec143d2ab28a11c4c530f3f8132ed0aec447391f8345f4fe8e68be8ed08")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@40.9.0:", type="build")
    depends_on("py-versioningit", type="build")
    depends_on("py-mdanalysis@2.1.0:", type=("build", "run"))
    depends_on("py-scipy@1.5.0:", type=("build", "run"))
    depends_on("py-matplotlib@1.5.1:", type=("build", "run"))
    depends_on("py-numpy@1.22.3:", type=("build", "run"))
