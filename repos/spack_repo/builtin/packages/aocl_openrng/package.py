# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class AoclOpenrng(CMakePackage):
    """AOCL-OpenRNG is AMD's fork of the OpenRNG random number generator
    library. It provides pseudo-random and quasi-random generators and
    statistical distributions through an API compatible with the random
    number generation component of Intel's Vector Statistics Library (VSL).

    The default build is the AOCL-optimized library and links AOCL-LibM on
    x86_64. ``~aocl`` builds Arm's generic OpenRNG instead. This release
    always installs both the shared and static libraries.
    """

    _name = "aocl-openrng"
    homepage = "https://github.com/amd/openrng"
    url = "https://github.com/amd/openrng/archive/6.0.0.tar.gz"
    git = "https://github.com/amd/openrng.git"

    maintainers("amd-toolchain-support")

    license("MIT OR Apache-2.0 WITH LLVM-exception")

    version("6.0.0", sha256="314862e51f13c69b2349e2987c3ba3c7f95cda06ba624c3bba45d6e9ef1bb6f6")

    variant("aocl", default=True, sticky=True, description="Build the AOCL-optimized library")
    variant("ilp64", default=False, description="Use the ILP64 integer interface")
    variant("benchmarks", default=False, description="Build benchmarks")
    variant("examples", default=False, description="Build and install examples")
    variant("docs", default=False, description="Build documentation")

    conflicts("%gcc@:9", msg="AOCL-OpenRNG requires GCC 10 or newer")
    conflicts("%clang@:9", msg="AOCL-OpenRNG requires Clang 10 or newer")
    requires(
        "target=x86_64:",
        "target=aarch64:",
        policy="one_of",
        msg="OpenRNG supports x86_64 and AArch64",
    )
    requires(
        "target=x86_64:",
        when="+aocl",
        msg="The AOCL-optimized build is x86_64-only and links AOCL-LibM",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.26:", type="build")
    depends_on("python@3:", type="build")

    # OpenRNG's CMake looks for au_cpuid from AOCL-Utils; AOCL-LibM 6.0+ is required.
    depends_on("aocl-libm@6:", when="+aocl")
    depends_on("aocl-utils@6:", when="+aocl")

    patch("use-mathjax.patch", when="+docs")
    depends_on("doxygen", when="+docs", type="build")

    @property
    def libs(self):
        """Find the shared libopenrng. The static archive is installed too."""
        return find_libraries("libopenrng", root=self.prefix, shared=True, recursive=True)

    @property
    def build_targets(self):
        targets = ["all"]
        if self.spec.satisfies("+docs"):
            targets.append("html")
        return targets

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            self.define("OPENRNG_INTERFACE", "ilp64" if spec.satisfies("+ilp64") else "lp64"),
            self.define_from_variant("AOCL_OPENRNG_BUILD", "aocl"),
            self.define_from_variant("BUILD_BENCH", "benchmarks"),
            self.define_from_variant("BUILD_EXAMPLES", "examples"),
            self.define_from_variant("BUILD_DOCS", "docs"),
            self.define("BUILD_TESTING", False),
        ]

        if spec.satisfies("+aocl"):
            args.append(self.define("AOCL_ROOT", spec["aocl-libm"].prefix))
            cpuid = find_libraries(
                "libau_cpuid", root=spec["aocl-utils"].prefix, shared=False, recursive=True
            )
            if cpuid:
                args.append(self.define("AOCL_CPUID_STATIC", cpuid[0]))

        return args

    @run_after("install")
    def install_bench(self):
        if self.spec.satisfies("+benchmarks"):
            bench_dir = join_path(self.build_directory, "bench")
            mkdirp(self.prefix.bin.benchmarks)

            for bench_exe in find(bench_dir, "bench_*", recursive=False):
                if is_exe(bench_exe):
                    install(bench_exe, self.prefix.bin.benchmarks)
