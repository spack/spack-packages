# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack.package import *


class Mrustc(MakefilePackage):
    """mrustc is an alternative rust compiler written in C++

    It is sufficient to bootstrap rust, but not for general rust compilation.
    """

    homepage = "https://github.com/thepowersgang/mrustc"
    url = "https://github.com/thepowersgang/mrustc/archive/refs/tags/v0.11.2.tar.gz"

    license("MIT", checked_by="becker33")

    version("0.11.2", sha256="baf1e86311e004a638b35730b4d7e72644938a6bbbbf65a862245b92ba5325ad")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("python", type="build")

    depends_on("zlib")

    provides("rust-bootstrapper")

    def build(self, spec, prefix):
        with working_dir(self.build_directory):
            make("bin/mrustc")
            make("-f", "minicargo.mk", "bin/minicargo")

    def install(self, spec, prefix):
        install_tree(join_path(self.build_directory, "bin"), prefix.bin)
