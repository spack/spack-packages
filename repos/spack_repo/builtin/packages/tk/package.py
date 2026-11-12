# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack_repo.builtin.build_systems import autotools, nmake
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.nmake import NMakePackage
from spack_repo.builtin.build_systems.sourceforge import SourceforgePackage

from spack.package import *

# Tk's nmake build needs two files from the *paired* Tcl release (see the
# "platform=windows" block in the Tk class below and
# NMakeBuilder.fixup_tk_nmake_build): win/tclWinPort.h and win/rules.vc.
# Keyed by Tk version: (tcl commit sha, tclWinPort.h sha256, rules.vc sha256).
_TCL_WIN_FILES = {
    "9.0.2": (
        "9b38e7eaac00e5617f1c6d51f8ca38798674a091",
        "dacfd960292c80512b9c36e315a929b89af033c860b29f178b4443f712da8de6",
        "1b468a44b64231c86b020e3e320770d96b2632e61f4da437666fd01b4857a961",
    ),
    "8.6.17": (
        "433df5b20a8bd6957c3bda981c83d65202eb7de7",
        "492d73b19ea26bebbc71f92a0dbbd121f9d3dd36707ce407f1ee585a376d08c7",
        "fc8a1f19537357a90a3f534cd0280b1e7eaa6fe724a54e55f5fd7675930c3fb9",
    ),
    "8.6.11": (
        "17b5b3e0201cdf92d3c125776e1b2dd453f225bd",
        "44f68347bf3f79e872b5d9813eeb4683198a8fccce6e7710d03220954d0fd50e",
        "7c284c0c9cb96652ba5da72de0449a796a790b4c51781826886d057a975612e0",
    ),
    "8.6.10": (
        "f19d3d1f630f128feddb2728f4c8d222934a38ee",
        "a74dcca2e283daef16b73df94e5a192b3ad584c833f37d6e2ebee54be91b88cb",
        "36ba572910ec7247757579a8412ce964013db1e37078ce40daf66a765736ab32",
    ),
    "8.6.8": (
        "1725b7469560f802f132a87abce59ae3228dd0ed",
        "f6ee7759309a231e1f00fbbb5199a2abb9a6c974a7d190e670451f1df4cef743",
        "e06f07354c193ffc300b2845ea9a4b2eec4e00d3137a982a95c7285c2df8a990",
    ),
}


