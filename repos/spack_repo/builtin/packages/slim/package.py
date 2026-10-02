# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Slim(CMakePackage):
    """SLiM is a general-purpose, forward-in-time population genetics simulation
    framework, combining a fast engine written in C++ with the embedded Eidos
    scripting language for configuring models. It builds the `slim` and `eidos`
    command-line tools, with an optional Qt-based GUI (SLiMgui) available
    through the `gui` variant.

    This recipe is developed and validated against Amazon Linux 2023, the
    target deployment platform for this cluster. SLiM's command-line build has
    no platform-specific code paths, so other platforms are expected to work
    but are not the validated target.
    """

    homepage = "https://messerlab.org/slim/"
    url = "https://github.com/MesserLab/SLiM/archive/refs/tags/v5.2.tar.gz"
    git = "https://github.com/MesserLab/SLiM.git"

    maintainers("jaguillette")

    license("GPL-3.0-or-later")

    version("5.2", sha256="ec13f5bcc1784786a556594fa362605cc569b66d3e31838513ab71138df65341")
    version("5.1", sha256="e8341014271d12cd872c78738c4c80e57864fb0fb2e33b44ae6b7aedf364fc56")
    version("4.3", sha256="b390a6638a915d6f955608610bca6e94fc0f4d62f5ad07376b2aa98756e8c81d")

    variant("gui", default=False, description="Build the Qt-based SLiMgui GUI")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    # Upstream requires only CMake 2.8.12 for the CLI build and 3.1.0 when
    # SLiMgui is enabled; pinning to the higher floor unconditionally is
    # simpler and is already satisfied by any reasonably modern CMake.
    depends_on("cmake@3.1:", type="build")

    # SLiM vendors GSL, Boost, tskit, and zlib directly into its source tree,
    # so the command-line `slim`/`eidos` build has no external dependencies
    # beyond a C/C++ compiler and CMake.

    # SLiMgui's CMakeLists.txt tries Qt6 first, falling back to Qt5; this
    # package targets the Qt6 path only via qt-base, matching the modern
    # dependency this repo already prefers for other Qt6-capable GUI apps.
    depends_on("qt-base +gui+widgets+opengl", when="+gui")
    # SLiMgui's CMakeLists.txt also calls find_package(OpenGL REQUIRED)
    # directly (not just through Qt), and links OpenGL::GL itself.
    depends_on("gl", when="+gui")

    def cmake_args(self):
        return [self.define_from_variant("BUILD_SLIMGUI", "gui")]

    def test_slim(self):
        """run SLiM's built-in self-test"""
        with test_part(self, "test_slim", purpose="check `slim -testSLiM` reports SUCCESS"):
            slim = which(self.prefix.bin.slim, required=True)
            out = slim("-testSLiM", output=str, error=str)
            assert "SUCCESS" in out

    def test_eidos(self):
        """run Eidos's built-in self-test"""
        with test_part(self, "test_eidos", purpose="check `eidos -testEidos` reports SUCCESS"):
            eidos = which(self.prefix.bin.eidos, required=True)
            out = eidos("-testEidos", output=str, error=str)
            assert "SUCCESS" in out
