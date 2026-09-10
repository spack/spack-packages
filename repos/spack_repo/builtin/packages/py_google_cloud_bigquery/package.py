# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGoogleCloudBigquery(PythonPackage):
    """Google BigQuery API client library."""

    homepage = "https://github.com/googleapis/python-bigquery"
    pypi = "google_cloud_bigquery/google_cloud_bigquery-3.38.0.tar.gz"

    license("Apache-2.0")

    version("3.38.0", sha256="8afcb7116f5eac849097a344eb8bfda78b7cfaae128e60e019193dd483873520")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-google-api-core@2.11.1:2+grpc")
        depends_on("py-google-auth@2.14.1:2")
        depends_on("py-google-cloud-core@2.4.1:2")
        depends_on("py-google-resumable-media@2")
        depends_on("py-packaging@24.2:")
        depends_on("py-python-dateutil@2.8.2:2")
        depends_on("py-requests@2.21:2")
