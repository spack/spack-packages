# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack_repo.builtin.build_systems import nmake
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.nmake import NMakePackage

from spack.package import *


class Mpdecimal(AutotoolsPackage, NMakePackage):
    """mpdecimal is a package for correctly-rounded arbitrary precision
    decimal floating point arithmetic."""

    homepage = "https://www.bytereef.org/mpdecimal/"
    url = "https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-2.4.2.tar.gz"
    list_url = "https://www.bytereef.org/mpdecimal/download.html"
    tags = ["windows"]

    license("BSD-2-Clause")

    version("4.0.0", sha256="942445c3245b22730fd41a67a7c5c231d11cb1b9936b9c0f76334fb7d0b4468c")
    version("2.5.1", sha256="9f9cd4c041f99b5c49ffb7b59d9f12d95b683d88585608aa56a6307667b2b21f")
    version("2.4.2", sha256="83c628b90f009470981cf084c5418329c88b19835d8af3691b930afccb7d79c7")

    build_system("autotools", "nmake", default="autotools")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("gmake", type="build", when="build_system=autotools")

    @property
    def libs(self):
        if self.spec.satisfies("platform=windows"):
            # only an import library is generated for Windows
            # due to symbol visibility
            return find_libraries("libmpdec*", root=self.prefix.lib, runtime=False)
        # Suffix is .so, even on macOS
        return LibraryList(find(self.prefix.lib, "libmpdec.so"))


class NMakeBuilder(nmake.NMakeBuilder):
    @property
    def makefile_root(self):
        return os.path.join(self.pkg.stage.source_path, "libmpdec")

    def nmake_args(self):
        # ansi64 is what upstream's vcbuild_arm64.bat uses; x64 additionally
        # assembles vcdiv64.asm.
        machine = "x64" if self.spec.satisfies("target=x86_64:") else "ansi64"
        # Makefile.vc invokes $(CC) unquoted, rather than deal with quouting, let
        # spack's configured msvc runtime environment define the compiler
        return [
            self.define("MACHINE", machine),
            self.define("DEBUG", "0"),
            self.define("CC", "cl"),
        ]

    @run_before("build")
    def copy_makefile(self):
        # Every rule in Makefile.vc depends on a file literally named
        # "Makefile"...
        with working_dir(self.makefile_root):
            copy("Makefile.vc", "Makefile")

    def install(self, pkg, spec, prefix):
        # libmpdec has no install target on Windows.
        mkdirp(prefix.include)
        mkdirp(prefix.lib)
        mkdirp(prefix.bin)
        with working_dir(self.makefile_root):
            # Generated from mpdecimal{32,64}vc.h by the build.
            install("mpdecimal.h", prefix.include)
            for dll in glob.glob("libmpdec-*.dll"):
                install(dll, prefix.bin)
            for implib in glob.glob("libmpdec-*.dll.lib"):
                install(implib, prefix.lib)
