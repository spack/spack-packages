# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Sage(Package):
    """Proteomics search & quantification"""

    homepage = "https://sage-docs.vercel.app"
    url = "https://github.com/lazear/sage/archive/refs/tags/v0.14.7.tar.gz"

    license("MIT")

    version(
        "0.15.0-beta.2", sha256="1a0a67372f04c4f69d635270a33ab8f7308f4eb9783f3fda433bed3215f74810"
    )
    version("0.14.7", sha256="894b59429a67dc22592fc65fca547ee6d67f8bada71d09f7c1a81524b65fe6da")

    depends_on("rust@1.85:", type=("build", "test"), when="@0.15:")
    depends_on("rust@:1.79", type=("build", "test"), when="@:0.14.7")

    def patch(self):
        copy("Cargo.lock", "crates/sage-cli")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("build", "--release")

        if self.run_tests:
            sage = Executable("target/release/sage")
            sage("tests/config.json")

        cargo("install", "--path", "crates/sage-cli", "--root", prefix, "--locked")
