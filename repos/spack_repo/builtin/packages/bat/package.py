# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Bat(CargoPackage):
    """A cat(1) clone with wings."""

    homepage = "https://github.com/sharkdp/bat"
    url = "https://github.com/sharkdp/bat/archive/v0.13.0.tar.gz"

    license("Apache-2.0")

    version("0.26.1", sha256="4474de87e084953eefc1120cf905a79f72bbbf85091e30cf37c9214eafcaa9c9")
    version("0.26.0", sha256="ccf3e2b9374792f88797a28ce82451faeae0136037cb8c8b56ba0a6c1a94fd69")
    version("0.24.0", sha256="907554a9eff239f256ee8fe05a922aad84febe4fe10a499def72a4557e9eedfb")
    version("0.23.0", sha256="30b6256bea0143caebd08256e0a605280afbbc5eef7ce692f84621eb232a9b31")
    version("0.21.0", sha256="3dff1e52d577d0a105f4afe3fe7722a4a2b8bb2eb3e7a6a5284ac7add586a3ee")
    version("0.13.0", sha256="f4aee370013e2a3bc84c405738ed0ab6e334d3a9f22c18031a7ea008cd5abd2a")
    version("0.12.1", sha256="1dd184ddc9e5228ba94d19afc0b8b440bfc1819fef8133fe331e2c0ec9e3f8e2")

    depends_on("rust@1.87:", type="build", when="@0.26:")
    depends_on("rust@1.74:", type="build", when="@0.25:")
    depends_on("rust@1.70:", type="build", when="@0.24:")
    depends_on("rust@1.64:", type="build", when="@0.23:")
