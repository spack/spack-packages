# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMsgspec(PythonPackage):
    """A fast serialization and validation library, with builtin support
    for JSON, MessagePack, YAML, and TOML."""

    homepage = "https://jcristharif.com/msgspec/"
    pypi = "msgspec/msgspec-0.20.0.tar.gz"

    version("0.20.0", sha256="692349e588fde322875f8d3025ac01689fead5901e7fb18d6870a44519d62a29")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")  # todo(thomas-bouvier): should depend on py-setuptools@80: but it breaks concretization
    depends_on("py-setuptools-scm@8:", type="build")
