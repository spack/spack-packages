# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyItables(PythonPackage):
    """Python DataFrames as interactive DataTables."""

    homepage = "https://github.com/mwouts/itables"
    git = "https://github.com/mwouts/itables.git"
    pypi = "itables/itables-2.7.1.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="gLydDeb")

    version("2.7.1", sha256="67f375e773ddf748da2ec2250fd21a242aaa63835b4ebe816840be01bcfa98e8")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
