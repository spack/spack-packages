# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Alpaka(CMakePackage, CudaPackage):
    """Abstraction Library for Parallel Kernel Acceleration."""

    homepage = "https://github.com/alpaka-group/alpaka"
    url = "https://github.com/alpaka-group/alpaka/archive/refs/tags/0.9.0.tar.gz"
    git = "https://github.com/alpaka-group/alpaka.git"

    maintainers("vvolkl")

    license("MPL-2.0-no-copyleft-exception")

    version("develop", branch="develop")
    version("2.1.1", sha256="2d30a43594c55067297947b0ec83300e4f2899497464c5cc6f142c823f3ea1b2")
    # 2.1.0 is deprecated due to the buffer/view arrow operator bug
    # see https://github.com/alpaka-group/alpaka/pull/2600
    version(
        "2.1.0",
        sha256="e5de511561d7630e856e58b6e191e054f627938d4be70cfefdc47c388449d77f",
        deprecated=True,
    )
    version("1.3.0", sha256="8caec8de11a5537c721d2112c97252f06ffee709392ea02fcf62df4b50511714")
    version("2.0.0", sha256="ed313117aa922ef7260ec37bc5f79d750ae5547f0b9e0380a016590aa3a98e8b")
    version("1.2.0", sha256="069ea68ac950b17cffb3a3e790973aa5115f07ab23c0247a167e815b3c6e6fa2")
    version("1.1.0", sha256="95a8f1b706105d8a213116b6ba00e27bd904855c377f5a22a04aa0b86054dc35")
    version("1.0.0", sha256="38223dc1ca5bcf3916ff91f8825fb8caab7047430877222847e0ceb93bffecc9")
    version("0.9.0", sha256="3b2a5631366619fab5f3ceaf860219362f35db6c1148a601a3779a836cf29363")

    variant(
        "backend",
        multi=True,
        values=(
            "serial",
            "threads",
            "tbb",
            "omp2_gridblock",
            "omp2_blockthread",
            "cuda",
            "cuda_only",
            "hip",
            "hip_only",
        ),
        description="Backends to enable",
        default="serial",
    )

    variant("examples", default=False, description="Build alpaka examples")

    depends_on("cxx", type="build")  # generated

    variant(
        "boost_atomic_ref",
        default=False,
        when="@2:",
        description="To use atomic ref from boost, if C++20 std::atomic_ref is not available",
    )
    depends_on("boost@1.74:")
    depends_on("boost@1.78:+atomic", when="@2: +boost_atomic_ref")

    depends_on("cmake@3.18:")
    depends_on("cmake@3.22:", when="@1:")
    depends_on("cmake@3.25:", when="@2:")

    # make sure no other backend is enabled if using cuda_only or hip_only
    for v in ("serial", "threads", "tbb", "omp2_gridblock", "omp2_blockthread", "cuda", "hip"):
        conflicts("backend=cuda_only,%s" % v)
        conflicts("backend=hip_only,%s" % v)
    conflicts("backend=cuda_only,hip_only")

    # todo: add conflict between cuda 11.3 and gcc 10.3.0
    # see https://github.com/alpaka-group/alpaka/issues/1297

    def cmake_args(self):
        spec = self.spec
        args = []
        if spec.satisfies("backend=serial"):
            args.append(self.define("ALPAKA_ACC_CPU_B_SEQ_T_SEQ_ENABLE", True))
        if self.spec.satisfies("backend=threads"):
            args.append(self.define("ALPAKA_ACC_CPU_B_SEQ_T_THREADS_ENABLE", True))
        if spec.satisfies("backend=tbb"):
            args.append(self.define("ALPAKA_ACC_CPU_B_TBB_T_SEQ_ENABLE", True))
        if spec.satisfies("backend=omp2_gridblock"):
            args.append(self.define("ALPAKA_ACC_CPU_B_OMP2_T_SEQ_ENABLE", True))
        if spec.satisfies("backend=omp2_blockthread"):
            args.append(self.define("ALPAKA_ACC_CPU_B_SEQ_T_OMP2_ENABLE", True))
        if spec.satisfies("backend=cuda"):
            args.append(self.define("ALPAKA_ACC_GPU_CUDA_ENABLE", True))
        if spec.satisfies("backend=cuda_only"):
            args.append(self.define("ALPAKA_ACC_GPU_CUDA_ENABLE", True))
            args.append(self.define("ALPAKA_ACC_GPU_CUDA_ONLY_MODE", True))
        if spec.satisfies("backend=hip"):
            args.append(self.define("ALPAKA_ACC_GPU_HIP_ENABLE", True))
        if spec.satisfies("backend=hip_only"):
            args.append(self.define("ALPAKA_ACC_GPU_HIP_ENABLE", True))
            args.append(self.define("ALPAKA_ACC_GPU_HIP_ONLY_MODE", True))

        args.append(self.define_from_variant("alpaka_BUILD_EXAMPLES", "examples"))
        # need to define, as it is explicitly declared as an option by alpaka:
        args.append(self.define("BUILD_TESTING", self.run_tests))
        return args
