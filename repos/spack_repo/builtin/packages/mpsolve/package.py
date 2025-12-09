# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Mpsolve(AutotoolsPackage):
    """MPSolve is a multiprecision polynomial solver designed as a
    universal blackbox for solving polynomials and secular
    equations. It supports arbitrary precision approximation, provides
    guaranteed inclusion radii for computed roots, and exploits
    polynomial structure such as sparsity and special coefficient
    domains. MPSolve can also be specialized for particular classes of
    polynomials, enabling large-scale computations like the roots of
    the Mandelbrot polynomial of degree over two million."""

    homepage = "https://numpi.dm.unipi.it/scientific-computing-libraries/mpsolve/"

    maintainers("d-torrance")

    license("GPL-3.0-or-later", checked_by="d-torrance")

    version(
        "3.2.3",
        sha256="1f2e239c698c783b63a5e6903e76316c0335a01d71c466a8551e8a3f790b3971",
        url="https://numpi.dm.unipi.it/wp-content/uploads/2025/08/mpsolve-3.2.3.tar.bz2",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("gmp")
