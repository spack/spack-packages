# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsBuilder, AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage
from spack_repo.builtin.build_systems.meson import MesonBuilder, MesonPackage

from spack.package import *


class Freetype(AutotoolsPackage, CMakePackage, MesonPackage):
    """FreeType is a freely available software library to render fonts.
    It is written in C, designed to be small, efficient, highly customizable,
    and portable while capable of producing high-quality output (glyph images)
    of most vector and bitmap font formats."""

    homepage = "https://www.freetype.org/index.html"
    url = "https://download.savannah.gnu.org/releases/freetype/freetype-2.10.1.tar.gz"
    list_url = "https://download.savannah.gnu.org/releases/freetype/"
    git = "https://gitlab.freedesktop.org/freetype/freetype.git"

    maintainers("michaelkuhn")

    license("FTL OR GPL-2.0-or-later")

    version("2.14.3", sha256="e61b31ab26358b946e767ed7eb7f4bb2e507da1cfefeb7a8861ace7fd5c899a1")
    version("2.14.2", sha256="752c2671f85c54a84b7f0dd2b5cd26b6b741117033886ffbc5ac89a68464b848")
    version("2.14.1", sha256="174d9e53402e1bf9ec7277e22ec199ba3e55a6be2c0740cb18c0ee9850fc8c34")
    version("2.14.0", sha256="73819bbf34c84f18b89ebbd35107d3ae92c604ff7336cd09ff1452930c2dcb9c")
    version("2.13.3", sha256="5c3a8e78f7b24c20b25b54ee575d6daa40007a5f4eea2845861c3409b3021747")
    version("2.13.2", sha256="1ac27e16c134a7f2ccea177faba19801131116fd682efc1f5737037c5db224b5")
    version("2.13.1", sha256="0b109c59914f25b4411a8de2a506fdd18fa8457eb86eca6c7b15c19110a92fa5")
    version("2.13.0", sha256="a7aca0e532a276ea8d85bd31149f0a74c33d19c8d287116ef8f5f8357b4f1f80")
    version("2.12.1", sha256="efe71fd4b8246f1b0b1b9bfca13cfff1c9ad85930340c27df469733bbb620938")
    version("2.12.0", sha256="7940a46eeb0255baaa87c553d72778c4f8daa2b8888c8e2a05766a2a8686740c")
    version("2.11.1", sha256="f8db94d307e9c54961b39a1cc799a67d46681480696ed72ecf78d4473770f09b")
    version("2.11.0", sha256="a45c6b403413abd5706f3582f04c8339d26397c4304b78fa552f2215df64101f")
    version("2.10.4", sha256="5eab795ebb23ac77001cfb68b7d4d50b5d6c7469247b0b01b2c953269f658dac")
    version("2.10.2", sha256="e09aa914e4f7a5d723ac381420949c55c0b90b15744adce5d1406046022186ab")
    version("2.10.1", sha256="3a60d391fd579440561bf0e7f31af2222bc610ad6ce4d9d7bd2165bca8669110")
    version("2.10.0", sha256="955e17244e9b38adb0c98df66abb50467312e6bb70eac07e49ce6bd1a20e809a")
    version("2.9.1", sha256="ec391504e55498adceb30baceebd147a6e963f636eb617424bcfc47a169898ce")
    version("2.7.1", sha256="162ef25aa64480b1189cdb261228e6c5c44f212aac4b4621e28cf2157efb59f5")
    version("2.7", sha256="7b657d5f872b0ab56461f3bd310bd1c5ec64619bd15f0d8e08282d494d9cfea4")
    version("2.6.1", sha256="0a3c7dfbda6da1e8fce29232e8e96d987ababbbf71ebc8c75659e4132c367014")
    version("2.5.3", sha256="41217f800d3f40d78ef4eb99d6a35fd85235b64f81bc56e4812d7672fca7b806")

    version("master", branch="master")
    version("2.10.3", tag="VER-2-10-3", commit="337670af0a1e94df3718c6467ca544ecb0282731")

    # CMake build does not install freetype-config, which is needed by most packages
    build_system("cmake", "autotools", conditional("meson", when="@2.11:"),
                 default="autotools")

    variant("freetype-config", default=True,
            when="@2.9.1: build_system=autotools",
            description="Build the 'freetype-config' binary.")
    variant("bzip2", default=True,
            description="Build with bzip2 support.")
    variant("png", default=True,
            description="Build with png support.")
    variant("zlib", default=False,
            description="Build with zlib support.")
    # Harrowing issue: https://github.com/harfbuzz/harfbuzz/issues/2524.
    variant("harfbuzz", default="no",
            values=("dynamic", "yes", "no"),
            description="Build with harfbuzz support.\n"
            "If 'dynamic' is selected, harfbuzz will be accessed with dlopen().")
    variant("brotli", default=False,
            description="Build with brotli support.")
    variant("svg", default=False,
            description="Build with svg support.")

    depends_on("c", type="build")  # generated

    depends_on("bzip2", when="+bzip2")
    depends_on("libpng", when="+png")
    depends_on("zlib-api", when="+zlib")
    depends_on("harfbuzz", when="harfbuzz=yes")
    # depends_on("harfbuzz@10:+shared", when="harfbuzz=dynamic", type="run")
    depends_on("brotli", when="+brotli")
    depends_on("librsvg", when="+svg")

    depends_on("pkgconfig", type="build")

    with when("build_system=autotools"):
        with default_args(type="build"):
            depends_on("automake@1.10.1:")
            depends_on("libtool@2.2.4:")
            depends_on("autoconf@2.62:")
            depends_on("m4")
            depends_on("gmake")
        variant("shared", default=True, description="Build shared libraries")
        variant("pic", default=True, description="Enable position-independent code (PIC)")
        requires("+pic", when="+shared")
    with when("build_system=cmake"):
        depends_on("cmake@3.12:3.31", type="build")
        variant("shared", default=True, description="Build shared libraries")
        variant("pic", default=True, description="Enable position-independent code (PIC)")
        requires("+pic", when="+shared")
    depends_on("meson@0.55:", type="build", when="build_system=meson")

    conflicts(
        "%intel",
        when="@2.8:2.10.2",
        msg="freetype-2.8 to 2.10.2 cannot be built with icc (does not support __builtin_shuffle)",
    )

    patch("windows.patch", when="@2.9.1")

    def url_for_version(self, version):
        url = "https://download.savannah.gnu.org/releases/{}/freetype-{}.tar.gz"
        if version >= Version("2.7"):
            directory = "freetype"
        else:
            directory = "freetype/freetype-old"
        return url.format(directory, version)

    @property
    def headers(self):
        headers = find_headers("*", self.prefix.include, recursive=True)
        headers.directories = [self.prefix.include.freetype2]
        return headers


