# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class _4ti2(AutotoolsPackage):
    """4ti2 is a software package for algebraic, geometric, and
    combinatorial problems on linear spaces. It provides tools for
    working with integer linear systems, Hilbert bases, Graver bases,
    Gröbner bases, and related structures that arise in combinatorial
    optimization and algebraic geometry."""

    homepage = "https://4ti2.github.io/"
    url = "https://github.com/4ti2/4ti2/releases/download/Release_1_6_13/4ti2-1.6.13.tar.gz"

    maintainers("d-torrance")

    license("GPL-2.0-or-later", checked_by="d-torrance")

    version("1.6.13", sha256="f59e1ea5563d2188b0e8ff61a8584845a899e3e54a570305f6f99b26c9b1e6b5")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("glpk")
    depends_on("gmp")

    depends_on("which", type="run")
