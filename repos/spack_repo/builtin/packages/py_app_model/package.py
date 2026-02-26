# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAppModel(PythonPackage):
    """app-model is a generic application schema implemented in python, for
    declarative organization of application data, such as menus, keybindings,
    actions/commands, etc..."""

    homepage = "https://github.com/pyapp-kit/app-model"
    pypi = "app_model/app_model-0.5.0.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.4.0", sha256="ccf667999f6c659e921ca3490b6da176971e67cf2f41abc34e33caa8cfa18573")
    version("0.1.4", sha256="67f5cdf16f79e22844f2bdb91fd90e81d05077c5882bc3536f9d74b515a5b1d4")

    variant("qt", default=False, description="Install QT libraries")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-psygnal@0.10:", when="@0.4:")
        depends_on("py-psygnal@0.3.4:")
        depends_on("py-pydantic@2.8:", when="@0.5:")
        depends_on("py-pydantic@1.10.18:", when="@0.4")
        depends_on("py-pydantic@1.8.2:1", when="@0.1.4:0.1")
        depends_on("py-pydantic-compat@0.1.1:", when="@0.4")
        depends_on("py-in-n-out@0.1.5:")
        depends_on("py-typing-extensions@4.12:")

        with when("+qt"):
            depends_on("py-qtpy@2.4.0:")
            depends_on("py-superqt@0.7.2: +iconify")
