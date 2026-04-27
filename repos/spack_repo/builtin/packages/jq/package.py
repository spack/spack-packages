# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Jq(AutotoolsPackage):
    """jq is a lightweight and flexible command-line JSON processor."""

    homepage = "https://jqlang.org/"
    url = "https://github.com/jqlang/jq/releases/download/jq-1.6/jq-1.6.tar.gz"

    license("MIT")

    version("1.8.1", sha256="2be64e7129cecb11d5906290eba10af694fb9e3e7f9fc208a311dc33ca837eb0")
    version("1.8.0", sha256="91811577f91d9a6195ff50c2bffec9b72c8429dc05ec3ea022fd95c06d2b319c")
    depends_on("c", type="build")  # generated

    depends_on("oniguruma")
    depends_on("bison@3.0:", type="build")

    def configure_args(self):
        # on darwin, required math functions like lgammaf_r are gated behind
        # explicit reentrant flag
        if sys.platform == "darwin":
            return ["CPPFLAGS=-D_REENTRANT"]
        else:
            return []

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def install_test(self):
        jq = self.command
        f = os.path.join(os.path.dirname(__file__), "input.json")

        assert jq(".bar", input=f, output=str) == "2\n"
