# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEcmwfOpendata(PythonPackage):
    """A package to download ECMWF open data."""

    homepage = "https://github.com/ecmwf/ecmwf-opendata"
    pypi = "ecmwf-opendata/ecmwf-opendata-0.3.3.tar.gz"

    license("Apache-2.0")

    version("0.3.8", sha256="8a9c29ba369088477f9db2a2dabdb8f5282f02f6756e83d4288b38ed4d663c29")
    version("0.3.3", sha256="6f3181c7872b72e5529d2b4b7ec6ff08d37c37beee0a498f7f286410be178c6a")

    depends_on("py-setuptools", type="build")
    depends_on("py-multiurl@0.2.1:", type=("build", "run"))
