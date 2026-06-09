# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Omnictl(GoPackage):
    """
    A CLI for accessing Omni API.
    """

    homepage = "https://github.com/siderolabs/omni"
    url = "https://github.com/siderolabs/omni/archive/refs/tags/v1.7.0.tar.gz"

    maintainers("RobertMaaskant")

    license("BUSL-1.1", checked_by="RobertMaaskant")

    version("1.8.2", sha256="40addbfac6c38e923df03d622b6d150d51fc254c4a622b4edd34658213cad36d")
    version("1.7.0", sha256="07dd01d8d724f59697e2754027dcbd12ee6e5bf2da1348e5b32d844e7eef4288")

    depends_on("go@1.26.3:", type="build", when="@1.8.1:")
    depends_on("go@1.26.2:", type="build", when="@1.7.0:")

    build_directory = "cmd/omnictl"
