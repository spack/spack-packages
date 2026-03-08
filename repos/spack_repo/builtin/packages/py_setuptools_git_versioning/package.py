# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySetuptoolsGitVersioning(PythonPackage):
    """Use git repo data for building a version number according PEP-440"""

    homepage = "https://setuptools-git-versioning.readthedocs.io/"
    pypi = "setuptools-git-versioning/setuptools-git-versioning-1.13.3.tar.gz"

    maintainers("angus-g")

    license("MIT")

    version("2.0.0", sha256="85b5fbe7bda8e9c24bbd9e587a9d4b91129417f4dd3e11e3c0d5f3f835fc4d4d")
    version("1.13.6", sha256="75e3e8c4528fa21ca2417a1f222fdaaa4d2ca7d8536c44affad827c6ec9ba0d4")
    version("1.13.5", sha256="af9ad1e8103b5abb5b128c2db4fef99407328ac9c12f65d3ff9550c4bb39ad1c")
    version("1.13.4", sha256="0edb4aef1661eb84b6eff729e66c13ac8bc34baad035a05aaccfb46d4bbd5fcd")
    version("1.13.3", sha256="9dfc59a31dcadcae04bcddc50534ccfc07a25a3180ab5cc1b1e3730217971c63")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("git")
    depends_on("py-toml@0.10.2:", when="^python@:3.10", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
