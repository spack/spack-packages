# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Shadowenv(CargoPackage):
    """
    Shadowenv provides a way to perform a set of manipulations to the process
    environment upon entering a directory in a shell. These manipulations are reversed
    when leaving the directory, and there is some limited ability to make the
    manipulations dynamic.
    """

    homepage = "https://shopify.github.io/shadowenv/"
    url = "https://github.com/Shopify/shadowenv/archive/3.4.0.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("3.4.0", sha256="86313a5022a8e897ceb52a51479fa7a921e44cd520cf04d111ba711684791e44")

    depends_on("c", type="build")
    depends_on("rust@1.80:", type="build")
