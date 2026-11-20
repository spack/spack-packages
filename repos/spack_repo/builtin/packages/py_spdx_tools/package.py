# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySpdxTools(PythonPackage):
    """Python library to parse, validate and create SPDX documents."""

    homepage = "https://github.com/spdx/tools-python"
    pypi = "spdx_tools/spdx_tools-0.8.5.tar.gz"

    maintainers("ebagrenrut")

    license("Apache-2.0")

    version("0.8.5", sha256="be600beb2f762f0116025e05490d399e724f668bef84025a7c421bb266688bdb")

    variant("viz", default=False, description="Support graph generation via networkx")

    with default_args(type="build"):
        depends_on("py-setuptools@61.2:")
        depends_on("py-setuptools-scm@3.4.3: +toml")

    with default_args(type=("build", "run")):
        depends_on("py-beartype")
        depends_on("py-click")
        depends_on("py-license-expression")
        depends_on("py-ply")
        depends_on("py-pyyaml")
        depends_on("py-rdflib")
        depends_on("py-semantic-version")
        depends_on("py-uritools")
        depends_on("py-xmltodict")

        depends_on("py-networkx", when="+viz")
        depends_on("py-pygraphviz", when="+viz")

        depends_on("python@3.10:")
