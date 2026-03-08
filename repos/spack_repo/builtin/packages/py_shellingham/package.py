# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyShellingham(PythonPackage):
    """Tool to Detect Surrounding Shell"""

    homepage = "https://github.com/sarugaku/shellingham"
    pypi = "shellingham/shellingham-1.4.0.tar.gz"

    license("0BSD")

    version("1.5.4", sha256="8dbca0739d487e5bd35ab3ca4b36e11c4078f3a234bfce294b0a0291363404de")
    version(
        "1.5.0.post1", sha256="823bc5fb5c34d60f285b624e7264f4dda254bc803a3774a147bf99c0e3004a28"
    )
    version("1.5.0", sha256="72fb7f5c63103ca2cb91b23dee0c71fe8ad6fbfd46418ef17dbe40db51592dad")
    version("1.4.0", sha256="4855c2458d6904829bd34c299f11fdeed7cfefbf8a2c522e4caea6cd76b3171e")

    depends_on("python@2.6:2.7,3.4:", type=("build", "run"))
    depends_on("python@3.4:", when="@1.5.0:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
