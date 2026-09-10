# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCwlUpgrader(PythonPackage):
    """Common Workflow Language standalone document upgrader"""

    homepage = "https://github.com/common-workflow-language/cwl-upgrader"
    pypi = "cwl-upgrader/cwl-upgrader-1.2.4.tar.gz"

    license("Apache-2.0")

    version(
        "1.2.15",
        sha256="bb9e098ba6d1cc82c36dff1cbaad6779d6d9beab5324cf44a121d7faf7d58672",
        url="https://files.pythonhosted.org/packages/d7/f8/0159b1785cbb3e0b1538cd53ee64ffe94d9b3c2e4867ad47f2e071c5f9ec/cwl_upgrader-1.2.15.tar.gz",
    )
    version("1.2.4", sha256="b25fc236407343d44cc830ac3f63eed395b8d872fc7e17db92cde583d4a3b2ec")

    depends_on("python@3.6:3", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-ruamel-yaml@0.16.0:0.17.21", when="^python@3.10:", type=("build", "run"))
    depends_on("py-ruamel-yaml@0.15.98:0.17.21", when="^python@3.9:", type=("build", "run"))
    depends_on("py-ruamel-yaml@0.15.78:0.17.21", when="^python@3.8:", type=("build", "run"))
    depends_on("py-ruamel-yaml@0.15.71:0.17.21", type=("build", "run"))
    depends_on("py-schema-salad", type=("build", "run"))

    with when("@1.2.15:"):
        depends_on("py-setuptools@61.2:", type="build")
        depends_on("python@3.10:", type=("build", "run"))
        depends_on("py-ruamel-yaml@0.16.0:0.19", type=("build", "run"))
