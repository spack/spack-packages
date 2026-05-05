# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyClarabel(PythonPackage):
    """Clarabel Conic Interior Point Solver for Rust / Python"""

    homepage = "https://clarabel.org"
    pypi = "clarabel/clarabel-0.11.1.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("0.11.1", sha256="e7c41c47f0e59aeab99aefff9e58af4a8753ee5269bbeecbd5526fc6f41b9598")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-maturin@1", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-cffi", type=("build", "run"))
