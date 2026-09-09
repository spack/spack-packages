# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyInteregular(PythonPackage):
    """A regex intersection checker."""

    homepage = "https://github.com/MegaIng/interegular"
    pypi = "interegular/interegular-0.3.3.tar.gz"

    version("0.3.3", sha256="d9b697b21b34884711399ba0f0376914b81899ce670032486d0d048344a76600")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
