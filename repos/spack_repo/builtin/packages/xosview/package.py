# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Xosview(MakefilePackage):
    """Classic X11 system monitoring tool"""

    homepage = "https://www.pogo.org.uk/~mark/xosview/"
    url = "https://www.pogo.org.uk/~mark/xosview/releases/xosview-1.25.tar.gz"
    git = "https://github.com/hills/xosview"

    supplier = "Person: Mark Hills"

    maintainers("schallee")

    license("GPL-2.0-only", checked_by="schallee")

    version("1.25", sha256="e5f5ec03a0611397f8aafd07f05d4763726d9911139d9e267c5f308af9a6955b")

    depends_on("cxx", type="build")
    depends_on("gmake", type="build")

    depends_on("libx11")
    depends_on("libxpm")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("PREFIX", self.prefix)

    def install(self, spec, prefix):
        make("install")
