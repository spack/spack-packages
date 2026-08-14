# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class FflasFfpack(AutotoolsPackage):
    """FFLAS-FFPACK is a library for dense linear algebra over finite
    fields, providing high-performance implementations of classical
    and fast matrix algorithms (e.g., Gaussian elimination, rank,
    determinant, minimal/characteristic polynomials) using Givaro for
    finite field arithmetic."""

    homepage = "https://linbox-team.github.io/fflas-ffpack/"
    url = "https://github.com/linbox-team/fflas-ffpack/releases/download/v2.5.0/fflas-ffpack-2.5.0.tar.gz"

    maintainers("d-torrance")

    license("LGPL-2.1-or-later", checked_by="d-torrance")

    version("2.5.0", sha256="dafb4c0835824d28e4f823748579be6e4c8889c9570c6ce9cce1e186c3ebbb23")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("pkgconfig", type="build")

    depends_on("givaro")
    depends_on("lapack")

    # require blas w/o threads
    depends_on("blas")
    for pkg in [
        "acfl",
        "amdblis",
        "armpl-gcc",
        "atlas",
        "blis",
        "essl",
        "intel-oneapi-mkl",
        "nvpl-blas",
        "openblas",
    ]:
        depends_on(f"{pkg} threads=none", when=f"^[virtuals=blas] {pkg}")

    # fix build w/ netlib-lapack
    with when("@2.5.0"):
        # https://github.com/linbox-team/fflas-ffpack/pull/384
        patch(
            "https://github.com/linbox-team/fflas-ffpack/commit/2cd3a04050f2fa447d8a9c8265f32f25f4cb6546.patch?full_index=1",
            sha256="86186030f6d82f4ce2ae5acc5de23568bd057ef177d31ff6a717e7cc7697aa60",
        )
        # https://github.com/linbox-team/fflas-ffpack/pull/385
        patch(
            "https://github.com/linbox-team/fflas-ffpack/commit/97ee718ebc054d3dda020223a7d777786f7ad924.patch?full_index=1",
            sha256="15b956fa5188f5c6f684c578004230f7f996144cc63429323d3b89e296d509e0",
        )
        # https://github.com/linbox-team/fflas-ffpack/pull/403
        patch(
            "https://github.com/linbox-team/fflas-ffpack/commit/9994f6aa5fc2e3677b14c3d12671ba46ce5a58b5.patch?full_index=1",
            sha256="d3562239a4e04b5411e638ab5752afbe7649a38d97fd27f07928fb129a2648c6",
        )

    def configure_args(self):
        blas_headers = self.spec["blas"].headers + self.spec["lapack"].headers
        blas_libs = self.spec["blas"].libs + self.spec["lapack"].libs
        return [
            f"--with-blas-cflags={blas_headers.include_flags}",
            f"--with-blas-libs={blas_libs.ld_flags}",
        ]
