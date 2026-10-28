# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Et(CMakePackage):
    """
    eT is an open source program with coupled cluster, multiscale and multilevel methods.
    """

    homepage = "https://etprogram.org"
    git = "https://gitlab.com/eT-program/eT"

    license("GPL-3.0-only")

    version("development", branch="development", submodules=True )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("mpi")
    depends_on("python@3.7:")
    depends_on("lapack")
    depends_on("blas")
    depends_on("libint@2: tune=et")
    depends_on("cmake@3.22:", type="build")
    
    @property
    def build_directory(self):
        return os.path.join(self.prefix,"build")

    @property
    def root_cmakelists_dir(self) -> str:
        """The relative path to the directory containing CMakeLists.txt

        This path is relative to the root of the extracted tarball,
        not to the ``build_directory``. Defaults to the current directory.
        """
        return self.prefix

    def patch(self):
        filter_file(
            r"(default_path =.*.parent)",
            r"\1.parent",
            "dev_tools/autogenerate_files.py"
        )

    def cmake_args(self):
        args = []
        mathlibs = self.spec['blas'].libs + self.spec['lapack'].libs
        args.extend(
            [
                f"-DENABLE_64BIT_INTEGERS=ON",
                f"-DENABLE_OMP=ON",
                f"-DENABLE_THREADED_MKL=ON",
                f"-DENABLE_RUNTIME_CHECKS=OFF",
                f"-DENABLE_FORCED_BATCHING=OFF",
                f"-DENABLE_INITIALIZE_NAN=OFF",
                f"-DENABLE_PCMSOLVER=OFF",
                f"-DENABLE_PFUNIT=OFF",
                f"-DINTEGRAL_LIBRARY=libint",
                f"-DOEI_LIBRARY=libint",
                f"-DERI_LIBRARY=libint",
                f"-DLIBINT2_ROOT=" + self.spec["libint"].prefix,
                f"-DENABLE_AUTO_BLAS=OFF",
                f"-DENABLE_AUTO_LAPACK=OFF",
                f"-DEXTRA_LINKER_FLAGS={mathlibs.ld_flags}",
            ]
        )

        return args

    def cmake(self, spec, prefix):
        # Run generator
        # Builds in-place.
        install_tree(".", prefix)
        python = which("python")
        with working_dir(self.prefix):
            python("./dev_tools/autogenerate_files.py")
        options = self.std_cmake_args
        options += self.cmake_args()
        options.append(os.path.abspath(self.root_cmakelists_dir))
        with working_dir(self.build_directory, create=True):
            cmake(*options)

    def install(self, spec, prefix):
        pass

    def setup_run_environment(self, env):
        etdir = join_path(self.prefix, "build")
        env.prepend_path("PATH", etdir)
