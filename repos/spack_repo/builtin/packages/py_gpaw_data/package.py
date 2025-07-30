# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyGpawData(PythonPackage):
    """Data package for PAW files and other data files for the GPAW DFT code."""

    homepage = "https://gpaw.readthedocs.io/"
    pypi = "gpaw_data/gpaw_data-1.0.1.tar.gz"

    maintainers("alikhamze")

    license("GPL-3.0-or-later", checked_by="alikhamze")

    version("1.0.1", sha256="28212110aa04daae333ef1260b281d70b818ad9cf4282078624ee3fc7a8fc05c")
    with default_args(deprecated=True):
        version("1.0.0", sha256="28212110aa04daae333ef1260b281d70b818ad9cf4282078624ee3fc7a8fc05c")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    # depends_on("py-foo", type=("build", "run"))

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
