# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDpath(PythonPackage):
    """Filesystem-like pathing and searching for dictionaries."""

    homepage = "https://github.com/dpath-maintainers/dpath-python"
    pypi = "dpath/dpath-2.1.6.tar.gz"

    license("MIT")

    version("2.2.0", sha256="34f7e630dc55ea3f219e555726f5da4b4b25f2200319c8e6902c394258dd6a3e")
    version("2.1.6", sha256="f1e07c72e8605c6a9e80b64bc8f42714de08a789c7de417e49c3f87a19692e47")
    version("2.0.1", sha256="bea06b5f4ff620a28dfc9848cf4d6b2bfeed34238edeb8ebe815c433b54eb1fa")

    depends_on("py-setuptools", type="build")
