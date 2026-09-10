# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyApebench(PythonPackage, CudaPackage):
    """APEBench is a JAX-based tool to evaluate autoregressive neural emulators for PDEs
    on periodic domains in 1d, 2d, and 3d. It comes with an efficient reference simulator
    based on spectral methods that is used for procedural data generation (no need to download
    large datasets with APEBench). Since this simulator can also be embedded into emulator training
    (e.g., for a "solver-in-the-loop" correction setting), this is the first benchmark suite to
    support differentiable physics."""

    homepage = "https://tum-pbs.github.io/apebench-paper/"
    pypi = "apebench/apebench-0.1.1.tar.gz"

    maintainers("abhishek1297")
    license("MIT", checked_by="abhishek1297")

    version("0.1.1", sha256="c5ddd47799f0799b2c2e72c27d3d81993f6fa218a04b1df93d4c1850e4893bf9")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("python@3.10:3.12", type=("build", "run"))

    with default_args(type="run"):
        for arch in CudaPackage.cuda_arch_values:
            cuda_specs = f"+cuda cuda_arch={arch}"
            with when(cuda_specs):
                depends_on(f"py-jaxlib {cuda_specs}")
                depends_on(f"py-equinox@0.11.3: {cuda_specs}")
                depends_on(f"py-exponax@0.1.0 {cuda_specs}")
                depends_on(f"py-pdequinox@0.1.2 {cuda_specs}")
                depends_on(f"py-trainax@0.0.2 {cuda_specs}")

        depends_on("py-jax@0.4.13:")
        depends_on("py-jaxtyping@0.2.20:")
        depends_on("py-typing-extensions@4.5.0:")
        depends_on("py-tqdm@4.63.2:")
        depends_on("py-matplotlib@3.8.1:")
        depends_on("py-pandas@2.2.0:")
        depends_on("py-seaborn@0.13.0:")
        depends_on("py-optax@0.2.0:")

        with when("~cuda"):
            depends_on("py-equinox@0.11.3:")
            depends_on("py-exponax@0.1.0")
            depends_on("py-pdequinox@0.1.2")
            depends_on("py-trainax@0.0.2")

    def setup_run_environment(self, env):
        if "+cuda" in self.spec:
            cuda_home = self.spec["cuda"].prefix
            # This is an irrelevant lib path and it is purely used by NVIDIA profilers.
            # But, since JAX throws RuntimeError on it, we set this path.
            env.prepend_path("LD_LIBRARY_PATH", f"{cuda_home}/extras/CUPTI/lib64")
