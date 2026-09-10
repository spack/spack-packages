# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIntake(PythonPackage):
    """Data catalog, search and load"""

    homepage = "https://github.com/intake/intake"
    git = "https://github.com/intake/intake.git"
    pypi = "intake/intake-2.0.8.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("2.0.8", sha256="731d484a002de2f659bb988f406b35037234a35c17b08776d9a5e4838ecf2769")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@64:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")
    depends_on("py-fsspec@2023:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-platformdirs", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
