# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVcsVersioning(PythonPackage):
    """The blessed package to manage your versions by vcs metadata."""

    homepage = "https://github.com/pypa/setuptools-scm"
    pypi = "vcs_versioning/vcs_versioning-2.5.0.tar.gz"
    supplier = "PyPA"

    license("MIT")

    version("2.5.0", sha256="956a796e31f80fe714d219d6d1df15a6bf247d10f6d851bf4b98279d0a42da55")

    with default_args(type="build"):
        depends_on("py-setuptools@45:")
        depends_on("py-packaging@26.2:")
        depends_on("py-typing-extensions@4.1:", when="^python@:3.10")

    with default_args(type=("build", "run")):
        depends_on("py-packaging@26.2:")
        depends_on("py-tomli@1:", when="^python@:3.10")
        depends_on("py-typing-extensions@4.1:", when="^python@:3.10")
