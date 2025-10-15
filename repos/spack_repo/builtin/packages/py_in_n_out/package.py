# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyInNOut(PythonPackage):
    """A lightweight dependency injection and result processing framework for
    Python using type hints. Emphasis is on simplicity, ease of use, and
    minimal impact on source code."""

    homepage = "https://github.com/pyapp-kit/in-n-out"
    pypi = "in_n_out/in_n_out-0.2.1.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.2.1", sha256="43cde2b7de981d41a6d70618a2b7bd989481095922a53ead4dc75f2bbd5dffea")

    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-hatchling", type="build")
