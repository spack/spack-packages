# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import autotools, cached_cmake
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack_repo.builtin.build_systems.cached_cmake import (
    CachedCMakeBuilder,
    CachedCMakePackage,
    cmake_cache_option,
    cmake_cache_string,
)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


class Samrai(AutotoolsPackage, CachedCMakePackage, CudaPackage):
    """SAMRAI (Structured Adaptive Mesh Refinement Application Infrastructure)
    is an object-oriented C++ software library enables exploration of
    numerical, algorithmic, parallel computing, and software issues
    associated with applying structured adaptive mesh refinement
    (SAMR) technology in large-scale parallel application development.

    """

    homepage = "https://computing.llnl.gov/projects/samrai"
    url = "https://github.com/LLNL/SAMRAI/archive/refs/tags/v-3-15-0.tar.gz"
    list_url = homepage
    git = "https://github.com/LLNL/SAMRAI.git"

    # using build_system 'cached_cmake'
    version("4.5.0", tag="v-4-5-0", submodules=True)
    version("4.3.0", tag="v-4-3-0")
    version("2022.2.9", commit="dc87a7a05cd5edccdb417a0796a5f6a4f68cd9f0")
    version("2021.11.4", commit="e600573bf774022126a7539240a6a6c2e44b8e64")
    version("2021.2.16", commit="39017121bda44fff713fe3b01cb1e063be93023b")

    # using build_system 'autotools'
    version("3.12.0", sha256="b8334aa22330a7c858e09e000dfc62abbfa3c449212b4993ec3c4035bed6b832")
    version("3.11.5", sha256="6ec1f4cf2735284fe41f74073c4f1be87d92184d79401011411be3c0671bd84c")
    version("3.11.4", sha256="fa87f6cc1cb3b3c4856bc3f4d7162b1f9705a200b68a5dc173484f7a71c7ea0a")
    # Version 3.11.3 permissions don't allow downloading
    version("3.11.2", sha256="fd9518cc9fd8c8f6cdd681484c6eb42114aebf2a6ba4c8e1f12b34a148dfdefb")
    version("3.11.1", sha256="14317938e55cb7dc3eca21d9b7667a256a08661c6da988334f7af566a015b327")
    version("3.10.0", sha256="8d6958867f7165396459f4556e439065bc2cd2464bcfe16195a2a68345d56ea7")
    version("3.9.1", sha256="ce0aa9bcb3accbd39c09dd32cbc9884dc00e7a8d53782ba46b8fe7d7d60fc03f")
    version("3.8.0", sha256="0fc811ca83bd72d238f0efb172d466e80e5091db0b78ad00ab6b93331a1fe489")
    version("3.7.3", sha256="19eada4f351a821abccac0779fde85e2ad18b931b6a8110510a4c21707c2f5ce")
    version("3.7.2", sha256="c20c5b12576b73a1a095d8ef54536c4424517adaf472d55d48e57455eda74f2d")
    version(
        "3.6.3-beta", sha256="7d9202355a66b8850333484862627f73ea3d7620ca84cde757dee629ebcb61bb"
    )
    version(
        "3.5.2-beta", sha256="9a591fc962edd56ea073abd13d03027bd530f1e61df595fae42dd9a7f8b9cc3a"
    )
    version(
        "3.5.0-beta", sha256="3e10c55d7b652b6feca902ce782751d4b16c8ad9d4dd8b9e2e9ec74dd64f30da"
    )
    version(
        "3.4.1-beta", sha256="5aadc813b75b65485f221372e174a2691e184e380f569129e7aa4484ca4047f8"
    )
    version(
        "3.3.3-beta", sha256="c07b5dc8d56a8f310239d1ec6be31182a6463fea787a0e10b54a3df479979cac"
    )
    version(
        "3.3.2-beta", sha256="430ea1a77083c8990a3c996572ed15663d9b31c0f8b614537bd7065abd6f375f"
    )
    version("2.4.4", sha256="33242e38e6f4d35bd52f4194bd99a014485b0f3458b268902f69f6c02b35ee5c")

    def url_for_version(self, version):
        if version >= Version("4.3.0"):
            url = f"https://github.com/LLNL/SAMRAI/archive/refs/tags/v-3-15-0.tar.gz"
        else:
            url = f"https://computing.llnl.gov/projects/samrai/download/SAMRAI-v3.11.2.tar.gz"
        return url

    # Debug mode reduces optimization, includes assertions, debug symbols
    # and more print statements
    variant(
        "debug", default=False, description="Compile with reduced optimization and debugging on"
    )
    variant("silo", default=False, description="Compile with support for silo")
    variant("mpi", default=True, description="Build with MPI", when="@4:")
    variant(
        "cxxstd",
        default="14",
        values=("11", "14", "17"),
        multi=False,
        description="C++ standard",
        when="@4:",
    )
    variant("tests", default=False, description="Build tests", when="@4:")
    variant("docs", default=False, description="Build docs", when="@4:")
    variant("tools", default=False, description="Build tools", when="@4:")
    variant("fortran", default=True, description="Enable fortran", when="@4:")
    variant("openmp", default=False, description="Enable openmp", when="@4:")
    variant("conduit", default=True, description="Enable conduit", when="@4:")
    variant("raja", default=True, description="Enable Raja", when="@4:")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    build_system(
        conditional("cmake", when="@4:"), conditional("autotools", when="@:3"), default="cmake"
    )

    with when("build_system=cmake"):
        depends_on("mpi", when="+mpi")
        depends_on("zlib")
        depends_on("hdf5")  # This used to be hdf5+mpi
        depends_on("blt")

        depends_on("raja")  # TODO: check if this is only for +cuda
        depends_on("umpire")  # Umpire is needed when building with Raja

        # Miranda needs SAMRAI with conduit
        depends_on("conduit")

    depends_on("m4", type="build")
    depends_on("boost@:1.64.0", when="@3.0.0:3.11.99", type="build")
    depends_on("silo+mpi", when="+silo")

    with when("build_system=autotools"):
        depends_on("mpi")
        depends_on("zlib-api")
        depends_on("hdf5+mpi")
        # TODO: replace this with an explicit list of components of Boost,
        # for instance depends_on('boost +filesystem')
        # See https://github.com/spack/spack/pull/22303 for reference
        depends_on(Boost.with_default_variants, when="@3.0.0:3.11.99", type="build")

    # don't build SAMRAI 3+ with tools with gcc
    # 23/01/12: this causes issues with out version+gcc
    patch("no-tool-build.patch", when="@3.0.0:3.12.0%gcc")

    def flag_handler(self, name, flags):
        if name == "ldflags":
            flags.append("-lz")
        return (flags, None, None)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        spec = self.spec
        if "+cuda" in spec:
            env.set("CUDAHOSTCXX", spack_cxx)

    def check(self):
        if self.spec.satisfies("+tests"):
            with working_dir(self.build_directory):
                make("test")
                make("check")

    def cmake_args(self):
        return []


