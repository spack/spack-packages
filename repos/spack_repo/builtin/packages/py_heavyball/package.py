# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHeavyball(PythonPackage):
    """Efficient Optimizers"""

    homepage = "https://github.com/HomebrewML/HeavyBall"
    git = "https://github.com/HomebrewML/HeavyBall.git"
    pypi = "heavyball/heavyball-2.3.1.tar.gz"

    maintainers("LydDeb")

    license("BSD-2-Clause", checked_by="LydDeb")

    version("2.3.1", sha256="125e1858860063a319c5699736474d173b6121c82bc2b14e9c0bd5ea28bdcd4b")

    depends_on("python@3.9:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@75:")

    with default_args(type=("build", "run")):
        depends_on("py-opt-einsum@3.4.0:")
        depends_on("py-numpy@2.2:2")
        depends_on("py-torch@2.3.4:")
