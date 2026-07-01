# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os
import shutil

from spack_repo.builtin.build_systems.cached_cmake import (
    CachedCMakePackage,
    cmake_cache_option,
    cmake_cache_path,
    cmake_cache_string,
)

from spack.package import *


def cmake_cache_entry(name, value, vtype=None, force=False):
    """
    Helper that creates CMake cache entry strings used in
    'host-config' files.
    """
    if vtype is None:
        if value == "ON" or value == "OFF":
            vtype = "BOOL"
        else:
            vtype = "PATH"
    force_str = " FORCE" if force else ""
    return 'set({0} "{1}" CACHE {2} ""{3})\n\n'.format(name, value, vtype, force_str)


class Conduit(CachedCMakePackage):
    """Conduit is an open source project from Lawrence Livermore National
    Laboratory that provides an intuitive model for describing hierarchical
    scientific data in C++, C, Fortran, and Python. It is used for data
    coupling between packages in-core, serialization, and I/O tasks."""

    homepage = "https://software.llnl.gov/conduit"
    url = "https://github.com/LLNL/conduit/releases/download/v0.3.0/conduit-v0.3.0-src-with-blt.tar.gz"
    git = "https://github.com/LLNL/conduit.git"
    tags = ["radiuss", "e4s"]

    license("BSD-3-Clause")
    test_requires_compiler = True

    version("develop", branch="develop", submodules=True)
    # note: the main branch in conduit was renamed to develop, this next entry
    # is to bridge any spack dependencies that are still using the name master
    version("master", branch="develop", submodules=True)
    # note: 2021-05-05 latest tagged release is now preferred instead of develop
    version("0.9.7", sha256="e207016e453dd360b2d9a5a1245e53a9aa26ed83fdfb02cc08fc7bfed664f923")
    version("0.9.6", sha256="370780082f095ebcb5c43067b650c78325088df726488dc5c6d414e7037c847d")
    version("0.9.5", sha256="d93294efbf0936da5a27941e13486aa1a04a74a59285786a2303eed19a24265a")
    version("0.9.4", sha256="c9edfb2ff09890084313ad9c2d83bfb7c10e70b696980762d1ae1488f9f08e6c")
    version("0.9.3", sha256="2968fa8df6e6c43800c019a008ef064ee9995dc2ff448b72dc5017c188a2e6d4")
    version("0.9.2", sha256="45d5a4eccd0fc978d153d29c440c53c483b8f29dfcf78ddcc9aa15c59b257177")
    version("0.9.1", sha256="a3f1168738dcf72f8ebf83299850301aaf56e803f40618fc1230a755d0d05363")
    version("0.9.0", sha256="844e012400ab820967eef6cec15e1aa9a68cb05119d0c1f292d3c01630111a58")
    version("0.8.8", sha256="99811e9c464b6f841f52fcd47e982ae47cbb01cba334cff43eabe13eea58c0df")
    version("0.8.7", sha256="f3bf44d860783f4e0d61517c5e280c88144af37414569f4cf86e2d29b3ba5293")
    version("0.8.6", sha256="8ca5d37033143ed7181c7286dd25a3f6126ba0358889066f13a2b32f68fc647e")
    version("0.8.5", sha256="b4a6f269a81570a4597e2565927fd0ed2ac45da0a2500ce5a71c26f7c92c5483")
    version("0.8.4", sha256="55c37ddc668dbc45d43b60c440192f76e688a530d64f9fe1a9c7fdad8cd525fd")
    version("0.8.3", sha256="a9e60945366f3b8c37ee6a19f62d79a8d5888be7e230eabc31af2f837283ed1a")
    version("0.8.2", sha256="928eb8496bc50f6d8404f5bfa70220250876645d68d4f35ce0b99ecb85546284")
    version("0.8.1", sha256="488f22135a35136de592173131d123f7813818b7336c3b18e04646318ad3cbee")
    version("0.8.0", sha256="0607dcf9ced44f95e0b9549f5bbf7a332afd84597c52e293d7ca8d83117b5119")
    version("0.7.2", sha256="359fd176297700cdaed2c63e3b72d236ff3feec21a655c7c8292033d21d5228a")
    version("0.7.1", sha256="460a480cf08fedbf5b38f707f94f20828798327adadb077f80dbab048fd0a07d")
    version("0.7.0", sha256="ecaa9668ebec5d4efad19b104d654a587c0adbd5f502128f89601408cb4d7d0c")
    version("0.6.0", sha256="078f086a13b67a97e4ab6fe1063f2fef2356df297e45b43bb43d74635f80475d")
    version("0.5.1", sha256="68a3696d1ec6d3a4402b44a464d723e6529ec41016f9b44c053676affe516d44")
    version("0.5.0", sha256="7efac668763d02bd0a2c0c1b134d9f5ee27e99008183905bb0512e5502b8b4fe")
    version("0.4.0", sha256="c228e6f0ce5a9c0ffb98e0b3d886f2758ace1a4b40d00f3f118542c0747c1f52")
    version("0.3.1", sha256="7b358ca03bb179876291d4a55d6a1c944b7407a80a588795b9e47940b1990521")
    version("0.3.0", sha256="52e9cf5720560e5f7492876c39ef2ea20ae73187338361d2744bdf67567da155")
    # note: checksums on github automatic release source tars changed ~9/17
    version("0.2.1", sha256="796576b9c69717c52f0035542c260eb7567aa351ee892d3fbe3521c38f1520c4")
    version("0.2.0", sha256="31eff8dbc654a4b235cfcbc326a319e1752728684296721535c7ca1c9b463061")

    maintainers("cyrush")

    root_cmakelists_dir = "src"

    ###########################################################################
    # package variants
    ###########################################################################

    variant("examples", default=True, description="Build Conduit examples")
    variant("shared", default=True, description="Build Conduit as shared libs")
    variant("test", default=True, description="Enable Conduit unit tests")
    variant("utilities", default=True, description="Build Conduit utilities")

    # variants for python support
    variant("python", default=False, description="Build Conduit Python support")
    variant("fortran", default=True, description="Build Conduit Fortran support")

    # variants for comm and i/o
    variant("mpi", default=True, description="Build Conduit MPI Support")
    # set to false for systems that implicitly link mpi
    variant("blt_find_mpi", default=True, description="Use BLT CMake Find MPI logic")
    variant("hdf5", default=True, description="Build Conduit HDF5 support")
    # TODO: remove 'compat' variant when VisIt starts distributing HDF5
    # binaries
    variant(
        "hdf5_compat",
        default=True,
        when="+hdf5",
        description="Build Conduit with HDF5 1.8.x (compatibility mode)",
    )
    variant("silo", default=False, description="Build Conduit Silo support")
    variant("adios", default=False, description="Build Conduit ADIOS support")
    variant("parmetis", default=True, description="Build Conduit Parmetis support")

    # zfp compression
    variant("zfp", default=False, description="Build Conduit ZFP support")

    # variants for dev-tools (docs, etc)
    variant("doc", default=False, description="Build Conduit's documentation")
    # doxygen support is wip, since doxygen has several dependencies
    # we want folks to explicitly opt in to building doxygen
    variant("doxygen", default=False, description="Build Conduit's Doxygen documentation")
    # caliper
    variant("caliper", default=False, description="Build Conduit Caliper support")

    ###########################################################################
    # package dependencies
    ###########################################################################

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    #######################
    # BLT
    #######################
    depends_on("blt", type="build")
    depends_on("blt@0.6.2:", type="build", when="@0.9:")

    #######################
    # CMake
    #######################
    # cmake 3.14.1 or newer basic requirement
    depends_on("cmake@3.14.1:", type="build")
    # cmake 3.21.0 or newer for conduit 0.9.0
    depends_on("cmake@3.21.0:", type="build", when="@0.9.0:")

    #######################
    # Python
    #######################
    depends_on("python", when="+python")
    extends("python", when="+python")
    depends_on("py-numpy", when="+python", type=("build", "run"))
    depends_on("py-mpi4py", when="+python+mpi", type=("build", "run"))
    depends_on("py-pip", when="+python", type="build")
    depends_on("py-wheel", when="+python", type="build")
    depends_on("py-setuptools", when="+python", type="build")

    #######################
    # I/O Packages
    #######################

    ###############
    # HDF5
    ###############
    depends_on("hdf5", when="+hdf5")
    depends_on("hdf5~shared", when="+hdf5~shared")
    # Require older HDF5 to ensure compatibility with VisIt: see #29132
    depends_on("hdf5@1.8.0:1.8", when="+hdf5+hdf5_compat")

    ###############
    # Silo
    ###############
    # we are not using silo's fortran features
    depends_on("silo+shared", when="+silo+shared")
    depends_on("silo~shared", when="+silo~shared")

    ###############
    # ADIOS
    ###############
    depends_on("adios+mpi~hdf5+shared", when="+adios+mpi+shared")
    depends_on("adios+mpi~hdf5~shared~blosc", when="+adios+mpi~shared")
    depends_on("adios~mpi~hdf5+shared", when="+adios~mpi+shared")
    depends_on("adios~mpi~hdf5~shared~blosc", when="+adios~mpi~shared")

    #######################
    # ZFP
    #######################
    depends_on("zfp  bsws=8", when="+zfp")

    # hdf5 zfp plugin when both hdf5 and zfp are on
    depends_on("h5z-zfp~fortran", when="+hdf5+zfp")

    #######################
    # Parmetis
    #######################
    depends_on("parmetis+shared", when="+parmetis+shared")
    depends_on("parmetis~shared", when="+parmetis~shared")
    depends_on("metis+shared", when="+parmetis+shared")
    depends_on("metis~shared", when="+parmetis~shared")

    #######################
    # MPI
    #######################
    depends_on("mpi", when="+mpi")

    #######################
    # Caliper
    #######################
    depends_on("caliper", when="+caliper")

    #######################
    # Documentation related
    #######################
    depends_on("py-sphinx", when="+python+doc", type="build")
    depends_on("py-sphinx-rtd-theme", when="+python+doc", type="build")
    depends_on("doxygen", when="+doc+doxygen")

    conflicts("+parmetis", when="~mpi", msg="Parmetis support requires MPI")

    # Tentative patch for fj compiler
    # Cmake will support fj compiler and this patch will be removed
    patch("fj_flags.patch", when="%fj")
    patch("bpparametis.patch", when="@0.8.1")

    # Add missing include for numeric_limits
    # https://github.com/LLNL/conduit/pull/773
    patch(
        "https://github.com/LLNL/conduit/commit/eb7dfce2229aac3b9644d422a44948509034e3c6.patch?full_index=1",
        when="@:0.7.2",
        sha256="379a1b68928d9078e7302efe694f43c51c8f2c26db4a58ab3fd753746b96b284",
    )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CTEST_OUTPUT_ON_FAILURE", "1")
        # conduit uses a <=1.10 api version before 0.8
        if "@:0.7 +hdf5" in self.spec and "@1.10:" in self.spec["hdf5"]:
            env.append_flags("CFLAGS", "-DH5_USE_110_API")
            env.append_flags("CXXFLAGS", "-DH5_USE_110_API")

    def url_for_version(self, version):
        """
        Provide proper url
        """
        v = str(version)
        if v == "0.2.0":
            return "https://github.com/LLNL/conduit/archive/v0.2.0.tar.gz"
        elif v == "0.2.1":
            return "https://github.com/LLNL/conduit/archive/v0.2.1.tar.gz"
        else:
            # starting with v 0.3.0, conduit uses BLT
            # (https://github.com/llnl/blt) as a submodule, since github does
            # not automatically package source from submodules, conduit
            # provides a custom src tarball
            return "https://github.com/LLNL/conduit/releases/download/v{0}/conduit-v{1}-src-with-blt.tar.gz".format(
                v, v
            )

    ##############################
    # Init compiler config entries
    ##############################
    def initconfig_compiler_entries(self):
        spec = self.spec
        entries = super().initconfig_compiler_entries()
        f_compiler = getattr(self.compiler, "fc", None)
        cpp_compiler = getattr(self.compiler, "cxx", "")
        rpaths = list(self.compiler.extra_rpaths)

        #  Note: This is not needed if we add `extra_rpaths` to this compiler spec case
        if (f_compiler is not None) and ("gfortran" in f_compiler) and ("clang" in cpp_compiler):
            libdir = os.path.join(os.path.dirname(os.path.dirname(f_compiler)), "lib")
            for _libpath in [libdir, libdir + "64"]:
                if os.path.exists(_libpath):
                    rpaths.append(_libpath)

        linkerflags = ""
        for rpath in rpaths:
            linkerflags += "-Wl,-rpath,{} ".format(rpath)
        entries.append(
            cmake_cache_string(
                "CMAKE_EXE_LINKER_FLAGS", "${CMAKE_EXE_LINKER_FLAGS} " + linkerflags, force=True
            )
        )
        if spec.satisfies("+shared"):
            entries.append(
                cmake_cache_string(
                    "CMAKE_SHARED_LINKER_FLAGS",
                    "${CMAKE_SHARED_LINKER_FLAGS} " + linkerflags,
                    force=True,
                )
            )

        if spec.satisfies("%cce"):
            entries.append(
                cmake_cache_string("CMAKE_Fortran_FLAGS", "${CMAKE_Fortran_FLAGS} -ef", force=True)
            )

        sys_type = os.environ.get("SYS_TYPE", str(spec.architecture))
        on_blueos = "blueos" in sys_type

        # extra fun for blueos
        if on_blueos and "+fortran" in spec and (f_compiler is not None) and ("xlf" in f_compiler):
            flags = "-WF,-C! -qxlf2003=polymorphic"
            entries.append(cmake_cache_string("BLT_FORTRAN_FLAGS", flags))
            # Grab lib directory for the current fortran compiler
            libdir = os.path.join(os.path.dirname(os.path.dirname(f_compiler)), "lib")
            rpaths = "-Wl,-rpath,{0} -Wl,-rpath,{0}64".format(libdir)

            flags = "${BLT_EXE_LINKER_FLAGS} -lstdc++ " + rpaths
            entries.append(cmake_cache_string("BLT_EXE_LINKER_FLAGS", flags))
            if spec.satisfies("+shared"):
                flags = "${CMAKE_SHARED_LINKER_FLAGS} " + rpaths
                entries.append(cmake_cache_string("CMAKE_SHARED_LINKER_FLAGS", flags, force=True))
        return entries

    #########################
    # Init mpi config entries
    #########################
    def initconfig_mpi_entries(self):
        spec = self.spec
        entries = super().initconfig_mpi_entries()
        entries.append(cmake_cache_option("ENABLE_MPI", spec.satisfies("+mpi")))
        if spec.satisfies("+mpi"):
            entries.append(cmake_cache_option("ENABLE_FIND_MPI", spec.satisfies("+blt_find_mpi")))
        return entries

    ######################################
    # Init package-specific config entries
    ######################################
    def initconfig_package_entries(self):
        spec = self.spec
        entries = super().initconfig_package_entries()

        entries.append(cmake_cache_path("BLT_SOURCE_DIR", spec["blt"].prefix))

        entries.append(cmake_cache_option("BUILD_SHARED_LIBS", spec.satisfies("+shared")))
        entries.append(cmake_cache_option("ENABLE_EXAMPLES", spec.satisfies("+examples")))
        entries.append(cmake_cache_option("ENABLE_UTILS", spec.satisfies("+utilities")))
        entries.append(cmake_cache_option("ENABLE_FORTRAN", spec.satisfies("+fortran")))
        entries.append(cmake_cache_option("ENABLE_PYTHON", spec.satisfies("+python")))

        if spec.satisfies("+python"):
            entries.append(cmake_cache_path("PYTHON_EXECUTABLE", spec["python"].command.path))
            try:
                entries.append(cmake_cache_path("PYTHON_MODULE_INSTALL_PREFIX", python_platlib))
            except NameError:
                pass

        enable_docs = False
        if spec.satisfies("+doc"):
            if spec.satisfies("+python"):
                enable_docs = True
                sphinx_build_exe = join_path(spec["py-sphinx"].prefix.bin, "sphinx-build")
                entries.append(cmake_cache_path("SPHINX_EXECUTABLE", sphinx_build_exe))
            if spec.satisfies("+doxygen"):
                doxygen_exe = spec["doxygen"].command.path
                entries.append(cmake_cache_path("DOXYGEN_EXECUTABLE", doxygen_exe))
        entries.append(cmake_cache_option("ENABLE_DOCS", enable_docs))

        entries.append(cmake_cache_option("ENABLE_TESTS", spec.satisfies("+test")))

        if spec.satisfies("+hdf5"):
            entries.append(cmake_cache_path("HDF5_DIR", spec["hdf5"].prefix))
            if spec.satisfies("^zlib-api"):
                # HDF5 depends on zlib
                entries.append(cmake_cache_path("ZLIB_DIR", spec["zlib-api"].prefix))
        if spec.satisfies("+silo"):
            entries.append(cmake_cache_path("SILO_DIR", spec["silo"].prefix))
        if spec.satisfies("+adios"):
            entries.append(cmake_cache_path("ADIOS_DIR", spec["adios"].prefix))
        if spec.satisfies("+zfp"):
            entries.append(cmake_cache_path("ZFP_DIR", spec["zfp"].prefix))
        if spec.satisfies("+hdf5+zfp"):
            entries.append(cmake_cache_path("H5ZZFP_DIR", spec["h5z-zfp"].prefix))
        if spec.satisfies("+parmetis"):
            entries.append(cmake_cache_path("PARMETIS_DIR", spec["parmetis"].prefix))
            entries.append(cmake_cache_path("METIS_DIR", spec["metis"].prefix))
        if spec.satisfies("+caliper"):
            entries.append(cmake_cache_path("CALIPER_DIR", spec["caliper"].prefix))
            entries.append(cmake_cache_path("ADIAK_DIR", spec["adiak"].prefix))

        return entries

    # cmake args handled by CachedCMakePackage
    def cmake_args(self):
        return []

    @run_after("build")
    @on_package_attributes(run_tests=True)
    def build_test(self):
        with working_dir(self.build_directory):
            tty.msg("Running Conduit Unit Tests...")
            make("test")

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_install(self):
        """
        Checks the spack install of conduit using conduit's
        using-with-cmake example
        """
        print("Checking Conduit installation...")
        spec = self.spec
        install_prefix = spec.prefix
        example_src_dir = join_path(install_prefix, "examples", "conduit", "using-with-cmake")
        print("Checking using-with-cmake example...")
        with working_dir("check-conduit-using-with-cmake-example", create=True):
            cmake_args = ["-DCONDUIT_DIR={0}".format(install_prefix), example_src_dir]
            cmake(*cmake_args)
            make()
            example = Executable("./conduit_example")
            example()
        print("Checking using-with-make example...")
        example_src_dir = join_path(install_prefix, "examples", "conduit", "using-with-make")
        example_files = glob.glob(join_path(example_src_dir, "*"))
        with working_dir("check-conduit-using-with-make-example", create=True):
            for example_file in example_files:
                shutil.copy(example_file, ".")
            make("CONDUIT_DIR={0}".format(install_prefix))
            example = Executable("./conduit_example")
            example()
