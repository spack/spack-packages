# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySparse(PythonPackage):
    """This library provides multi-dimensional sparse arrays."""

    homepage = "https://sparse.pydata.org"
    pypi = "sparse/sparse-0.11.2.tar.gz"

    maintainers("LydDeb")

    license("BSD-3-Clause")

    version("0.17.0", sha256="6b1ad51a810c5be40b6f95e28513ec810fe1c785923bd83b2e4839a751df4bf7")
    version("0.11.2", sha256="bc5c35dbc81242237feb7a8e1f7d9c5e9dd9bb0910f6ec55f50dcc379082864f")

    depends_on("python@3.10:", type=("build", "run"), when="@0.17.0")
    depends_on("python@3.6:3", type=("build", "run"), when="@0.11.2")
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@64:", type="build", when="@0.17.0")
    depends_on("py-setuptools-scm@8:", type="build", when="@0.17.0")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-numpy@1.17:", type=("build", "run"), when="@0.17.0")
    depends_on("py-scipy@0.19:", type=("build", "run"))
    depends_on("py-numba@0.49:", type=("build", "run"))
