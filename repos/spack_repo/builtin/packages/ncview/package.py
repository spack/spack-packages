# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Ncview(AutotoolsPackage):
    """Simple viewer for NetCDF files."""

    homepage = "https://cirrus.ucsd.edu/ncview/"

    license("GPL-3.0-only")

    version("2.1.11", sha256="597cfddf9c2d7993e9b0b86bca1b73839567ee9116ee33f6d750a449b5033d91")
    version("2.1.10", sha256="08d9cefb58a25b41316296074dccfe24147c3b7ea1af071cbfe785eff9f0dc65")
    version("2.1.9", sha256="e2317ac094af62f0adcf68421d70658209436aae344640959ec8975a645891af")
    version("2.1.8", sha256="e8badc507b9b774801288d1c2d59eb79ab31b004df4858d0674ed0d87dfc91be")
    version("2.1.7", sha256="a14c2dddac0fc78dad9e4e7e35e2119562589738f4ded55ff6e0eca04d682c82")

    depends_on("c", type="build")  # generated

    depends_on("netcdf-c")
    depends_on("udunits")
    depends_on("libpng")
    depends_on("libxaw")

    def flag_handler(self, name, flags):
        # The package does not build with C dialects newer than gnu17, so set gnu17
        # for GCC 15 and newer which default to gnu23
        if name == "cflags" and self.spec.satisfies("%gcc@15:"):
            flags.append("-std=gnu17")
        return (flags, None, None)

    def patch(self):
        # Disable the netcdf-c compiler check, save and restore the
        # modification timestamp of the file to prevent autoreconf.
        patched_file = "configure"
        with keep_modification_time(patched_file):
            filter_file(
                "if test x$CC_TEST_SAME != x$NETCDF_CC_TEST_SAME; then",
                "if false; then",
                patched_file,
                string=True,
            )

    def url_for_version(self, version):
        if version >= Version("2.1.9"):
            return f"https://cirrus.ucsd.edu/~pierce/ncview/ncview-{version}.tar.gz"
        else:
            return f"ftp://cirrus.ucsd.edu/pub/ncview/ncview-{version}.tar.gz"
