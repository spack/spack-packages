# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySnakemakeInterfaceCommon(PythonPackage):
    """Common functions and classes for Snakemake and its plugins."""

    homepage = "https://github.com/snakemake/snakemake-interface-common"
    pypi = "snakemake_interface_common/snakemake_interface_common-1.17.3.tar.gz"
    maintainers("w8jcik")

    license("MIT")

    version("1.22.0", sha256="ef1fa710a15629be4cc352b938596ab5235ecf0b615c5845f086d6c5da10cb88")
    version("1.21.0", sha256="0b6f0ef2c1a19fa8c20d676f4e355b8ba7058e142640a1c3c36fd1b9e110ef53")
    version("1.20.2", sha256="2857fc1f0baefd77d3bfa98938e1954d94f8b68df1f7910b92d1279153c84688")
    version("1.19.4", sha256="99cfbbd01def8f75e67eb0fd244ab7ee3abb3b3f12597f6d14d0c8b92e407340")
    version("1.18.0", sha256="2810abb68c1d2e5da69f271c9a0fc819dd9e62249c01db63793504011c7ad39a")
    version("1.17.4", sha256="c2142e1b93cbc18c2cf41d15968ba8688f60b077c8284e5de057cccfc215d4d3")
    version("1.17.3", sha256="cca6e2c728072a285a8e750f00fdd98d9c50063912184c41f8b89e4cab66c7b0")
    version("1.17.1", sha256="555c8218d9b68ddc1046f94a517e7d0f22e15bdc839d6ce149608d8ec137b9ae")

    depends_on("python@:3", type=("build", "run"))
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build", when="@1.18:")
    depends_on("py-wheel", type="build", when="@1.18:")

    depends_on("py-argparse-dataclass@2:", type=("build", "run"), when="@1.18:")
    depends_on("py-argparse-dataclass@2", type=("build", "run"), when="@:1.17")
    depends_on("py-configargparse@1.7:", type=("build", "run"), when="@1.18:")
    depends_on("py-packaging@24:25", type=("build", "run"), when="@1.20.1:")

    # Historical dependencies
    depends_on("py-poetry-core", type="build", when="@:1.17")
    depends_on("py-configargparse@1.7:1", type=("build", "run"), when="@:1.17")
    depends_on("py-semver@3", type=("build", "run"), when="@1.19:1.19.2")
    depends_on("py-packaging@25", type=("build", "run"), when="@1.19.3:1.20.0")
