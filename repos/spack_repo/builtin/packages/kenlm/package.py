# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Kenlm(CMakePackage):
    """Faster and Smaller Language Model Queries with KenML"""

    homepage = "https://kheafield.com/code/kenlm/"
    git = "https://github.com/kpu/kenlm.git"

    version("master", branch="master")

    variant("python", default=True, description="Build Python bindings")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.10:", type="build")
    depends_on("boost@1.41.0: +program_options +thread +system +test", type="build")
    depends_on("eigen@3.1.0:", type="build")

    extends("python", when="+python")
    # Python 3.13 breaks the build
    # https://github.com/kpu/kenlm/pull/468
    # https://github.com/kpu/kenlm/pull/473
    depends_on("python@:3.12", when="+python", type=("build", "run"))
    depends_on("py-cython@0.29.35:", type="build", when="+python")

    def cmake_args(self):
        return [
            self.define("BUILD_SHARED_LIBS", False),
            self.define("KENLM_MAX_ORDER", 6),
            self.define_from_variant("ENABLE_PYTHON", "python"),
        ]

    def setup_build_environment(self, env):
        env.set("CXXFLAGS", "-fPIC")
