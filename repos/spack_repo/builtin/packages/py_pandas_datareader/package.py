# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPandasDatareader(PythonPackage):
    """Up-to-date remote data access for pandas. Works for multiple versions of pandas"""

    homepage = "https://pypi.org/project/pandas-datareader"
    pypi = "pandas-datareader/pandas_datareader-0.11.1.tar.gz"
    git = "https://github.com/pydata/pandas-datareader.git"

    maintainers("climbfuji")

    license("BSD-3-Clause", checked_by="climbfuji")

    version("0.11.1", sha256="e1eadb6d2ccaa4b7a876a1c81b6ff0307fa7a08b56f7799862a50207c2e65a05")
    version("0.11.0", sha256="6c86360127f0b4c4451495574e162da058cf6154a185503310df70c417e0e266")
    version("0.10.0", sha256="9fc3c63d39bc0c10c2683f1c6d503ff625020383e38f6cbe14134826b454d5a6")

    def url_for_version(self, version):
        if isinstance(version, str):
            version = Version(version)

        if version < Version("0.11.0"):
            return f"https://files.pythonhosted.org/packages/source/p/pandas-datareader/pandas-datareader-{version}.tar.gz"

        return super().url_for_version(version)

    # Versioneer bundled with 0.10.0 uses APIs removed in Python 3.12.
    patch("py312-versioneer.patch", when="@0.10.0 ^python@3.12:")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("python@3.11:", when="@0.11.0:", type=("build", "run"))
    depends_on("py-setuptools@0.64:", type="build")
    depends_on("py-setuptools-scm@8", type="build")

    depends_on("py-lxml", type="run")
    depends_on("py-pandas@1.5.3:", when="@0.10.0", type="run")
    depends_on("py-pandas@2.1.4:", when="@0.11.0:", type="run")
    depends_on("py-statsmodels@0.12:", when="@0.10.0", type="run")
    depends_on("py-requests@2.19:", type="run")
