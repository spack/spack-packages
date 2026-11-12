# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPasqalCloud(PythonPackage):
    """Software development kit for Pasqal cloud platform."""

    homepage = "https://github.com/pasqal-io/pasqal-cloud"
    pypi = "pasqal_cloud/pasqal_cloud-0.23.0.tar.gz"

    supplier = "Organization: Pasqal Cloud Services"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("0.23.0", sha256="8d76b1678fd84421be0aca0351beae5ee2086286fa238f26a1ef399685a4bec8")

    with default_args(type="build"):
        depends_on("py-setuptools@42:")

    with default_args(type=("build", "run")):
        depends_on("py-auth0-python@3.23.1:3")
        depends_on("py-requests@2.25.1:2")
        depends_on("py-pyjwt@2.5.0:2 +crypto")
        depends_on("py-pydantic@2.6.0:2")
        depends_on("py-pulser-core@1.8:")
        depends_on("py-tenacity@9.1:")
