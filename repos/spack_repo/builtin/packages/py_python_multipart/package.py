# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonMultipart(PythonPackage):
    """A streaming multipart parser for Python"""

    homepage = "https://github.com/andrew-d/python-multipart"
    pypi = "python_multipart/python_multipart-0.0.17.tar.gz"

    license("Apache-2.0")

    version("0.0.20", sha256="8dd0cab45b8e23064ae09147625994d090fa46f5b0d1e13af944c331a7fa9d13")
    version("0.0.17", sha256="41330d831cae6e2f22902704ead2826ea038d0419530eadff3ea80175aec5538")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.8:", type=("build", "run"))
