# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMui4py(PythonPackage):
    """Python bindings for the Multiscale Universal Interface (MUI) Library"""

    homepage = "https://mxui.github.io/"
    git = "https://github.com/MxUI/MUI.git"
    url = "https://github.com/MxUI/MUI/archive/refs/tags/2.0.tar.gz"

    build_directory = "wrappers/Python"

    maintainers("blairSmcc03")

    license("GPL-3.0 OR Apache-2.0", checked_by="blairSmcc03")

    version("2.0", sha256="fdddd4ffe72c22356eb53707567622a9bfb8d17836a9677a980f035e87e1b295")
    version("master", branch="master")

    depends_on("mui@2", when="@2")
    depends_on("mui@master", when="@master")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-pybind11", type=("build"))
    depends_on("py-numpy@1.21:", type=("build", "run"))
    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("cmake@3.27:", type=("build"))

    def setup_build_environment(self, env):
        env.append_path("CPLUS_INCLUDE_PATH", self.spec["mui"].prefix.include)
