# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTrainax(PythonPackage, CudaPackage):
    """Convenience abstractions using optax to train neural networks to autoregressively
    emulate time-dependent problems taking care of trajectory subsampling and offering a wide
    range of training methodologies (regarding unrolling length and including
    differentiable physics).
    """

    homepage = "https://fkoehler.site/trainax/"
    pypi = "trainax/trainax-0.0.2.tar.gz"

    maintainers("abhishek1297")
    license("MIT", checked_by="abhishek1297")

    version("0.0.2", sha256="3c7eeeb94e351db7ff0b036b1c1fb6f78ddc25ab72d6c1afe69547cbefa70ca8")
    version("0.0.1", sha256="19552dfca2d6f9d7e69963e978628adb19dc2ba9cb9563b510c19e136116c23a")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.8:3.12", type=("build", "run"))

    with default_args(type="run"):
        for arch in CudaPackage.cuda_arch_values:
            cuda_specs = f"+cuda cuda_arch={arch}"
            depends_on(f"py-jaxlib@0.4.13: {cuda_specs}", when=f"{cuda_specs}")

        depends_on("py-jax@0.4.13:")
        depends_on("py-jaxtyping@0.2.20:")
        depends_on("py-typing-extensions@4.5.0:")
        depends_on("py-tqdm@4.63.2:")
        depends_on("py-optax@0.2.0:")
        depends_on("py-equinox@0.11.3:")
