# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libcgroup(AutotoolsPackage):
    """Library of control groups."""

    homepage = "https://github.com/libcgroup/libcgroup/"
    url = "https://github.com/libcgroup/libcgroup/releases/download/v3.1.0/libcgroup-3.1.0.tar.gz"

    license("LGPL-2.1-only")

    version("3.1.0", sha256="976ec4b1e03c0498308cfd28f1b256b40858f636abc8d1f9db24f0a7ea9e1258")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("m4", type="build")
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("linux-pam")
    depends_on("systemd")
