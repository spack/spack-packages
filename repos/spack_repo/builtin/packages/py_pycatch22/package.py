# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPycatch22(PythonPackage):
    """Python implementation of the catch22 time-series features."""

    homepage = "https://github.com/DynamicsAndNeuralSystems/pycatch22"
    pypi = "pycatch22/pycatch22-0.4.5.tar.gz"

    license("GPL-3.0-or-later")

    version("0.5.0", sha256="9a2de6f5fa4b23080e4e3a162d20f29a02f88a8afb9c2c6caf0a7f40c09d1899")
    version("0.4.5", sha256="7ec844c659f22bedc66847ac866ef2bd86ffbbd4d8114b5e97f699f20a6f9f81")

    depends_on("c", type="build")
    depends_on("python@3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
