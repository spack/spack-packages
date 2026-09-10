# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBackportsTarfile(PythonPackage):
    """Backport of CPython tarfile module."""

    homepage = "https://github.com/jaraco/backports.tarfile"
    pypi = "backports_tarfile/backports_tarfile-1.2.0.tar.gz"

    license("MIT")

    version("1.2.0", sha256="d75e02c268746e1b8144c278978b6e98e85de6ad16f8e4b0844a154557eca991")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@61.2:", type="build")
    depends_on("py-setuptools-scm+toml@3.4.1:", type="build")
