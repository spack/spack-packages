# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class GitLfs(MakefilePackage):
    """Git LFS is a system for managing and versioning large files in
    association with a Git repository.  Instead of storing the large files
    within the Git repository as blobs, Git LFS stores special "pointer
    files" in the repository, while storing the actual file contents on a
    Git LFS server."""

    homepage = "https://git-lfs.github.com"
    url = "https://github.com/git-lfs/git-lfs/archive/v2.6.1.tar.gz"

    tags = ["build-tools"]

    executables = ["^git-lfs$"]

    maintainers("sethrj")

    license("MIT")

    version("3.7.1", sha256="0e83566a9e2477e03627e7fd6bf81f01fadbf93dcaf6abd2686fca90f6bac7dd")
    version("3.7.0", sha256="ab173702840627feb5f8a408dd5406fa322f3eadaa69938d9226b183d5be25a6")
    version("3.6.1", sha256="d682a12c0bc48d08d28834dd0d575c91d53dd6c6db63c45c2db7c3dd2fb69ea4")

    depends_on("go@1.24:", type="build", when="@3.7:")
    depends_on("go@1.23:", type="build", when="@3.6:")
    depends_on("git@2.0.0:", type="run", when="@3.7:")
    depends_on("git@1.8.2:", type="run")

    patch("patches/issue-10702.patch", when="@2.7.0:2.7.1")

    parallel = False

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"git-lfs/(\S+)", output)
        return match.group(1) if match else None

    # Git-lfs does not provide an 'install' target in the Makefile
    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path("bin", "git-lfs"), prefix.bin)
