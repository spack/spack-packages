# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *
import os

class Alps(CMakePackage):
    """
    The ALPS project (Algorithms and Libraries for Physics Simulations) aims at providing generic
    parallel algorithms for classical and quantum lattice models and provides utility classes and
    algorithm for many others.
    """

    homepage = "https://github.com/ALPSim/ALPS"
    url = "https://github.com/ALPSim/ALPS/archive/refs/tags/v2.3.4.tar.gz"

    maintainers("Ooolab","egull")

    license("MIT", checked_by="Ooolab")

    version("2.3.4", sha256="bc65453bb88cc42de77c2963a44966fb3c92e80ff8e8e29e80fb87694fba41d7")
    version("2.3.3-beta.6", sha256="eb0c8115b034dd7a9dd585d277c4f86904ba374cdbdd130545aca1c432583b68")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    # update version constraint on every boost release after providing version & checksum info
    # in resources dictionary below
    depends_on("boost@1.80:")  # Just for headers. Note that the checksums are listed below
    depends_on("fftw")
    depends_on("hdf5 ~mpi+hl")
    depends_on("lapack")
    depends_on("python", type=("build", "link", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("mpi")
    
    extends("python")

    # https://github.com/ALPSim/ALPS/issues/9
    #conflicts(
    #    "%gcc@14", when="@:2.3.3-beta.6", msg="use gcc older than version 14 or else build fails"
    #)

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
        if 'boost' in self.spec:
            boost_spec = self.spec['boost']
            # Compare versions: only apply patch if boost version > 1.87
            if boost_spec.version > Version('1.87'):
                # Fix boost::is_same and boost::add_const for >=Boost 1.88.0 compatibility
                # These type traits were moved to std:: in >=Boost 1.88.0
                
                # First, let's add necessary includes
                filter_file(
                    '#include <boost/type_traits.hpp>',
                    '#include <boost/type_traits.hpp>\n#include <type_traits>',
                    'src/alps/numeric/matrix/strided_iterator.hpp'
                )
                
                filter_file(
                    '#include <boost/type_traits.hpp>',
                    '#include <boost/type_traits.hpp>\n#include <type_traits>',
                    'src/alps/numeric/matrix/matrix_element_iterator.hpp'
                )
                
                # Now replace boost::is_same with std::is_same
                filter_file(
                    'boost::is_same',
                    'std::is_same',
                    'src/alps/numeric/matrix/strided_iterator.hpp'
                )
                
                filter_file(
                    'boost::is_same',
                    'std::is_same',
                    'src/alps/numeric/matrix/matrix_element_iterator.hpp'
                )
                
                # Replace boost::add_const with std::add_const
                filter_file(
                    'boost::add_const',
                    'std::add_const',
                    'src/alps/numeric/matrix/strided_iterator.hpp'
                )
                
                filter_file(
                    'boost::add_const',
                    'std::add_const',
                    'src/alps/numeric/matrix/matrix_element_iterator.hpp'
                )

    def cmake_args(self):
        args = []
        #this will ensure availability of the cstddef header on darwin (mac)
        cstdlibstr=""
        if self.spec.satisfies("platform=darwin"):
          cstdlibstr=" -stdlib=libc++"

        args.append(
            "-DCMAKE_CXX_FLAGS={0}".format(
                self.compiler.cxx14_flag
                + " -fpermissive -DBOOST_NO_AUTO_PTR -DBOOST_FILESYSTEM_NO_CXX20_ATOMIC_REF"
                + " -DBOOST_TIMER_ENABLE_DEPRECATED"
                + cstdlibstr
            )
        )
        
        # Point to boost source files that need to be compiled
        boost_src_dir = os.path.join(self.stage.source_path, "boost_source_files")
        args.append(
            "-DBoost_SRC_DIR={0}".format(boost_src_dir)
        )
        
        # Tell CMake to compile boost from source
        args.append(
            "-DBoost_USE_STATIC_LIBS=ON"
        )
        
        args.append(
            "-DBoost_USE_STATIC_RUNTIME=OFF"
        )
        
        # Add MPI support - just specify compilers (minimal change)
        args.append(
            "-DMPI_CXX_COMPILER={0}".format(self.spec['mpi'].mpicxx)
        )
        
        args.append(
            "-DMPI_C_COMPILER={0}".format(self.spec['mpi'].mpicc)
        )
        
        # Add Python support
        args.append(
            "-DPYTHON_EXECUTABLE={0}".format(self.spec['python'].command.path)
        )
        
        args.append(
            "-DPYTHON_INCLUDE_DIR={0}".format(self.spec['python'].headers.directories[0])
        )
        
        args.append(
            "-DPYTHON_LIBRARY={0}".format(self.spec['python'].libs[0])
        )
        
        return args
        
        
    def setup_build_environment(self, env):
        # Set up environment for boost source compilation
        boost_src_dir = os.path.join(self.stage.source_path, 'boost_source_files')
        env.set('BOOST_ROOT', boost_src_dir)
        env.set('Boost_SRC_DIR', boost_src_dir)
        
        # Include paths for compilation
        env.append_path('CPLUS_INCLUDE_PATH', self.spec['python'].headers.directories[0])
        
        # For MPI - set compiler wrappers
        env.set('MPI_CXX', self.spec['mpi'].mpicxx)
        env.set('MPI_CC', self.spec['mpi'].mpicc)
        env.set('MPICXX', self.spec['mpi'].mpicxx)
        
        # Add MPI include path if available
        if hasattr(self.spec['mpi'], 'headers'):
            env.append_path('CPLUS_INCLUDE_PATH', self.spec['mpi'].headers.directories[0])
        
        # For Python
        env.set('PYTHON', self.spec['python'].command.path)
        
        # Compiler flags
        env.append_flags('CXXFLAGS', '-fpermissive')
        env.append_flags('CXXFLAGS', '-DBOOST_NO_AUTO_PTR')
        env.append_flags('CXXFLAGS', '-DBOOST_FILESYSTEM_NO_CXX20_ATOMIC_REF')
        env.append_flags('CXXFLAGS', '-DBOOST_TIMER_ENABLE_DEPRECATED')
        env.append_flags('CXXFLAGS', self.compiler.cxx14_flag)


    @run_after("install")
    def relocate_python_stuff(self):
        pyalps_dir = join_path(python_platlib, "pyalps")
        with working_dir(self.prefix):
            copy_tree("pyalps", pyalps_dir)
        with working_dir(self.prefix.lib):
            copy_tree("pyalps", pyalps_dir)
            # in pip installed pyalps package, xml dir is provided under platlib/pyalps
            copy_tree("xml", join_path(pyalps_dir, "xml"))
