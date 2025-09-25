# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Givaro(AutotoolsPackage):
    """Givaro is a C++ library focused on arithmetic and algebraic
    computations. It supports finite fields, finite rings,
    polynomials, algebraic number fields, and other algebraic
    structures. Givaro is widely used as a building block in computer
    algebra systems and research software for number theory, algebra,
    and cryptography."""

    homepage = "https://casys.gricad-pages.univ-grenoble-alpes.fr/givaro/"
    url = "https://github.com/linbox-team/givaro/releases/download/v4.2.1/givaro-4.2.1.tar.gz"

    maintainers("d-torrance")

    license("CECILL-B", checked_by="d-torrance")

    version("4.2.1", sha256="feefb7445842ceb756f8bb13900d975b530551e488a2ae174bda7b636251de43")

    depends_on("cxx", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    depends_on("gmp")
