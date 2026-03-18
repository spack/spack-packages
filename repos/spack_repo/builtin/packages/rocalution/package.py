# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import itertools
import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Rocalution(CMakePackage):
    """rocALUTION is a sparse linear algebra library with focus on
    exploring fine-grained parallelism on top of AMD's Radeon Open
    eCosystem Platform ROCm runtime and toolchains, targeting modern
    CPU and GPU platforms. Based on C++ and HIP, it provides a portable,
     generic and flexible design that allows seamless integration with
    other scientific software packages."""

    homepage = "https://github.com/ROCm/rocALUTION"
    git = "https://github.com/ROCm/rocALUTION.git"
    url = "https://github.com/ROCm/rocALUTION/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    maintainers("cgmb", "srekolam", "renjithravindrankannath", "afzpatel")
    libraries = ["librocalution"]

    license("MIT")

    version("7.2.0", sha256="15cf2f3cded70c300a2b5ee2af5b887397640ece922b4e384daef26e3ef65656")
    version("7.1.1", sha256="354c892f1e6964977631c681876dbb45a96d4ed07a103403232ca5ec7c85a3cf")
    version("7.1.0", sha256="0f8d8c24317b30d7269841b9fe5ab2d24dddd3d5132e84b4f8ac1cd9d30b0ff2")
    version("7.0.2", sha256="638e9c5f677a8b8c3437dacdcdd0f0d7cc70546d8bbd4e86813a5b90703a0619")
    version("7.0.0", sha256="0ca9d0e4a9ade70370cb2cc5c8f29206507a7e941385933ba41a39ea82b53d5a")
    version("6.4.3", sha256="e74efb3ed6925c5552e5c488f40ac9610e00f100433d9bda92ccb6985878f46f")
    version("6.4.2", sha256="74520eba1005c4db4d7c9bc1cb00469acd6d65755ca53cd1bb842c82dd418570")
    version("6.4.1", sha256="42e1478edd1a96a5b72dd71b8859529bbcb0cac2f4ad36b907fa2479e7cab629")
    version("6.4.0", sha256="dcd6cccb55136362bedb4681f10eb9c9fe7f958f63802f85573732c2cd7a5185")
    version("6.3.3", sha256="bec6388e74b74922c2dc3af0d73ff0e4cafdabad9e8473181079df09de81c11a")
    version("6.3.2", sha256="b13118a5c0af08a666d80af78d52bdfba12ed134f6745ab36d8de75ed3bc7584")
    version("6.3.1", sha256="94b78b34ac750c09831aa70a3d7f8cd220c540a75e4f91c391ba435de420c536")
    version("6.3.0", sha256="a7476e1ce79915cb8e01917de372ae6b15d7e51b1a25e15cde346dadf2391068")
    version("6.2.4", sha256="993c55e732d0ee390746890639486649f36ae806110cf7490b9bb5d49b0663c0")
    version("6.2.1", sha256="94f15add5316c81529ce84ae8bf2701e9a4df57d08eda04a2f70147d31b12632")
    version("6.2.0", sha256="fd9ad0aae5524d3995343d4d7c1948e7b21f0bdf5b1203d1de58548a814a9c39")
    version("6.1.2", sha256="5f9fb302ab1951a1caf54ed31b41d6f41a353dd4b5ee32bc3de2e9f9244dd4ef")
    version("6.1.1", sha256="1f80b33813291c2e81e5b1efc325d3f5bb6592c8670c016930d01e73e74ab46b")
    version("6.1.0", sha256="699a9b73844fcd4e30d0607b4042dc779f9bcdc27ad732e7a038968ff555af2b")
    version("6.0.2", sha256="453f889677728b510286d4c72952b343cac63c45e2cb8b801d8388a2ec599d2a")
    version("6.0.0", sha256="cabf37691b8db00c82bda49c7dcfaefd9b9067b7d097afa43b7a5f86c45bff99")
    version("5.7.1", sha256="b95afa1285759843c5fea1ad6e1c1edf283922e0d448db03a3e1f42b6942bc24")
    version("5.7.0", sha256="48232a0d1250debce89e39a233bd0b5d52324a2454c078b99c9d44965cbbc0e9")

    amdgpu_targets = ROCmPackage.amdgpu_targets

    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    conflicts("+asan", when="os=rhel9")
    conflicts("+asan", when="os=centos7")
    conflicts("+asan", when="os=centos8")

    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.5:", type="build")

    for ver in [
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
        "7.2.0",
    ]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"rocprim@{ver}", when=f"@{ver}")
        for tgt in itertools.chain(["auto"], amdgpu_targets):
            rocblas_tgt = tgt if tgt != "gfx900:xnack-" else "gfx900"
            depends_on(
                f"rocblas@{ver} amdgpu_target={rocblas_tgt}", when=f"@{ver} amdgpu_target={tgt}"
            )
            depends_on(f"rocsparse@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")
            depends_on(f"rocrand@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}")
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")

    depends_on("googletest@1.10.0:", type="test")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CXX", self.spec["hip"].hipcc)
        if self.spec.satisfies("+asan"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def patch(self):
        with working_dir("src/base/hip"):
            filter_file(
                "^#include <rocrand/rocrand.hpp>",
                "#include <rocrand.hpp>",
                "hip_rand_normal.hpp",
                "hip_rand_uniform.hpp",
            )

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            return "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        return None

    def cmake_args(self):
        args = [
            self.define("SUPPORT_HIP", "ON"),
            self.define("SUPPORT_MPI", "OFF"),
            self.define("BUILD_CLIENTS_SAMPLES", "OFF"),
            self.define("BUILD_CLIENTS_TESTS", self.run_tests),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            self.define("CMAKE_MODULE_PATH", self.spec["hip"].prefix.lib.cmake.hip),
        ]
        if "auto" not in self.spec.variants["amdgpu_target"]:
            if self.spec.satisfies("@7.1:"):
                args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
            else:
                args.append(self.define_from_variant("AMDGPU_TARGETS", "amdgpu_target"))

        if self.spec.satisfies("^cmake@3.21.0:3.21.2"):
            args.append(self.define("__skip_rocmclang", "ON"))

        if self.spec.satisfies("@:6.3.1"):
            args.append(self.define("BUILD_FILE_REORG_BACKWARD_COMPATIBILITY", True))

        return args

    @run_after("build")
    @on_package_attributes(run_tests=True)
    def check_build(self):
        exe = Executable(join_path(self.build_directory, "clients", "staging", "rocalution-test"))
        exe()
