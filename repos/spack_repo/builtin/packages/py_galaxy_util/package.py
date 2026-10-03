# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGalaxyUtil(PythonPackage):
    """Galaxy Generic Utilities"""

    homepage = "https://github.com/galaxyproject/galaxy"
    pypi = "galaxy-util/galaxy-util-22.1.2.tar.gz"

    license("CC-BY-3.0")

    version("24.0.0", sha256="00d0e4e0fb71004c7416cca6cb6a7cab2fd63956ac8d3cb4426effbe0c7027fc")
    version("23.2.1", sha256="1b57991187fb44201acab6a96dbf6205d74a700e304f0bfbb336c51c8af35204")
    version("23.1.4", sha256="8209c79728707f105ba698c1a7aded41de15dc5af47942f351f73a35ade54911")
    version("23.1.3", sha256="7f03c02726d3f72dc8ccd28dd25773ab93fee641e2f7e1166a20a6914623d70e")
    version("23.1.2", sha256="0089f4c28bae20b961ceb11eae3b5c93ca3fac5e02090d58de40cfd0e12e9f07")
    version("23.1.1", sha256="a7d708ce5d5650f2b2f6f794332923a05ea15e5072ca9c2ff148f2e488260fa6")
    version("23.0.6", sha256="85b7b2319c6a7dd708502e2ef6bd749e24e7909237bcdf46cf27652822de49e3")
    version("23.0.5", sha256="b71026ab12cfab4e13e016e61fe20258a7dc798a3e90d67d12368ae4d87335d4")
    version("23.0.4", sha256="12b8636972b5f7922f4973978cb433b03af17c89abe7264addc3bbbb60e975fc")
    version("23.0.3", sha256="1d08d374c9492057f281ca04c487fc49ee2f42b98ff3b5624735f3be9bdd0538")
    version("23.0.2", sha256="d299b4f59047c2a2a4fc8d7c1365bbcdbe7622f98b5f56bb65895be133a35d83")
    version("23.0.1", sha256="9785ae04b7217b3350dbbe7885661d6c04a626fea616744534b8bd5b3c2e30ef")
    version("22.1.2", sha256="80257c94dc9122ebf80d643aa3962fe8beda23dbba8fc4820a0d2b720f479f98")

    depends_on("py-setuptools", when="@:23,24:", type="build")
    depends_on("py-setuptools@:71", when="@23.0.1:23.1.1", type="build")

    depends_on("py-bleach", type=("build", "run"))
    depends_on("py-boltons", type=("build", "run"))
    depends_on("py-docutils", type=("build", "run"))
    depends_on("py-importlib-resources", type=("build", "run"))
    depends_on("py-markupsafe", when="@:23", type=("build", "run"))
    depends_on("py-packaging@:21", when="@:22.0.6", type=("build", "run"))
    depends_on("py-packaging", when="@23:", type=("build", "run"))
    depends_on("py-pycryptodome", when="@:23", type=("build", "run"))
    depends_on("py-pyparsing", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-routes", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-zipstream-new", type=("build", "run"))
