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

    depends_on("blas")
    depends_on("givaro")
    depends_on("lapack")
