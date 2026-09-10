# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPystacClient(PythonPackage):
    """Python library for working with Spatiotemporal Asset Catalog (STAC)."""

    homepage = "https://github.com/stac-utils/pystac-client.git"
    pypi = "pystac-client/pystac_client-0.8.5.tar.gz"

    license("Apache-2.0")

    version("0.8.5", sha256="7fba8d4f3c641ff7e840084fc3a53c96443a227f8a5889ae500fc38183ccd994")

    with default_args(type="build"):
        depends_on("py-setuptools@61:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@0.8:")
        # setup.py imports 'imp', removed in Python 3.12
        depends_on("python@:3.11", when="@:0.6")

        depends_on("py-requests@2.28.2:")
        depends_on("py-pystac@1.10:+validation")
        depends_on("py-python-dateutil@2.8.2:")
