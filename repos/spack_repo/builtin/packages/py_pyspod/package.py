# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyspod(PythonPackage):
    """Python Spectral Proper Orthogonal Decomposition"""

    homepage = "https://github.com/MathEXLab/PySPOD"
    git = "https://github.com/MathEXLab/PySPOD.git"
    pypi = "pyspod/pyspod-2.0.0.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("2.0.0", sha256="b27b23e35b7fb3a2672d7707951e1756ae7d60aa196aa03aa095225bec9df5a4")

    depends_on("python@3.7:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-setuptools@42:")

    with default_args(type=("build", "run")):
        depends_on("py-importlib-metadata@:4", when="^python@:3.7")
        depends_on("py-psutil")
        depends_on("py-tqdm")
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-h5py")
        depends_on("py-netcdf4")
        depends_on("py-xarray")
        depends_on("py-matplotlib")
        depends_on("py-pyyaml")
