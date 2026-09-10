# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCrc32c(PythonPackage):
    """A python package implementing the crc32c algorithm in hardware and software."""

    homepage = "https://github.com/ICRAR/crc32c"
    pypi = "crc32c/crc32c-2.7.1.tar.gz"

    license("LGPL-2.1-or-later")

    version("2.7.1", sha256="f91b144a21eef834d64178e01982bb9179c354b3e9e5f4c803b0e5096384968c")

    depends_on("python@3.7:", type=("build", "link", "run"))

    with default_args(type="build"):
        depends_on("c")
        depends_on("py-setuptools")
