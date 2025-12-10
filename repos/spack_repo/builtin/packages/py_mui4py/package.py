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
#     spack install py-mui4py
#
# You can edit this file again by typing:
#
#     spack edit py-mui4py
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMui4py(PythonPackage):
    """Python bindings for the Multiscale Universal Interface (MUI) Library"""
    homepage = "https://mxui.github.io/"
    git      = "https://github.com/MxUI/MUI.git"

    build_directory = "wrappers/Python"

    maintainers("Wendi-L", "SLongshaw")

    license("Apache-2.0", checked_by="blairSmcc03")

    version("2.0", branch="master")


    extends("python")

    depends_on("mui")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pip",      type="build")
    depends_on("py-setuptools", type="build")

    # pybind11 & runtime deps for the bindings
    depends_on("py-pybind11",          type=("build", "run"))
    depends_on("py-numpy@1.22:",       type=("build", "run"))
    depends_on("py-mpi4py@3.0.0",            type=("build", "run"))

    def setup_build_environment(self, env):
        env.append_path("CPLUS_INCLUDE_PATH", self.spec["mui"].prefix.include)