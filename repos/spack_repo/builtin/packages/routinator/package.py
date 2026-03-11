# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Routinator(Package):
    """An RPKI Validator and RTR server written in Rust"""

    homepage = "https://nlnetlabs.nl/projects/rpki/about/"
    url = "https://github.com/NLnetLabs/routinator/archive/refs/tags/v0.11.2.tar.gz"

    maintainers("aweits")

    license("BSD-3-Clause")

    version("0.14.0", sha256="861e90f395344be19880485185df47e8fd258cc583b82be702af660b466955cb")
    version("0.12.1", sha256="8150fe544f89205bb2d65bca46388f055cf13971d3163fe17508bf231f9ab8bc")

    depends_on("rust@1.63:", when="@0.12.1")
    depends_on("rust@1.70:", when="@0.13.0:")

    def install(self, spec, prefix):
        cargo = which("cargo", required=True)
        cargo("install", "--root", prefix, "--path", ".")
