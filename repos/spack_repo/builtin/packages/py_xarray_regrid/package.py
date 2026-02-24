# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXarrayRegrid(PythonPackage):
    """Regridding utility for xarray"""

    homepage = "https://github.com/xarray-contrib/xarray-regrid"
    pypi = "xarray_regrid/xarray_regrid-0.4.0.tar.gz"

    maintainers("Chrismarsh")

    license("Apache-2.0", checked_by="Chrismarsh")

    version("0.4.2", sha256="96525d39b0290efa59e0255cebd35be028052f1b347bfb10fd259b4380289673")
    version("0.4.1", sha256="2c8a7baa321c2451aa42b387fef3b22ecd7bdf693e7ee5c52ebe5168482a1e2a")
    version("0.4.0", sha256="f0bef6a346e247c657ed293752b5685f3b559b32de546889ca9e9fca14b81f3a")

    variant("accel", default=True, description="Improve performance in certain cases")

    depends_on("py-hatchling", type="build")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))
    depends_on("py-flox", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    with when("+accel"):
        depends_on("py-sparse", type=("build", "run"))
        depends_on("py-opt-einsum", type=("build", "run"))
        depends_on("py-dask +distributed", type=("build", "run"))
