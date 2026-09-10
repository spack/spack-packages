# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRassumfrassum(PythonPackage):
    """Connect an LSP client to multiple LSP servers."""

    homepage = "https://github.com/joaotavora/rassumfrassum"
    pypi = "rassumfrassum/rassumfrassum-0.3.3.tar.gz"

    maintainers("alecbcs")

    license("GPL-3.0-only", checked_by="alecbcs")

    version("0.3.3", sha256="1acd9083069f8fd9b5b5d55cc359385174dbc606d2e5ac1308834191be472217")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@61:")
