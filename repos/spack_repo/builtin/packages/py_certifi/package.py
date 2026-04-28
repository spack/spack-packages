# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCertifi(PythonPackage):
    """Certifi: A carefully curated collection of Root Certificates for validating
    the trustworthiness of SSL certificates while verifying the identity of TLS
    hosts."""

    homepage = "https://github.com/certifi/python-certifi"
    pypi = "certifi/certifi-2020.6.20.tar.gz"

    license("MPL-2.0")

    version("2026.2.25", sha256="e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7")
    version("2026.1.4", sha256="ac726dd470482006e014ad384921ed6438c457018f4b3d204aea4281258b2120")
    version("2025.7.14", sha256="8ea99dbdfaaf2ba2f9bac77b9249ef62ec5218e7c2b2e903378ed5fccf765995")
    version("2025.4.26", sha256="0a816057ea3cdefcef70270d2c515e4506bbc954f417fa5ade2021213bb8f0c6")

    with default_args(type="build"):
        depends_on("py-setuptools@42:")
