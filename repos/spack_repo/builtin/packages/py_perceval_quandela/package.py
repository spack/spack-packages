# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPercevalQuandela(PythonPackage):
    """A powerful Quantum Photonic Framework."""

    homepage = "https://github.com/Quandela/Perceval"
    pypi = "perceval_quandela/perceval_quandela-1.2.4.tar.gz"

    supplier = "Organization: quandela"

    maintainers("LydDeb")

    version("1.2.4", sha256="f793ae5123d203f96974f8a27eeb17d183912946db3c55ba37f3c4294c6115bc")

    with default_args(type="build"):
        depends_on("py-setuptools@42:")
        depends_on("py-scmver")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:3.14")
        depends_on("py-sympy@1.12:1")
        depends_on("py-numpy@1.26:2")
        depends_on("py-scipy@1.13:1")
        depends_on("py-tabulate@0.9:0")
        depends_on("py-matplotlib@:3")
        depends_on("py-exqalibur@1.4.1:1")
        depends_on("py-multipledispatch@:1")
        depends_on("py-drawsvg@2:")
        depends_on("py-requests@:2")
        depends_on("py-networkx@3.1:3")
        depends_on("py-latexcodec@:3")
        depends_on("py-platformdirs@:4")
        depends_on("py-tqdm")