class AutotoolsBuilder(AutotoolsBuilder):
    build_directory = "builds/unix"

    def configure_args(self):
        args = []
        if '+freetype-config' in self.spec:
            args.append("--enable-freetype-config")
        args.append('--enable-year2038')
        args.extend(self.enable_or_disable("shared"))
        args.extend(self.with_or_without("pic"))
        args.extend(self.with_or_without("brotli"))
        args.extend(self.with_or_without("bzip2"))
        harfbuzz_dep = self.spec.variants["harfbuzz"].value
        if harfbuzz_dep == "dynamic":
            args.append("--with-harfbuzz=dynamic")
        elif harfbuzz_dep == "yes":
            args.append("--with-harfbuzz=yes")
        else:
            assert harfbuzz_dep == "no", harfbuzz_dep
            args.append("--without-harfbuzz")
        args.extend(self.with_or_without("png"))
        args.extend(self.with_or_without("zlib"))
        args.extend(self.with_or_without("librsvg", variant="svg"))
        return args


class CMakeBuilder(CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define_from_variant("FT_REQUIRE_BROTLI", "brotli"),
            self.define_from_variant("FT_REQUIRE_BZIP2", "bzip2"),
            self.define_from_variant("FT_REQUIRE_PNG", "png"),
            self.define_from_variant("FT_REQUIRE_ZLIB", "zlib"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            self.define("FT_ENABLE_ERROR_STRINGS", True),
        ]
        if '~brotli' in self.spec:
            args.append(self.define("FT_DISABLE_BROTLI", True))
        if '~bzip2' in self.spec:
            args.append(self.define("FT_DISABLE_BZIP2", True))
        if '~png' in self.spec:
            args.append(self.define("FT_DISABLE_PNG", True))
        if '~zlib' in self.spec:
            args.append(self.define("FT_DISABLE_ZLIB", True),)
        harfbuzz_dep = self.spec.variants["harfbuzz"].value
        if harfbuzz_dep == "dynamic":
            args.append(self.define("FT_DYNAMIC_HARFBUZZ", True))
        elif harfbuzz_dep == "yes":
            args.append(self.define("FT_REQUIRE_HARFBUZZ", True))
        else:
            assert harfbuzz_dep == "no", harfbuzz_dep
            args.append(self.define("FT_DISABLE_HARFBUZZ", True))
        return args

class MesonBuilder(MesonBuilder):
    def meson_args(self):
        args = [
            self.enable_from_variant("brotli"),
            self.enable_from_variant("bzip2"),
            self.enable_from_variant("png"),
            self.enable_from_variant("zlib"),
            self.define("error_strings", True),
        ]
        harfbuzz_dep = self.spec.variants["harfbuzz"].value
        if harfbuzz_dep == "dynamic":
            args.append(self.define("harfbuzz", "dynamic"))
        elif harfbuzz_dep == "yes":
            args.append(self.define("harfbuzz", True))
        else:
            assert harfbuzz_dep == "no", harfbuzz_dep
            args.append(self.define("harfbuzz", False))
        return args
