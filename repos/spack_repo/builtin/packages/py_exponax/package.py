# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyExponax(PythonPackage, CudaPackage):
    """Efficient Differentiable n-d PDE solvers built on top of JAX & Equinox."""

    homepage = "https://fkoehler.site/exponax/"
    pypi = "exponax/exponax-0.1.0.tar.gz"

    maintainers("abhishek1297")
    license("MIT", checked_by="abhishek1297")

    version("0.1.0", sha256="25acdb5c1b76f5706316750a3133f427f0faec441a1ffe3b90697d5f32abb5e7")
    version("0.0.1", sha256="e2a201752d38dbfd233d52c2f59ed0dc344ccbb3e796b26c2713c6a2357d7366")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.10:3.12", type=("build", "run"))

    with default_args(type="run"):
        for arch in CudaPackage.cuda_arch_values:
            cuda_specs = f"+cuda cuda_arch={arch}"
            depends_on(f"py-jaxlib@0.4.13: {cuda_specs}", when=f"{cuda_specs}")

        depends_on("py-jax@0.4.13:")
        depends_on("py-jaxtyping@0.2.20:")
        depends_on("py-typing-extensions@4.5.0:")
        depends_on("py-matplotlib@3.8.1:")
        depends_on("py-equinox@0.11.3:")
