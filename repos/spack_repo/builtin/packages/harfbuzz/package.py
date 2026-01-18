# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import sys

from spack_repo.builtin.build_systems import autotools, cmake, meson
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.meson import MesonPackage

from spack.package import *

IS_WINDOWS = sys.platform == "win32"


class Harfbuzz(MesonPackage, AutotoolsPackage, CMakePackage):
    """The Harfbuzz package contains an OpenType text shaping engine."""

    homepage = "https://github.com/harfbuzz/harfbuzz"
    url = "https://github.com/harfbuzz/harfbuzz/releases/download/9.0.0/harfbuzz-9.0.0.tar.xz"
    git = "https://github.com/harfbuzz/harfbuzz.git"

    build_system(
        conditional("autotools", when="@:2.9"),
        conditional("meson", when="@3:"),
        conditional("cmake", when="@10:"),
        default="meson" if not IS_WINDOWS else "cmake",
    )

    # HarfBuzz is licensed under the so-called "Old MIT" license,
    # for which no SPDX identifier is listed at https://spdx.org/licenses/
    # Ref: https://github.com/harfbuzz/harfbuzz/blob/main/COPYING
    license("MIT-old", checked_by="wdconinc")

    maintainers("AlexanderRichert-NOAA")

    version("11.5.1", sha256="972a60a8d274d49e70361da6920c3a73dfb0fb4387f6c6811906a47ba634d8a1")
    version("11.4.1", sha256="7aafab93115eb56cdc9a931ab7d19ff60d7f2937b599d140f17236f374e32698")
    version("11.3.3", sha256="e1fbca6b32a91ae91ecd9eb2ca8d47a5bfe2b1cb2e54855ab7a0b464919ef358")
    version("11.2.1", sha256="093714c8548a285094685f0bdc999e202d666b59eeb3df2ff921ab68b8336a49")
    version("11.2.0", sha256="50f7d0a208367e606dbf6eecc5cfbecc01a47be6ee837ae7aff2787e24b09b45")
    version("11.1.0", sha256="477f0d48c34dc32093b45304178eb9733361ca1832b5159879c99e6d40227969")
    version("11.0.1", sha256="4a7890090538136db64742073af4b4d776ab8b50e6855676a8165eb8b7f60b7a")
    version("11.0.0", sha256="f16351bafe214725fe2c1d5b59f0d93e49905a4b247899fb90d70cff953a2b9b")
    version("10.4.0", sha256="480b6d25014169300669aa1fc39fb356c142d5028324ea52b3a27648b9beaad8")
    version("10.3.0", sha256="cd63fc3cbae32622588e46e0670fabf78ee6cff44a6348ca7f037dae9a32f9ea")
    version("10.2.0", sha256="620e3468faec2ea8685d32c46a58469b850ef63040b3565cde05959825b48227")
    version("10.1.0", sha256="6ce3520f2d089a33cef0fc48321334b8e0b72141f6a763719aaaecd2779ecb82")
    version("10.0.1", sha256="b2cb13bd351904cb9038f907dc0dee0ae07127061242fe3556b2795c4e9748fc")
    version("10.0.0", sha256="c2dfe016ad833a5043ecc6579043f04e8e6d50064e02ad449bb466e6431e3e04")
    version("9.0.0", sha256="a41b272ceeb920c57263ec851604542d9ec85ee3030506d94662067c7b6ab89e")
    version("8.5.0", sha256="77e4f7f98f3d86bf8788b53e6832fb96279956e1c3961988ea3d4b7ca41ddc27")
    version("8.4.0", sha256="af4ea73e25ab748c8c063b78c2f88e48833db9b2ac369e29bd115702e789755e")
    version("8.3.1", sha256="f73e1eacd7e2ffae687bc3f056bb0c705b7a05aee86337686e09da8fc1c2030c")
    version("8.3.0", sha256="109501eaeb8bde3eadb25fab4164e993fbace29c3d775bcaa1c1e58e2f15f847")
    version("7.3.0", sha256="20770789749ac9ba846df33983dbda22db836c70d9f5d050cb9aa5347094a8fb")
    version("7.2.0", sha256="fc5560c807eae0efd5f95b5aa4c65800c7a8eed6642008a6b1e7e3ffff7873cc")
    version("6.0.0", sha256="1d1010a1751d076d5291e433c138502a794d679a7498d1268ee21e2d4a140eb4")
    version("5.3.1", sha256="4a6ce097b75a8121facc4ba83b5b083bfec657f45b003cd5a3424f2ae6b4434d")
    version("5.1.0", sha256="2edb95db668781aaa8d60959d21be2ff80085f31b12053cdd660d9a50ce84f05")
    version("4.2.1", sha256="bd17916513829aeff961359a5ccebba6de2f4bf37a91faee3ac29c120e3d7ee1")
    version("4.1.0", sha256="f7984ff4241d4d135f318a93aa902d910a170a8265b7eaf93b5d9a504eed40c8")
    version("4.0.1", sha256="98f68777272db6cd7a3d5152bac75083cd52a26176d87bc04c8b3929d33bce49")
    version("3.4.0", sha256="7158a87c4db82521fc506711f0c8864115f0292d95f7136c8812c11811cdf952")
    version("3.3.2", sha256="1c13bca136c4f66658059853e2c1253f34c88f4b5c5aba6050aba7b5e0ce2503")
    version("3.2.0", sha256="0ada50a1c199bb6f70843ab893c55867743a443b84d087d54df08ad883ebc2cd")
    version("3.1.2", sha256="4056b1541dd8bbd8ec29207fe30e568805c0705515632d7fec53a94399bc7945")
    version(
        "2.9.1",
        sha256="0edcc980f526a338452180e701d6aba6323aef457b6686976a7d17ccbddc51cf",
        deprecated=True,
    )

    variant("graphite2", default=False, description="enable support for graphite2 font engine")
    variant(
        "coretext",
        default=False,
        when="platform=darwin",
        description="Enable CoreText shaper backend on macOS",
    )
    variant("shared", default=True, when="build_system=cmake", description="Build shared harfbuzz")

    with when("build_system=cmake"):
        with when("platform=windows"):
            variant(
                "uniscribe",
                default=False,
                description="Enable Uniscribe shaper backend on Windows",
            )
            variant(
                "directwrite",
                default=False,
                description="Enable directwrite shaper backend on Windows",
            )
            variant("gdi", default=False, description="Enable GDI integration helpers on Windows")
        # CMake system dropped a number of source files
        # they're correctly added as of 11.5
        patch("harfbuzz_10_0_cmake_add_missing_table_sources.patch", when="@10:11.1")
        patch("harfbuzz_11_2_cmake_add_missing_table_sources.patch", when="@11.2:11.3")
        patch("harfbuzz_11_4_cmake_add_missing_table_sources.patch", when="@11.4")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with when("build_system=meson"):
        depends_on("meson@0.60:", when="@11.1:")
        depends_on("meson@0.55:", when="@3.2.1:")
        depends_on("meson@0.52:")
        # harfbuzz's Meson only supports autotools based
        # freetype
        depends_on("freetype build_system=autotools")
        depends_on("cairo build_system=meson")

    for plat in ["linux", "darwin", "freebsd"]:
        with when(f"platform={plat}"):
            variant("gobject", default=False, description="Enable GObject introspection")
            variant(
                "utils",
                default=False,
                when="build_system=cmake",
                description="Build harfbuzz utils",
            )
            depends_on("pkgconfig", type="build")
            depends_on("glib")
            depends_on("gobject-introspection")
            depends_on("cairo+pdf+ft")

    depends_on("icu4c")
    depends_on("freetype")
    depends_on("zlib-api")
    depends_on("graphite2", when="+graphite2")

    conflicts("%intel", msg="harfbuzz-2.3.1 does not build with the Intel compiler")

    # Function borrowed from superlu
    def flag_handler(self, name, flags):
        flags = list(flags)
        if name == "cxxflags":
            flags.append(self.compiler.cxx11_flag)
        if name == "cflags":
            if self.spec.satisfies("%gcc@:5.1"):
                flags.append("-std=gnu99")
        return None, None, flags

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("GI_TYPELIB_PATH", join_path(self.prefix.lib, "girepository-1.0"))

    def setup_dependent_run_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)
        env.prepend_path("GI_TYPELIB_PATH", join_path(self.prefix.lib, "girepository-1.0"))

    @when("@:8")
    def patch(self):
        change_sed_delimiter("@", ";", "src/Makefile.in")


