# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMui4py(PythonPackage):
    """Python bindings for the Multiscale Universal Interface (MUI) Library"""

    homepage = "https://mxui.github.io/"
    git = "https://github.com/MxUI/MUI.git"

    build_directory = "wrappers/Python"

    maintainers("Wendi-L", "SLongshaw")

    license("Apache-2.0", checked_by="blairSmcc03")

    version("2.0", branch="master")

    extends("python")

    depends_on("mui")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("py-pybind11", type=("build", "run"))
    depends_on("py-numpy@1.22:", type=("build", "run"))
    depends_on("py-mpi4py@3.0.0", type=("build", "run"))

    def setup_build_environment(self, env):
        env.append_path("CPLUS_INCLUDE_PATH", self.spec["mui"].prefix.include)
