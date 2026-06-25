# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDeisaDask(PythonPackage):
    """Deisa: Dask-Enabled In Situ Analytics."""

    homepage = "https://github.com/deisa-project/deisa-dask"
    pypi = "deisa_dask/deisa_dask-0.3.0.tar.gz"

    maintainers("thomas-bouvier", "benoitmartin88")

    license("MIT")

    version("0.5.1", sha256="bcab744b7eb6479eac69c065ebedcc330f3ddf00d2440858e8716ffeb1898fd9")
    version("0.5.0", sha256="8b359207f4924da94b8203db9d6247af57e575ab2e18b49b6890989770040e79")
    version("0.4.1", sha256="acfcb41e4384a6a90ca91bce47f29b0e147e660f2dfddb82240cf9d464a9cdfc")
    version("0.3.0", sha256="615483d3c21e05c1cdf0564db0245f7f6ba979e75c25a0292d3d42fcc4cf6d23")

    variant("mpi", default=True, description="Compile with MPI support.", when="@0.5.1:")

    depends_on("py-setuptools@61:", type="build", when="@0.5.1:")
    depends_on("py-setuptools", type="build")
    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-deisa-core@0.5.0:", when="@0.4.0:", type=("build", "run"))
    depends_on("py-deisa-core@0.1.0", when="@0.3.0", type=("build", "run"))
    depends_on("py-dask@2024.9.0:", when="@0.5:", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-distributed", type=("build", "run"))
    depends_on("py-toolz", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"), when="@0.5.1:")

    depends_on("py-mpi4py", type=("build", "run"), when="+mpi")
