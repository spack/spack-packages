# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyReferencing(PythonPackage):
    """JSON Referencing + Python."""

    homepage = "https://referencing.readthedocs.io/"
    pypi = "referencing/referencing-0.35.1.tar.gz"
    git = "https://github.com/python-jsonschema/referencing.git"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("0.37.0", sha256="44aefc3142c5b842538163acb373e24cce6632bd54bdb01b21ad5863489f50d8")
    version("0.36.2", sha256="df2e89862cd09deabbdba16944cc3f10feb6b3e6f18e902f7cc25609a34775aa")
    version("0.35.1", sha256="25b42124a6c8b632a425174f24087783efb348a6f1e0008e63cd4466fedf703c")

    with default_args(type="build"):
        depends_on("py-hatchling")
        depends_on("py-hatchling@1.26:", when="@0.36:")
        depends_on("py-hatch-vcs")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@0.37:")
        depends_on("python@3.9:", when="@0.36:")
        depends_on("python@3.8:", when="@:0.35")

        depends_on("py-attrs@22.2.0:")
        depends_on("py-rpds-py@0.7.0:")
        depends_on("py-typing-extensions@4.4:", when="@0.36.1: ^python@:3.12")
