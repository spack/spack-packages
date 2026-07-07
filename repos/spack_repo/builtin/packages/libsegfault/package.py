# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libsegfault(AutotoolsPackage):
    """This projects contains tools and library provided by glibc that either
    have been deprecated of moved out from the project. currently, in contains:
    LibSegFault."""

    homepage = "https://github.com/zatrazz/glibc-tools"
    git = "https://github.com/zatrazz/glibc-tools.git"

    maintainers("etiennemlb")

    license("GPL-2.0")

    version("2023-07-25", commit="ff16adff4a6af738eb4deabfb0eb107f6fa6e048")

    depends_on("c", type="build")

    flag_handler = build_system_flags
