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
    version("2.3.0", sha256="1d0d71cfa3c2bc4f8dfb3d4a15c144eb8aa6a09d9da98923d410994a2ef826ea")

    depends_on("python@3.8:", type=("build", "run"), when="@3.1.2:")
    depends_on("python@3.7:", type=("build", "run"))

    depends_on("py-hatchling", type="build", when="@3:")
    depends_on("py-importlib-metadata@3.6:", type=("build", "run"), when="^python@:3.9")
    depends_on("py-packaging@17.1:", type=("build", "run"))
    depends_on("py-tomli@1.2:2", type=("build", "run"), when="^python@:3.10")

    # Historical dependencies
    depends_on("py-setuptools@46.4:", type="build", when="@:2")
