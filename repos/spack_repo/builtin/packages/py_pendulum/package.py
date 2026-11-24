# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPendulum(PythonPackage):
    """Python datetimes made easy."""

    homepage = "https://pendulum.eustace.io/"
    pypi = "pendulum/pendulum-3.1.0.tar.gz"

    license("MIT")

    version("3.1.0", sha256="66f96303560f41d097bee7d2dc98ffca716fbb3a832c4b3062034c2d45865015")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-maturin@1", type="build")

    depends_on("py-python-dateutil@2.6:", type=("build", "run"))
    depends_on("py-tzdata@2020.1:", type=("build", "run"))
