# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyReferencing(PythonPackage):
    """JSON Referencing + Python."""

    homepage = "https://referencing.readthedocs.io/"
    pypi = "referencing/referencing-0.35.1.tar.gz"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("0.36.2", sha256="df2e89862cd09deabbdba16944cc3f10feb6b3e6f18e902f7cc25609a34775aa")
    version("0.35.1", sha256="25b42124a6c8b632a425174f24087783efb348a6f1e0008e63cd4466fedf703c")

    depends_on("python@3.9:", type=("build", "run"), when="@0.36:")
    depends_on("python@3.8:", type=("build", "run"), when="@:0.35")
    depends_on("py-hatchling", type="build")
    depends_on("py-hatchling@1.26:", when="@0.36:", type="build")
    depends_on("py-hatch-vcs", type="build")

    depends_on("py-attrs@22.2.0:", type=("build", "run"))
    depends_on("py-rpds-py@0.7.0:", type=("build", "run"))
    depends_on("py-typing-extensions@4.4:", type=("build", "run"), when="@0.36.1: ^python@:3.12")
