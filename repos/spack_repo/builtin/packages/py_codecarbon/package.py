# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCodecarbon(PythonPackage):
    """Track emissions from Compute and recommend ways to reduce their
    impact on the environment."""

    homepage = "https://mlco2.github.io/codecarbon/"
    pypi = "codecarbon/codecarbon-3.0.4.tar.gz"

    version("3.0.4", sha256="6f47dd6fa52fd25936b632bf22f85e7df0e8def683d68df55487e0f4e8bd688c")

    depends_on("py-setuptools@61:", type="build")
    depends_on("py-wheel", type="build")

    depends_on("python@3.7:", type=("build", "run"))

    depends_on("arrow", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-fief-client +cli", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-prometheus-client", type=("build", "run"))
    depends_on("py-psutil@6:", type=("build", "run"))
    depends_on("py-py-cpuinfo", type=("build", "run"))
    depends_on("py-pydantic", type=("build", "run"))
    depends_on("py-pynvml", type=("build", "run"))
    depends_on("py-rapidfuzz", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-questionary", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-typer", type=("build", "run"))
