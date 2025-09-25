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
        "2025-08-12",
        sha256="64dfd5b1026700e0a0a324964749da9adc69ae5e51e899bf16ff47d6fd0e9a5e",
        expand=False,
    )

    # Make spack checksum work
    def url_for_version(self, version):
        return "https://curl.se/ca/cacert-{0}.pem".format(version)

    def setup_dependent_package(self, module, dep_spec):
        """Returns the absolute path to the bundled certificates"""
        self.spec.pem_path = join_path(self.prefix.share, "cacert.pem")

    # Install the the pem file as share/cacert.pem
    def install(self, spec, prefix):
        share = join_path(prefix, "share")
        # https://github.com/spack/spack/issues/32948
        mkdirp(share)
        install("cacert-{0}.pem".format(spec.version), join_path(share, "cacert.pem"))