class CachedCMakeBuilder(cached_cmake.CachedCMakeBuilder):

    @property
    def libs(self):
        libs = [
            "SAMRAI_appu",
            "SAMRAI_geom",
            "SAMRAI_solv",
            "SAMRAI_algs",
            "SAMRAI_mesh",
            "SAMRAI_math",
            "SAMRAI_pdat",
            "SAMRAI_xfer",
            "SAMRAI_hier",
            "SAMRAI_tbox",
        ]
        libs = [("lib" + x) for x in libs]
        return find_libraries(libs, self.spec.prefix, shared=False, recursive=True)

    def initconfig_mpi_entries(self):
        spec = self.spec
        entries = super().initconfig_mpi_entries()
        # entries = []
        entries.append(cmake_cache_option("ENABLE_MPI", spec.satisfies("+mpi")))
        return entries

    def initconfig_package_entries(self):
        spec = self.spec
        entries = super().initconfig_package_entries()
        # entries = []
        entries.append(cmake_cache_path("BLT_SOURCE_DIR", spec["blt"].prefix))

        if spec.satisfies("+tests"):
            entries.append(cmake_cache_option("ENABLE_SAMRAI_TESTS", True))
            entries.append(cmake_cache_option("ENABLE_TESTS", True))
        else:
            entries.append(cmake_cache_option("ENABLE_SAMRAI_TESTS", False))
            entries.append(cmake_cache_option("ENABLE_TESTS", False))

        entries.append(
            cmake_cache_string("BLT_CXX_STD", f"c++{self.spec.variants['cxxstd'].value}")
        )
        entries.append(cmake_cache_option("ENABLE_DOCS", spec.satisfies("+docs")))
        entries.append(cmake_cache_option("ENABLE_TOOLS", spec.satisfies("+tools")))
        entries.append(cmake_cache_option("ENABLE_FORTRAN", spec.satisfies("+fortran")))
        entries.append(cmake_cache_option("ENABLE_OPENMP", spec.satisfies("+openmp")))
        entries.append(cmake_cache_option("ENABLE_CONDUIT", spec.satisfies("+conduit")))
        entries.append(cmake_cache_option("ENABLE_RAJA", spec.satisfies("+raja")))

        # Warning (KW 6/2024) -- setting the CMAKE_Fortran_COMPILER to the default (env['FC'])
        # produced lots of weird errors. Seems like it was related to Samrai's use
        # of FIXED formatting for its Fortran (rather than FREE formatting)
        entries.insert(0, cmake_cache_path("CMAKE_C_COMPILER", env["CC"]))
        entries.insert(0, cmake_cache_path("CMAKE_CXX_COMPILER", env["CXX"]))
        entries.insert(0, cmake_cache_path("CMAKE_Fortran_COMPILER", env["SPACK_FC"]))

        if self.spec.satisfies("+conduit"):
            entries.append(cmake_cache_string("CONDUIT_DIR", spec["conduit"].prefix))

        if self.spec.satisfies("+raja"):
            entries.append(cmake_cache_string("RAJA_DIR", spec["raja"].prefix))
            entries.append(
                cmake_cache_string(
                    "umpire_DIR", join_path(spec["umpire"].prefix, "share/umpire/cmake")
                )
            )

        entries.append(cmake_cache_option("ENABLE_CUDA", spec.satisfies("+cuda")))
        if self.spec.satisfies("+cuda"):
            entries.append(
                cmake_cache_string("CMAKE_CUDA_STANDARD", spec.variants["cxxstd"].value)
            )
            entries.append(cmake_cache_string("CMAKE_CUDA_EXTENSIONS", False))
            entries.append(
                cmake_cache_string("CMAKE_CUDA_ARCHITECTURES", spec.variants["cuda_arch"].value)
            )

        return entries


