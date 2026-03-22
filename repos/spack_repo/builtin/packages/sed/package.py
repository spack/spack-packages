# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *


class Sed(AutotoolsPackage, GNUMirrorPackage):
    """GNU implementation of the famous stream editor."""

    git = "git://git.sv.gnu.org/sed"
    homepage = "https://www.gnu.org/software/sed/"
    gnu_mirror_path = "sed/sed-4.8.tar.xz"

    license("GPL-3.0-or-later")

    version("4.9", sha256="6e226b732e1cd739464ad6862bd1a1aba42d7982922da7a53519631d24975181")
    version("4.8", sha256="f79b0cfea71b37a8eeec8490db6c5f7ae7719c35587f21edb0617f370eeff633")
    version("4.2.2", sha256="f048d1838da284c8bc9753e4506b85a1e0cc1ea8999d36f6995bcb9460cddbd7")
    version("4.1", sha256="57c86e7c17b8af6d6ecbdc17086ad22ec72d815f0db8a475a1d9adef2879f922")

    version("master", branch="master")
    version("arbitrary", commit="0e2491480a2ccb4736aa919c1d7bd197fcaee885")

    depends_on("c", type="build")  # generated

    # Avoid symlinking GNUMakefile to GNUMakefile
    build_directory = "spack-build"

    executables = ["^sed$"]

    tags = ["build-tools"]

    _bz2_range = ver("4.2:4.2")
    def url_for_version(self, version):
        if version in self.__class__._bz2_range:
            self.gnu_mirror_path = "sed/sed-{0}.tar.bz2".format(version)
        elif version < Version("4.2"):
            self.gnu_mirror_path = "sed/sed-{0}.tar.gz".format(version)
        return super().url_for_version(version)

    _version_at_eol = re.compile(r'\s+([0-9]+\.[0-9]+\S*)$')
    @classmethod
    def determine_version(cls, exe):
        exe = Executable(exe)
        m = cls._version_at_eol.search(exe("--version").splitlines()[0])
        if m:
            return m.group(1)
        return None

    def flag_handler(self, name, flags):
        if name == "cflags":
            if self.spec.satisfies("%oneapi@2023.0.0:"):
                flags.append("-Wno-error=incompatible-function-pointer-types")
        return (flags, None, None)
