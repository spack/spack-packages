# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJinxed(PythonPackage):
    """Jinxed Terminal Library"""

    homepage = "https://github.com/Rockhopper-Technologies/jinxed"
    pypi = "jinxed/jinxed-2.1.0.tar.gz"

    license("MPL-2.0", checked_by="mr-c")

    version("2.1.0", sha256="7e755b831faa2443d44fb4ce7c0202eb9c3ed39bd5bf1193365888f4f6092b54")

    with default_args(type="build"):
        depends_on("py-setuptools")
