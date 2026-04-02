# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems import autotools, cmake

from spack.package import *


class Libharu(autotools.AutotoolsPackage, cmake.CMakePackage):
    """libharu - free PDF library.

    Haru is a free, cross platform, open-sourced software library for
    generating PDF."""

    homepage = "http://libharu.org"
    git = "https://github.com/libharu/libharu.git"

    license("custom")

    version("master", branch="master")
    version("2.4.5", sha256="0ed3eacf3ceee18e40b6adffbc433f1afbe3c93500291cd95f1477bffe6f24fc")
    version("2.4.4", sha256="227ab0ae62979ad65c27a9bc36d85aa77794db3375a0a30af18acdf4d871aee6")
    version("2.4.3", sha256="a2c3ae4261504a0fda25b09e7babe5df02b21803dd1308fdf105588f7589d255")
    version("2.4.2", sha256="226de46ffb035714f6f3c9ab52f22ca83d95c7af8480f7fd133537f072cda6cc")
    version("2.4.1", sha256="1af88a3b53af0b322c5af207935aefaf5b18847da4b70826725f18465fd43ec9")
    version("2.4.0", sha256="d1c38c0492257c61fb60c85238d500c05184fd8e9e68fecba9cf304ff2d8726d")
    version("2.3.0", sha256="8f9e68cc5d5f7d53d1bc61a1ed876add1faf4f91070dbc360d8b259f46d9a4d2")
    version("2.2.0", sha256="5e63246d2da0272a9dbe5963fd827c7efa6e29d97a2d047c0d4c5f0b780f10b5")

    build_system(
        conditional("cmake", when="@2.4:"), conditional("autotools", when="@:2.3"), default="cmake"
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    with when("build_system=cmake"):
        depends_on("cmake@3.10:", type="build")

    with when("build_system=autotools"):
        depends_on("libtool", type="build")
        depends_on("autoconf", type="build")
        depends_on("automake", type="build")

    depends_on("libpng")
    depends_on("zlib-api")

    def url_for_version(self, version):
        if version >= Version("2.4"):
            url = "https://github.com/libharu/libharu/archive/refs/tags/v{0}.tar.gz"
            return url.format(version)
        else:
            url = "https://github.com/libharu/libharu/archive/RELEASE_{0}.tar.gz"
            return url.format(version.underscored)


class AutotoolsBuilder(autotools.AutotoolsBuilder):
    def autoreconf(self, pkg, spec, prefix):
        """execute their autotools wrapper script"""
        if os.path.exists("./buildconf.sh"):
            bash = which("bash", required=True)
            bash("./buildconf.sh", "--force")

    def configure_args(self):
        """Point to spack-installed zlib and libpng"""
        spec = self.spec
        args = []

        args.append(f"--with-zlib={spec['zlib-api'].prefix}")
        args.append(f"--with-png={spec['libpng'].prefix}")

        return args
