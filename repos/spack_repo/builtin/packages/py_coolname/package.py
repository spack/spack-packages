# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCoolname(PythonPackage):
    """Random name and slug generator."""

    homepage = "https://github.com/alexanderlukanin13/coolname"
    pypi = "coolname/coolname-2.2.0.tar.gz"

    version("2.2.0", sha256="6c5d5731759104479e7ca195a9b64f7900ac5bead40183c09323c7d0be9e75c7")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
