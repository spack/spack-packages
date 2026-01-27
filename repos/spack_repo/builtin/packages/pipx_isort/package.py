# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.pipx import PipxPackage

from spack.package import *


class PipxIsort(PipxPackage):
    """isort is a Python utility / library to sort imports alphabetically and
    automatically separate into sections and by type."""

    homepage = "https://github.com/timothycrosley/isort"
    pypi = "isort/isort-5.12.0.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("7.0.0", sha256="5513527951aadb3ac4292a41a16cbc50dd1642432f5e8c20057d414bdafb4187")
    version("6.1.0", sha256="9b8f96a14cfee0677e78e941ff62f03769a06d412aabb9e2a90487b3b7e8d481")
    version("6.0.1", sha256="1cb5df28dfbc742e490c5e41bad6da41b805b0a8be7bc93cd0fb2a8a890ac450")
    version("5.13.2", sha256="48fdfcb9face5d58a4f6dde2e72a1fb8dcaf8ab26f95ab49fab84c2ddefb0109")
    version("5.12.0", sha256="8bef7dde241278824a6d83f44a544709b065191b95b6e50894bdc722fcba0504")

    depends_on("python@3.10:", when="@7:")
    depends_on("python@3.9:", when="@6:")
    depends_on("python@3.8:")
