# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMendeleev(PythonPackage):
    """Pythonic periodic table of elements."""

    homepage = "https://github.com/lmmentel/mendeleev"
    pypi = "mendeleev/mendeleev-1.1.0.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("1.1.0", sha256="34081dd9ae58823287382e8defde8276003d8c2784367bb1271e8e32e7fd07e8")

    depends_on("python@3.9:3.13", type=("build", "run"))
    depends_on("py-poetry-core@1.1.0:", type="build")
    depends_on("py-colorama@0.4", type=("build", "run"))
    depends_on("py-numpy@2.0", type=("build", "run"))
    depends_on("py-pyfiglet@0.8", type=("build", "run"))
    depends_on("py-pygments@2.11", type=("build", "run"))
    depends_on("py-pandas@2.1", type=("build", "run"), when="^python@3.12:3.13")
    depends_on("py-pandas@1.1.0:", type=("build", "run"), when="^python@:3.11")
    depends_on("py-sqlalchemy@1.4.0:", type=("build", "run"))
    depends_on("py-deprecated@1.2", type=("build", "run"))
    depends_on("py-pydantic@2.9", type=("build", "run"))
