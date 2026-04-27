# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Rocprim(CMakePackage):
    """Radeon Open Compute Parallel Primitives Library"""

    homepage = "https://github.com/ROCm/rocPRIM"
    git = "https://github.com/ROCm/rocm-libraries.git"

    tags = ["rocm"]
    maintainers("cgmb", "srekolam", "renjithravindrankannath", "afzpatel")
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/rocPRIM/archive/refs/tags/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-libraries/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.1", sha256="bc5140deec3b1c93c13796a8a6d2cb7e50aa87fd89f60f87c8d801d66f2fd156")
    version("7.2.0", sha256="8ad5f4a11f1ed8a7b927f2e65f24083ca6ce902a42021a66a815190a91ccb654")
    version("7.1.1", sha256="a96a1e7113f8bdd82475d7d44e1827264850865920884521f20081fecdf1972c")
    version("7.1.0", sha256="97f190a84d03ed64d8db85fe9b1aece669cc216214052231f16be29e9ba1d3f9")
    version("7.0.2", sha256="bde28c7d08b46ba46d9ab13496d0d63353e4eae0e7e884167c10bccc9ebcb933")
    version("7.0.0", sha256="e4cbdeae91e95e1fb7388c39a8686ec8015599f579190538e6ada8b1dec244c2")
    version("6.4.3", sha256="b66feed30fe53aa8f2f8902604394c72f156b6517f8e5174d5b9d0b3dfcbb3c1")
    version("6.4.2", sha256="c228a7b434f7b9cb70204e43326a07bf31f4dacb15ae5e34ea1cfd839d0d459b")
    version("6.4.1", sha256="ff84b839bbe07fd2c97771c1b864dac641bfa654a652e75b0e7fed5e3ec5bb7c")
    version("6.4.0", sha256="c35c568b83f8894fc3b9b722343b0ea75c3bd961be24075fb3527d5230788e26")
    version("6.3.3", sha256="15e4f8dfc71175c568f8afa87e3e0e3c7ad0680c8bca0d9db3a39936ec185813")
    version("6.3.2", sha256="fbb4839992eaba838f798408636da30f0d61b669513dae185ab790c5fa5595c4")
    version("6.3.1", sha256="37690d9f326d68379d52a21fe9184061d38b15263a566f1f182d539e4b3277d5")
    version("6.3.0", sha256="d97c6edcf1f636721f8c023b54f3fad968b48b0709a95ecd640ec0ab1057069e")
    version("6.2.4", sha256="c567aa5e3209dd00aefe5052dde8ceb5bcc3a4aeeeb3ad8dc322f8d0791fc07f")
    version("6.2.1", sha256="55cfa8a4224bcd2dcf2298e7938c983a8bb0c1c072fc8295c198e53785b521ac")
    version("6.2.0", sha256="cd9be3a030830c96c940dc69e4a00f2701539a7e10b62ab1181ab83eeef31e57")
    version("6.1.2", sha256="560b65fffb103c11bee710e4eb871fd47dd84dfe99f5762a19c5650e490fd85d")
    version("6.1.1", sha256="94b265b6b4ed366b0ba008ef77ab6623b7b880b45874f202c887f01b67905922")
    version("6.1.0", sha256="9f02e5f8be90baa679a28f83927495ddf0e17d684536e1f820021e8c3e8e6c84")
    version("6.0.2", sha256="d3998720d3206965335902f8f67ca497b320a33b810cd19b2a2264505cb38779")
    version("6.0.0", sha256="51f26c9f891a64c8db8df51d75d86d404d682092fd9d243e966ac6b2a6de381a")
    version("5.7.1", sha256="15d820a0f61aed60efbba88b6efe6942878b02d912f523f9cf8f33a4583d6cd7")
    version("5.7.0", sha256="a1bf94bbad13a0410b49476771270606d8a9d257188ee3ec3a37eee80540fe9b")

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

    depends_on("cmake@3.10.2:", type="build")
    depends_on("numactl", type="link")
    depends_on("googletest@1.10.0:", type="test")

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
        "7.2.1",
    ]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"comgr@{ver}", when=f"@{ver}")
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.2:"):
            return "projects/rocprim"
        else:
            return "."

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CXX", self.spec["hip"].hipcc)
        if self.spec.satisfies("+asan"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def cmake_args(self):
        args = [
            self.define("ONLY_INSTALL", (not self.run_tests)),
            self.define("BUILD_TEST", self.run_tests),
            self.define("BUILD_BENCHMARK", "OFF"),
            self.define("BUILD_EXAMPLE", "OFF"),
            self.define("CMAKE_MODULE_PATH", self.spec["hip"].prefix.lib.cmake.hip),
        ]

        if "auto" not in self.spec.variants["amdgpu_target"]:
            args.append(self.define_from_variant("AMDGPU_TARGETS", "amdgpu_target"))

        if self.spec.satisfies("^cmake@3.21.0:3.21.2"):
            args.append(self.define("__skip_rocmclang", "ON"))
        if self.spec.satisfies("@:6.3.1"):
            args.append(self.define("BUILD_FILE_REORG_BACKWARD_COMPATIBILITY", True))

        return args
