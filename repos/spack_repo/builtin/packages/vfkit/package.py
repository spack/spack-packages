# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Vfkit(MakefilePackage):
    """Simple command line tool to start VMs through the macOS Virtualization framework."""

    homepage = "https://github.com/crc-org/vfkit"
    url = "https://github.com/crc-org/vfkit/archive/refs/tags/v0.6.1.tar.gz"

    license("Apache-2.0", checked_by="cmelone")

    version("0.6.1", sha256="e35b44338e43d465f76dddbd3def25cbb31e56d822db365df9a79b13fc22698c")

    depends_on("go@1.23.0:", type="build")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        env["CGO_ENABLED"] = "1"
        env["CGO_CFLAGS"] = "-mmacosx-version-min=11.0"
        make("out/vfkit")
        install("out/vfkit", prefix.bin)