class AutotoolsBuilder(autotools.AutotoolsBuilder):
    def configure_args(self):
        options = []
        options.extend(
            [
                "--with-CXX=%s" % self.spec["mpi"].mpicxx,
                "--with-CC=%s" % self.spec["mpi"].mpicc,
                "--with-F77=%s" % self.spec["mpi"].mpifc,
                "--with-M4=%s" % self.spec["m4"].prefix,
                "--with-hdf5=%s" % self.spec["hdf5"].prefix,
                "--with-zlib=%s" % self.spec["zlib-api"].prefix,
                "--without-blas",
                "--without-lapack",
                "--with-hypre=no",
                "--with-petsc=no",
            ]
        )

        # SAMRAI 2 used templates; enable implicit instantiation
        if self.spec.satisfies("@:3"):
            options.append("--enable-implicit-template-instantiation")

        if "+debug" in self.spec:
            options.extend(["--disable-opt", "--enable-debug"])
        else:
            options.extend(["--enable-opt", "--disable-debug"])

        if "+silo" in self.spec:
            options.append("--with-silo=%s" % self.spec["silo"].prefix)

        if "+shared" in self.spec:
            options.append("--enable-shared")

        if self.spec.satisfies("@3.0:3.11"):
            options.append("--with-boost=%s" % self.spec["boost"].prefix)

        return options

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        if self.spec.satisfies("@3.12:"):
            env.append_flags("CXXFLAGS", self.compiler.cxx11_flag)
