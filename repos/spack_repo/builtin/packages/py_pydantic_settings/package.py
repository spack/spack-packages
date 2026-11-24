# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPydanticSettings(PythonPackage):
    """Settings management using Pydantic."""

    homepage = "https://github.com/pydantic/pydantic-settings"
    pypi = "pydantic_settings/pydantic_settings-2.6.1.tar.gz"

    license("MIT", checked_by="wdconinc")

    version("2.14.0", sha256="24285fd4b0e0c06507dd9fdfd331ee23794305352aaec8fc4eb92d4047aeb67d")
    version("2.6.1", sha256="e0f92546d8a9923cb8941689abf85d6601a8c19a23e97a34b2964a2e3f813ca0")

    depends_on("py-hatchling", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@2.14:")
        depends_on("py-typing-inspection@0.4:")
        depends_on("python@3.8:")
        depends_on("py-pydantic@2.7.0:")
        depends_on("py-python-dotenv@0.21:")
