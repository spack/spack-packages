# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLogomaker(PythonPackage):
    """Software for creating highly customized sequence logos"""

    homepage = "https://github.com/jbkinney/logomaker"
    pypi = "logomaker/logomaker-0.8.7.tar.gz"

    maintainers("Markus92")

    license("MIT", checked_by="Markus92")

    version("0.8.7", sha256="63783ce6e24449d6f1f01ce29c4ae1b91f6e54bc198e5da40ad18fcd0efc3302")

    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-hatchling", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