class Tk(AutotoolsPackage, NMakePackage, SourceforgePackage):
    """Tk is a graphical user interface toolkit that takes developing desktop
    applications to a higher level than conventional approaches. Tk is the standard GUI
    not only for Tcl, but for many other dynamic languages, and can produce rich, native
    applications that run unchanged across Windows, Mac OS X, Linux and more."""

    homepage = "https://www.tcl.tk"
    sourceforge_mirror_path = "tcl/tk8.6.5-src.tar.gz"
    tags = ["windows"]

    license("TCL")

    version("9.0.2", sha256="76fb852b2f167592fe8b41aa6549ce4e486dbf3b259a269646600e3894517c76")
    version(
        "8.6.17",
        sha256="e4982df6f969c08bf9dd858a6891059b4a3f50dc6c87c10abadbbe2fc4838946",
        preferred=True,
    )
    version("8.6.11", sha256="5228a8187a7f70fa0791ef0f975270f068ba9557f57456f51eb02d9d4ea31282")
    version("8.6.10", sha256="63df418a859d0a463347f95ded5cd88a3dd3aaa1ceecaeee362194bc30f3e386")
    version("8.6.8", sha256="49e7bca08dde95195a27f594f7c850b088be357a7c7096e44e1158c7a5fd7b33")
    version("8.6.6", sha256="d62c371a71b4744ed830e3c21d27968c31dba74dd2c45f36b9b071e6d88eb19d")
    version("8.6.5", sha256="fbbd93541b4cd467841208643b4014c4543a54c3597586727f0ab128220d7946")
    version("8.6.3", sha256="ba15d56ac27d8c0a7b1a983915a47e0f635199b9473cf6e10fbce1fc73fd8333")
    version("8.5.19", sha256="407af1de167477d598bd6166d84459a3bdccc2fb349360706154e646a9620ffa")

    variant("xft", default=True, description="Enable X FreeType")
    variant("xss", default=True, description="Enable X Screen Saver")

    extends("tcl", type=("build", "link", "run"))

    depends_on("c", type="build")

    depends_on("tcl@8.6:8.6", type=("build", "link", "run"), when="@8.6:8.6")
    depends_on("tcl@9.0:", type=("build", "link", "run"), when="@9.0:")
    depends_on("libx11", when="platform=linux")
    depends_on("libx11", when="platform=darwin")
    depends_on("libxft", when="+xft platform=linux")
    depends_on("libxft", when="+xft platform=darwin")
    depends_on("libxscrnsaver", when="+xss platform=linux")
    depends_on("libxscrnsaver", when="+xss platform=darwin")

    build_system("autotools", "nmake", default="autotools")

    # Tk's win/rules.vc (shared with Tcl, located via win/rules-ext.vc) hard-codes
    # "Tk always builds against Tcl source, not an installed Tcl" and refuses to
    # build otherwise despite the same file already knowing how to build
    # any *other* Tcl extension against an installed Tcl... We patch that one spot
    # (see fixup_tk_nmake_build) to make Tk use that same "installed
    # Tcl" logic instead of requiring a Tcl source tree, so Tk can be built and
    # installed as a fully independent package, like on every other platform.
    #
    # Tk's C sources also directly include exactly one Tcl header that Tcl does
    # not install publicly: win/tclWinPort.h (a small, self-contained Windows
    # porting shim, not a private API surface). We fetch just that single file,
    # matching the paired Tcl release, instead of vendoring any Tcl source.
    #
    # This build only works from Tk 8.6.8 onward:
    # - 8.5.19 needs Tcl's private tclInt.h/tclPort.h from generic/tkMain.c,
    #   which pulls in much more of Tcl's internals; not supported here.
    # - 8.6.3:8.6.6 ship their own self-contained win/rules.vc that never
    #   defines _WIN32_WINNT/NTDDI_VERSION, and fails to compile against
    #   modern Windows SDKs (syntax errors inside winnt.h); not worth
    #   chasing for old point releases.
    conflicts(
        "build_system=nmake",
        when="@:8.5",
        msg="tk's nmake build needs private Tcl headers for @:8.5; not supported",
    )
    conflicts(
        "build_system=nmake",
        when="@8.6.3:8.6.6",
        msg="tk@8.6.3:8.6.6's bundled nmake build files don't compile against "
        "modern Windows SDKs; not supported",
    )

    with when("platform=windows"):
        for _tk_ver, (_tcl_sha, _winport_sha256, _rules_sha256) in _TCL_WIN_FILES.items():
            resource(
                name="tclwinport-h",
                url=f"https://raw.githubusercontent.com/tcltk/tcl/{_tcl_sha}/win/tclWinPort.h",
                sha256=_winport_sha256,
                expand=False,
                placement="win",
                when=f"@{_tk_ver}",
            )
            resource(
                name="tcl-rules-vc",
                url=f"https://raw.githubusercontent.com/tcltk/tcl/{_tcl_sha}/win/rules.vc",
                sha256=_rules_sha256,
                expand=False,
                placement="win",
                when=f"@{_tk_ver}",
            )

    # https://core.tcl-lang.org/tk/tktview/3598664fffffffffffff
    # https://core.tcl-lang.org/tk/info/8b679f597b1d17ad
    # https://core.tcl-lang.org/tk/info/997b17c343444e48
    patch(
        "https://raw.githubusercontent.com/macports/macports-ports/v2.7.0-archive/x11/tk/files/patch-unix-Makefile.in.diff",
        sha256="54bba3d2b3550b7e2c636881c1a3acaf6e1eb743f314449a132864ff47fd0010",
        level=0,
        when="@:8.6.11 platform=darwin",
    )
    patch(
        "https://raw.githubusercontent.com/macports/macports-ports/v2.7.0-archive/x11/tk/files/patch-dyld_fallback_library_path.diff",
        sha256="9ce6512f1928db9987986f4d3540207c39429395d5234bd6489ba9d86a6d9c31",
        level=0,
        when="platform=darwin",
    )

    @property
    def _tk_name(self):
        ver_suffix = self.version.up_to(2)
        win_suffix = ""
        if sys.platform == "win32":
            if self.spec.satisfies("@:8.7"):
                win_suffix = "t"
            ver_suffix = ver_suffix.joined
        return f"{ver_suffix}{win_suffix}"

    def test_tk_help(self):
        """run tk help"""
        self.command("-h")

    def test_tk_load(self):
        """check that tk can be loaded"""
        test_data_dir = self.test_suite.current_test_data_dir
        test_file = test_data_dir.join("test.tcl")
        tcl = self.spec["tcl"].command
        tcl(test_file)

    @property
    def command(self):
        """Returns the wish command.

        Returns:
            Executable: the wish command
        """
        # Although we symlink wishX.Y to wish, we also need to support external
        # installations that may not have this symlink, or may have multiple versions
        # of Tk installed in the same directory.
        exe = ".exe" if sys.platform == "win32" else ""
        return Executable(os.path.realpath(self.prefix.bin.join(f"wish{self._tk_name}{exe}")))

    @property
    def libs(self):
        lib = "lib" if not sys.platform == "win32" else ""
        return find_libraries([f"{lib}tk{self._tk_name}"], root=self.prefix, recursive=True)

    def _find_script_dir(self):
        # Put more-specific prefixes first
        check_prefixes = [
            join_path(self.prefix, "share", "tk{0}".format(self.version.up_to(2))),
            self.prefix,
        ]
        for prefix in check_prefixes:
            result = find_first(prefix, "tk.tcl")
            if result:
                return os.path.dirname(result)
        raise RuntimeError("Cannot locate tk.tcl")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        """Set TK_LIBRARY to the directory containing tk.tcl.

        For further info, see:

        * https://www.tcl-lang.org/man/tcl/TkCmd/tkvars.htm
        """
        # When using tkinter from within spack provided python+tkinter,
        # python will not be able to find Tk unless TK_LIBRARY is set.
        env.set("TK_LIBRARY", self._find_script_dir())

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        """Set TK_LIBRARY to the directory containing tk.tcl.

        For further info, see:

        * https://www.tcl-lang.org/man/tcl/TkCmd/tkvars.htm
        """
        env.set("TK_LIBRARY", self._find_script_dir())


