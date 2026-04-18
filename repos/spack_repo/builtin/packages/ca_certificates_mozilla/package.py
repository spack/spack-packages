# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class CaCertificatesMozilla(Package):
    """The Mozilla CA certificate store in PEM format"""

    homepage = "https://curl.se/docs/caextract.html"
    url = "https://curl.se/ca/cacert-2021-04-13.pem"

    maintainers("haampie")

    version(
        "2026-03-19",
        sha256="b6e66569cc3d438dd5abe514d0df50005d570bfc96c14dca8f768d020cb96171",
        expand=False,
    )
    version(
        "2025-08-12",
        sha256="64dfd5b1026700e0a0a324964749da9adc69ae5e51e899bf16ff47d6fd0e9a5e",
        expand=False,
        deprecated=True,
    )

    def url_for_version(self, version):
        return f"https://curl.se/ca/cacert-{version}.pem"

    def setup_dependent_package(self, module, dependent_spec):
        """Returns the absolute path to the bundled certificates"""
        self.spec.pem_path = join_path(self.prefix.share, "cacert.pem")

    # Install the the pem file as share/cacert.pem
    def install(self, spec, prefix):
        share = join_path(prefix, "share")
        # https://github.com/spack/spack/issues/32948
        mkdirp(share)
        install(f"cacert-{spec.version}.pem", join_path(share, "cacert.pem"))
