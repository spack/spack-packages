# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyChemiscope(PythonPackage):
    """An interactive structure/property explorer for materials and molecules"""

    homepage = "https://chemiscope.org"
    pypi = "chemiscope/chemiscope-0.8.6.tar.gz"

    maintainers("Luthaf", "RMeli")

    license("BSD-3-Clause", checked_by="RMeli")

    version("0.8.6", sha256="d5e9a95f3b6106a281c0c7bfad837aac504052b841b36dee690187cd3545140d")

    # pyproject.toml requires-python
    depends_on("python@3.10:", type=("build", "run"))

    # pyproject.toml [build-system]
    depends_on("py-setuptools", type="build")
    depends_on("py-jupyterlab@4:", type="build")

    # pyproject.toml dependencies
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-ipywidgets@7:8", type=("build", "run"))
