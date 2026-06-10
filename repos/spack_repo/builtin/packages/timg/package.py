# ruff: noqa: F403, F405
# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# Mandatory options:
#     WITH_GRAPHICSMAGICK    : (default: ON) main image loading library
# Highly-recommended:
#     WITH_LIBSIXEL          : (ON) use libsixel to output images in sixel graphics format
#     WITH_TURBOJPEG         : (ON) if enabled, uses this for faster jpeg file loading
#     WITH_POPPLER           : (ON) high-quality faster PDF renderer; needs poppler and cairo (*)
#     WITH_RSVG              : (ON) high-quality SVG renderer; needs librsvg and cairo (*)
# Optional:
#     WITH_VIDEO_DECODING    : (OFF) allow for video decoding, requires ffmpeg-related libraries
#     WITH_OPENSLIDE_SUPPORT : (OFF) image format used in scientific applications, rarely used
#     WITH_QOI_IMAGE         : (ON) allow decoding of Quite Ok Image format QOI, small and simple
#     WITH_STB_IMAGE         : (OFF) compile the simpler STB image library directly into timg bin
#                              when Graphicsmagick is not suitable for dependency pruning reasons;
#                              output can be slower and of less quality, it will always only be
#                              attempted after other image loading fails;
#                              recommeded to be turned off if you can use GraphicsMagick and
#                              want to reduce potential security vectors
#     WITH_VIDEO_DEVICE      : (OFF) allows accessing connected video devices;
#                               e.g. you can watch your webcam input (requires WITH_VIDEO_DECODING)
#
# (*) if not compiled-in, will fallback to GraphicsMagick, but that typically results
# in lower quality renderings
#

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Timg(CMakePackage):
    """Timg: a terminal image and video viewer."""

    homepage = "https://github.com/hzeller/timg"
    url = "https://github.com/hzeller/timg/archive/refs/tags/v1.6.3.tar.gz"
    git = "https://github.com/hzeller/timg.git"

    license("GPL-2.0-only", checked_by="foglienimatteo")

    version("1.6.3", sha256="59c908867f18c81106385a43065c232e63236e120d5b2596b179ce56340d7b01")
    version("1.6.2", sha256="a5fb4443f55552d15a8b22b9ca4cb5874eb1a988d3b98fe31d61d19b2c7b9e56", deprecated=True)
    version("1.6.1", sha256="08147c41ce4cea61b6c494ad746e743b7c4501cfd247bec5134e8ede773bf2af", deprecated=True)
    version("1.6.0", sha256="9e1b99b4eaed82297ad2ebbde02e3781775e3bba6d3e298d7598be5f4e1c49af", deprecated=True)
    version("1.5.3", sha256="ddf2fb1fb2376d31957415d278bc34ff0ef574eb69ef96ddcb564c392d2e4c27", deprecated=True)
    version( "1.5.2", sha256="f0c604e2cab03bbd213b20333a9b90ea1211af730de2b914402e7275111f804e", deprecated=True)
    version( "1.5.1", sha256="ac8905e4615d964eee6b014b9ff3413160cfc5b73f547e91736bc06c928ac811", deprecated=True)
    version( "1.5.0", sha256="aa457f401b0517ba814efc62ededa3ab3f4edc1f40fb6048c58d52f01dfd9ba2", deprecated=True)
    version( "1.4.5", sha256="3c96476ce4ba2af4b9f639c5b59ded77ce1a4511551a04555ded105f14398e01", deprecated=True)

    # Build dependencies
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.5:", type="build")
    depends_on("pkgconfig", type="build")

    # Mandatory dependencies
    depends_on("graphicsmagick")
    depends_on("libexif")
    depends_on("libdeflate")

    # Variants
    # Highly-recommended
    variant("sixel", default=True, description="Output images in Sixel graphics format")
    variant("turbojpeg", default=True, description="Faster JPEG loading")
    variant( "poppler", default=True, description="High-quality PDF rendering using poppler and cairo" )
    variant( "rsvg", default=True, description="High-quality SVG renderering using librsvg and cairo" )
    # Optional
    variant("video", default=False, description="Enable video decoding via FFmpeg")
    variant("openslide", default=False, description="Enable Openslide support (image format used in scientific applications, rarely used)", )
    variant("qoi", default=True, description="Enable decoding of Quite Ok Image format QOI, small and simple", )
    variant("stb", default=False, description="Enable compilation of simpler STB image library directly into binary; fallback for imagemagick", )
    variant( "videodevice", default=False, description="Enables accessing connected video devices (e.g. your webcam input); requires '+video' variant", )
    # Variants' dependencies
    depends_on("libsixel", when="+sixel")
    depends_on("libjpeg-turbo", when="+turbojpeg")
    # NOTE: we enforce the glib variant on the upstream poppler dependency whenever the
    # poppler variant is activated for timg
    depends_on("poppler+glib", when="+poppler")
    depends_on("cairo", when="+poppler")
    depends_on("librsvg", when="+rsvg")
    depends_on("cairo", when="+rsvg")
    depends_on("ffmpeg", when="+video")
    depends_on("openslide", when="+openslide")
    depends_on("ffmpeg", when="+videodevice")

    def cmake_args(self):
        args = [
            # Highly-recommended
            self.define_from_variant("WITH_LIBSIXEL", "sixel"),
            self.define_from_variant("WITH_TURBOJPEG", "turbojpeg"),
            self.define_from_variant("WITH_POPPLER", "poppler"),
            self.define_from_variant("WITH_RSVG", "rsvg"),
            # Optional
            self.define_from_variant("WITH_VIDEO_DECODING", "video"),
            self.define_from_variant("WITH_OPENSLIDE_SUPPORT", "openslide"),
            self.define_from_variant("WITH_QOI_IMAGE", "qoi"),
            self.define_from_variant("WITH_STB_IMAGE", "stb"),
            self.define_from_variant("WITH_VIDEO_DEVICE", "videodevice"),
        ]
        return args
