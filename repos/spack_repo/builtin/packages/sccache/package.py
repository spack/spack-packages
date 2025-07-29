# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems import cargo
from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Sccache(CargoPackage):
    """Sccache is a ccache-like tool. It is used as a compiler wrapper and avoids
    compilation when possible. Sccache has the capability to utilize caching in
    remote storage environments, including various cloud storage options, or
    alternatively, in local storage."""

    homepage = "https://github.com/mozilla/sccache"
    url = "https://github.com/mozilla/sccache/archive/refs/tags/v0.8.2.tar.gz"

    tags = ["build-tools"]

    executables = [r"^sccache$", r"^sscache-dist$"]

    license("Apache-2.0", checked_by="pranav-sivaraman")

    version("0.10.0", sha256="2c9f82c43ce6a1b1d9b34f029ce6862bedc2f01deff45cde5dffc079deeba801")
    version("0.8.2", sha256="2b3e0ef8902fe7bcdcfccf393e29f4ccaafc0194cbb93681eaac238cdc9b94f8")

    variant(
        "dist-server",
        default=False,
        description="Enables the sccache-dist binary",
        when="platform=linux",
    )

    depends_on("c", type="build")
    depends_on("rust@1.75:", type="build", when="@0.8.2:")
    depends_on("pkgconfig", type="build", when="platform=linux")

    depends_on("openssl", when="+dist-server")

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.match(r"sccache (\S+)", output)
        return match.group(1) if match else None

    @classmethod
    def determine_variants(cls, exes, version_str):
        if any(os.path.basename(path) == "sccache-dist" for path in exes):
            return "+dist-server"
        else:
            return "~dist-server"


class CargoBuilder(cargo.CargoBuilder):
    @property
    def build_args(self):
        if self.spec.satisfies("+dist-server"):
            return ["--features=dist-server"]

        return []
