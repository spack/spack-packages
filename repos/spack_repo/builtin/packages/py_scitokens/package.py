# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScitokens(PythonPackage):
    """SciToken reference implementation library."""

    homepage = "https://scitokens.org"
    pypi = "scitokens/scitokens-1.9.7.tar.gz"
    git = "https://github.com/scitokens/scitokens.git"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("1.9.7", sha256="9aabefbd68859e94a3909f3dc08bd73c0e7a9c08203c16de338c9512ace821e3")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-cryptography")
        depends_on("py-pyjwt@1.6.1:")
        depends_on("py-requests")
