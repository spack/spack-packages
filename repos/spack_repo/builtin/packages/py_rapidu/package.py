# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRapidu(PythonPackage):
    """A faster du that explains why a disk quota is full: inode counts, quota
    tables, and space held by deleted files that are still open."""

    homepage = "https://github.com/PursuitOfDataScience/rapidu"
    pypi = "rapidu/rapidu-0.6.0.tar.gz"

    maintainers("PursuitOfDataScience")

    license("MIT")

    version("0.6.0", sha256="5e8a32fb573372973841ccc662aef8a300cc587b904d1b57783b7d2751ac47f5")

    depends_on("python@3.6:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@64:")
        depends_on("py-setuptools-scm@8:")
