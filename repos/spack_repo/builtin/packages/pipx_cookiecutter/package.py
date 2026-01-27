# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.pipx import PipxPackage

from spack.package import *


class PipxCookiecutter(PipxPackage):
    """Create projects swiftly from cookiecutters (project templates) with this
    command-line utility."""

    homepage = "https://cookiecutter.readthedocs.io/en/latest/"
    url = "https://github.com/cookiecutter/cookiecutter/archive/2.6.0.tar.gz"

    maintainers("ebagrenrut")

    license("BSD-3-Clause")

    version("2.6.0", sha256="da014a94d85c1b1be14be214662982c8c90d860834cbf9ddb2391a37ad7d08be")

    depends_on("python@3.7:")
