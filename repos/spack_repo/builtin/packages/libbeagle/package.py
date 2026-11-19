# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems import autotools, cmake
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Libbeagle(CMakePackage, AutotoolsPackage, CudaPackage):
    """BEAGLE is a high-performance library for evaluating phylogenetic likelihoods
    on CPUs and GPUs, used by programs such as BEAST and MrBayes."""

    homepage = "https://github.com/beagle-dev/beagle-lib"
    url = "https://github.com/beagle-dev/beagle-lib/archive/v3.1.2.tar.gz"

    license("LGPL-3.0-or-later", when="@:3")
    license("MIT", when="@4:")

    version("4.0.1", sha256="9d258cd9bedd86d7c28b91587acd1132f4e01d4f095c657ad4dc93bd83d4f120")
    version("3.1.2", sha256="dd872b484a3a9f0bce369465e60ccf4e4c0cd7bd5ce41499415366019f236275")
    version(
        "2.1.2",
        sha256="82ff13f4e7d7bffab6352e4551dfa13afabf82bff54ea5761d1fc1e78341d7de",
        url="https://github.com/beagle-dev/beagle-lib/archive/beagle_release_2_1_2.tar.gz",
    )

    build_system(
        conditional("cmake", when="@4:"), conditional("autotools", when="@:3"), default="cmake"
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    with when("build_system=autotools"):
        depends_on("autoconf", type="build")
        depends_on("automake", type="build")
        depends_on("libtool", type="build")
        depends_on("m4", type="build")
        depends_on("subversion", type="build")
        depends_on("pkgconfig", type="build")

    # the JNI library BEAST uses needs a JDK to build
    depends_on("java", type="build")
    depends_on("opencl", when="+opencl")

    cuda_arch_values = CudaPackage.cuda_arch_values
    variant("opencl", default=False, description="Include OpenCL (GPU) support")
    variant(
        "cuda_arch",
        description="CUDA architecture",
        default="none",
        values=("none",) + cuda_arch_values,
        multi=False,
    )
    conflicts("cuda_arch=none", when="+cuda", msg="must select a CUDA architecture")

    def patch(self):
        if self.spec.satisfies("@4:"):
            # Spack injects the target flags; this is a plain set(), so -D can't override it
            filter_file(
                "set(BEAGLE_OPTIMIZE_FOR_NATIVE_ARCH true)",
                "set(BEAGLE_OPTIMIZE_FOR_NATIVE_ARCH false)",
                "CMakeLists.txt",
                string=True,
            )
            if self.spec.satisfies("+cuda"):
                # kernels are embedded as PTX; build it for the requested arch
                filter_file(
                    "-D_POSIX_C_SOURCE -std=c++11",
                    "-D_POSIX_C_SOURCE -std=c++11 -arch=compute_{0}".format(
                        self.spec.variants["cuda_arch"].value
                    ),
                    "libhmsbeagle/GPU/CMake_CUDA/CMakeLists.txt",
                    string=True,
                )
            return

        # update cuda architecture if necessary
        if self.spec.satisfies("+cuda"):
            cuda_arch = self.spec.variants["cuda_arch"].value
            archflag = "-arch=compute_{0}".format(cuda_arch)

            filter_file(
                "-arch compute_13", "", "libhmsbeagle/GPU/kernels/Makefile.am", string=True
            )

            filter_file(r'(NVCCFLAGS="-O3).*(")', r"\1 {0}\2".format(archflag), "configure.ac")

            # point CUDA_LIBS to libcuda.so
            filter_file(
                "-L$with_cuda/lib", "-L$with_cuda/lib64/stubs", "configure.ac", string=True
            )


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_CUDA", "cuda"),
            self.define_from_variant("BUILD_OPENCL", "opencl"),
            self.define("BUILD_JNI", True),
        ]
        if self.spec.satisfies("+cuda"):
            cuda = self.spec["cuda"].prefix
            args.append(self.define("CUDA_TOOLKIT_ROOT_DIR", cuda))
            # hmsbeagle-cuda links -lcuda; use the toolkit stub so no driver is needed
            args.append(self.define("CMAKE_SHARED_LINKER_FLAGS", f"-L{cuda.lib64.stubs}"))
        return args


class AutotoolsBuilder(autotools.AutotoolsBuilder):
    def autoreconf(self, pkg, spec, prefix):
        which("bash", required=True)("autogen.sh")

    def configure_args(self):
        args = [
            # Since spack will inject architecture flags turn off -march=native
            # when building libbeagle.
            "--disable-march-native"
        ]

        if self.spec.satisfies("+cuda"):
            args.append("--with-cuda={0}".format(self.spec["cuda"].prefix))
        else:
            args.append("--without-cuda")

        if self.spec.satisfies("+opencl"):
            args.append("--with-opencl={0}".format(self.spec["opencl"].prefix))
        else:
            args.append("--without-opencl")

        return args
