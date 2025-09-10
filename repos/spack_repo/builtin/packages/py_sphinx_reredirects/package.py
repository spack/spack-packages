# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PySphinxReredirects(PythonPackage):
    """Extension for Sphinx that handles redirects for moved pages."""

    homepage = "https://documatt.com/sphinx-reredirects/"
    pypi = "sphinx_reredirects/sphinx_reredirects-1.0.0.tar.gz"

    license("MIT", checked_by="alecbcs")

    version("1.0.0", sha256="7c9bada9f1330489fcf4c7297a2d6da2a49ca4877d3f42d1388ae1de1019bf5c")

    depends_on("python@3.11:", type=("build", "run"))

    depends_on("py-flit-core@3.2:3", type="build")

    depends_on("py-sphinx@7.4:8", type=("build", "run"))
