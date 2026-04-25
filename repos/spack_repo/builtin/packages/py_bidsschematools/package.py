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

    version("1.2.2", sha256="4401991b68acca8e8b24c28ba096796c3794260d722b1aad31229ffce941391b")
    version("1.0.10", sha256="e241dd798cc8686d4ab8b625e4d84ef3093d472a158cccd88a850496e4a4a8b9")

    depends_on("python@3.10:", type=("build", "run"), when="@1.2.2:")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-pdm-backend", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-acres@0.5:", when="@1.2.2:")
        depends_on("py-acres")
        depends_on("py-click@8.1:", when="@1.2.2:")
        depends_on("py-click")
        depends_on("py-pyyaml@6:", when="@1.2.2:")
        depends_on("py-pyyaml")
