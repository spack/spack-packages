# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Portaudio(AutotoolsPackage):
    """PortAudio is a free, cross-platform, open-source, audio I/O library.  It lets you write
    simple audio programs in 'C' or C++ that will compile and run on many platforms including
    Windows, Macintosh OS X, and Unix (OSS/ALSA)."""

    homepage = "https://www.portaudio.com/"
    url = "https://github.com/PortAudio/portaudio/archive/refs/tags/v19.7.0.tar.gz"

    license("Custom")

    version("19.7.0", sha256="5af29ba58bbdbb7bbcefaaecc77ec8fc413f0db6f4c4e286c40c3e1b83174fa0")

    depends_on("c", type="build")

    depends_on("alsa-lib", type="link")

    def configure_args(self):
        args = ["--with-alsa"]
        return args
