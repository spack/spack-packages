# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyrometheus(PythonPackage):
    """Code generation for combustion thermochemistry, based on Cantera."""

    homepage = "https://pyrometheus.readthedocs.io"
    pypi = "pyrometheus/pyrometheus-1.0.7.tar.gz"
    git = "https://github.com/pyrometheus/pyrometheus.git"

    maintainers("sbryngelson")

    license("MIT")

    version("1.0.7", sha256="fd8e1f95868121ea541bbed94657645f5d636a265be5bfd92bebdf38124b5b28")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("cantera+python@3.1:", type=("build", "run"))
    depends_on("py-mako", type=("build", "run"))
    depends_on("py-pymbolic", type=("build", "run"))
