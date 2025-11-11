# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonExtension

from spack.package import *


class TsneCuda(CMakePackage, CudaPackage, PythonExtension):
    """tsne-cuda is an optimized CUDA version of FIt-SNE algorithm with
    associated python modules. Authors find that their implementation of t-SNE
    can be up to 1200x faster than Sklearn, or up to 50x faster than
    Multicore-TSNE when used with the right GPU."""

    homepage = "https://github.com/CannyLab/tsne-cuda/"
    url = "https://github.com/CannyLab/tsne-cuda/archive/refs/tags/3.0.1.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("3.0.1", sha256="0f778247191f483df22dc4dbed792c9a6a9152ee7404329c4d9da3fd9a8774d6")
    version("3.0.0", sha256="6f5a0c5c0c54a4a74837e0e84fa37396ca6912a2031bdf6e846d5c01254e3e2c")

    patch("fix_cmakelists.patch")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.20:3.30", type="build")  # CMake 3.31 messes a bit too much with find CUDA

    depends_on("cuda@9:")
    depends_on("blas")
    depends_on("lapack")
    depends_on("gflags@2.2:")
    depends_on("googletest@1.10:", type=("build", "link", "run"))
    depends_on("faiss@1.6.5: +cuda +shared", type=("build", "link", "run"))
    depends_on("cxxopts")

    variant("cuda", default=True, description="Use CUDA acceleration")
    conflicts("~cuda", msg="CUDA is a hard requirement")
    conflicts(
        "cuda_arch=none",
        when="+cuda",
        msg="Must specify CUDA compute capabilities of your GPU, see "
        "https://developer.nvidia.com/cuda-gpus",
    )

    variant("python", default=False, description="Install Python bindings.")

    extends("python", when="+python")
    depends_on("python@3.6:", when="+python")
    depends_on("py-numpy@1.14.1:", when="+python")

    def cmake_args(self):
        cuda_arch = self.spec.variants["cuda_arch"].value
        cuda_gencode = " ".join(self.cuda_flags(cuda_arch))

        args = []
        args.append(self.define("FAISS_GPU_INCLUDE_DIR", self.spec["faiss"].libs))
        args.append(self.define_from_variant("BUILD_PYTHON", "python"))
        args.append(self.define("CUDA_ARCH", cuda_gencode))
        return args
