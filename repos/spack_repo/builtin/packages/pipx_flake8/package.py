# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.pipx import PipxPackage

from spack.package import *


class PipxFlake8(PipxPackage):
    """Flake8 is a wrapper around PyFlakes, pycodestyle, and Ned Batchelder's McCabe
    script."""

    homepage = "https://github.com/PyCQA/flake8"
    pypi = "flake8/flake8-6.1.0.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("7.3.0", sha256="fe044858146b9fc69b551a4b490d69cf960fcb78ad1edcb84e7fbb1b4a8e3872")
    version("7.2.0", sha256="fa558ae3f6f7dbf2b4f22663e5343b6b6023620461f8d4ff2019ef4b5ee70426")
    version("7.1.1", sha256="049d058491e228e03e67b390f311bbf88fce2dbaa8fa673e7aea87b7198b8d38")
    version("6.1.0", sha256="d5b3857f07c030bdb5bf41c7f53799571d75c4491748a3adcd47de929e34cd23")

    depends_on("python@3.9:", when="@7.2:")
    depends_on("python@3.8:")
