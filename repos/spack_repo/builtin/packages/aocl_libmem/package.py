# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class AoclLibmem(CMakePackage):
    """
    AOCL-LibMem is a Linux library of data movement and manipulation
    functions (such as memcpy and strcpy) highly optimized for AMD Zen
    micro-architecture.

    This library has multiple implementations of each function that can be
    chosen based on the application requirements as per alignments, instruction
    choice, threshold values, and tunable parameters.

    By default, this library will choose the best fit implementation based on
    the underlying micro-architectural support for CPU features and instructions.

    LICENSING INFORMATION: By downloading, installing and using this software,
    you agree to the terms and conditions of the AMD AOCL-LibMem license
    agreement.  You may obtain a copy of this license agreement from
    https://www.amd.com/en/developer/aocl/libmem/eula/libmem-4-2-eula.html
    """

    _name = "aocl-libmem"
    homepage = "https://www.amd.com/en/developer/aocl/libmem.html"
    git = "https://github.com/amd/aocl-libmem"
    url = "https://github.com/amd/aocl-libmem/archive/4.2.tar.gz"

    maintainers("amd-toolchain-support")

    version("5.3", sha256="15ca49e5874d84a039f680dfc0cef849c983cbc982c321161ce8b2c4fd359be6")
    version("5.2", sha256="06b56596fe32a4528a93d18a827bd5cbd814115d16390c6f2ae93d6b5715d41d")
    version("5.1", sha256="e03bc712a576b3e14ae433a696558e121dc67aac7fc1b4dca9b727605784e994")
    version("5.0", sha256="d3148db1a57fec4f3468332c775cade356e8133bf88385991964edd7534b7e22")
    version("4.2", sha256="4ff5bd8002e94cc2029ef1aeda72e7cf944b797c7f07383656caa93bcb447569")

    variant("logging", default=False, description="Enable/Disable logger")
    variant("tunables", default=False, description="Enable/Disable user input")
    variant("shared", default=True, description="build shared library")
    variant(
        "vectorization",
        default="auto",
        when="@:5.0",
        description="Use hardware vectorization support",
        values=("avx2", "avx512", "auto"),
        multi=False,
    )

    # Add new variant for dynamic dispatcher support
    variant(
        "dynamic-dispatch",
        default=False,
        when="@5.1:",
        description="Single portable optimized library"
        " to execute on different x86 CPU architectures",
    )
    variant(
        "vectorization",
        default="none",
        when="@5.1:",
        description="Use hardware vectorization support",
        values=("avx2", "avx512", "auto", "none"),
        multi=False,
    )

    # validator needs to be built only for AuthenticAMD targets
    patch(
        "cmake.patch",
        sha256="43453a83f322de7c89264439b2e9cbde855e50f550e13ebc884d13d959002092",
        when="@5.0",
    )

    # vectorization or ISA has precedence over +dynamic-dispatch and tunables
    requires(
        "vectorization=none",
        when="+dynamic-dispatch",
        msg=(
            "+dynamic-dispatch requires vectorization=none. Set vectorization to 'none' "
            "when enabling dynamic-dispatch."
        ),
    )
    requires(
        "vectorization=none",
        when="+tunables",
        msg=(
            "+tunables requires vectorization=none. Set vectorization to 'none' when "
            "enabling tunables."
        ),
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.22:", when="@:5.0", type="build")
    depends_on("cmake@3.26:", when="@5.1:", type="build")

    @property
    def libs(self):
        """find libmem libs function"""
        shared = "+shared" in self.spec
        return find_libraries("libaocl-libmem", root=self.prefix, recursive=True, shared=shared)

    def cmake_args(self):
        """Runs ``cmake`` in the build directory"""
        spec = self.spec

        args = []
        args.append(self.define_from_variant("ENABLE_LOGGING", "logging"))
        args.append(self.define_from_variant("ENABLE_TUNABLES", "tunables"))
        args.append(self.define_from_variant("BUILD_SHARED_LIBS", "shared"))

        if spec.satisfies("@:5.0"):
            vectorization = spec.variants["vectorization"].value
            if vectorization == "auto":
                target = spec.target
                if "avx512" in target:
                    args.append("-DALMEM_ARCH=avx512")
                elif "avx2" in target:
                    args.append("-DALMEM_ARCH=avx2")
                else:
                    args.append("-DALMEM_ARCH=none")
            else:
                args.append(self.define("ALMEM_ARCH", vectorization))

        # Managing Renamed CMake Option Values
        if self.spec.satisfies("@5.1:"):
            args.append(self.define_from_variant("ALMEM_LOGGING", "logging"))
            args.append(self.define_from_variant("ALMEM_TUNABLES", "tunables"))
            args.append(self.define_from_variant("ALMEM_DYN_DISPATCH", "dynamic-dispatch"))

            if self.spec.satisfies("vectorisation=auto"):
                if "avx512" in self.spec.target:
                    args.append("-DALMEM_ISA=avx512")
                elif "avx2" in self.spec.target:
                    args.append("-DALMEM_ISA=avx2")
            else:
                args.append(self.define("ALMEM_ISA", self.spec.variants["vectorization"].value))

        return args
