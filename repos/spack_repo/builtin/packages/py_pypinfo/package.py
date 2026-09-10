# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPypinfo(PythonPackage):
    """View PyPI download statistics with ease."""

    homepage = "https://github.com/ofek/pypinfo"
    pypi = "pypinfo/pypinfo-22.0.0.tar.gz"

    license("MIT")

    version("22.0.0", sha256="4bc900c96b8827d22a674eee6a34c549939452a4174ee17fd3eafcaff594c408")

    depends_on("py-hatchling", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-binary")
        depends_on("py-click")
        depends_on("py-google-cloud-bigquery@2.11:")
        depends_on("py-packaging@16.2:")
        depends_on("py-platformdirs")
        depends_on("py-tinydb@4:")
        depends_on("py-tinyrecord@0.2:")
