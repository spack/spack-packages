# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Mscp(CMakePackage):
    """mscp: Parallel (multi-threaded) file transfer via SSH a fast alternative to scp."""

    homepage = "https://github.com/upa/mscp"
    git = "https://github.com/upa/mscp.git"

    version("0.2.4", tag="v0.2.4", submodules=True)

    depends_on("c", type="build")

    depends_on("cmake@3.13:", type="build")
    depends_on("zlib-api")
    depends_on("openssl")

    # mscp depends on a patched libssh. The patch introduces asynchronous SFTP Write, which is derived from https://github.com/limes-datentechnik-gmbh/libssh (see Re: SFTP Write async)
    @run_before("cmake")
    def patch_libssh(self):
        src = self.stage.source_path
        git = which("git", required=True)
        desc = git("-C", join_path(src, "libssh"), "describe", output=str).strip()
        patch_file = join_path(src, "patch", f"{desc}.patch")
        patch = which("patch", required=True)
        patch("-d", join_path(src, "libssh"), "-p1", "-i", patch_file)
