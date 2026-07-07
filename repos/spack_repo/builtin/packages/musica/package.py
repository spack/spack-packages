# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Musica(CMakePackage):
    """MUSICA - The multi-scale interface for chemistry and aerosols

    MUSICA is a software package which exposes a flexible
    API for including aerosol and gas-phase chemistry in
    many contexts across languages and platforms. It is designed to
    be used in conjunction with other software packages, such as
    climate models, to provide a comprehensive framework for
    simulating atmospheric chemistry processes.
    """

    homepage = "https://github.com/NCAR/musica"
    url = "https://github.com/NCAR/musica/archive/refs/tags/v0.15.0.tar.gz"
    git = "https://github.com/NCAR/musica.git"

    maintainers("kshores", "boulderdaze")

    license("Apache-2.0", checked_by="kshores")

    # Versions
    version("0.15.0", sha256="48a01c082d8db8731add80c691c7794e7069927fa17ec21e093ad1774b8cd30b")
    version("0.14.5", sha256="31d9c75e8a4852f8f053f43a44313f3b392911056b72f63209eb2f091c7e486a")
    version("0.14.4", sha256="8de573c1cf9100087efa6ae4871f0d0bd8b41e75a67e43b62761410e5740d0d6")
    version("0.14.2", sha256="78cdab4e355535e1201bb8a4c997187bb59014984b956525dd8ed04c22669953")
    version("0.14.1", sha256="c776fc224b4d40cbc0371726240fd7f02b142c969ce1418627f63e0e4ec81829")
    version("0.14.0", sha256="f6841780747c522bfa4a27da0ec694373e08aa2488a748cd3dea81be5472db0c")
    version("0.13.0", sha256="fec033c39d48081185fcbbab96effe0a8c0994b91d8660f9b91d12ebad3b29d4")
    version("0.12.0", sha256="e81279fbdd42af8bf6540f18e72857ed34e081421a90333c77f9952a3069363b")
    version("0.10.1", sha256="edefab03a676a449761997734e6c5b654b2c4f92ce8f1cc66ef63b8ae8ccccf1")

    # Options from CMake
    variant("mpi", default=False, description="Enable MPI support")
    variant("openmp", default=False, description="Enable OpenMP support")
    variant("tests", default=True, description="Enable tests")
    variant("fortran", default=False, description="Build Fortran interface")
    variant("micm", default=True, description="Enable MICM support")
    variant("tuvx", default=True, description="Enable TUV-x support")

    # Dependencies
    depends_on("cmake@3.21:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("mpi", when="+mpi")
    depends_on("netcdf-fortran", when="+tuvx")

    def cmake_args(self):
        args = [
            self.define_from_variant("MUSICA_ENABLE_MPI", "mpi"),
            self.define_from_variant("MUSICA_ENABLE_OPENMP", "openmp"),
            self.define_from_variant("MUSICA_ENABLE_TESTS", "tests"),
            self.define_from_variant("MUSICA_BUILD_FORTRAN_INTERFACE", "fortran"),
            self.define_from_variant("MUSICA_ENABLE_MICM", "micm"),
            self.define_from_variant("MUSICA_ENABLE_TUVX", "tuvx"),
            self.define("MUSICA_ENABLE_INSTALL", True),
        ]
        return args
