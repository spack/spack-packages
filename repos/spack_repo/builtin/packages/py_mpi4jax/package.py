# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMpi4jax(PythonPackage, CudaPackage):
    """Zero-copy MPI communication of JAX arrays, for turbo-charged HPC applications in
    Python."""

    homepage = "https://github.com/mpi4jax/mpi4jax"
    pypi = "mpi4jax/mpi4jax-0.3.11.post3.tar.gz"

    maintainers("bhaveshshrimali")

    license("MIT")

    version("0.9.1", sha256="dc72ba69cc70250ef097f1ba62b2bfeabc2b328943f3b4e2fc27238915bebe34")
    version(
        "0.3.11.post3",
        sha256="ad4c5840c81ead40b68f4885d705c06eeca22cd4e998790de589c6566db75a75",
        deprecated=True,
    )

    with default_args(type=("build", "link", "run")):
        depends_on("python@3.10:", when="@0.9.1")
        depends_on("python")

    with default_args(type="build"):
        depends_on("py-setuptools@82.0.1:", when="@0.9.1")
        depends_on("py-setuptools@42:")
        depends_on("py-cython@0.21:")

    with default_args(type=("build", "run")):
        depends_on("py-nanobind@2:", when="@0.9.1")
        depends_on("py-mpi4py@3.0.1:")
        depends_on("py-numpy")
        depends_on("py-jax@0.6:", when="@0.9.1")
        depends_on("py-jax@0.3.25:")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if "+cuda" in self.spec:
            env.set("CUDA_PATH", self.spec["cuda"].prefix)
