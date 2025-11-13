# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPdequinox(PythonPackage, CudaPackage):
    """A collection of neural architectures for emulating Partial Differential Equations (PDEs)
    in JAX agnostic to the spatial dimension (1D, 2D, 3D) and boundary conditions
    (Dirichlet, Neumann, Periodic). This package is built on top of Equinox."""

    homepage = "https://fkoehler.site/pdequinox/"
    pypi = "pdequinox/pdequinox-0.1.2.tar.gz"

    maintainers("abhishek1297")
    license("MIT", checked_by="abhishek1297")

    version("0.1.2", sha256="7ee9dcbf277cbb94cda508034c0955600a03bc4c664bede5eb61b4a4b99b54c5")
    version("0.1.0", sha256="07f7516fe26823e6c3b71f1ed5a170e97cc34ff1d1349435d4b7469adc540d3a")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.8:3.12", type=("build", "run"))

    with default_args(type="run"):
        for arch in CudaPackage.cuda_arch_values:
            cuda_specs = f"+cuda cuda_arch={arch}"
            depends_on(f"py-jaxlib@0.4.13: {cuda_specs}", when=f"{cuda_specs}")

        depends_on("py-jax@0.4.13:")
        depends_on("py-jaxtyping@0.2.20:")
        depends_on("py-typing-extensions@4.5.0:")
        depends_on("py-equinox@0.11.3:")
