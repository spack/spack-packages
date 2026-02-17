# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsBuilder, AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage

from spack.package import *

VARIANTS = [
    # Internal codecs
    "ccitt",
    "packbits",
    "lzw",
    "thunder",
    "next",
    "logluv",
    # External codecs
    "zlib",
    "libdeflate",
    "pixarlog",
    "jpeg",
    "old-jpeg",
    "jpeg12",
    "jbig",
    "lerc",
    "lzma",
    "zstd",
    "webp",
]


class Libtiff(CMakePackage, AutotoolsPackage):
    """LibTIFF - Tag Image File Format (TIFF) Library and Utilities."""

    homepage = "http://www.simplesystems.org/libtiff/"
    url = "https://download.osgeo.org/libtiff/tiff-4.1.0.tar.gz"

    maintainers("adamjstewart")

    license("libtiff")

    version("4.7.1", sha256="f698d94f3103da8ca7438d84e0344e453fe0ba3b7486e04c5bf7a9a3fabe9b69")
    version("4.7.0", sha256="67160e3457365ab96c5b3286a0903aa6e78bdc44c4bc737d2e486bcecb6ba976")

    # GUI
    variant("opengl", default=False, description="use OpenGL (required for tiffgt viewer)")

    # Internal codecs
    variant("ccitt", default=True, description="support for CCITT Group 3 & 4 algorithms")
    variant("packbits", default=True, description="support for Macintosh PackBits algorithm")
    variant("lzw", default=True, description="support for LZW algorithm")
    variant("thunder", default=True, description="support for ThunderScan 4-bit RLE algorithm")
    variant("next", default=True, description="support for NeXT 2-bit RLE algorithm")
    variant("logluv", default=True, description="support for LogLuv high dynamic range algorithm")

    # External codecs
    variant("zlib", default=True, description="use zlib")
    variant("libdeflate", default=False, description="use libdeflate")
    variant("pixarlog", default=False, description="support for Pixar log-format algorithm")
    variant("jpeg", default=True, description="use libjpeg")
    variant("old-jpeg", default=False, description="support for Old JPEG compression")
    variant("jpeg12", default=False, description="enable libjpeg 8/12-bit dual mode")
    variant("jbig", default=False, description="use ISO JBIG compression")
    variant("lerc", default=False, description="use libLerc")
    variant("lzma", default=False, description="use liblzma")
    variant("zstd", default=False, description="use libzstd")
    variant("webp", default=False, description="use libwebp")

    build_system("cmake", "autotools", default="cmake")

    variant("shared", default=True, description="Build shared")
    variant("pic", default=False, description="Enable position-independent code (PIC)")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    with when("build_system=cmake"):
        depends_on("cmake@3.9:", type="build")

    depends_on("zlib-api", when="+zlib")
    depends_on("zlib-api", when="+pixarlog")
    depends_on("jpeg@5:", when="+jpeg")
    depends_on("jbigkit", when="+jbig")
    depends_on("lerc", when="+lerc")
    depends_on("xz", when="+lzma")
    depends_on("zstd@1:", when="+zstd")
    depends_on("libwebp", when="+webp")

    conflicts("+libdeflate", when="~zlib")
    conflicts("+jpeg12", when="~jpeg")
    conflicts("+lerc", when="~zlib")

    def patch(self):
        # Remove flags not recognized by the NVIDIA compiler
        if self.spec.satisfies("%nvhpc@:20.11"):
            filter_file(
                'vl_cv_prog_cc_warnings="-Wall -W"', 'vl_cv_prog_cc_warnings="-Wall"', "configure"
            )


class CMakeBuilder(CMakeBuilder):
    def cmake_args(self):
        args = [self.define_from_variant(var) for var in VARIANTS]
        args.append("-Dsphinx=OFF")
        args += [self.define_from_variant("tiff-opengl", "opengl")]
        args += [self.define_from_variant("BUILD_SHARED_LIBS", "shared")]
        args += [self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic")]

        # Remove empty strings
        args = [arg for arg in args if arg]

        return args


class AutotoolsBuilder(AutotoolsBuilder):
    def configure_args(self):
        args = []
        for var in VARIANTS:
            args.extend(self.enable_or_disable(var))

        args.append("--disable-sphinx")

        args.extend(self.enable_or_disable("opengl"))
        args.extend(self.enable_or_disable("shared"))
        args.extend(self.with_or_without("pic"))

        return args
