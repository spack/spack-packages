# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Imagemagick(AutotoolsPackage):
    """ImageMagick is a software suite to create, edit, compose,
    or convert bitmap images."""

    homepage = "https://www.imagemagick.org"
    url = "https://github.com/ImageMagick/ImageMagick/archive/7.0.2-7.tar.gz"

    license("ImageMagick")

    version("7.1.1-39", sha256="b2eb652d9221bdeb65772503891d8bfcfc36b3b1a2c9bb35b9d247a08965fd5d")
    version("7.1.1-29", sha256="27bd25f945efdd7e38f6f9845a7c0a391fdb732f652dda140b743769c5f106e8")
    version("7.1.1-11", sha256="98bb2783da7d5b06e7543529bd07b50d034fba611ff15e8817a0f4f73957d934")

    variant("ghostscript", default=False, description="Compile with Ghostscript support")
    variant("rsvg", default=False, description="Enable RSVG support")
    variant("zlib", default=False, description="Enable zlib support")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("pkgconfig", type="build")

    depends_on("fontconfig@2.1:")
    depends_on("freetype@2.8:")
    depends_on("jpeg")
    depends_on("pango@1.28.1:")
    depends_on("libpng@1:")
    depends_on("librsvg@2.9:", when="+rsvg")
    depends_on("libtiff@4:")
    depends_on("ghostscript", when="+ghostscript")
    depends_on("ghostscript-fonts", when="+ghostscript")
    depends_on("zlib-api", when="+zlib")

    def configure_args(self):
        args = []
        spec = self.spec
        if spec.satisfies("+ghostscript"):
            args.append("--with-gslib")
            gs_font_dir = spec["ghostscript-fonts"].prefix.share.font
            args.append("--with-gs-font-dir={0}".format(gs_font_dir))
        else:
            args.append("--without-gslib")
        args.extend(self.with_or_without("rsvg"))
        args.extend(self.with_or_without("zlib"))
        return args

    @property
    def libs(self):
        return find_libraries("libMagick*", root=self.prefix, recursive=True)
