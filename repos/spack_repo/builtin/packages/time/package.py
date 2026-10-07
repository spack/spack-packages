# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *


class Time(AutotoolsPackage, GNUMirrorPackage):
    """The time command runs another program, then displays
    information about the resources used by that program."""

    homepage = "https://www.gnu.org/software/time/"
    gnu_mirror_path = "time/time-1.9.tar.gz"

    license("GPL-3.0-only")

    version("1.10", sha256="e8c29fb4ab599d8478e41e8618f50db8aede9c90af27d0d2ef28ae50d5de09c3")
    version("1.9", sha256="fbacf0c81e62429df3e33bda4cee38756604f18e01d977338e23306a3e3b521e")

    depends_on("c", type="build")  # generated

    build_directory = "spack-build"