class SetupEnvironment:
    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("XDG_DATA_DIRS", self.prefix.share)
        env.prepend_path("GI_TYPELIB_PATH", join_path(self.prefix.lib, "girepository-1.0"))


class MesonBuilder(meson.MesonBuilder, SetupEnvironment):
    def meson_args(self):
        graphite2 = "enabled" if self.pkg.spec.satisfies("+graphite2") else "disabled"
        coretext = "enabled" if self.pkg.spec.satisfies("+coretext") else "disabled"
        introspection = "enabled" if self.pkg.spec.satisfies("+gobject") else "disabled"
        config_args = [
            # disable building of gtk-doc files following #9885 and #9771
            "-Ddocs=disabled",
            "-Dfreetype=enabled",
            f"-Dgraphite2={graphite2}",
            f"-Dcoretext={coretext}",
            f"-Dintrospection={introspection}",
        ]
        if IS_WINDOWS:
            config_args.extend(["-Dcairo=disabled", "-Dglib=disabled"])
        return config_args


class AutotoolsBuilder(autotools.AutotoolsBuilder, SetupEnvironment):
    def configure_args(self):
        args = []

        # disable building of gtk-doc files following #9771
        args.append("--disable-gtk-doc-html")
        true = which("true")
        args.append(f"GTKDOC_CHECK={true}")
        args.append(f"GTKDOC_CHECK_PATH={true}")
        args.append(f"GTKDOC_MKPDF={true}")
        args.append(f"GTKDOC_REBASE={true}")
        args.extend(self.with_or_without("graphite2"))
        args.extend(self.with_or_without("coretext"))
        args.extend(self.with_or_without("gobject"))

        return args


class CMakeBuilder(cmake.CMakeBuilder, SetupEnvironment):
    def cmake_args(self):
        use_gobject = self.spec.satisfies("+gobject")
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("HB_HAVE_FREETYPE", True),
            self.define("HB_HAVE_ICU", True),
            self.define_from_variant("HB_HAVE_GRAPHITE2", "graphite2"),
            self.define_from_variant("HB_HAVE_UNISCRIBE", "uniscribe"),
            self.define_from_variant("HB_HAVE_GDI", "gdi"),
            self.define_from_variant("HB_HAVE_DIRECTWRITE", "directwrite"),
            self.define_from_variant("HB_HAVE_CORETEXT", "coretext"),
            self.define("HB_HAVE_GLIB", use_gobject),
            self.define("HB_HAVE_CAIRO", use_gobject),
            self.define("HB_BUILD_UTILS", use_gobject and self.spec.satisfies("+utils")),
            self.define("HB_HAVE_GOBJECT", use_gobject),
            self.define("HB_HAVE_INTROSPECTION", use_gobject),
        ]

        return args
