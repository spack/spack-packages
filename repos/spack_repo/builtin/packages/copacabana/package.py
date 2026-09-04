# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Copacabana(Package):
    """Copacabana - the CMake package tools a C++ library's build, tests, documentation
    and packaging are written with, shared by a family of header-only libraries."""

    homepage = "https://github.com/jfalcou/copacabana"
    url = "https://github.com/jfalcou/copacabana/archive/refs/tags/v7.tar.gz"
    git = "https://github.com/jfalcou/copacabana.git"

    maintainers("jfalcou")

    license("BSL-1.0")

    version("main", branch="main")
    version("7", sha256="c24436ebcdda92b87d02b28d4c6f9d5c20a58ac254725280d142e8d72e8c6412")

    # CPM fetches this at configure time from the projects using it. A consumer points
    # CPM_COPACABANA_SOURCE at this prefix instead, which has the layout the fetch would have.
    def install(self, spec, prefix):
        install_tree("copacabana", prefix.copacabana)
        install("LICENSE", prefix)
