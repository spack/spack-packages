# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class PyTilelang(PythonPackage, CudaPackage, ROCmPackage):
    """Domain-specific language designed to streamline
    the development of high-performance GPU/CPU/Accelerators kernels"""

    license("MIT")
    homepage = "https://tilelang.com/"
    git = "https://github.com/tile-ai/tilelang.git"
    submodules = True

    # Exact set of modules is version- and variant-specific, just attempt to import the
    # core libraries to ensure that the package was successfully installed.
    import_modules = ["tilelang", "tilelang.language", "tilelang.intrinsics"]

    version("main", branch="main")
    version("0.1.7", tag="v0.1.7", commit="305c854be59b73eee297e24eb370bd75a8ff4179")
    version("0.1.5", tag="v0.1.5", commit="a32009bf1e314b514c07389123648ba19009f3a5")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type="build"):
        # https://github.com/tile-ai/tilelang/blob/v0.1.7/pyproject.toml
        depends_on("py-scikit-build-core", when="@0.1.7:")
        depends_on("py-cython@3.0.0:", when="@0.1.7:")

        # https://github.com/tile-ai/tilelang/blob/v0.1.5/pyproject.toml
        depends_on("cmake@3.26:")
        depends_on("py-packaging", when="@:0.1.5")
        depends_on("py-setuptools@61:", when="@:0.1.5")
        # depends_on("py-wheel") # inherited if `pip` is the build system

        # https://github.com/tile-ai/tilelang/blob/v0.1.5/requirements-build.txt
        depends_on("py-build", when="@:0.1.5")
        depends_on("py-tox", when="@:0.1.5")
        depends_on("py-auditwheel", when="@:0.1.5")
        depends_on("patchelf", when="@:0.1.5")

    with default_args(type=["build", "run"]):
        # https://github.com/tile-ai/tilelang/pull/1403
        depends_on("py-torch-c-dlpack-ext", when="@0.1.7:")
        # https://github.com/tile-ai/tilelang/blob/v0.1.7/pyproject.toml
        depends_on("py-apache-tvm-ffi@:0.1.1", when="@0.1.7:")
        depends_on("py-tqdm@4.62.3:", when="@0.1.7:")
        # https://github.com/tile-ai/tilelang/blob/v0.1.5/requirements.txt
        depends_on("py-cython")
        depends_on("py-numpy@1.23.5:")
        depends_on("py-tqdm@4.62.3:")
        depends_on("py-typing-extensions@4.10.0:")
        depends_on("py-cloudpickle")
        depends_on("py-ml-dtypes")
        depends_on("py-psutil")
        depends_on("py-torch")

    def cmake_args(self):
        return [
            self.define_from_variant("USE_CUDA", "cuda"),
            self.define_from_variant("USE_ROCM", "rocm"),
        ]

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # OSError: libnvrtc.so.12: cannot open shared object file: No such file or directory
        if self.spec.satisfies("+cuda"):
            env.prepend_path("LD_LIBRARY_PATH", self.spec["cuda"].prefix.lib64)
