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

    homepage = "https://github.com/ALPSim/ALPS"
    url = "https://github.com/ALPSim/ALPS/archive/refs/tags/v2.3.4-beta.2.tar.gz"

    maintainers("Ooolab", "egull", "Sinan81")

    license("BSL-1.0", when="@:2.3.3", checked_by="Sinan81")
    license("MIT", when="@2.3.4:", checked_by="Ooolab")

    version(
        "2.3.4-beta.2",
        sha256="ca2e1307630e6fccac279ab7711036f7c6dee43c386fd6f24cfc77c86a3c7f1c",
        preferred=True,
    )
    version("2.3.3", sha256="73d8c9038d00c7f768f65474b2a657d5c49daf105ddfcaef7d16737500b5d02f")

    variant("mpi", default=True, description="Build with MPI support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on(
        "boost@1.80:", type="build"
    )  # Just for headers. Note that the checksums are listed below
    depends_on("fftw")
    depends_on("lapack")
    depends_on("python", type=("build", "link", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("mpi", when="+mpi")
    depends_on("hdf5+mpi+hl", when="+mpi")
    depends_on("hdf5~mpi+hl", when="~mpi")
    depends_on("zlib-api")

    extends("python")

    # See https://github.com/ALPSim/ALPS/issues/6#issuecomment-2604912169
    # for why this is needed
    for boost_version, boost_checksum in (
        # boost version, shasum
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
            when="^boost@{0}".format(boost_version),
            name="boost_source_files",
            url="https://downloads.sourceforge.net/project/boost/boost/{0}/boost_{1}.tar.bz2".format(
                boost_version, boost_version.replace(".", "_")
            ),
            sha256=boost_checksum,
            destination="",
            placement="boost_source_files",
        )

    # Patch for >=Boost 1.88.0 compatibility
    def patch(self):
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
        args = []

        # Platform-specific C++ flags (e.g., -stdlib=libc++ on macOS)
        cstdlibstr = ""
        if self.spec.satisfies("platform=darwin"):
            cstdlibstr = " -stdlib=libc++"

        # Assemble the full C++ flags string
        cxx_flags = (
            self.compiler.cxx14_flag
            + " -fpermissive -DBOOST_NO_AUTO_PTR -DBOOST_FILESYSTEM_NO_CXX20_ATOMIC_REF"
            + " -DBOOST_TIMER_ENABLE_DEPRECATED"
            + cstdlibstr
        )

        args.append(self.define("CMAKE_CXX_FLAGS", cxx_flags))

        # Boost source directory
        boost_src_dir = os.path.join(self.stage.source_path, "boost_source_files")
        args.append(self.define("Boost_SRC_DIR", boost_src_dir))

        # Boost linking options
        args.append(self.define("Boost_USE_STATIC_LIBS", True))  # → -DBoost_USE_STATIC_LIBS=ON
        args.append(
            self.define("Boost_USE_STATIC_RUNTIME", False)
        )  # → -DBoost_USE_STATIC_RUNTIME=OFF

        # MPI support
        if self.spec.satisfies("+mpi"):
            args.append(self.define("MPI_CXX_COMPILER", self.spec["mpi"].mpicxx))
            args.append(self.define("MPI_C_COMPILER", self.spec["mpi"].mpicc))
        else:
            args.append(self.define("ENABLE_MPI", False))

        # RPATH settings
        args.append(self.define("CMAKE_INSTALL_RPATH_USE_LINK_PATH", True))
        args.append(self.define("CMAKE_BUILD_WITH_INSTALL_RPATH", True))

        # Point to Spack's HDF5
        args.append(self.define("HDF5_DIR", self.spec["hdf5"].prefix))

        return args

    def setup_build_environment(self, env):
        # Set up environment for boost source compilation
        boost_src_dir = os.path.join(self.stage.source_path, "boost_source_files")
        env.set("BOOST_ROOT", boost_src_dir)
        env.set("Boost_SRC_DIR", boost_src_dir)

        # Include paths for compilation
        env.append_path("CPLUS_INCLUDE_PATH", self.spec["python"].headers.directories[0])

        # For MPI - set compiler wrappers
        if "+mpi" in self.spec:
            env.set("MPI_CXX", self.spec["mpi"].mpicxx)
            env.set("MPI_CC", self.spec["mpi"].mpicc)
            env.set("MPICXX", self.spec["mpi"].mpicxx)

        # Add MPI include path if available
        if hasattr(self.spec["mpi"], "headers"):
            env.append_path("CPLUS_INCLUDE_PATH", self.spec["mpi"].headers.directories[0])

        # For Python
        env.set("PYTHON", self.spec["python"].command.path)

        # Compiler flags
        env.append_flags("CXXFLAGS", "-fpermissive")
        env.append_flags("CXXFLAGS", "-DBOOST_NO_AUTO_PTR")
        env.append_flags("CXXFLAGS", "-DBOOST_FILESYSTEM_NO_CXX20_ATOMIC_REF")
        env.append_flags("CXXFLAGS", "-DBOOST_TIMER_ENABLE_DEPRECATED")
        env.append_flags("CXXFLAGS", self.compiler.cxx14_flag)
