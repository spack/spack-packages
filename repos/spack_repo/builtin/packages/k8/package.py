# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class K8(Package):
    """K8 is a Javascript shell based on Google's V8 Javascript engine."""

    homepage = "https://github.com/attractivechaos/k8"
    url = "https://github.com/attractivechaos/k8/releases/download/v0.2.4/k8-0.2.4.tar.bz2"

    version("1.0", sha256="61504dad2d63404bf523d3f8d0a8bfd72ec78aa7bd79bdf9291a4f629cfb9c02")
    version("0.2.4", sha256="da8a99c7f1ce7f0cb23ff07ce10510e770686b906d5431442a5439743c0b3c47")

    requires(
        "platform=linux target=x86_64:",
        "platform=darwin target=aarch64:",
        policy="one_of",
        msg="package is only available for darwin aarch64 or linux x86_64",
    )

    depends_on("zlib-api", type="run")

    def install(self, spec, prefix):
        if self.spec.satisfies("platform=darwin target=aarch64:"):
            if self.spec.satisfies("@=0.2.4"):
                os.rename("k8-Darwin", "k8")
            elif self.spec.satisfies("@1.0:"):
                os.rename("k8-arm64-Darwin", "k8")

        if self.spec.satisfies("platform=linux target=x86_64:"):
            if self.spec.satisfies("@=0.2.4"):
                os.rename("k8-Linux", "k8")
            elif self.spec.satisfies("@1.0:"):
                os.rename("k8-x86_64-Linux", "k8")

        install_tree(".", prefix.bin)
