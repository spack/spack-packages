# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re
import sys
from contextlib import contextmanager

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Perl(Package):  # Perl doesn't use Autotools, it should subclass Package
    """Perl 5 is a highly capable, feature-rich programming language with over
    27 years of development."""

    homepage = "https://www.perl.org"
    # URL must remain http:// so Spack can bootstrap curl
    url = "http://www.cpan.org/src/5.0/perl-5.34.0.tar.gz"
    tags = ["windows", "build-tools"]

    maintainers("LydDeb")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    executables = [r"^perl(-?\d+.*)?$"]

    # TODO: resolve the circular dependency between perl and libxcrypt.
    unresolved_libraries = ["libcrypt.so.*"]

    # see https://www.cpan.org/src/README.html for
    # explanation of version numbering scheme

    # Maintenance releases (even numbers)
    version("5.42.0", sha256="e093ef184d7f9a1b9797e2465296f55510adb6dab8842b0c3ed53329663096dc")
    version("5.40.2", sha256="10d4647cfbb543a7f9ae3e5f6851ec49305232ea7621aed24c7cfbb0bef4b70d")
    version("5.40.0", sha256="c740348f357396327a9795d3e8323bafd0fe8a5c7835fc1cbaba0cc8dfe7161f")

    # Development releases (odd numbers)
    version("5.39.10", sha256="4b7ffb3e068583fa5c8413390c998b2c15214f205ce737acc485b40932b9f419")

    extendable = True

    depends_on("c", type="build")  # generated

    if sys.platform != "win32":
        depends_on("gmake", type="build")
        depends_on("gdbm")
        depends_on("berkeley-db")
        depends_on("bzip2")
        depends_on("zlib-api")

    conflicts("%msvc@:19.29.30136")
    conflicts("%nvhpc@:20.11")

    # Make sure we don't get "recompile with -fPIC" linker errors when using static libs
    conflicts("^zlib~shared~pic", msg="Needs position independent code when using static zlib")
    conflicts("^bzip2~shared~pic", msg="Needs position independent code when using static bzip2")

    # Installing cpanm alongside the core makes it safe and simple for
    # people/projects to install their own sets of perl modules.  Not
    # having it in core increases the "energy of activation" for doing
    # things cleanly.
    variant("cpanm", default=True, description="Optionally install cpanm with the core packages.")
    variant("shared", default=True, description="Build a shared libperl.so library")
    variant("threads", default=True, description="Build perl with threads support")
    variant("open", default=True, description="Support open.pm")
    variant("opcode", default=True, description="Support Opcode.pm")

    resource(
        name="cpanm",
        url="http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/App-cpanminus-1.7042.tar.gz",
        sha256="9da50e155df72bce55cb69f51f1dbb4b62d23740fb99f6178bb27f22ebdf8a46",
        destination="cpanm",
        placement="cpanm",
    )

    phases = ["configure", "build", "install"]

    def patch(self):
        # https://github.com/Perl/perl5/issues/15544 long PATH(>1000 chars) fails a test
        os.chmod("lib/perlbug.t", 0o644)
        filter_file("!/$B/", "! (/(?:$B|PATH)/)", "lib/perlbug.t")
        # Several non-existent flags cause Intel@19.1.3 to fail
        with when("%intel@19.1.3"):
            os.chmod("hints/linux.sh", 0o644)
            filter_file("-we147 -mp -no-gcc", "", "hints/linux.sh")

    @classmethod
    def determine_version(cls, exe):
        perl = Executable(exe)
        output = perl("--version", output=str, error=str)
        if output:
            match = re.search(r"perl.*\(v([0-9.]+)\)", output)
            if match:
                return match.group(1)
        return None

    @classmethod
    def determine_variants(cls, exes, version):
        for exe in exes:
            perl = Executable(exe)
            output = perl("-V", output=str, error=str)
            variants = ""
            if output:
                match = re.search(r"-Duseshrplib", output)
                if match:
                    variants += "+shared"
                else:
                    variants += "~shared"
                match = re.search(r"-Duse.?threads", output)
                if match:
                    variants += "+threads"
                else:
                    variants += "~threads"
            path = os.path.dirname(exe)
            if "cpanm" in os.listdir(path):
                variants += "+cpanm"
            else:
                variants += "~cpanm"
            # this is just to detect incomplete installs
            # normally perl installs open.pm
            perl(
                "-e",
                "use open OUT => qw(:raw)",
                output=os.devnull,
                error=os.devnull,
                fail_on_error=False,
            )
            variants += "+open" if perl.returncode == 0 else "~open"
            # this is just to detect incomplete installs
            # normally perl installs Opcode.pm
            perl("-e", "use Opcode", output=os.devnull, error=os.devnull, fail_on_error=False)
            variants += "+opcode" if perl.returncode == 0 else "~opcode"
            return variants

    # On a lustre filesystem, patch may fail when files
    # aren't writeable so make pp.c user writeable
    # before patching. This should probably walk the
    # source and make everything writeable in the future.
    # The patch "zlib-ng.patch" also fail. So, apply chmod
    # to Makefile.PL and Zlib.xs too.
    def do_stage(self, mirror_only=False):
        # Do Spack's regular stage
        super().do_stage(mirror_only)
        # Add write permissions on files to be patched
        files_to_chmod = [
            join_path(self.stage.source_path, "pp.c"),
            join_path(self.stage.source_path, "cpan/Compress-Raw-Zlib/Makefile.PL"),
            join_path(self.stage.source_path, "cpan/Compress-Raw-Zlib/Zlib.xs"),
        ]
        for filename in files_to_chmod:
            try:
                perm = os.stat(filename).st_mode
                os.chmod(filename, perm | 0o200)
            except OSError:
                continue

    def nmake_arguments(self):
        args = []
        if self.spec.satisfies("%msvc"):
            args.append("CCTYPE=%s" % self["msvc"].short_msvc_version)
        else:
            raise RuntimeError("Perl unsupported for non MSVC compilers on Windows")
        args.append("INST_TOP=%s" % windows_sfn(self.prefix.replace("/", "\\")))
        args.append("INST_ARCH=\\$(ARCHNAME)")
        if self.spec.satisfies("~shared"):
            args.append("ALL_STATIC=%s" % "define")
        if self.spec.satisfies("~threads"):
            args.extend(["USE_MULTI=undef", "USE_ITHREADS=undef", "USE_IMP_SYS=undef"])
        if not self.is_64bit():
            args.append("WIN64=undef")
        return args

    def is_64bit(self):
        return "64" in str(self.spec.target.family)

    def configure_args(self):
        spec = self.spec
        prefix = self.prefix

        config_args = [
            "-des",
            "-Dprefix={0}".format(prefix),
            "-Dlocincpth=" + self.spec["gdbm"].prefix.include,
            "-Dloclibpth=" + self.spec["gdbm"].prefix.lib,
        ]

        # Extensions are installed into their private tree via
        # `INSTALL_BASE`/`--install_base` (see [1]) which results in a
        # "predictable" installation tree that sadly does not match the
        # Perl core's @INC structure.  This means that when activation
        # merges the extension into the extendee[2], the directory tree
        # containing the extensions is not on @INC and the extensions can
        # not be found.
        #
        # This bit prepends @INC with the directory that is used when
        # extensions are activated [3].
        #
        # [1] https://metacpan.org/pod/ExtUtils::MakeMaker#INSTALL_BASE
        # [2] via the activate method in the PackageBase class
        # [3] https://metacpan.org/pod/distribution/perl/INSTALL#APPLLIB_EXP
        config_args.append('-Accflags=-DAPPLLIB_EXP=\\"' + self.prefix.lib.perl5 + '\\"')

        # Discussion of -fPIC for Intel at:
        # https://github.com/spack/spack/pull/3081 and
        # https://github.com/spack/spack/pull/4416
        if spec.satisfies("%intel"):
            config_args.append("-Accflags={0}".format(self["c"].pic_flag))

        if "+shared" in spec:
            config_args.append("-Duseshrplib")

        if "+threads" in spec:
            config_args.append("-Dusethreads")

        # Development versions have an odd second component
        if spec.version[1] % 2 == 1:
            config_args.append("-Dusedevel")

        return config_args

    def configure(self, spec, prefix):
        if sys.platform == "win32":
            return
        configure = Executable("./Configure")
        # The Configure script plays with file descriptors and runs make towards the end,
        # which results in job tokens not being released under the make jobserver. So, we
        # disable the jobserver here, and let the Configure script execute make
        # sequentially. There is barely any parallelism anyway; the most parallelism is
        # in the build phase, in which the jobserver is enabled again, since we invoke make.
        configure.add_default_env("MAKEFLAGS", "")
        configure(*self.configure_args())

    def build(self, spec, prefix):
        if sys.platform == "win32":
            pass
        else:
            make()

    @run_after("build")
    @on_package_attributes(run_tests=True)
    def build_test(self):
        if sys.platform == "win32":
            win32_dir = os.path.join(self.stage.source_path, "win32")
            win32_dir = windows_sfn(win32_dir)
            with working_dir(win32_dir):
                nmake("test", ignore_quotes=True)
        else:
            make("test")

    def install(self, spec, prefix):
        if sys.platform == "win32":
            win32_dir = os.path.join(self.stage.source_path, "win32")
            win32_dir = windows_sfn(win32_dir)
            with working_dir(win32_dir):
                nmake("install", *self.nmake_arguments(), ignore_quotes=True)
        else:
            make("install")

    @run_after("install")
    def symlink_windows(self):
        if sys.platform != "win32":
            return
        win_install_path = os.path.join(self.prefix.bin, "MSWin32")
        if self.is_64bit():
            win_install_path += "-x64"
        else:
            win_install_path += "-x86"
        if self.spec.satisfies("+threads"):
            win_install_path += "-multi-thread"
        else:
            win_install_path += "-perlio"

        for f in os.listdir(os.path.join(self.prefix.bin, win_install_path)):
            lnk_path = os.path.join(self.prefix.bin, f)
            src_path = os.path.join(win_install_path, f)
            if not os.path.exists(lnk_path):
                symlink(src_path, lnk_path)

    @run_after("install")
    def install_cpanm(self):
        maker = make
        cpan_dir = join_path("cpanm", "cpanm")
        if sys.platform == "win32":
            maker = nmake
            cpan_dir = join_path(self.stage.source_path, cpan_dir)
            cpan_dir = windows_sfn(cpan_dir)
        if "+cpanm" in self.spec:
            with working_dir(cpan_dir):
                self.command("Makefile.PL")
                maker()
                maker("install")

    def _setup_dependent_env(self, env: EnvironmentModifications, dependent_spec: Spec):
        """Set PATH and PERL5LIB to include the extension and
        any other perl extensions it depends on,
        assuming they were installed with INSTALL_BASE defined."""
        perl_lib_dirs = []
        if dependent_spec.package.extends(self.spec):
            perl_lib_dirs.append(dependent_spec.prefix.lib.perl5)
        if perl_lib_dirs:
            perl_lib_path = ":".join(perl_lib_dirs)
            env.prepend_path("PERL5LIB", perl_lib_path)
        if sys.platform == "win32":
            env.append_path("PATH", self.prefix.bin)

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        self._setup_dependent_env(env, dependent_spec)

    def setup_dependent_run_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        self._setup_dependent_env(env, dependent_spec)

    def setup_dependent_package(self, module, dependent_spec):
        """Called before perl modules' install() methods.
        In most cases, extensions will only need to have one line:
        perl('Makefile.PL','INSTALL_BASE=%s' % self.prefix)
        """

        # If system perl is used through packages.yaml
        # there cannot be extensions.
        if dependent_spec.package.is_extension:
            # perl extension builds can have a global perl
            # executable function
            module.perl = self.command

            # Add variables for library directory
            module.perl_lib_dir = dependent_spec.prefix.lib.perl5

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if sys.platform == "win32":
            env.append_path("PATH", self.prefix.bin)
            return

        spec = self.spec

        # This is how we tell perl the locations of bzip and zlib.
        env.set("BUILD_BZIP2", "0")
        env.set("BZIP2_INCLUDE", spec["bzip2"].prefix.include)
        env.set("BZIP2_LIB", spec["bzip2"].libs.directories[0])
        env.set("BUILD_ZLIB", "0")
        env.set("ZLIB_INCLUDE", spec["zlib-api"].prefix.include)
        env.set("ZLIB_LIB", spec["zlib-api"].libs.directories[0])

    @run_after("install")
    def filter_config_dot_pm(self):
        """Run after install so that Config.pm records the compiler that Spack
        built the package with.  If this isn't done, $Config{cc} will
        be set to Spack's cc wrapper script.  These files are read-only, which
        frustrates filter_file on some filesystems (NFSv4), so make them
        temporarily writable.
        """
        if sys.platform == "win32":
            return
        kwargs = {"ignore_absent": True, "backup": False, "string": False}

        # Find the actual path to the installed Config.pm file.
        config_dot_pm = self.command(
            "-MModule::Loaded", "-MConfig", "-e", "print is_loaded(Config)", output=str
        )

        c_compiler = self["c"].cc
        with self.make_briefly_writable(config_dot_pm):
            match = "cc *=>.*"
            substitute = "cc => '{cc}',".format(cc=c_compiler)
            filter_file(match, substitute, config_dot_pm, **kwargs)

        # And the path Config_heavy.pl
        d = os.path.dirname(config_dot_pm)
        config_heavy = join_path(d, "Config_heavy.pl")

        with self.make_briefly_writable(config_heavy):
            match = "^cc=.*"
            substitute = "cc='{cc}'".format(cc=c_compiler)
            filter_file(match, substitute, config_heavy, **kwargs)

            match = "^ld=.*"
            substitute = "ld='{ld}'".format(ld=c_compiler)
            filter_file(match, substitute, config_heavy, **kwargs)

            match = "^ccflags='"
            substitute = "ccflags='%s " % " ".join(self.spec.compiler_flags["cflags"])
            filter_file(match, substitute, config_heavy, **kwargs)

    @contextmanager
    def make_briefly_writable(self, path):
        """Temporarily make a file writable, then reset"""
        perm = os.stat(path).st_mode
        os.chmod(path, perm | 0o200)
        yield
        os.chmod(path, perm)

    @property
    def command(self):
        """Returns the Perl command, which may vary depending on the version
        of Perl. In general, Perl comes with a ``perl`` command. However,
        development releases have a ``perlX.Y.Z`` command.

        Returns:
            Executable: the Perl command
        """
        for ver in ("", self.spec.version):
            ext = ""
            if sys.platform == "win32":
                ext = ".exe"
            path = os.path.join(self.prefix.bin, f"{self.spec.name}{ver}{ext}")
            if os.path.exists(path):
                return Executable(path)
        else:
            raise RuntimeError(f"Unable to locate {self.spec.name} command in {self.prefix.bin}")

    def test_version(self):
        """check version"""
        out = self.command("--version", output=str.split, error=str.split)
        expected = ["perl", str(self.spec.version)]
        for expect in expected:
            assert expect in out

    def test_hello(self):
        """ensure perl runs hello world"""
        msg = "Hello, World!"
        options = ["-e", "use warnings; use strict;\nprint('%s\n');" % msg]

        out = self.command(*options, output=str.split, error=str.split)
        assert msg in out
