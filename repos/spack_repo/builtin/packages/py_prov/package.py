# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyProv(PythonPackage):
    """A Python library for W3C Provenance Data Model (PROV).

    A library for W3C Provenance Data Model supporting PROV-JSON, PROV-XML and
    PROV-O (RDF)
    """

    homepage = "https://prov.readthedocs.io/"
    pypi = "prov/prov-2.0.0.tar.gz"
    git = "https://github.com/trungdong/prov.git"

    license("MIT")

    version("2.1.1", sha256="7d012b164f5bbb42e118ed9d25788ab012d09082b722bc9dd4e811a309ea57f5")
    version("2.0.0", sha256="b6438f2195ecb9f6e8279b58971e02bc51814599b5d5383366eef91d867422ee")
    version("1.5.1", sha256="7a2d72b0df43cd9c6e374d815c8ce3cd5ca371d54f98f837853ac9fcc98aee4c")

    variant("rdf", default=False, when="@2.0.2:", description="Enable rdf support")
    variant("xml", default=False, when="@2.0.2:", description="Enable xml support")
    variant(
        "dot",
        default=False,
        when="@:2.0.1",
        description="Graphical visualisation support for prov.model",
    )

    depends_on("python@3.9:", type=("build", "run"), when="@2.0.2:")
    depends_on("python@3.6:3", type=("build", "run"), when="@:2.0.1")
    depends_on("py-setuptools@40.8:", type="build", when="@2:")
    depends_on("py-setuptools", type="build")

    depends_on("py-networkx@2:", type=("build", "run"))
    depends_on("py-pydot@1.2:", type=("build", "run"), when="@2.0.2:")
    depends_on("py-python-dateutil@2.2:", type=("build", "run"))
    depends_on("graphviz", type=("build", "run"), when="@2.0.1:")

    depends_on("py-rdflib@4.2.1:6", type=("build", "run"), when="+rdf")
    depends_on("py-rdflib@4.2.1:6", type=("build", "run"), when="@:2.0.1")

    depends_on("py-lxml@3.3.5:", type=("build", "run"), when="+xml")
    depends_on("py-lxml@3.3.5:", type=("build", "run"), when="@:2.0.1")

    # Historical dependencies
    depends_on("py-pydot@1.2:", type=("build", "run"), when="+dot")
    depends_on("graphviz", type=("build", "run"), when="+dot")
