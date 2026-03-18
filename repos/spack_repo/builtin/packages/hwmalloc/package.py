from spack.package import *


class Hwmalloc(CMakePackage, CudaPackage, ROCmPackage):
    """HWMALLOC is a allocator which supports memory registration for e.g. remote memory access"""

    homepage = "https://github.com/ghex-org/hwmalloc"
    url = "https://github.com/ghex-org/hwmalloc/archive/refs/tags/v0.0.0.tar.gz"
    git = "https://github.com/ghex-org/hwmalloc.git"
    maintainers = ["boeschf", "msimberg"]

    version("0.4.0", sha256="1161048e915cf196a86a6241d7354dd56b0e02782000507bab19be5628763ab3")
    version("master", branch="master")

    depends_on("cxx", type="build")

    generator("ninja")

    depends_on("numactl", type=("build", "run"))
    depends_on("boost", type=("build"))
    depends_on("cmake@3.19:", type="build")

    conflicts("+cuda +rocm", msg="CUDA and ROCm support are mutually exclusive")

    variant(
        "numa-throws",
        default=False,
        description="True if numa_tools may throw during initialization",
    )
    variant("numa-local", default=True, description="Use numa_tools for local node allocations")
    variant("logging", default=False, description="print logging info to cerr")

    def cmake_args(self):
        args = [
            self.define_from_variant("HWMALLOC_NUMA_THROWS", "numa-throws"),
            self.define_from_variant("HWMALLOC_NUMA_FOR_LOCAL", "numa-local"),
            self.define_from_variant("HWMALLOC_ENABLE_LOGGING", "logging"),
            self.define("HWMALLOC_WITH_TESTING", self.run_tests),
        ]

        if "+cuda" in self.spec:
            args.append(self.define("HWMALLOC_ENABLE_DEVICE", True))
            args.append(self.define("HWMALLOC_DEVICE_RUNTIME", "cuda"))
        elif "+rocm" in self.spec:
            args.append(self.define("HWMALLOC_ENABLE_DEVICE", True))
            args.append(self.define("HWMALLOC_DEVICE_RUNTIME", "hip"))
        else:
            args.append(self.define("HWMALLOC_ENABLE_DEVICE", False))

        return args
