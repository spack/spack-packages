# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyassimp(PythonPackage):
    """Python bindings for the Open Asset Import Library (ASSIMP)"""

    homepage = "https://github.com/mikedh/pyassimp"
    pypi = "pyassimp/pyassimp-4.1.4.tar.gz"

    license("ISC")

    version("5.2.5", sha256="107d93780e4300d70698c4291c54dd32ff78e8cf0dafd56ac1801cd0260c36f3")
    version("4.1.4", sha256="266bd4be170d46065b8c2ad0f5396dad10938a6bbf9a566c4e4d56456e33aa6a")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("assimp")
