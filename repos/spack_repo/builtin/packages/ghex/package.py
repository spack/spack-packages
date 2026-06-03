# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Ghex(CMakePackage, CudaPackage, ROCmPackage):
    """Generic exascale-ready library for halo-exchange operations on variety of
    grids/meshes"""

    homepage = "https://ghex-org.github.io/GHEX"
    url = "https://github.com/ghex-org/GHEX/archive/refs/tags/v0.0.0.tar.gz"
    git = "https://github.com/ghex-org/GHEX.git"

    maintainers("boeschf", "msimberg")

    license("BSD-3-Clause", checked_by="msimberg")

    version("master", branch="master")
    version("0.6.0", sha256="7a9ebeef0f7dcbb2fa44c529f52d2be6cc2bf8a1720d232343b3f5fd071a1e92")
    version("0.5.0", sha256="b2324441c2210783a90e83439e0d5c8e0aa462a7797ebbc6e48a47dfcada4848")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    generator("ninja")

    depends_on("ninja", type="build")

    backends = ("mpi", "ucx", "libfabric")
    variant(
        "backend", default="mpi", description="Transport backend", values=backends, multi=False
    )
    variant("xpmem", default=False, description="Use xpmem shared memory")
    variant("python", default=True, description="Build Python bindings")

    depends_on("cmake@3.21:", type="build")
    depends_on("googletest", type="test")
    depends_on("mpi")
    depends_on("boost")
    depends_on("xpmem", when="+xpmem", type=("build", "run"))

    depends_on("gridtools")
    depends_on("oomph")
    for backend in backends:
        depends_on(f"oomph backend={backend}", when=f"backend={backend}")
    depends_on("oomph+cuda", when="+cuda")
    depends_on("oomph+rocm", when="+rocm")
    depends_on("oomph~rocm~cuda", when="~rocm~cuda")

    conflicts("+cuda +rocm", msg="CUDA and ROCm support are mutually exclusive")
    conflicts(
        "cuda_arch=none", when="+cuda", msg="CUDA support requires at least one architecture"
    )
    conflicts(
        "amdgpu_target=none", when="+rocm", msg="ROCm support requires at least one architecture"
    )

    with when("+python"):
        extends("python")
        depends_on("python@3.7:", type=("build", "run"))
        depends_on("py-pip", type="build")
        depends_on("py-pybind11", type="build", when="@:0.5")
        depends_on("py-nanobind", type="build", when="@0.6:")
        depends_on("py-mpi4py", type=("build", "run"))
        depends_on("py-numpy", type=("build", "run"))

        depends_on("py-pytest", when="+python", type="test")

    def cmake_args(self):
        spec = self.spec

        args = [
            self.define("GHEX_USE_BUNDLED_LIBS", False),
            self.define("GHEX_TRANSPORT_BACKEND", spec.variants["backend"].value.upper()),
            self.define_from_variant("GHEX_USE_XPMEM", "xpmem"),
            self.define_from_variant("GHEX_BUILD_PYTHON_BINDINGS", "python"),
            self.define("GHEX_WITH_TESTING", self.run_tests),
        ]

        if spec.satisfies("+python"):
            args.append(self.define("GHEX_PYTHON_LIB_PATH", python_platlib))

        if self.run_tests and spec.satisfies("^mpi=openmpi"):
            args.append(self.define("MPIEXEC_PREFLAGS", "--oversubscribe"))

        if spec.satisfies("+cuda"):
            arch_str = ";".join(spec.variants["cuda_arch"].value)
            args.append(self.define("CMAKE_CUDA_ARCHITECTURES", arch_str))
            args.append(self.define("GHEX_USE_GPU", True))
            args.append(self.define("GHEX_GPU_TYPE", "NVIDIA"))
        elif spec.satisfies("+rocm"):
            arch_str = ";".join(spec.variants["amdgpu_target"].value)
            args.append(self.define("CMAKE_HIP_ARCHITECTURES", arch_str))
            args.append(self.define("GHEX_USE_GPU", True))
            args.append(self.define("GHEX_GPU_TYPE", "AMD"))
        else:
            args.append(self.define("GHEX_USE_GPU", False))

        return args