class AnyBuilder(BaseBuilder):
    @run_after("install")
    def symlink_wish(self):
        # There's some logic regarding this suffix in the build system
        # but the way Spack builds tk, the Windows suffix is always 't'
        # unless the version is >= 8.7, in which case there is no suffix
        # if the build is ever switched to static, this will need to change
        # to be "s[t]"
        win_suffix = ""
        ver_suffix = self.pkg.version.up_to(2)
        if sys.platform == "win32":
            win_suffix = "t" if self.spec.satisfies("@:8.7") else ""
            win_suffix += ".exe"
            ver_suffix = ver_suffix.joined

        with working_dir(self.prefix.bin):
            symlink(f"wish{ver_suffix}{win_suffix}", "wish")


class AutotoolsBuilder(AnyBuilder, autotools.AutotoolsBuilder):
    configure_directory = "unix"

    def configure_args(self):
        spec = self.spec
        config_args = [
            "--with-tcl={0}".format(spec["tcl"].libs.directories[0]),
            "--x-includes={0}".format(spec["libx11"].headers.directories[0]),
            "--x-libraries={0}".format(spec["libx11"].libs.directories[0]),
        ]
        config_args += self.enable_or_disable("xft")
        config_args += self.enable_or_disable("xss")

        return config_args

    def install(self, pkg, spec, prefix):
        with working_dir(self.build_directory):
            make("install")

            # Some applications like Expect require private Tk headers.
            make("install-private-headers")

            # Copy source to install tree
            installed_src = join_path(spec.prefix, "share", pkg.name, "src")
            stage_src = os.path.realpath(pkg.stage.source_path)
            install_tree(stage_src, installed_src)

            # Replace stage dir -> installed src dir in tkConfig
            filter_file(
                stage_src, installed_src, join_path(self.pkg.libs.directories[0], "tkConfig.sh")
            )


