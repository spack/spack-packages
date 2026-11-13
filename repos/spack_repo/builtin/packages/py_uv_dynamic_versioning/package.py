# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUvDynamicVersioning(PythonPackage):
    """Dynamic versioning based on VCS tags for uv/hatch project."""

    homepage = "https://github.com/ninoseki/uv-dynamic-versioning/"
    pypi = "uv_dynamic_versioning/uv_dynamic_versioning-0.14.0.tar.gz"

    license("MIT")

    version("0.14.1", sha256="8642db686ce5c50417035e7a257ac73b7e5c3a7a32c33e45bd7e36ba22eeb648")
    version("0.14.0", sha256="574fbc07e87ace45c01d55967ad3b864871257b98ff5b8ac87c261227ac8db5b")

    depends_on("py-hatchling", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:3")
        depends_on("py-dunamai@1.26:1", when="@0.14.0")
        depends_on("py-dunamai@1.26.1:1.26", when="@0.14.1:")
        depends_on("py-hatchling@1.26:1")
        depends_on("py-hatchling@1.28:1", when="@0.14.1:")
        depends_on("py-jinja2@3")
        depends_on("py-tomlkit@0.13:0")
