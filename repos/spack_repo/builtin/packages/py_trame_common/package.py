# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTrameCommon(PythonPackage):
    """Dependency less classes and functions for trame."""

    homepage = "https://github.com/Kitware/trame-common"
    pypi = "trame_common/trame_common-1.1.0.tar.gz"

    maintainers("LydDeb")

    license("Apache-2.0", checked_by="LydDeb")

    version("1.1.1", sha256="6254970b75700510c58265e90fd38ba852b99c0e71293d24eed54819902bb01c")
    version("1.1.0", sha256="86280a72453571d91843f6a0cd8d0dbf283ddade6230915ccd244835d6bfa245")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
