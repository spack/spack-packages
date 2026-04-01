# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.sourceforge import SourceforgePackage

from spack.package import *


class Gsoap(AutotoolsPackage, SourceforgePackage):
    """The gSOAP toolkit is an extensive suite of portable C and C++
    software to develop XML Web services with powerful type-safe XML
    data bindings."""

    homepage = "https://www.genivia.com/products.html"

    sourceforge_mirror_path = "gsoap2/gsoap_2.8.127.zip"

    maintainers("greenc-FNAL", "gartung", "marcmengel", "vitodb")

    version("2.8.135", sha256="b11757e405d55d4674dfbf88c4fa6d7e24155cf64ed8ed578ccad2f2b555e98d")

    depends_on("openssl")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    def configure_args(self):
        return ["--enable-ipv6"]

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("PKG_CONFIG_PATH", "%s/lib/ldconfig" % self.prefix)

    def flag_handler(self, name, flags):
        if name in ["cflags", "cxxflags", "cppflags"]:
            flags.append(self.compiler.cc_pic_flag)

        return self.build_system_flags(name, flags)