class NMakeBuilder(AnyBuilder, nmake.NMakeBuilder):
    build_targets = ["release"]
    install_targets = ["install"]

    @property
    def makefile_root(self):
        return f"{self.stage.source_path}\\win"

    @property
    def makefile_name(self):
        return "makefile.vc"

    def nmake_args(self):
        return [
            self.define("TCLDIR", windows_sfn(self.spec["tcl"].prefix)),
            # Keep the Tk script library on disk (rather than embedded into
            # wish/tk86t.dll) so the existing _find_script_dir()/TK_LIBRARY
            # logic keeps working on Windows.
            self.define("OPTS", "noembed"),
        ]

    def nmake_install_args(self):
        return [self.define("INSTALLDIR", self.spec.prefix)]

    @run_before("build")
    def fixup_tk_nmake_build(self):
        win_dir = join_path(self.stage.source_path, "win")

        # Same fix as tcl's own tcl-quote-cc-path.patch: unquoted $(CC) in
        # cc32's definition breaks as soon as CC is an absolute path with
        # spaces, which is exactly what Spack sets it to for MSVC.
        filter_file(
            "cc32\t\t= $(CC)   # built-in default.",
            'cc32\t\t= "$(CC)"   # built-in default.',
            join_path(win_dir, "rules.vc"),
            string=True,
        )

        # Tk's win/rules-ext.vc searches for a Tcl
        # installation or source tree that ships its own rules.vc/targets.vc,
        # to decide which copy of the shared nmake support files to use. We
        # always ship our own (patched) copy of rules.vc as a resource, so
        # replace rules-ext.vc with a minimal version that always uses it,
        # instead of searching for and requiring Tcl's copy.
        with open(join_path(win_dir, "rules-ext.vc"), "w") as f:
            f.write(
                "!ifndef _RULES_EXT_VC\n"
                '!if [$(CC) -nologo -DNDEBUG "nmakehlp.c" -link -subsystem:console > nul]\n'
                "!endif\n"
                "NMAKEHLPC = nmakehlp.c\n"
                '!include "rules.vc"\n'
                "!endif\n"
            )

        # The vendored rules.vc hard-requires Tcl's *source* tree when
        # building Tk (DOING_TK), even though the exact same file already
        # knows how to build any other Tcl extension against an installed
        # Tcl (the "Case 2(c)/(d)" logic below). Make Tk use that same
        # "installed Tcl" logic instead.
        filter_file(
            r"_TCL_H  = $(_TCLDIR)\generic\tcl.h",
            (
                '!if exist("$(_TCLDIR)\\include\\tcl.h")\n'
                "TCLINSTALL = 1\n"
                "_TCL_H  = $(_TCLDIR)\\include\\tcl.h\n"
                "!else\n"
                "TCLINSTALL = 0\n"
                "_TCL_H  = $(_TCLDIR)\\generic\\tcl.h\n"
                "!endif"
            ),
            join_path(win_dir, "rules.vc"),
            string=True,
        )
