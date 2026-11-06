# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFreesasa(PythonPackage):
    """Python bindings for the FreeSASA library, used to calculate
    solvent accessible surface areas of proteins.
    """

    homepage = "https://freesasa.github.io/"
    pypi = "freesasa/freesasa-2.2.1.tar.gz"

    license("MIT", checked_by="V-Karch")

    version(
        "2.2.1",
        sha256="5630e65d619cf6a062028d7c6297afe8c5b18c677c75f1c32a0938399f4f6850",
    )

    # Build dependencies
    depends_on("c", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("py-cython@0.29.13:", type="build")

    # FreeSASA supports Python 3.7 and newer.
    depends_on("python@3.7:", type=("build", "run"))
