# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Ulmblas(MakefilePackage):
    """BLAS library (Fortran 77 and CBLAS interfaces) that selects its
    micro kernels for the CPU at load time."""

    homepage = "https://github.com/michael-lehn/ulmBLAS"
    url = "https://github.com/michael-lehn/ulmBLAS/archive/refs/tags/v0.4.2.tar.gz"
    git = "https://github.com/michael-lehn/ulmBLAS.git"

    maintainers("michael-lehn")

    license("BSD-3-Clause")

    version("0.4.2", sha256="897ff3e954d973de59e60d9ee1980b02cd8838e7c1fd7ec1b47f7666e66b815b")

    provides("blas")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    # the Netlib test programs of the check phase (the library is C++ only);
    # Spack's compiler wrapper for gfortran needs this declaration
    depends_on("fortran", type="build")

    # macOS: Apple Silicon only
    conflicts("platform=darwin target=x86_64:")

    def setup_build_environment(self, env):
        env.set("ULMBLAS_VERSION", str(self.spec.version))
        env.set("ULMBLAS_STATIC_LIBSTDCXX", "no")

    # FC=none: without libulmlapack, Reference-LAPACK on top of ulmBLAS (its
    # sources would be downloaded); LAPACK comes from a lapack provider, e.g.
    # netlib-lapack+external-blas
    @property
    def build_targets(self):
        return ["build-shared", f"PREFIX={self.prefix}", "FC=none"]

    @property
    def install_targets(self):
        return ["install-shared", f"PREFIX={self.prefix}", "FC=none"]

    def check(self):
        make("check-package", f"FC={spack_fc}")
