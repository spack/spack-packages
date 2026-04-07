# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class AlsaLib(AutotoolsPackage):
    """The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
    functionality to the Linux operating system. alsa-lib contains the user
    space library that developers compile ALSA applications against."""

    homepage = "https://www.alsa-project.org"
    url = "ftp://ftp.alsa-project.org/pub/lib/alsa-lib-1.2.15.2.tar.bz2"
    git = "https://github.com/alsa-project/alsa-lib.git"

    license("LGPL-2.1-or-later")

    version("1.2.15.3", sha256="7b079d614d582cade7ab8db2364e65271d0877a37df8757ac4ac0c8970be861e")
    version("1.2.15.2", sha256="637eefd4966ce738da44464494df2b2894e19778fac2f9e7c47277e2af9297f4")
    version("1.2.9", sha256="dc9c643fdc4ccfd0572cc685858dd41e08afb583f30460b317e4188275f615b2")
    version("1.2.8", sha256="1ab01b74e33425ca99c2e36c0844fd6888273193bd898240fe8f93accbcbf347")
    version("1.2.3.2", sha256="e81fc5b7afcaee8c9fd7f64a1e3043e88d62e9ad2c4cff55f578df6b0a9abe15")
    version("1.2.2", sha256="d8e853d8805574777bbe40937812ad1419c9ea7210e176f0def3e6ed255ab3ec")
    version("1.1.4.1", sha256="91bb870c14d1c7c269213285eeed874fa3d28112077db061a3af8010d0885b76")

    variant("python", default=False, description="enable python")
    variant("plugins", default=False, description="enable plugins")

    patch("python.patch", when="@1.1.4:1.1.5 +python")

    depends_on("c", type="build")  # generated
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")

    depends_on("python", type=("link", "run"), when="+python")

    conflicts("platform=darwin", msg="ALSA only works for Linux")

    def configure_args(self):
        spec = self.spec
        args = []
        if spec.satisfies("+plugins"):
            args.append("--with-pcm-plugins=all --with-ctl-plugins=all --enable-pcm")
        if spec.satisfies("+python"):
            args.append(f"--with-pythonlibs={spec['python'].libs.ld_flags}")
            args.append(f"--with-pythonincludes={spec['python'].headers.include_flags}")
        else:
            args.append("--disable-python")
        return args
