# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGvec(PythonPackage):
    """GVEC (Galerkin Variational Equilibrium Code) is an open-source software for the generation
    of three-dimensional ideal MHD equilibria. It provides the 'pygvec' executable and 'gvec'
    python package."""

    homepage = "https://gvec.readthedocs.io"
    pypi = "gvec/gvec-1.4.1.tar.gz"

    maintainers("tpadioleau", "Rykath")

    license("MIT", checked_by="tpadioleau")

    version("1.5.1", sha256="16fb9401387aed1b4c2ed7e13686ef33ee794072b8f3c0b0836c0db47ab5c36c")
    version("1.4.1", sha256="d3ad4f089115f742370e5a86b39d243cdf766b2f258ab471487be3c720a7b7e9")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("fortran")

        # Dependencies from CMakeLists.txt
        depends_on("pkgconfig")
        depends_on("cmake@3.22:4")

        # Build-only dependencies from pyproject.toml
        depends_on("py-setuptools-scm")
        depends_on("py-scikit-build-core@0.11:")

    with default_args(type=("build", "run")):
        # Dependencies from CMakeLists.txt
        depends_on("lapack")
        depends_on("netcdf-c")
        depends_on("netcdf-fortran")

        # Dependencies from pyproject.toml
        depends_on("python@3.10:")
        depends_on("py-f90nml")
        depends_on("py-f90wrap@0.3:1")
        depends_on("py-matplotlib")
        depends_on("py-numpy@2:")
        depends_on("py-pyevtk")
        depends_on("py-pyyaml")
        depends_on("py-requests")
        depends_on("py-scipy")
        depends_on("py-tabulate", when="@1.5.0:")
        depends_on("py-tomlkit")
        depends_on("py-tqdm")
        depends_on("py-xarray")

    def config_settings(self, spec, prefix):
        settings = {}
        if spec.satisfies("@1.5.1:"):
            # let spack handle architecture-specific flags
            settings["cmake.define.GVEC_ADD_COMPILE_FLAGS_MACHINE"] = ""
        return settings
