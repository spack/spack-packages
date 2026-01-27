# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.pipx import PipxPackage

from spack.package import *


class PipxPoetry(PipxPackage):
    """Python dependency management and packaging made easy."""

    homepage = "https://python-poetry.org/"
    pypi = "poetry/poetry-1.8.3.tar.gz"

    maintainers("ebagrenrut")

    version("2.3.1", sha256="423cbccfe3533155ce9f49e929780a1386e564b2d97d2380664ea388cfe1191c")
    version("2.1.4", sha256="bed4af5fc87fb145258ac5b1dae77de2cd7082ec494e3b2f66bca0f477cbfc5c")
    version("2.1.3", sha256="f2c9bd6790b19475976d88ea4553bcc3533c0dc73f740edc4fffe9e2add50594")
    version("1.8.5", sha256="eb2c88d224f58f36df8f7b36d6c380c07d1001bca28bde620f68fc086e881b70")
    version("1.8.3", sha256="67f4eb68288eab41e841cc71a00d26cf6bdda9533022d0189a145a34d0a35f48")

    depends_on("python@3.10:", when="@2.3:")
    depends_on("python@3.9:", when="@2.0:")
    depends_on("python@3.8:")
