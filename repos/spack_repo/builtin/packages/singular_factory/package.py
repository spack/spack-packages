# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class SingularFactory(AutotoolsPackage):
    """Factory is a C++ library for sparse multivariate polynomials over a
    variety of coefficient domains (integers, rationals, finite fields, and
    algebraic extensions). It implements efficient recursive representations
    and algorithms for GCDs, resultants, Chinese remaindering, and (absolute)
    factorization of multivariate polynomials. The library exposes a convenient
    interface via the CanonicalForm class that uses operator overloading to
    make polynomial operations feel like built-in types. Factory was originally
    developed by R. Stobbe and J. Schmidt and is currently maintained as part
    of the Singular project."""

    homepage = "https://www.singular.uni-kl.de/"
    url = "https://www.singular.uni-kl.de/ftp/pub/Math/Singular/Factory/factory-4.4.1.tar.gz"

    maintainers("d-torrance")

    license("GPL-2.0-or-later", checked_by="d-torrance")

    version("4.4.1", sha256="ba6a8a215448ebc0a0872a284cc9563c05a66d01944ef5fcfabfa5df672a68c0")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("flint")
    depends_on("gmp")
    depends_on("ntl+shared")

    # fix for building w/ flint >= 3.3.0 (backwards compatible w/ older flint)
    # https://github.com/Singular/Singular/pull/1278
    patch(
        "https://github.com/Singular/Singular/commit/05f5116e13c8a4f5f820c78c35944dd6d197d442.patch?full_index=1",
        sha256="20d4472a394fbb6559fdf07113b6a4693aa225e8ac484df72c3badbcd405c318",
        level=2,
        when="@:4.4.1",
    )
