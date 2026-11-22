# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Ulmblas(MakefilePackage):
    """BLAS (Fortran 77 and CBLAS interface) with micro kernels selected for
    the CPU at load time (x86-64: AVX-512, AVX2, SSE3 or generic; Apple
    Silicon: SME2 or NEON; Linux on aarch64: NEON)."""

    homepage = "https://github.com/michael-lehn/ulmBLAS"
    url = "https://github.com/michael-lehn/ulmBLAS/archive/refs/tags/v0.4.1.tar.gz"
    git = "https://github.com/michael-lehn/ulmBLAS.git"

    maintainers("michael-lehn")

    license("BSD-3-Clause")

    version("0.4.1", sha256="7b8f961438a00ddb35e258fba6322a249e9dc9d889831b454372cb0dd68883d2")

    provides("blas")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")
    # the Netlib test programs of the check phase (the library is C++ only);
    # Spack's compiler wrapper for gfortran needs this declaration
    depends_on("fortran", type="build")

    # macOS: Apple Silicon only
    conflicts("platform=darwin target=x86_64:")

    def setup_build_environment(self, env):
        env.set("ULMBLAS_VERSION", str(self.spec.version))
        env.set("ULMBLAS_STATIC_LIBSTDCXX", "no")
        env.set("ULMBLAS_INCLUDEDIR", self.prefix.include.ulmblas)
        env.set("FC", "none")
        env.set("MAKE", f"make -j{make_jobs}")

    def build(self, spec, prefix):
        sh = which("sh")
        sh("interfaces/install-shared.sh", prefix, extra_env={"ULMBLAS_STEP": "build"})

    def check(self):
        sh = which("sh")
        sh("packaging/check.sh", extra_env={"FC": spack_fc})

    def install(self, spec, prefix):
        sh = which("sh")
        sh("interfaces/install-shared.sh", prefix)

    @property
    def libs(self):
        return find_libraries("libulmblas", root=self.prefix, shared=True, recursive=True)

    @property
    def headers(self):
        return find_headers("cblas", root=self.prefix.include.ulmblas, recursive=False)
