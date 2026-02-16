# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyExpandvars(PythonPackage):
    """Expand system variables Unix style."""

    homepage = "https://github.com/sayanarijit/expandvars"
    pypi = "expandvars/expandvars-0.12.0.tar.gz"

    license("MIT")

    version("1.1.2", sha256="6c5822b7b756a99a356b915dd1267f52ab8a4efaa135963bd7f4bd5d368f71d7")
    version("1.1.1", sha256="98add8268b760dfee457bde1c17bf745795fdebc22b7ddab75fd3278653f1e05")
    version("0.12.0", sha256="7d1adfa55728cf4b5d812ece3d087703faea953e0c0a1a78415de9df5024d844")

    depends_on("python@3.6.2:", type=("build", "run"), when="@1.1.1:")
    depends_on("python@3:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
