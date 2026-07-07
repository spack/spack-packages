# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Helm(GoPackage):
    """The Kubernetes Package Manager"""

    homepage = "https://helm.sh"
    url = "https://github.com/helm/helm/archive/refs/tags/v4.1.3.tar.gz"

    maintainers("alecbcs")

    license("Apache-2.0")

    version("4.2.0", sha256="98d6b09a7dce667d0638bd293b6ef768cfc6ba51afda42b0fe0be1c7a021ceb7")
    version("4.1.4", sha256="cc365ae17de9bd856972198f9c372f9fd2146852434ade3b3c96303b564cdb15")
    version("4.1.3", sha256="a336010d2a5bebc0588995cfda20919c47b20c9f8ed3e4ada9241684854bbf9f")

    depends_on("go@1.26:", type="build", when="@4.2:")
    depends_on("go@1.25:", type="build", when="@4.1:")

    build_directory = "cmd/helm"
