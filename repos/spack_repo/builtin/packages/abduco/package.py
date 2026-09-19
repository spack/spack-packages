# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Abduco(MakefilePackage):
    """abduco provides session management i.e. it allows programs to be
    run independently from its controlling terminal. That is programs
    can be detached - run in the background - and then later reattached.
    Together with dvtm it provides a simpler and cleaner alternative to
    tmux or screen."""

    homepage = "https://github.com/martanne/abduco"
    url = "https://github.com/martanne/abduco/archive/v0.6.tar.gz"

    license("ISC")

    version("0.6", sha256="647d0381418f43a38f861d151b0efb2e3458ec651914e7d477956768b0af9bb7")
    version("0.5", sha256="0f7515455d982ca42fd0af4f9bf917c526345a80b929b6d69aaddf9915a8a9b8")
    version("0.4", sha256="6e22a535f96ec4999cde13654698504b724dc21c58b98763fda40d18e9bab121")

    depends_on("c", type="build")

    def install(self, spec, prefix):
        make(f"PREFIX={prefix}", "install")
