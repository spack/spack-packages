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

    maintainers("d-torrance")

    license("GPL-2.0-or-later", checked_by="d-torrance")

    version("1.6.15", sha256="070e639398fda1a4665b3291e5ea80f2ba280d9bffd50656ad8482d471b96965")
    version("1.6.14", sha256="1bc340173f93ca4abd30ea962118bd5057fdedf7e79c71d2a0c4cc9569f8b0b1")
    version("1.6.13", sha256="f59e1ea5563d2188b0e8ff61a8584845a899e3e54a570305f6f99b26c9b1e6b5")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("glpk")
    depends_on("gmp")

    depends_on("which", type="run")

    def url_for_version(self, version):
        return f"https://github.com/4ti2/4ti2/releases/download/Release_{version.underscored}/4ti2-{version}.tar.gz"
