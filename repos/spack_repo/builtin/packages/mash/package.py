# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Mash(AutotoolsPackage):
    """
    Fast genome and metagenome distance estimation using MinHash.
    """

    homepage = "https://mash.readthedocs.org/"
    url = "https://github.com/marbl/Mash/archive/refs/tags/v2.3.tar.gz"

    maintainers("marcusboden")

    version("2.3", sha256="f96cf7305e010012c3debed966ac83ceecac0351dbbfeaa6cd7ad7f068d87fe1")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    patch("gcc-11.patch", when="%gcc@11:")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("capnproto")
    depends_on("gsl")

    def patch(self):
        if self.spec.satisfies("target=aarch64:"):
            filter_file(
                "CXXFLAGS += -include src/mash/memcpyLink.h -Wl,--wrap=memcpy",
                "",
                "Makefile.in",
                string=True,
            )
            filter_file("CFLAGS += -include src/mash/memcpyLink.h", "", "Makefile.in", string=True)

            # Fix missing <cstdint> include needed by newer GCC/libstdc++
            if self.spec.satisfies("%gcc@12:"):
                patch(
                    "https://patch-diff.githubusercontent.com/raw/marbl/Mash/pull/192.patch?full_index=1",
                    sha256sum="b5a44b078fdf15cda8a535b30b209252ab8f9aff9fcbeb10edf2aa4a2d7d32eb",
                )

    def configure_args(self):
        args = []
        args.append("--with-capnp=" + self.spec["capnproto"].prefix)
        args.append("--with-gsl=" + self.spec["gsl"].prefix)
        return args
