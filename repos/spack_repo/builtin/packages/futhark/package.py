# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Futhark(Package):
    """Futhark is a data-parallel functional array language that compiles to
    fast, parallel code, with backends targeting multicore CPUs as well as
    GPUs via OpenCL, CUDA, HIP, and ISPC.

    Note: Spack does not have a Haskell toolchain, so a precompiled Futhark
    binary is downloaded instead of being compiled from source. Upstream only
    distributes a statically-linked Linux x86_64 binary per release, so this
    package is Linux x86_64 only. See #1408 for a discussion of the
    challenges with Haskell, and see the pandoc/shellcheck/git-annex
    packages for precedent of downloading a Haskell-derived binary.
    """

    homepage = "https://futhark-lang.org"

    executables = ["^futhark$"]

    license("ISC")

    maintainers("felsenhower")

    version(
        "0.27.1",
        sha256="11248f098643487627f69695be29d96dee351a56d3f27f3715da7cf0638a0b8f",
    )
    version(
        "0.26.4",
        sha256="bd07eba4c8f2b39ed7b494bf880a3fc5fe46254cd0cabd8ca1a63e5cf240f300",
    )
    version(
        "0.26.3",
        sha256="854039fec129e2f19f89ed8402c98356f4137dcb7eecab2c604be6b510c931ee",
    )
    version(
        "0.26.2",
        sha256="e84ba282054157515186088e5cd94bf2a07d71ef2cf8408cb0997735d146f7aa",
    )
    version(
        "0.26.1",
        sha256="dd566ced0c09904ab06eb5344661aa33bf5c3d108ccf5f4b4d04179584065c9d",
    )

    conflicts("platform=darwin", msg="Only Linux x86_64 binaries are published upstream")
    conflicts("platform=windows", msg="Only Linux x86_64 binaries are published upstream")
    conflicts("target=aarch64:", msg="Only Linux x86_64 binaries are published upstream")

    # These variants only make the headers/libraries/tools that the
    # respective Futhark backend shells out to (a system C compiler, nvcc,
    # hipcc, ispc, ...) available in the environment. They do not affect how
    # the futhark compiler itself is built, since it is a precompiled binary.
    variant("c", default=True, description="Make dependencies for the C backend available")
    variant(
        "opencl",
        default=False,
        description="Make dependencies for the opencl backend available",
    )
    variant(
        "cuda",
        default=False,
        description="Make dependencies for the cuda backend available",
    )
    variant(
        "hip",
        default=False,
        description="Make dependencies for the hip backend available",
    )
    variant(
        "ispc",
        default=False,
        description="Make dependencies for the ispc backend available",
    )
    variant(
        "python",
        default=False,
        description="Make dependencies for the python backend available",
    )
    variant(
        "pyopencl",
        default=False,
        description="Make dependencies for the pyopencl backend available",
    )

    requires("+c", when="+opencl")
    requires("+c", when="+cuda")
    requires("+c", when="+hip")
    requires("+c", when="+ispc")
    requires("+opencl", when="+pyopencl")
    requires("+python", when="+pyopencl")

    depends_on("c", when="+c", type="run")
    depends_on("opencl-c-headers", when="+opencl", type="run")
    depends_on("ocl-icd", when="+opencl", type="run")
    depends_on("cuda", when="+cuda", type="run")
    depends_on("hip", when="+hip", type="run")
    depends_on("ispc", when="+ispc", type="run")
    depends_on("python", when="+python", type="run")
    depends_on("py-pyopencl", when="+pyopencl", type="run")

    def url_for_version(self, version):
        return (
            f"https://github.com/diku-dk/futhark/releases/download/"
            f"v{version}/futhark-{version}-linux-x86_64.tar.xz"
        )

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.match(r"Futhark ([\d.]+)\.", output)
        return match.group(1) if match else None

    def install(self, spec, prefix):
        install_tree("bin", prefix.bin)
        install_tree("share", prefix.share)

    def setup_run_environment(self, env):
        if self.spec.satisfies("+c"):
            env.prepend_path("PATH", self.spec["c"].prefix.bin)

        if self.spec.satisfies("+opencl"):
            env.prepend_path("CPATH", self.spec["opencl-c-headers"].prefix.include)
            env.prepend_path("LIBRARY_PATH", self.spec["ocl-icd"].prefix.lib)
            env.prepend_path("LD_LIBRARY_PATH", self.spec["ocl-icd"].prefix.lib)

        if self.spec.satisfies("+cuda"):
            cuda_prefix = self.spec["cuda"].prefix
            env.set("CUDA_HOME", cuda_prefix)
            env.prepend_path("PATH", cuda_prefix.bin)
            env.prepend_path("CPATH", cuda_prefix.include)
            env.prepend_path("LIBRARY_PATH", cuda_prefix.lib64)
            env.prepend_path("LD_LIBRARY_PATH", cuda_prefix.lib64)

        if self.spec.satisfies("+hip"):
            hip_prefix = self.spec["hip"].prefix
            env.set("HIP_PATH", hip_prefix)
            env.prepend_path("PATH", hip_prefix.bin)
            env.prepend_path("CPATH", hip_prefix.include)
            env.prepend_path("LIBRARY_PATH", hip_prefix.lib)
            env.prepend_path("LD_LIBRARY_PATH", hip_prefix.lib)

        if self.spec.satisfies("+ispc"):
            env.prepend_path("PATH", self.spec["ispc"].prefix.bin)

        if self.spec.satisfies("+python"):
            env.prepend_path("PATH", self.spec["python"].prefix.bin)
