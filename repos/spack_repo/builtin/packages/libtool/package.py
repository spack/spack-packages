# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *


class Libtool(AutotoolsPackage, GNUMirrorPackage):
    """GNU Libtool is a script and file format that hides the complexity of using shared libraries
    behind a consistent, portable interface.

    In particular, libtool addresses portability concerns regarding shared libraries across
    operating systems, each of which maintain strongly-held and highly-variant ideas of what
    a library is. This ecosystem has thus far failed to develop a regulatory mechanism that
    incentivizes reconciling this variance through standard extensions and modification points to
    achieve consistent semantics for maintainers and users.

    This leaves the lowest-common denominator for any attempt to unify these distinctions as the
    portable shell script: and this is the interface employed by libtool.

    An important corollary is that the libtool format also supports static libraries, and therefore
    does not impose the decision of static or dynamic linking behavior until the maintainer or
    downstream user generates their final export artifact.
    Without this crucial capability, build systems for C and C++ often tend to impose
    @/m{significant duplication} of labor and code to support both generating output for both
    linking modes.

    Libtool instead @_y{codifies} those distinctions into its artifact structure, and thereby makes
    build processes easier to audit and maintain over time.
    """
    docstring_uses_rich_text = True
    docstring_has_extended_text = True

    git = "https://git.savannah.gnu.org/git/libtool.git"
    homepage = "https://www.gnu.org/software/libtool/"
    gnu_mirror_path = "libtool/libtool-2.4.6.tar.gz"

    license("LGPL-2.0-or-later AND GPL-2.0-or-later")

    version("develop", branch="master", submodules=True)

    version("2.6.0", sha256="80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880")
    version("2.5.4", sha256="da8ebb2ce4dcf46b90098daf962cffa68f4b4f62ea60f798d0ef12929ede6adf")
    version("2.4.7", sha256="04e96c2404ea70c590c546eba4202a4e12722c640016c12b9b2f1ce3d481e9a8")
    version("2.4.6", sha256="e3bd4d5d3d025a36c21dd6af7ea818a2afcd4dfc1ea5a17b39d7854bcd0c06e3")

    depends_on("c", type="build")  # generated

    depends_on("m4@1.4.6:", type="build")

    # the following are places in which libtool depends on findutils
    # https://github.com/autotools-mirror/libtool/blob/v2.4.7/build-aux/ltmain.in#L3296
    # https://github.com/autotools-mirror/libtool/blob/v2.4.6/build-aux/ltmain.in#L3278
    depends_on("findutils", type=("build", "run"))
    depends_on("file", type=("build", "run"))

    with when("@2.4.6:"):
        depends_on("autoconf@2.62:", type="test")
        depends_on("automake", type="test")

    with when("@develop"):
        depends_on("autoconf", type="build")
        depends_on("automake", type="build")
        depends_on("help2man", type="build")
        depends_on("xz", type="build")
        depends_on("texinfo", type="build")
        # Fix parsing of compiler output when collecting predeps and postdeps
        # https://lists.gnu.org/archive/html/bug-libtool/2016-03/msg00003.html
        patch("flag_space.patch")

    build_directory = "spack-build"

    tags = ["build-tools"]

    executables = ["^g?libtool(ize)?$"]

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"\(GNU libtool\)\s+(\S+)", output)
        return match.group(1) if match else None

    @when("@develop")
    def autoreconf(self, spec, prefix):
        Executable("./bootstrap")()

    @property
    def libs(self):
        return find_libraries(["libltdl"], root=self.prefix, recursive=True, shared=True)

    def _make_executable(self, name):
        return Executable(join_path(self.prefix.bin, name))

    def patch(self):
        # Remove flags not recognized by the NVIDIA compiler
        if self.spec.satisfies("%nvhpc@:20.11"):
            filter_file("-fno-builtin", "-Mnobuiltin", "configure")
            filter_file("-fno-builtin", "-Mnobuiltin", "libltdl/configure")

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.append_path("ACLOCAL_PATH", self.prefix.share.aclocal)

    def setup_dependent_package(self, module, dependent_spec):
        # Automake is very likely to be a build dependency, so we add
        # the tools it provides to the dependent module. Some build
        # systems differentiate between BSD libtool (e.g., Darwin) and
        # GNU libtool, so also add 'glibtool' and 'glibtoolize' to the
        # list of executables. See Homebrew:
        # https://github.com/Homebrew/homebrew-core/blob/master/Formula/libtool.rb
        executables = ["libtoolize", "libtool", "glibtoolize", "glibtool"]
        for name in executables:
            setattr(module, name, self._make_executable(name))

    @run_after("install")
    def post_install(self):
        # Some platforms name GNU libtool and GNU libtoolize
        # 'glibtool' and 'glibtoolize', respectively, to differentiate
        # them from BSD libtool and BSD libtoolize. On these BSD
        # platforms, build systems sometimes expect to use the assumed
        # GNU commands glibtool and glibtoolize instead of the BSD
        # variant; this happens frequently, for instance, on Darwin
        symlink(join_path(self.prefix.bin, "libtool"), join_path(self.prefix.bin, "glibtool"))
        symlink(
            join_path(self.prefix.bin, "libtoolize"), join_path(self.prefix.bin, "glibtoolize")
        )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        """Wrapper until spack has a real implementation of setup_test_environment()"""
        if self.run_tests:
            self.setup_test_environment(env)

    def setup_test_environment(self, env: EnvironmentModifications):
        """When Fortran is not provided, a few tests need to be skipped"""
        if self.compiler.f77 is None:
            env.set("F77", "no")
        if self.compiler.fc is None:
            env.set("FC", "no")

    @when("@2.4.6")
    def check(self):
        """installcheck of libtool-2.4.6 runs the full testsuite, skip 'make check'"""
        pass
