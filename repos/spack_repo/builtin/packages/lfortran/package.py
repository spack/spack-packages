# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Lfortran(CMakePackage):
    """Modern interactive LLVM-based Fortran compiler"""

    homepage = "https://lfortran.org"
    url = "https://github.com/lfortran/lfortran/releases/download/v0.49.0/lfortran-0.49.0.tar.gz"
    git = "https://github.com/lfortran/lfortran.git"

    maintainers("certik")
    license("BSD-3-Clause")

    # The build process uses 'git describe --tags' to get the package version
    version("main", branch="main", get_full_repo=True)
    version("0.63.0", sha256="e5ad61bc0571ec572dec542913858a9d9a6142ae5023ffc9517e1b0dc15da98c")
    version("0.62.0", sha256="6b34221fa85ab2e3f102a73bcbf59125318f637bbb64da34fe1200425eed4788")
    version("0.61.0", sha256="e832c1d76c371da7a7e11ef9e7b686d9047788136dcfb20093da5dc165fcd20f")
    version("0.54.0", sha256="a46c44f8398ed0d14ca051a08982a3001642449c06a3be1c30944c3e027bbf51")
    version("0.49.0", sha256="a9225fd33d34ce786f72a964a1179579caff62dd176a6a1477d2594fecdc7cd6")
    version("0.30.0", sha256="aafdfbfe81d69ceb3650ae1cf9bcd8a1f1532d895bf88f3071fe9610859bcd6f")
    version(
        "0.19.0",
        sha256="d496f61d7133b624deb3562677c0cbf98e747262babd4ac010dbd3ab4303d805",
        url="https://lfortran.github.io/tarballs/release/lfortran-0.19.0.tar.gz",
    )

    variant("kokkos", default=True, description="Build with Kokkos support")
    variant("llvm", default=True, description="Build with LLVM support")
    variant("stacktrace", default=True, description="Build with stacktrace support")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("python@3:", type="build", when="@main")
    depends_on("cmake", type="build")
    depends_on("cmake@3.22:", type="build", when="+kokkos")
    depends_on("kokkos", type=("build", "run"), when="+kokkos")
    depends_on("llvm@11:15", type=("build", "run"), when="@0.19.0+llvm")
    depends_on("llvm@11:16", type=("build", "run"), when="@0.30.0+llvm")
    depends_on("llvm@11:", type=("build", "run"), when="+llvm")
    depends_on("zlib-api")
    depends_on("re2c", type="build", when="@main")
    depends_on("bison@:3.4", type="build", when="@main")
    depends_on("binutils@2.38:", type="build", when="platform=linux")
    depends_on("zstd")
    depends_on("libunwind")

    def cmake_args(self):
        args = [
            self.define_from_variant("WITH_LLVM", "llvm"),
            self.define_from_variant("WITH_STACKTRACE", "stacktrace"),
            self.define_from_variant("WITH_KOKKOS", "kokkos"),
        ]

        # Only call bootstrap script for git checkout
        if self.spec.satisfies("@main"):
            args.append("-DLFORTRAN_BUILD_ALL=yes")

        return args
