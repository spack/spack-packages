# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPythonMumps(PythonPackage):
    """Python wrapper for the MUMPS solver (python_mumps)."""

    homepage = "https://gitlab.kwant-project.org/kwant/python-mumps"
    pypi = "python-mumps/python_mumps-0.0.6.tar.gz"

    maintainers("williampiat3", "akhmerov")

    license("BSD-2-Clause")

    version("0.0.6", sha256="58c33104f77c448e127e9e6da316f71dfb1a17719ecf022634669d513306b1fa")

    variant("mpi", default=True, description="Whether to have MPI support on python-mumps or not")

    # build dependencies
    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("meson@1.8:")
        depends_on("ninja")
        depends_on("py-meson-python@0.18:")
        depends_on("py-setuptools")
        depends_on("py-setuptools-scm")
        depends_on("py-cython@3.1.1:")
        depends_on("pkgconfig")

    # Python dependencies
    with default_args(type=("build", "run")):
        depends_on("python@3.10:")
        depends_on("py-numpy@2:")
        depends_on("py-mpi4py@4.1:4", when="+mpi")
        depends_on("py-scipy@1.13:")

    # Optional/test deps
    depends_on("py-pytest", type="test")

    # External solver
    depends_on("mumps+float+complex+double+metis+scotch+pkgconfig")
    depends_on("mumps+mpi", when="+mpi")
    depends_on("mumps~mpi", when="~mpi")

    patch("patch_meson_build.patch")
