# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIlluminaUtils(PythonPackage):
    """A library and collection of scripts to work with Illumina paired-end
    data (for CASAVA 1.8+)."""

    homepage = "https://github.com/meren/illumina-utils"
    pypi = "illumina-utils/illumina-utils-2.2.tar.gz"

    license("GPL-2.0-or-later")

    version(
        "2.14",
        sha256="5536158e97f9264d428fb7666b9f60a9a19568a2dbd77331426e8043f9d55564",
        url="https://files.pythonhosted.org/packages/fb/10/c365f42d9a2e9d8d17773b7a8e5fbabdd4b55f6207b6cad8a7451674e27d/illumina_utils-2.14.tar.gz",
    )
    version("2.3", sha256="0e8407b91d530d9a53d8ec3c83e60f25e7f8f80d06ce17b8e4f57a02d3262441")
    version("2.2", sha256="6039c72d077c101710fe4fdbfeaa30caa1c3c2c84ffa6295456927d82def8e6d")

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-python-levenshtein", type=("build", "run"))

    with when("@2.14:"):
        depends_on("py-setuptools@61:", type="build")
        depends_on("py-wheel", type="build")
