# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems import autotools
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
    url = "https://github.com/llnl/SAMRAI/releases/download/v-4-5-0/SAMRAI-v4.5.0.tar.gz"
    list_url = homepage
    git = "https://github.com/LLNL/SAMRAI.git"

    # using build_system 'cached_cmake' -- assets SAMRAI-v4.5.0.tar.gz
    version("4.5.0", sha256="1209a5be43d4aecfc2761f821f311cd54c9def45286edca3f4f0cc19dd8ba2ee")
    version("4.3.0", sha256="b124f5a44cbdf44e21341de47161357684a67aaca39b2ab2cf68b6edb794149b")
    version("4.2.1", sha256="dbd0b1f2c7f6c8eba2dc7e3535a73c97cbde929e8c08cecdbca8a98e2edf3bc1")
    version("4.2.0", sha256="34a256c99e29bee6dee017253a18cf1ed6435f0376e666e235e9092a895fabc6")
    version("4.1.2", sha256="2860c693ba495613ce0ea04cc72eb8749519a770d520ef0a83a54ecff3d515e3")
    version("4.1.1", sha256="ceb6e5b3b1587c45b8c41971f252974e40eae3d5fe9ad93269d969ea4acc2637")
    version("4.1.0", sha256="633968bf1d4ff9c0f1f0c31591f9bb665f8252231a9ca03b54c3b498239a5815")

    # using build_system 'autotools'
    version("3.12.0", sha256="3b02915bc3edc63da8960109e74ca7e61a1ca729d7631fa7a3635c7ca29c8266")
    version("3.11.5", sha256="22a6216ad451efeccaabfe9f37bd0364841f3e50cdc0e7829afc0ecaf81c6fba")
    version("3.11.4", sha256="a91884a89bd240c97f5f989b0decb7917a738e33c32a27795ba16b3cbe21bd76")

    # Version 3.11.3 permissions don't allow downloading
    version("3.11.2", sha256="b0889efe25f21becda48fe42ccbcccf12bcacf56f638e171db705f135c5550ae")
    version("3.11.1", sha256="8a02d51df50d0fdf4bc7ecc6dedc13b5d360bdd1f9a511264535a85cedd725e7")
    version("3.11.0", sha256="5d609efb0b72f40e17b65a498665e9a35efc608cb380221ac4d2a6d053009c6c")
    version("3.10.0", sha256="b63786a6597bfad03dd3fbd781f46ee1332c1b8e5af01c658fd9ed8cb93f1de2")
    version("3.9.1", sha256="93ffd4c7f1423a36f1452cc81d4742f75aab2e6dc16cb40931df159d0cf2f321")
    version("3.8.0", sha256="f3779f9816ddcc8e0a90c71f053e664bcd2c6169f8fd2fc37e1c2af6ceb5f1e4")
    version("3.7.3", sha256="3ef5b0ce70d6181d12e224624c734105093ec0b9a753a791965bcf4fd8aa1b65")
    version("3.7.2", sha256="f145b09b5b127ad63d7832cb29c001254027cb30f6a74d591792dbc8212a6aa8")
    version(
        "3.6.3-beta", sha256="6a9feb1dd61f4cf42d982acb26a05ae5596096b9d4ace2bb1bf797db47707505"
    )
    version(
        "3.5.2-beta", sha256="9bcf7d8237b3efcbcac980ec2c8276aa2c060b9d45160d176f688af0d31e7431"
    )
    version(
        "3.5.0-beta", sha256="dc43bb77769ad18a4a4c54b8c70710f900fe4990e62df7a5b6416f64bfc1bf9b"
    )
    version(
        "3.4.1-beta", sha256="0d039f0c2d3e21232bc909bf65b04725bfe7443ea35664554c7546497a61d90b"
    )
    version(
        "3.3.3-beta", sha256="8c9156401bd1db30ce591d5d0d5cbc6f24e24f997c61ebf55ed19e5b0a45041e"
    )
    version(
        "3.3.2-beta", sha256="57d71e6848183786d65fb008d82aad62b4856caf5a043d243a0616c58f500296"
    )
    version("2.4.4", sha256="300998d26f21b206de392baff316b31aa3d6926bfed85c7f0ca94cb12fb03be0")

    # Debug mode reduces optimization, includes assertions, debug symbols
    # and more print statements
    variant(
        "debug", default=False, description="Compile with reduced optimization and debugging on"
    )
    variant("silo", default=False, description="Compile with support for silo")
    variant("mpi", default=True, description="Build with MPI", when="@4:")
    variant(
        "cxxstd",
        default="20",
        values=("11", "14", "17", "20"),
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

    def url_for_version(self, version):
        if version >= Version("4"):
            base_url = "https://github.com/llnl/SAMRAI/releases/download/v-"
            return f"{base_url}{version.dashed}/SAMRAI-v{version}.tar.gz"
        elif version <= Version("3.11.0"):
            base_url = "https://github.com/llnl/SAMRAI/archive/refs/tags"
            return f"{base_url}/{version}.tar.gz"
        elif version < Version("4"):
            base_url = "https://github.com/llnl/SAMRAI/archive/refs/tags"
            return f"{base_url}/v-{version.dashed}.tar.gz"

        return f"{base_url}/{version}.tar.gz"

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


class CachedCMakeBuilder(CachedCMakeBuilder):

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
        entries.append(cmake_cache_option("ENABLE_MPI", spec.satisfies("+mpi")))
        return entries

    def initconfig_compiler_entries(self):
        entries = super().initconfig_compiler_entries()

        # Warning (KW 6/2024) -- setting the CMAKE_Fortran_COMPILER to the default (env['FC'])
        # produced lots of weird errors. Seems like it was related to Samrai's use
        # of FIXED formatting for its Fortran (rather than FREE formatting)
        entries.insert(0, cmake_cache_path("CMAKE_C_COMPILER", env["CC"]))
        entries.insert(0, cmake_cache_path("CMAKE_CXX_COMPILER", env["CXX"]))
        entries.insert(0, cmake_cache_path("CMAKE_Fortran_COMPILER", env["SPACK_FC"]))

        return entries

    def initconfig_package_entries(self):
        spec = self.spec
        entries = super().initconfig_package_entries()

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

        return entries

    def initconfig_hardware_entries(self):
        spec = self.spec
        entries = super().initconfig_hardware_entries()

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
