# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import depends_on, maintainers, version


class PyGestApi(PythonPackage):
    """Standardized interface for generators in optimization libraries"""

    homepage = "https://gest-api.readthedocs.io"
    pypi = "https://pypi.org/project/gest-api/"
    git = "https://github.com/campa-consortium/gest-api"

    maintainers("shudson")

    version("0.1.0", sha256="c5712721072fab8fdef7e976d4140db99729245f34ff36eefc0737c5197d25a8")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-pydantic@2:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
