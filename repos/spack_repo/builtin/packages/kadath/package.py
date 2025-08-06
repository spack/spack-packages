# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Kadath(CMakePackage):
    """KADATH SPECTRAL SOLVER.

    The Frankfurt University/Kadath (FUKA) Initial Data solver branch is
    a collection of ID solvers aimed at delivering consistent initial
    data (ID) solutions to the eXtended Conformal Thin-Sandwich (XCTS)
    formulation of Einstein's field equations for a variety of compact
    object configurations to include extremely compact, asymmetric, and
    mixed spin binaries.
    """

    homepage = "https://samueltootle.github.io/fuka/index.html"
    git = "https://bitbucket.org/fukaws/fuka.git"

    maintainers("eschnett")

    license("GPL-3.0-or-later")

    version("fuka", branch="fuka")
    version("2.3", tag="v2.3", commit="f8ee3c7795911e1363358bf155c70f649c100fb5")
    version(
        "ET_2025_05_v0", tag="ET_2025_05_v0", commit="f1259452c0a62eee3e37c2314691643659e02705"
    )
    version(
        "ET_2024_11_v0", tag="ET_2024_11_v0", commit="848b68cb9e7cf70b1e38b8135d4def6502db5aff"
    )
    version(
        "ET_2024_05_v0", tag="ET_2024_05_v0", commit="ac1b07452572a83c434a637c8171c02d0f36aafe"
    )
    version(
        "ET_2023_11_v0", tag="ET_2023_11_v0", commit="f6208ce5c2a0a9cdd7cd93611037ae077bed7265"
    )
    version("2.2", tag="v2.2", commit="c15aa72964bcddbaae1811cbab6dc2650e59b990")
    version("ET_2023_05v0", tag="ET_2023_05v0", commit="1e8e9c59dc0dc8746709b81c5c0c70dc73109309")
    version("2.1", tag="v2.1", commit="1e8e9c59dc0dc8746709b81c5c0c70dc73109309")

    variant("mpi", default=True, description="Enable MPI support")

    variant(
        "codes",
        multi=True,
        description="Codes to enable",
        values=("none", "BBH", "BH", "BHNS", "BNS", "NS"),
        default="none",
    )

    depends_on("cxx", type="build")  # generated
    depends_on("c", type="build")  # CMakeLists.txt doesn't specify language

    depends_on("blas")
    depends_on("boost cxxstd=17")  # kadath uses std=C++17
    depends_on("cmake @2.8:", type="build")
    depends_on("fftw-api @3:")
    depends_on("gsl")
    depends_on("lapack")
    depends_on("mpi", when="+mpi")
    depends_on("pgplot")
    depends_on("scalapack")

    root_cmakelists_dir = "build_release"

    def patch(self):
        for code in self.spec.variants["codes"].value:
            if code != "none":
                # Disable unwanted explicit include directory settings
                filter_file(
                    r"include_directories\(/usr",
                    "# include_directories(/usr",
                    join_path("codes", code, "CMakeLists.txt"),
                )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("HOME_KADATH", self.stage.source_path)

    def cmake_args(self):
        return [
            # kadath uses a non-standard option to enable MPI
            self.define_from_variant("PAR_VERSION", "mpi")
        ]

    def cmake(self, spec, prefix):
        options = self.std_cmake_args
        options += self.cmake_args()
        options.append(os.path.abspath(self.root_cmakelists_dir))
        with working_dir(self.build_directory, create=True):
            cmake(*options)
        for code in self.spec.variants["codes"].value:
            if code != "none":
                with working_dir(join_path("codes", code)):
                    cmake(*options)

    def build(self, spec, prefix):
        with working_dir(self.build_directory):
            make(*self.build_targets)
        for code in self.spec.variants["codes"].value:
            if code != "none":
                with working_dir(join_path("codes", code)):
                    make(*self.build_targets)

    def install(self, spec, prefix):
        mkdirp(prefix.include)
        install_tree("include", prefix.include)
        mkdirp(prefix.lib)
        install_tree("lib", prefix.lib)
