# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFastobo(PythonPackage):
    """A parser for the OBO (Open Biomedical Ontologies) file format."""

    homepage = "https://fastobo.readthedocs.io"
    pypi = "fastobo/fastobo-0.14.1.tar.gz"

    license("MIT")

    version("0.14.1", sha256="a230d780581332d041db29299f6c1b960b0228285d8de9981364540c14d069bc")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-maturin@1.2:1", type="build")
