# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestRetry(PythonPackage):
    """Adds the ability to retry flaky tests in CI environments."""

    homepage = "https://github.com/str0zzapreti/pytest-retry"
    pypi = "pytest_retry/pytest_retry-1.7.0.tar.gz"

    license("MIT")

    version("1.7.0", sha256="f8d52339f01e949df47c11ba9ee8d5b362f5824dff580d3870ec9ae0057df80f")

    depends_on("python@3.9:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@61:")

    with default_args(type=("build", "run")):
        depends_on("py-pytest@7:")
