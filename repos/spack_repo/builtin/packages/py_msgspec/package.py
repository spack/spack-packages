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

    version("0.20.0", sha256="86590e1ba6bcb6739a2dfc17d2323f028cb5884f4c6ce23db376999132c9a922")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools@80:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")
