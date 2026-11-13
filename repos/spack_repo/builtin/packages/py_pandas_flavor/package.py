# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPandasFlavor(PythonPackage):
    """The easy way to write your own Pandas flavor."""

    homepage = "https://github.com/pyjanitor-devs/pandas_flavor"
    pypi = "pandas_flavor/pandas_flavor-0.8.1.tar.gz"

    license("MIT")

    version("0.8.1", sha256="255fa5851833ee0132c4fdd6c1565ec1e938a8c2671c37e408006da6b2bdc366")

    with default_args(type="build"):
        depends_on("py-setuptools@61:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:")

        depends_on("py-pandas@0.23:")
        depends_on("py-xarray")
