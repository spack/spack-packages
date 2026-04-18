# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySnakeviz(PythonPackage):
    """A web-based viewer for Python profiler output."""

    homepage = "https://jiffyclub.github.io/snakeviz/"
    pypi = "snakeviz/snakeviz-2.2.2.tar.gz"

    license("BSD-3-Clause")

    version("2.2.2", sha256="08028c6f8e34a032ff14757a38424770abb8662fb2818985aeea0d9bc13a7d83")

    depends_on("py-setuptools@43:", type="build")
    depends_on("py-tornado@2:", type=("build", "run"))
