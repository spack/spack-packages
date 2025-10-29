# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re
import shutil

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Ghostscript(AutotoolsPackage):
    """An interpreter for the PostScript language and for PDF."""

    homepage = "https://ghostscript.com/"
    url = "https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs926/ghostscript-9.26.tar.gz"
    git = "https://git.ghostscript.com/ghostpdl.git"

    executables = [r"^gs$"]

    license("AGPL-3.0-or-later", checked_by="wdconinc")

    version("10.06.0", sha256="5bd6da34794928cc7e616f288e32bd0be7f9a5ca2d3c206a0af2c19a4e3a318f")
    version("10.05.0", sha256="56e77833de683825c420d0af8cb90aa8ba7da71ea6fb5624290cbc1b53fe7942")

    # --enable-dynamic is deprecated, but kept as a variant since it used to be default
    # https://github.com/ArtifexSoftware/ghostpdl/commit/fe0f842da782b097ce13c31fccacce2374ed6d4b
    variant("dynamic", default=False, description="Enable dynamically loaded drivers")

    # https://www.ghostscript.com/ocr.html
    variant("tesseract", default=False, description="Use the Tesseract library for OCR")
    variant("gtk", default=True, description="Enable gtk+ device for screen output")
    variant("krb5", default=True, description="Enable Kerberos 5 support")
    variant("x11", default=True, description="Enable X11 support")
    variant("dbus", default=True, description="Enable D-Bus support")

    depends_on("c", type="build")

    depends_on("pkgconfig", type="build")
    depends_on("krb5", type="link", when="+krb5")

    depends_on("freetype@2.4.2:")
    depends_on("fontconfig", type="link")
    depends_on("jpeg")
    depends_on("lcms")
    depends_on("libpng")
    depends_on("libtiff")
    depends_on("zlib-api")
    depends_on("libx11", when="+x11")
    depends_on("libxt", when="+x11")
    depends_on("libxext", when="+x11")
    depends_on("gtkplus", type="link", when="+gtk")
    depends_on("dbus", type="link", when="+dbus")
    depends_on("libiconv", type="link")

    # https://trac.macports.org/ticket/62832
    conflicts(
        "+tesseract", when="platform=darwin", msg="Tesseract does not build correctly on macOS"
    )

    patch("nogoto.patch", when="%fj@:4.1.0")

    build_targets = ["default", "so"]
    install_targets = ["install", "soinstall"]

    def url_for_version(self, version):
        baseurl = "https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs{0}/ghostscript-{1}.tar.gz"
        return baseurl.format(version.joined, version.dotted)

    def patch(self):
        """Ghostscript comes with all of its dependencies vendored.
        In order to build with Spack versions of these dependencies,
        we have to remove these vendored dependencies.

        Note that this approach is also recommended by Linux from Scratch:
        https://www.linuxfromscratch.org/blfs/view/svn/pst/gs.html
        """
        directories = ["freetype", "jpeg", "lcms2mt", "libpng", "zlib"]
        for directory in directories:
            shutil.rmtree(directory)

        filter_file(
            "ZLIBDIR=src",
            "ZLIBDIR={0}".format(self.spec["zlib-api"].prefix.include),
            "configure.ac",
            "configure",
            string=True,
        )

    def configure_args(self):
        args = [
            "--disable-compile-inits",
            "--with-system-libtiff",
            "--without-x",
            "--without-libiconv",
        ]

        args.extend(self.with_or_without("tesseract"))

        if self.spec.satisfies("+dynamic"):
            args.append("--enable-dynamic")
            args.append("--disable-hidden-visibility")
        else:
            args.append("--disable-dynamic")

        args.extend(self.enable_or_disable("gtk"))
        args.append("--with-libiconv=gnu")

        return args

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--help", output=str, error=str)
        match = re.search(r"GPL Ghostscript (\S+)", output)
        return match.group(1) if match else None
