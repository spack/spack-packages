# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from pathlib import Path

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Kdreg2(MakefilePackage):
    """HPE's kdreg2 kernel module."""

    homepage = "https://github.com/HewlettPackard/shs-kdreg2"
    git = "https://github.com/HewlettPackard/shs-kdreg2.git"

    supplier = "Organization: Hewlett Packard Enterprise"

    maintainers("AcerP-py")

    license("GPL-2.0 or LGPL-2.1")

    version("main", branch="main")
    version(
        "14.0.1",
        tag="release/shs-14.0.1",
        commit="2e1e7771e5bb7c8fc11e7e59cb1a4972595f1b30",
    )

    depends_on("c", type="build")

    requires("%c=gcc")

    requires("platform=linux", msg="only available on linux")

    def build(self, spec, prefix):
        make(f"CC={self.compiler.cc}", "modules", "build_info")

    def install(self, spec, prefix):
        src: Path = Path(self.stage.source_path)
        dest: Path = Path(prefix)

        # headers
        install_tree(str(src / "include"), str(dest / "include"))
        # this is for Libfabric which expects 'linux/kdreg2.h'
        mkdirp(str(dest / "include/linux"))
        force_symlink("../kdreg2.h", str(dest / "include/linux/kdreg2.h"))

        # module
        mkdirp(str(dest / "lib/modules"))
        install(str(src / "kdreg2.ko"), str(dest / "lib/modules"))

    @property
    def headers(self):
        return find_headers(["kdreg2"], self.prefix.include)
