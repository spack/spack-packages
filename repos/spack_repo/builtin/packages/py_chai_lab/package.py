# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyChaiLab(PythonPackage):
    """Chai Discovery tools for AI + protein research."""

    homepage = "https://www.chaidiscovery.com/"
    git = "https://github.com/chaidiscovery/chai-lab.git"
    pypi = "chai_lab/chai_lab-0.6.1.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("0.6.1", sha256="a4ef9737bbb9abfa1dbbd5e059b899fb3b48d6b916f4bf104f5325e1f224e238")

    # pyproject.toml
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hatchling@1.20:", type="build")
    depends_on("py-hatch-requirements-txt", type="build")
    # requirements.in
    # The dependence named "typer-slime" appears in the requirement.in file, but the PyPI page
    # for this package specifies not to install it.
    # Indeed, it does nothing more than depend on "typer".
    depends_on("py-typer@0.12", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-tqdm@4.66:4", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-gemmi@0.6.3:0.6", type=("build", "run"))
    depends_on("rdkit@2024_9_5:2024_9+python", type=("build", "run"))
    depends_on("py-biopython@1.83:", type=("build", "run"))
    depends_on("py-antipickle@0.2.0", type=("build", "run"))
    depends_on("py-tmtools@0.0.3:", type=("build", "run"))
    depends_on("py-modelcif@1.0:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas+parquet", type=("build", "run"))
    depends_on("py-pandera", type=("build", "run"))
    depends_on("py-numba@0.59:", type=("build", "run"))
    depends_on("py-einops@0.8", type=("build", "run"))
    depends_on("py-jaxtyping@0.2.25:", type=("build", "run"))
    depends_on("py-beartype@0.18:", type=("build", "run"))
    depends_on("py-torch@:2.6,2.3.1:", type=("build", "run"))
