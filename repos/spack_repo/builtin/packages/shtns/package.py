# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Shtns(AutotoolsPackage):
    """SHTns is a high performance library for Spherical Harmonic
    Transform written in C, aimed at numerical simulation (fluid
    flows, mhd, ...) in spherical geometries."""

    homepage = "https://nschaeff.bitbucket.io/shtns/index.html"

    maintainers("jagot")

    license("CECILL-2.1", checked_by="jagot")

    # The download page only provides the possibility to download the
    # whole repository, not tagged releases. The commit
    # f94e... corresponds to version 3.7.5, the latest version as of
    # this writing (2026-03-04).
    version(
        "3.7.5",
        sha256="b9a834e4ae0df5b9df070cb5df22d147614341fd99a788e41d97a29d2f5bf4f2",
        url="https://bitbucket.org/nschaeff/shtns/get/f94ecca74a08.zip",
    )
    depends_on("c", type="build")

    depends_on("fftw")
