# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Alps(CMakePackage):
    """
    The ALPS project (Algorithms and Libraries for Physics Simulations) aims at providing generic
    parallel algorithms for classical and quantum lattice models and provides utility classes and
    algorithm for many others.
    """

    homepage = "https://alps.comp-phys.org"
    url = "https://github.com/ALPSim/ALPS/archive/refs/tags/v3.0.0.tar.gz"
    git = "https://github.com/ALPSim/ALPS.git"

    maintainers("Ooolab", "egull", "Sinan81")

    # v2.3.3's LICENSE.txt is already the MIT license
    license("MIT", checked_by="egull")

    version("master", branch="master")
    version("3.0.0", sha256="ea44545afc570de7df8c01f093b769adf344f72579968b700e4e93df9eedb0ea")
    version(
        "2.3.4-beta.2",
        sha256="ca2e1307630e6fccac279ab7711036f7c6dee43c386fd6f24cfc77c86a3c7f1c",
    )
    version("2.3.3", sha256="73d8c9038d00c7f768f65474b2a657d5c49daf105ddfcaef7d16737500b5d02f")

    variant("mpi", default=True, description="Build with MPI support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    # No fortran: ALPS_BUILD_FORTRAN defaults OFF and is not enabled here

    depends_on("cmake@3.18:", type="build")
    depends_on("cmake@3.22:", type="build", when="@3:")

    # --- Boost, two schemes ---
    # @3: consumes an externally built (Spack) Boost via ALPS_USE_SYSTEM_BOOST.
    # Spack's infinity-version ordering means that @master also satisfies @3:.
    # Compiled Boost with all required library components.
    # Minimum 1.69: boost::system became header-only in 1.69; ALPS_USE_SYSTEM_BOOST
    # omits it from the explicit link list, which is only valid for Boost >= 1.69.
    depends_on(
        "boost@1.69:"
        "+filesystem+serialization+system+program_options"
        "+regex+thread+date_time+chrono+timer+iostreams+test+python",
        type=("build", "link"),
        when="@3:",
    )
    depends_on("boost+mpi", when="@3: +mpi")
    depends_on("boost~mpi", when="@3: ~mpi")
    # Boost >= 1.87 supports NumPy 2. Older Boost can auto-detect NumPy and
    # compile its incompatible NumPy module even when boost~numpy is requested.
    requires("^boost@1.87:", when="@3: ^py-numpy@2:")
    requires("^boost+numpy", when="@3: ^boost@1.87:")
    requires("^boost+numpy", when="@3: ^boost@1.69:1.86 ^py-numpy@:1")

    # Legacy 2.x releases compile Boost from a source tree staged as a resource;
    # this dependency only selects which source tarball resource is staged
    # (see the resource table below). Upper bound must match the last entry
    # in that table.
    depends_on("boost@1.80:1.90", type="build", when="@:2.3.4")

    depends_on("fftw")
    # Keep the DAG truly serial for ~mpi: fftw defaults to +mpi, which would
    # otherwise pull in an MPI that ALPS's CMake then finds and links.
    depends_on("fftw~mpi", when="~mpi")
    depends_on("blas")
    depends_on("lapack")
    depends_on("python@3.9:", type=("build", "link", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("mpi", when="+mpi")
    # Serial HDF5 even for +mpi: ALPS's CMakeLists warns "ALPS does not use
    # parallel HDF5. The standard version is preferred."
    depends_on("hdf5~mpi+hl")
    depends_on("zlib-api")

    extends("python")

    # Boost source tree for legacy 2.x releases, which build Boost themselves.
    # See https://github.com/ALPSim/ALPS/issues/6#issuecomment-2604912169
    # for why this is needed
    for boost_version, boost_checksum in (
        # boost version, shasum
        ("1.90.0", "49551aff3b22cbc5c5a9ed3dbc92f0e23ea50a0f7325b0d198b705e8ee3fc305"),
        ("1.89.0", "85a33fa22621b4f314f8e85e1a5e2a9363d22e4f4992925d4bb3bc631b5a0c7a"),
        ("1.88.0", "46d9d2c06637b219270877c9e16155cbd015b6dc84349af064c088e9b5b12f7b"),
        ("1.87.0", "af57be25cb4c4f4b413ed692fe378affb4352ea50fbe294a11ef548f4d527d89"),
        ("1.86.0", "1bed88e40401b2cb7a1f76d4bab499e352fa4d0c5f31c0dbae64e24d34d7513b"),
        ("1.85.0", "7009fe1faa1697476bdc7027703a2badb84e849b7b0baad5086b087b971f8617"),
        ("1.84.0", "cc4b893acf645c9d4b698e9a0f08ca8846aa5d6c68275c14c3e7949c24109454"),
        ("1.83.0", "6478edfe2f3305127cffe8caf73ea0176c53769f4bf1585be237eb30798c3b8e"),
        ("1.82.0", "a6e1ab9b0860e6a2881dd7b21fe9f737a095e5f33a3a874afc6a345228597ee6"),
        ("1.81.0", "71feeed900fbccca04a3b4f2f84a7c217186f28a940ed8b7ed4725986baf99fa"),
        ("1.80.0", "1e19565d82e43bc59209a168f5ac899d3ba471d55c7610c677d4ccf2c9c500c0"),
    ):
        resource(
            when="@:2.3.4 ^boost@{0}".format(boost_version),
            name="boost_source_files",
            url="https://downloads.sourceforge.net/project/boost/boost/{0}/boost_{1}.tar.bz2".format(
                boost_version, boost_version.replace(".", "_")
            ),
            sha256=boost_checksum,
            destination="",
            placement="boost_source_files",
        )

    # Patch for >=Boost 1.88.0 compatibility (legacy 2.x releases only; the
    # 3.x sources already carry these fixes)
    def patch(self):
        if self.spec.satisfies("@3:"):
            return

        # Only apply patch for Boost versions greater than 1.87
        # Check if boost dependency is specified and get its version
        if "boost" not in self.spec:
            return

        boost_spec = self.spec["boost"]
        # Compare versions: only apply patch if boost version > 1.87
        if boost_spec.version > Version("1.87"):
            # Fix boost::is_same and boost::add_const for >=Boost 1.88.0 compatibility
            # These type traits were moved to std:: in >=Boost 1.88.0

            # First, let's add necessary includes
            filter_file(
                "#include <boost/type_traits.hpp>",
                "#include <boost/type_traits.hpp>\n#include <type_traits>",
                "src/alps/numeric/matrix/strided_iterator.hpp",
            )

            filter_file(
                "#include <boost/type_traits.hpp>",
                "#include <boost/type_traits.hpp>\n#include <type_traits>",
                "src/alps/numeric/matrix/matrix_element_iterator.hpp",
            )

            # Now replace boost::is_same with std::is_same
            filter_file(
                "boost::is_same", "std::is_same", "src/alps/numeric/matrix/strided_iterator.hpp"
            )

            filter_file(
                "boost::is_same",
                "std::is_same",
                "src/alps/numeric/matrix/matrix_element_iterator.hpp",
            )

            # Replace boost::add_const with std::add_const
            filter_file(
                "boost::add_const",
                "std::add_const",
                "src/alps/numeric/matrix/strided_iterator.hpp",
            )

            filter_file(
                "boost::add_const",
                "std::add_const",
                "src/alps/numeric/matrix/matrix_element_iterator.hpp",
            )

    def cmake_args(self):
        args = [
            # ALPS's cache variable is ALPS_ENABLE_MPI and defaults to ON,
            # so it must be set OFF explicitly for ~mpi
            self.define_from_variant("ALPS_ENABLE_MPI", "mpi"),
            # Explicit rather than relying on the double-negative
            # NOT_ALPS_BUILD_PYTHON default in ALPS's CMakeLists
            self.define("ALPS_BUILD_PYTHON", True),
            self.define("CMAKE_INSTALL_RPATH_USE_LINK_PATH", True),
            self.define("CMAKE_BUILD_WITH_INSTALL_RPATH", True),
            self.define("HDF5_DIR", self.spec["hdf5"].prefix),
            # HDF5 supplies its own compression dependencies. ALPS does not
            # call SZIP directly, and probing it can add unrelated host headers.
            self.define("CMAKE_DISABLE_FIND_PACKAGE_SZIP", True),
            # Hand the concretized BLAS/LAPACK to ALPS explicitly.  Its
            # FindLapack.cmake otherwise probes the host first (MKLROOT in the
            # environment, Accelerate on macOS) and links whatever it finds
            # there instead of the Spack-built provider.
            self.define("BLAS_LIBRARY", self.spec["blas"].libs.joined(";")),
            self.define("LAPACK_LIBRARY", self.spec["lapack"].libs.joined(";")),
        ]

        if self.spec.satisfies("+mpi"):
            args += [
                self.define("MPI_CXX_COMPILER", self.spec["mpi"].mpicxx),
                self.define("MPI_C_COMPILER", self.spec["mpi"].mpicc),
            ]

        if self.spec.satisfies("@3:"):
            # Consume the Spack-built Boost directly
            args += [
                self.define("ALPS_USE_SYSTEM_BOOST", True),
                self.define("BOOST_ROOT", self.spec["boost"].prefix),
                self.define("Boost_USE_STATIC_LIBS", self.spec["boost"].satisfies("~shared")),
            ]
        else:
            # Legacy 2.x releases build Boost from the staged source tree.
            # Platform-specific C++ flags: -stdlib=libc++ defeats ALPS's
            # obsolete clang logic that would otherwise force libstdc++
            cstdlibstr = ""
            if self.spec.satisfies("platform=darwin"):
                cstdlibstr = " -stdlib=libc++"

            cxx_flags = (
                self.compiler.cxx14_flag
                + " -fpermissive -DBOOST_NO_AUTO_PTR -DBOOST_FILESYSTEM_NO_CXX20_ATOMIC_REF"
                + " -DBOOST_TIMER_ENABLE_DEPRECATED"
                + cstdlibstr
            )

            args += [
                self.define("CMAKE_CXX_FLAGS", cxx_flags),
                self.define(
                    "Boost_SRC_DIR", os.path.join(self.stage.source_path, "boost_source_files")
                ),
                self.define("Boost_USE_STATIC_LIBS", True),
                self.define("Boost_USE_STATIC_RUNTIME", False),
            ]

        return args

    def setup_build_environment(self, env):
        # Python headers for ALPS C extension compilation
        env.append_path("CPLUS_INCLUDE_PATH", self.spec["python"].headers.directories[0])

        # For MPI - set compiler wrappers
        if "+mpi" in self.spec:
            env.set("MPI_CXX", self.spec["mpi"].mpicxx)
            env.set("MPI_CC", self.spec["mpi"].mpicc)
            env.set("MPICXX", self.spec["mpi"].mpicxx)
            if hasattr(self.spec["mpi"], "headers"):
                env.append_path("CPLUS_INCLUDE_PATH", self.spec["mpi"].headers.directories[0])

        if self.spec.satisfies("@3:"):
            # BOOST_ROOT as env var for FindBoost module-mode detection
            env.set("BOOST_ROOT", self.spec["boost"].prefix)
        else:
            # Set up environment for boost source compilation
            boost_src_dir = os.path.join(self.stage.source_path, "boost_source_files")
            env.set("BOOST_ROOT", boost_src_dir)
            env.set("Boost_SRC_DIR", boost_src_dir)

            # For Python
            env.set("PYTHON", self.spec["python"].command.path)
