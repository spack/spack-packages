# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestLazyFixtures(PythonPackage):
    """Allows you to use fixtures in @pytest.mark.parametrize."""

    homepage = "https://github.com/dev-petrov/pytest-lazy-fixtures"
    pypi = "pytest_lazy_fixtures/pytest_lazy_fixtures-1.4.0.tar.gz"

    license("MIT")

    version("1.4.0", sha256="f544b60c96b909b307558a62cc1f28f026f11e9f03d7f583a1dc636de3dbcb10")
    version("1.3.4", sha256="7dd2c110830897b83f041d3a503cbdda10c98ced6dca7602fc43e2f6017c27ed")

    # Python version compatibility requirement
    depends_on("python@3.8:", type=("build", "run"))

    # Build system dependencies (PEP 517 standard via Hatchling)
    depends_on("py-hatchling", type="build")

    # Runtime dependencies
    depends_on("py-pytest@7.1:", type=("build", "run"))
