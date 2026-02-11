# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCodecarbon(PythonPackage):
    """Track emissions from Compute and recommend ways to reduce their
    impact on the environment."""

    homepage = "https://mlco2.github.io/codecarbon/"
    pypi = "codecarbon/codecarbon-3.2.1.tar.gz"

    version("3.2.2", sha256="a848c3960d48312fb527c9565c7dc6264035dc104eb40007564ef0ed4479bb22")
    version("3.2.1", sha256="04571e4d4758936587b7145de557f4aa0f53c83c771318f9a12d67ff039fc95c")

    depends_on("python@3.7:", type=("build", "run"))
    # PEP639 requires setuptools>77, to be upstreamed in codecarbon
    depends_on("py-setuptools@77:", type="build")

    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-fief-client +cli", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pandas@2.3.3:", when="^python@3.14:", type=("build", "run"))
    depends_on("py-prometheus-client", type=("build", "run"))
    depends_on("py-psutil@6:", type=("build", "run"))
    depends_on("py-py-cpuinfo", type=("build", "run"))
    depends_on("py-pydantic", type=("build", "run"))
    depends_on("py-nvidia-ml-py", type=("build", "run"))
    depends_on("py-rapidfuzz", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-questionary", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-typer", type=("build", "run"))
