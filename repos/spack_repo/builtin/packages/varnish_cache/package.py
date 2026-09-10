# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class VarnishCache(AutotoolsPackage):
    """This is Varnish Cache, the high-performance HTTP accelerator."""

    homepage = "https://www.varnish-cache.org/"
    url = "https://github.com/varnishcache/varnish-cache/archive/refs/tags/varnish-6.4.0.tar.gz"

    license("BSD-2-Clause")

    version("7.6.1", sha256="6cfa30d761fa5edf33322048564cda3ee99de93ee57732c10f720d98d12f1899")

    depends_on("c", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("pcre2")
    depends_on("readline")
    depends_on("python", type=("build", "run"))
    depends_on("py-sphinx", type=("build", "run"))
    depends_on("py-docutils", type=("build", "run"))
