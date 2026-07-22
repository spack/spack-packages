# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Spheral(CMakePackage):
    """Spheral++ provides a steerable parallel environment for performing coupled hydrodynamical and gravitational numerical simulations."""

    homepage = "https://github.com/llnl/spheral"
    url = "https://github.com/llnl/spheral/archive/refs/tags/v2026.06.0.tar.gz"
    git = "https://github.com/llnl/spheral.git"

    version("develop", branch="develop")
    version("2026.06.0", sha256="06ef78ba1d400250541b9a2fe66636e914ac5a00e23afd370c463d440369688b")
    version("2025.12.0", sha256="d770750cf81e8f945976c157c3401cfb3c15a67c5291c78a9378e09c32103d11")
    version("2025.06.1", sha256="d4048308b5f79cf5a4e0ac7a00a16d7da9f75501283b20432f2a09c7253454ed")
    version("2025.06.0", sha256="e570ad199519b6c7acf5c4255a2b31d7230ffa01af73f92b5e5a10323ab27c78")
    version("2025.01.0", sha256="7e5b267ca0c5f0c3ac2d96ad08497b883f4fa15345db77575d23aaf53ee61220")
    version("2024.06.1", sha256="18892ad49195157623b95c93d55b55bfea2602003726c00d789419f7bdfe0fc1")
    version("2024.06.0", sha256="ef02f2f19cabd89911907da7eb9447116493da3db25101272a749b69539b88c7")
    version("2024.01.1", sha256="ad1ec0e51cfb7c6d7610e96ed84ef6b5324de31187efe6aa37584431b03b3352")
    version("2024.01.0", sha256="86ffef944943b5219b69d05aac07f30bc120082f7a73d6ed7aaf3d84181e6e79")
    version("2023.06.0", sha256="a373d7efb42a75ddaeca70373d1e91a6b655a718ba71879132c7ba7d9554af3f")
    version("2023.03.2", sha256="1f20c382d86dfdeed8bce338ef54bc5b855315adac37f52dd42412d630eeab56")
    version("2023.03.1", sha256="a4e818fdb7d5d1fa9b67247ef2a0e5b80f3346a87da166112a4b1944f79df211")
    version("2023.03.0", sha256="52544b9f031914a2b625d8f9ec822348e4b61076980a0029ac34c07ab459dc1c")
    version("2022.6.1", sha256="d2efc04b1e82d711089ce54c7843d219b17c97eca093a8c19c410abb35d57118")
    
    # Define variants
    variant("mpi", default=True, description="Enable MPI Support.")
    variant("openmp", default=True, description="Enable OpenMP Support.")
    variant("cuda", default=False, description="Enable CUDA.")
    variant("docs", default=False, description="Enable building Docs.")
    variant("tests", default=False, description="Enable test support libs, including py-ats.")
    variant("shared", default=True, description="Build C++ libs as shared (disable for static).")
    variant(
        "cxxonly", default=False, description="Enable CXX-only build (disable Python bindings)."
    )
    variant("aneos", default=False, description="Enable ANEOS support.")
    variant("opensubdiv", default=False, description="Enable OpenSubdiv support.")
    variant("helmholtz", default=False, description="Enable Helmholtz EOS support.")
    variant("artificial_conduction", default=False, description="Enable Artificial Conduction.")
    variant("external_force", default=False, description="Enable External Force.")
    variant("gravity", default=False, description="Enable Gravity.")
    variant(
        "gsph",
        default=False,
        description="Enable Generalized Smoothed Particle Hydrodynamics (GSPH).",
    )
    variant(
        "svph", default=False, description="Enable Smoothed Volume Particle Hydrodynamics (SVPH)."
    )
    variant("external_chai", default=True, description="Use external CHAI library.")
    variant("boost_header_only", default=True, description="Use Boost header-only libraries.")
    variant("one_dim", default=True, description="Enable 1D kernels")
    variant("sundials", default=False, description="Enable sundials solver")
    variant("globaldt_reduction", default=False, description="Enable GlobalDt reduction.")
    variant("longcsdt", default=False, description="Enable LongCsDt.")
    variant("external_install", default=True, description="Use external install mode.")

    variant(
        "cxxstd",
        default="20",
        values=("11", "14", "17", "20", "23"),
        description="C++ standard to build with",
    )

    # Dependencies
    with default_args(type="build"):
        depends_on("cxx")
        depends_on("c")
        depends_on("fortran")
        depends_on("blt")
        depends_on("cmake@3.24:")
        depends_on("python")
        depends_on("opensubdiv", when="+opensubdiv")

    depends_on("boost")
    depends_on("eigen")
    depends_on("qhull")
    depends_on("silo")
    depends_on("hdf5")
    depends_on("polyclipper")
    depends_on("polytope")
    depends_on("caliper")
    depends_on("conduit")
    depends_on("axom")
    depends_on("raja")
    depends_on("umpire")
    depends_on("chai", when="+external_chai")
    depends_on("zlib-api")
    depends_on("opensubdiv", type="build", when="+opensubdiv")
    depends_on("sundials", when="+sundials")
    depends_on("mpi", when="+mpi")

    def cmake_args(self):
        args = []

        args.append(self.define("BLT_SOURCE_DIR", self.spec["blt"].prefix))
        args.append(self.define("SPHERAL_BLT_DIR", self.spec["blt"].prefix))
        args.append(self.define("boost_DIR", self.spec["boost"].prefix))
        args.append(self.define("eigen_DIR", self.spec["eigen"].prefix))
        args.append(self.define("qhull_DIR", self.spec["qhull"].prefix))
        args.append(self.define("silo_DIR", self.spec["silo"].prefix))
        args.append(self.define("hdf5_DIR", self.spec["hdf5"].prefix))
        args.append(self.define("polyclipper_DIR", self.spec["polyclipper"].prefix))
        args.append(self.define("polytope_DIR", self.spec["polytope"].prefix))
        args.append(self.define("caliper_DIR", self.spec["caliper"].prefix))
        args.append(self.define("conduit_DIR", self.spec["conduit"].prefix))
        args.append(self.define("axom_DIR", self.spec["axom"].prefix))
        args.append(self.define("raja_DIR", self.spec["raja"].prefix))
        args.append(self.define("umpire_DIR", self.spec["umpire"].prefix))
        if self.spec.satisfies("+external_chai"):
            args.append(self.define("chai_DIR", self.spec["chai"].prefix))
        args.append(self.define("zlib_DIR", self.spec["zlib-api"].prefix))
        args.append(self.define("ZLIB_ROOT", self.spec["zlib-api"].prefix))
        args.append(self.define_from_variant("BOOST_HEADER_ONLY", "boost_header_only"))
        args.append(self.define_from_variant("SPHERAL_ENABLE_ANEOS", "aneos"))
        args.append(self.define_from_variant("SPHERAL_ENABLE_OPENSUBDIV", "opensubdiv"))
        if self.spec.satisfies("+opensubdiv"):
            args.append(self.define("opensubdiv_DIR", self.spec["opensubdiv"].prefix))
        args.append(self.define_from_variant("SPHERAL_ENABLE_HELMHOLTZ", "helmholtz"))
        args.append(self.define_from_variant("SPHERAL_ENABLE_SUNDIALS", "sundials"))
        if self.spec.satisfies("+sundials"):
            args.append(self.define("sundials_DIR", self.spec["sundials"].prefix))
        args.append(
            self.define_from_variant(
                "SPHERAL_ENABLE_ARTIFICIAL_CONDUCTION", "artificial_conduction"
            )
        )
        args.append(self.define_from_variant("SPHERAL_ENABLE_EXTERNAL_FORCE", "external_force"))
        args.append(self.define_from_variant("SPHERAL_ENABLE_GRAVITY", "gravity"))
        args.append(self.define_from_variant("SPHERAL_ENABLE_GSPH", "gsph"))
        args.append(self.define_from_variant("SPHERAL_ENABLE_SVPH", "svph"))
        args.append(
            self.define_from_variant("SPHERAL_ENABLE_GLOBALDT_REDUCTION", "globaldt_reduction")
        )
        args.append(self.define_from_variant("SPHERAL_ENABLE_LONGCSDT", "longcsdt"))
        args.append(self.define_from_variant("SPHERAL_ENABLE_TESTS", "tests"))
        args.append(self.define("SPHERAL_ENABLE_PYTHON", not self.spec.satisfies("+cxxonly")))
        args.append(self.define_from_variant("SPHERAL_EXTERNAL_INSTALL", "external_install"))
        args.append(self.define("SPHERAL_ENABLE_STATIC", not self.spec.satisfies("+shared")))
        args.append(self.define_from_variant("SPHERAL_ENABLE_SHARED", "shared"))
        args.append(self.define("ENABLE_STATIC_TPL", not self.spec.satisfies("+shared")))
        args.append(self.define_from_variant("ENABLE_1D", "one_dim"))
        args.append(self.define_from_variant("ENABLE_CUDA", "cuda"))
        args.append(self.define_from_variant("ENABLE_OPENMP", "openmp"))
        args.append(self.define_from_variant("ENABLE_MPI", "mpi"))
        args.append(self.define_from_variant("ENABLE_DOCS", "docs"))
        args.append(self.define_from_variant("USE_EXTERNAL_CHAI", "external_chai"))
        args.append(self.define("BLT_CXX_STD", f"c++{self.spec.variants.get('cxxstd').value}"))
        args.append(self.define("HDF5_DIR", self.spec["hdf5"].prefix))
        args.append(self.define("HDF5_C_COMPILER_EXECUTABLE", self.spec["hdf5"].prefix.bin.h5pcc))
        args.append(self.define("HDF5_USE_STATIC_LIBRARIES", not self.spec.satisfies("+shared")))

        return args
