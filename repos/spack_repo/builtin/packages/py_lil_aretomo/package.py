# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLilAretomo(PythonPackage):
    """A lightweight Python API for AreTomo."""

    homepage = "https://github.com/teamtomo/lil-aretomo"
    pypi = "lil_aretomo/lil_aretomo-0.1.1.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.1.1", sha256="02ccb0efbf2c06304570117f142e78331bfffdde46864e22de11c6cd7f30f178")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-setuptools-scm@3.4: +toml", type="build")

    depends_on("aretomo", type="run")
