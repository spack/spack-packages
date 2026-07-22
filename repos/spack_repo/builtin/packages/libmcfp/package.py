# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Libmcfp(CMakePackage):
    """A library for parsing command line arguments and configuration files and making them
    available throughout a program.
    """

    homepage = "https://github.com/mhekkel/libmcfp"
    url = "https://github.com/mhekkel/libmcfp/archive/refs/tags/v1.4.2.tar.gz"

    license("BSD-2-Clause", checked_by="snehring")

    version("1.4.2", sha256="dcdf3e81601081b2a9e2f2e1bb1ee2a8545190358d5d9bec9158ad70f5ca355e")

    depends_on("cxx", type="build")
