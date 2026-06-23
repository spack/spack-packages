# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNumkong(PythonPackage):
    """Portable mixed-precision math, linear algebra, and retrieval kernels."""

    homepage = "https://github.com/ashvardanian/NumKong"
    pypi = "numkong/numkong-7.7.0.tar.gz"

    license("Apache-2.0")

    version("7.7.0", sha256="a7605738c2ca96e2f85747fdf670625ba5fa10cccef90055e247a1a21b92f920")
    version("7.4.5", sha256="08ba372de44b08ecb989d8f3afdfe33857b92346033b85ff6721faa4588f4852")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
