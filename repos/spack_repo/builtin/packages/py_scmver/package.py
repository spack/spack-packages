# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScmver(PythonPackage):
    """A package version manager based on SCM tags."""

    homepage = "https://github.com/hattya/scmver"
    pypi = "scmver/scmver-1.9.tar.gz"

    supplier = "Person: Akinori Hattori"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("1.9", sha256="eeedfb7dabe9e326fb8a07ff59dea10da0fa0f523f36f32f475a49aee2c1d5f0")

    with default_args(type="build"):
        depends_on("py-setuptools@77:")
