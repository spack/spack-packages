# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEtuples(PythonPackage):
    """Python S-expression emulation using tuple-like objects."""

    homepage = "https://github.com/pythological/etuples"
    pypi = "etuples/etuples-0.3.10.tar.gz"

    license("Apache-2.0")

    version("0.3.10", sha256="26fde81d7e822837146231bfce4d6ba67eab5d7ed55bc58ba7437c2568051167")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@80:", type="build")
    depends_on("py-setuptools-scm", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-cons")
        depends_on("py-multipledispatch")
