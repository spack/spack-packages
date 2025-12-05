# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Gvproxy(MakefilePackage):
    """A new network stack based on gVisor."""

    homepage = "https://github.com/containers/gvisor-tap-vsock"
    url = "https://github.com/containers/gvisor-tap-vsock/archive/refs/tags/v0.8.6.tar.gz"

    license("Apache-2.0", checked_by="cmelone")

    version("0.8.6", sha256="eb08309d452823ca7e309da2f58c031bb42bb1b1f2f0bf09ca98b299e326b215")

    depends_on("go@1.23.0:", type="build")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        make("gvproxy")
        install("bin/gvproxy", prefix.bin)
