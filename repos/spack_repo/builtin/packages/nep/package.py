# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Nep(CMakePackage):
    """NEP (NetCDF Expansion Pack) provides high-performance compression for
    HDF5/NetCDF-4 files with LZ4 and BZIP2 compression algorithms."""

    homepage = "https://github.com/Intelligent-Data-Design-Inc/NEP"
    url = "https://github.com/Intelligent-Data-Design-Inc/NEP/archive/v1.0.0.tar.gz"
    git = "https://github.com/Intelligent-Data-Design-Inc/NEP.git"

    maintainers("edhartnett")

    license("Apache-2.0")

    version("develop", branch="main")
    version("1.3.0", sha256="acf8f8a1360b521cef3f6f57fdeced64d2d78e765e8fd644ce435487fe74a003")

    variant("docs", default=True, description="Build documentation with Doxygen")
    variant("lz4", default=True, description="Enable LZ4 compression support")
    variant("bzip2", default=True, description="Enable BZIP2 compression support")
    variant("fortran", default=True, description="Build Fortran wrappers")

    depends_on("netcdf-c@4.9:", type=("build", "link"))
    depends_on("hdf5@1.12:+hl~mpi", type=("build", "link"))
    depends_on("lz4", when="+lz4", type=("build", "link"))
    depends_on("bzip2", when="+bzip2", type=("build", "link"))
    depends_on("netcdf-fortran", when="+fortran", type=("build", "link"))
    depends_on("doxygen", when="+docs", type="build")

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_DOCUMENTATION", "docs"),
            self.define_from_variant("ENABLE_FORTRAN", "fortran"),
        ]
        return args

    def check(self):
        """Run tests to verify build."""
        with working_dir(self.build_directory):
            make("test")

    @run_after("install")
    def check_install(self):
        """Verify that plugin libraries are installed."""
        plugin_dir = join_path(self.prefix.lib, "plugin")
        if "+lz4" in self.spec:
            assert os.path.exists(join_path(plugin_dir, "libh5lz4.so"))
        if "+bzip2" in self.spec:
            assert os.path.exists(join_path(plugin_dir, "libh5bzip2.so"))
