# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.ruby import RubyPackage

from spack.package import *


class RubyCharlockHolmes(RubyPackage):
    """Character encoding detection, brought to you by ICU."""

    homepage = "https://github.com/brianmario/charlock_holmes"
    url = "https://rubygems.org/downloads/charlock_holmes-0.7.9.gem"

    license("MIT", checked_by="suzanneprentice")

    version(
        "0.7.9",
        sha256="b49e8a11ce1921e2c5b65511bb864ae51720ce9bd1c336ccf0e89e6c8ae62db0",
        expand=False,
    )

    depends_on("icu4c@74.2", type=("build", "link", "run"))

    def install(self, spec, prefix):
        gem(
            "install",
            "--install-dir",
            prefix,
            "charlock_holmes",
            "--",
            f"--with-icu-dir={spec['icu4c'].prefix}",
        )
