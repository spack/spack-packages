# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-app-model
#
# You can edit this file again by typing:
#
#     spack edit py-app-model
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

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

    # version("0.5.0", sha256="fa329cf7b730572cce3daeac6678bbeaf1cf0a7dd485bf2c666b5508d54c8d0f")
    version("0.4.0", sha256="ccf667999f6c659e921ca3490b6da176971e67cf2f41abc34e33caa8cfa18573")

    variant("qt", default=False, description="Install QT libraries")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    depends_on("py-psygnal@0.10:", type=("build", "run"))
    depends_on("py-pydantic@2.8:", when="@0.5:", type=("build", "run"))
    depends_on("py-pydantic@1.10.18:", when="@0.4", type=("build", "run"))
    depends_on("py-pydantic-compat@0.1.1:", when="@0.4", type=("build", "run"))
    depends_on("py-in-n-out@0.1.5:", type=("build", "run"))
    depends_on("py-typing-extensions@4.12:", type=("build", "run"))

    with default_args(when="+qt", type=("build", "run")):
        depends_on("py-pyqt@2.4.0:")
        depends_on("py-superqt@0.7.2: +iconify")
