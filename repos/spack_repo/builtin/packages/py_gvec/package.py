# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGvec(PythonPackage):
    """GVEC (Galerkin Variational Equilibrium Code) is an open-source software
    for the generation of three-dimensional ideal MHD equilibria."""

    homepage = "https://gvec.readthedocs.io"

    pypi = "gvec/gvec-1.4.1.tar.gz"

    maintainers("tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("1.4.1", sha256="d3ad4f089115f742370e5a86b39d243cdf766b2f258ab471487be3c720a7b7e9")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    # Dependencies from CMakeLists.txt
    depends_on("pkgconfig", type="build")
    depends_on("cmake@3.22:4", type="build")
    depends_on("lapack")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")

    # Build dependencies from pyproject.toml
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-scikit-build-core@0.11:", type="build")

    # Dependencies from pyproject.toml
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-f90nml", type=("build", "run"))
    depends_on("py-f90wrap@0.3:1", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy@2:", type=("build", "run"))
    depends_on("py-pyevtk", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-tomlkit", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))
