# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVersioningit(PythonPackage):
    """Versioning It with your Version In Git."""

    homepage = "https://github.com/jwodder/versioningit"
    pypi = "versioningit/versioningit-3.3.0.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("3.3.0", sha256="b91ad7d73e73d21220e69540f20213f2b729a1f9b35c04e9e137eaf28d2214da")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-importlib-metadata@3.6:", type=("build", "run"), when="^python@:3.9")
    depends_on("py-packaging@17.1:", type=("build", "run"))
    depends_on("py-tomli@1.2:2", type=("build", "run"), when="^python@:3.10")
