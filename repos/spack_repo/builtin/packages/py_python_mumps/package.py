# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT

import os

from spack_repo.builtin.build_systems.meson import MesonBuilder
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonMumps(PythonPackage):
    """Python wrapper for the MUMPS solver (python_mumps)."""

    homepage = "https://gitlab.kwant-project.org/kwant/python-mumps"
    url = "https://pypi.org/packages/source/p/python-mumps/python_mumps-0.0.6.tar.gz"

    maintainers = ["williampiat3"]

    version("0.0.6", sha256="58c33104f77c448e127e9e6da316f71dfb1a17719ecf022634669d513306b1fa")

    variant("mpi", default=True, description="Whether to have MPI support on python-mumps or not")

    # build dependencies
    with default_args(type="build"):
        depends_on("meson")
        depends_on("ninja")
        depends_on("py-meson-python")
        depends_on("py-setuptools")
        depends_on("py-setuptools-scm")
        depends_on("py-cython")

    # Python dependencies
    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        depends_on("py-mpi4py", when="+mpi")
        depends_on("py-scipy")

    # Optional/test deps
    depends_on("py-pytest", type="test")

    # External solver
    depends_on("mumps+float+complex+double+metis+scotch+pkgconfig", when="+mpi")
    depends_on("mumps~mpi+float+complex+double+metis+scotch+pkgconfig", when="~mpi")

    patch("patch_meson_build.patch")

    @run_before("install")
    def setup_meson(self) -> None:
        """Running meson setup before building the package"""
        # Building with meson
        options = []
        if self.spec["meson"].satisfies("@0.64:"):
            options.append("setup")
        options.append(os.path.abspath(self.stage.source_path))
        options += MesonBuilder.std_args(self)
        builddir = "builddir"
        options.append(builddir + "/")
        with working_dir(join_path(self.build_directory, builddir), create=True):
            self.module.meson(*options)
