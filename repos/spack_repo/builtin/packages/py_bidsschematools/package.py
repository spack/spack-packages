# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBidsschematools(PythonPackage):
    """Python tools for working with the BIDS schema."""

    homepage = "https://github.com/bids-standard/bids-specification"
    pypi = "bidsschematools/bidsschematools-1.0.10.tar.gz"

    license("MIT")

    version("1.0.10", sha256="e241dd798cc8686d4ab8b625e4d84ef3093d472a158cccd88a850496e4a4a8b9")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")

    depends_on("py-acres", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
