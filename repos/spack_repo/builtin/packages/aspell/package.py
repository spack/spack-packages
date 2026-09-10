# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *


# See also: AspellDictPackage
class Aspell(AutotoolsPackage, GNUMirrorPackage):
    """GNU Aspell is a Free and Open Source spell checker designed to
    eventually replace Ispell."""

    homepage = "http://aspell.net/"
    gnu_mirror_path = "aspell/aspell-0.60.6.1.tar.gz"

    extendable = True  # support activating dictionaries

    maintainers("alecbcs")

    license("LGPL-2.1-or-later")

    version("0.60.8.2", sha256="57fe4863eae6048f72245a8575b44b718fb85ca14b9f8c0afc41b254dfd76919")
    version("0.60.8.1", sha256="d6da12b34d42d457fa604e435ad484a74b2effcd120ff40acd6bb3fb2887d21b")
    version("0.60.8", sha256="f9b77e515334a751b2e60daab5db23499e26c9209f5e7b7443b05235ad0226f2")
    version("0.60.6.1", sha256="f52583a83a63633701c5f71db3dc40aab87b7f76b29723aeb27941eff42df6e1")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("ncurses", type="link")

    patch("fix_cpp.patch")
    patch("issue-519.patch", when="@:0.60.6.1")

    # allow aspell to build with newer compilers that enforce template instantiation
    # e.g. gcc@15: and clang
    patch(
        "https://github.com/GNUAspell/aspell/commit/ee6cbb12ff36a1e6618d7388a78dd4e0a2b44041.patch?full_index=1",
        sha256="96e6b23947744e5d1374640a38cf20ec541b64c00a063cbed6d1fcc3e3fc19ee",
        when="@:0.60.8.1",
    )

    def configure_args(self):
        return [f"--enable-curses={self.spec['ncurses:wide'].libs.ld_flags}"]

    # workaround due to https://github.com/GNUAspell/aspell/issues/591
    @run_after("configure", when="@0.60.8:")
    def make_missing_files(self):
        make("gen/dirs.h")
        make("gen/static_filters.src.cpp")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("ASPELL_CONF", f"prefix {self.prefix}")
