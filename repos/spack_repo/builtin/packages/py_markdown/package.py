# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMarkdown(PythonPackage):
    """This is a Python implementation of John Gruber's Markdown. It is
    almost completely compliant with the reference implementation, though
    there are a few very minor differences. See John's Syntax
    Documentation for the syntax rules.
    """

    homepage = "https://python-markdown.github.io/"
    pypi = "markdown/Markdown-2.6.11.tar.gz"

    license("BSD-3-Clause")

    # need to update the pypi as the older versions are not visible
    # putting a url for the latest version temporarily
    version(
        "3.10.2",
        sha256="994d51325d25ad8aa7ce4ebaec003febcce822c3f8c911e3b17c52f7f589f950",
        url="https://files.pythonhosted.org/packages/2b/f4/69fa6ed85ae003c2378ffa8f6d2e3234662abd02c10d216c0ba96081a238/markdown-3.10.2.tar.gz",
    )
    version("3.4.1", sha256="3b809086bb6efad416156e00a0da66fe47618a5d6918dd688f53f40c8e4cfeff")
    version("3.3.4", sha256="31b5b491868dcc87d6c24b7e3d19a0d730d59d3e46f4eea6430a321bed387a49")
    version("3.1.1", sha256="2e50876bcdd74517e7b71f3e7a76102050edec255b3983403f1a63e7c8a41e7a")

    with default_args(type="build"):
        depends_on("py-setuptools@77.0:", when="@3.10.2:")
        depends_on("py-setuptools@36.6:", when="@:3.4")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@3.10.2:")
        depends_on("python@3.7:", when="@3.4.1:")
        depends_on("python@3.6:", when="@3.3.4:")
        depends_on("python@2.7:2.8,3.3.5:", when="@3.1.1")

        depends_on("py-importlib-metadata", when="@3.3.4: ^python@:3.7")
        depends_on("py-importlib-metadata@4.4:", when="@3.4.1: ^python@:3.9")
