# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class Pyrefly(PythonPackage):
    """A fast type checker and language server for Python with powerful IDE features."""

    homepage = "https://pyrefly.org/"
    pypi = "pyrefly/pyrefly-0.58.0.tar.gz"

    license("MIT")

    version("0.58.0", sha256="4512b89cd8db95e8994537895ff41ad60e6211643442f8e33ed93bb59f88a256")

    depends_on("py-maturin@1.10.2:1", type="build")
