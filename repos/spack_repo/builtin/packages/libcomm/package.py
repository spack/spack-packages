# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Libcomm(Package):
    """LibComm is a header-only communication library from the ABACUS
    ecosystem. It is required by LibRI, which ABACUS uses for
    resolution-of-identity hybrid functional (EXX) calculations."""

    homepage = "https://github.com/abacusmodeling/LibComm"
    url = "https://github.com/abacusmodeling/LibComm/archive/refs/tags/v0.1.1.tar.gz"

    maintainers("s8ga")

    license("GPL-3.0-only", checked_by="s8ga")

    version("0.1.1", sha256="9c47b6ea9573bffa4232c0bef63714d4c3af820c6b7539cfa6e294ca2b8ba4af")
    version("0.1.0", sha256="48899b9877bcddf3cc03e4e7323e38cfd802d756b7bafba58f151f81a3fa6ed4")

    depends_on("cxx", type="build")

    sanity_check_is_file = [join_path("include", "Comm", "Comm_Tools.h")]

    def install(self, spec, prefix):
        install_tree("include", prefix.include)
