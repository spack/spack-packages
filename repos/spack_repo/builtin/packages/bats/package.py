# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Bats(Package):
    """Bats is a TAP-compliant testing framework for Bash."""

    homepage = "https://github.com/bats-core/bats-core"
    url = "https://github.com/bats-core/bats-core/archive/refs/tags/v1.13.0.tar.gz"

    license("MIT")

    version("1.13.0", sha256="a85e12b8828271a152b338ca8109aa23493b57950987c8e6dff97ba492772ff3")
    version("1.10.0", sha256="a1a9f7875aa4b6a9480ca384d5865f1ccf1b0b1faead6b47aa47d79709a5c5fd")
    version(
        "0.4.0",
        sha256="480d8d64f1681eee78d1002527f3f06e1ac01e173b761bc73d0cf33f4dc1d8d7",
        url="https://github.com/sstephenson/bats/archive/v0.4.0.tar.gz",
    )

    def install(self, spec, prefix):
        bash = which("bash", required=True)
        bash("./install.sh", prefix)
