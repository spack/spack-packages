# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJedi(PythonPackage):
    """An autocompletion tool for Python that can be used for text editors."""

    homepage = "https://github.com/davidhalter/jedi"
    pypi = "jedi/jedi-0.9.0.tar.gz"

    maintainers("alecbcs")

    license("MIT")

    version("0.20.0", sha256="c3f4ccbd276696f4b19c54618d4fb18f9fc24b0aef02acf704b23f487daa1011")
    version("0.19.2", sha256="4770dc3de41bde3966b02eb84fbcf557fb33cce26ad23da12c742fb50ecb11f0")
    version("0.18.2", sha256="bae794c30d07f6d910d32a7048af09b5a39ed740918da923c6b780790ebac612")
    version("0.18.1", sha256="74137626a64a99c8eb6ae5832d99b3bdd7d29a3850fe2aa80a4126b2a7d949ab")
    version("0.18.0", sha256="92550a404bad8afed881a137ec9a461fed49eca661414be45059329614ed0707")
    version("0.17.2", sha256="86ed7d9b750603e4ba582ea8edc678657fb4007894a12bcf6f4bb97892f31d20")
    version("0.17.1", sha256="807d5d4f96711a2bcfdd5dfa3b1ae6d09aa53832b182090b222b5efb81f52f63")

    with default_args(type=("build", "run")):
        depends_on("python@:3.9", when="@:0.17.1")
        depends_on("python@:3.10", when="@:0.18.1")
        depends_on("python@:3.11", when="@:0.19.0")
        depends_on("python@:3.12", when="@:0.19.1")
        depends_on("python@:3.13", when="@:0.19.2")
        depends_on("python@:3.14", when="@0.20:")

        depends_on("py-setuptools")

        depends_on("py-parso@0.7", when="@0.17")
        depends_on("py-parso@0.8", when="@0.18.0:")
        depends_on("py-parso@0.8.4:0.8", when="@0.19.2:")
        depends_on("py-parso@0.8.6:0.8", when="@0.20:")
