# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Multichase(MakefilePackage):
    """Multichase pointer chaser benchmark."""

    homepage = "https://github.com/google/multichase"
    git = "https://github.com/google/multichase.git"

    license("Apache-2.0")

    # There are no releases or tags in the repo
    version("master", branch="master")

    # glibc-static is not available in most environments
    variant("static", default=False, description="Link statically (requires glibc-static)")

    depends_on("c", type="build")

    def build(self, spec, prefix):
        make_args = []
        if "+static" not in spec:
            make_args.append("LDFLAGS=-g -O3 -pthread")
        make(*make_args)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("multichase", prefix.bin)
        install("multiload", prefix.bin)
        install("pingpong", prefix.bin)
        install("fairness", prefix.bin)
