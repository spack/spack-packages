# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libsndfile(AutotoolsPackage):
    """Libsndfile is a C library for reading and writing files containing
    sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
    through one standard library interface. It is released in source code
    format under the Gnu Lesser General Public License."""

    homepage = "https://github.com/libsndfile/libsndfile"
    url = (
        "https://github.com/libsndfile/libsndfile/releases/download/1.2.2/libsndfile-1.2.2.tar.xz"
    )

    license("LGPL-2.1-or-later")

    version("1.2.2", sha256="3799ca9924d3125038880367bf1468e53a1b7e3686a934f098b7e1d286cdb80e")

    variant("alsa", default=False, description="Use alsa in example programs")
    variant(
        "external-libs", default=False, description="Build with support for FLAC, Ogg and Vorbis"
    )
    variant("sqlite", default=False, description="Build with sqlite support")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("pkgconfig", type="build")
    depends_on("alsa-lib", when="+alsa")
    depends_on("flac@1.3.1:", when="+external-libs")
    depends_on("libogg@1.3.0:", when="+external-libs")
    depends_on("libvorbis@1.2.3:", when="+external-libs")
    depends_on("sqlite@3.2:", when="+sqlite")

    def configure_args(self):
        args = []

        args += self.enable_or_disable("alsa")
        args += self.enable_or_disable("external-libs")
        args += self.enable_or_disable("sqlite")

        return args
