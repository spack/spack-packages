# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Hipblaslt(CMakePackage):
    """hipBLASLt is a library that provides general matrix-matrix operations with a flexible API
    and extends functionalities beyond a traditional BLAS library"""

    homepage = "https://github.com/ROCm/hipBLASLt"
    git = "https://github.com/ROCm/rocm-libraries.git"

    maintainers("srekolam", "afzpatel", "renjithravindrankannath")
    tags = ["rocm"]
    libraries = ["libhipblaslt"]

    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.0.2"):
            url = "https://github.com/ROCm/hipBLASLt/archive/refs/tags/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-libraries/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.0", sha256="8ad5f4a11f1ed8a7b927f2e65f24083ca6ce902a42021a66a815190a91ccb654")
    version("7.1.1", sha256="2c00694c6131192354b0e785e4dcb06a302e4b7891ec50ca30927e05ba7b368b")
    version("7.1.0", sha256="d9e138a15e8195a7e9b5e15240e50c557b830d50a2bafa27db14dad3884dbfd8")
    version("7.0.2", sha256="52d7c1c6852f501f5bd37fa962e6538592741792593a173d8b6963b8f7bd2c41")
    version("7.0.0", sha256="9a38822eea27080dbeab7dd9d39b4bdaeb7c25bc5d19ca6ccf24674c3b34dbae")
    version("6.4.3", sha256="64252588faf8a9089838e8f427e911617916fd6905a8cc65370e8d25fafdf0e4")
    version("6.4.2", sha256="5e5f4a84aa4e5ef6018d0d91e97fc20394c7c17822cc8fb8307fff07b1d91823")
    version("6.4.1", sha256="929f781f86df40143c3ab98df2d746170dedb6788e368335e24c84796285a8a4")
    version("6.4.0", sha256="a4baa0c7336db9d46a0884c8ccfd0fb7e00a502b478aed9f588aa26fa8773353")
    version("6.3.3", sha256="f32d666b37bdbecbf924cc98653fa3d30a0de629039d4dad44d35a2082e39e5a")
    version("6.3.2", sha256="cc4875b1a5cf1708a7576c42aff6b4cb790cb7337f5dc2df33119a4aadcef027")
    version("6.3.1", sha256="9a18a2e44264a21cfe58ed102fd3e34b336f23d6c191ca2da726e8e0883ed663")
    version("6.3.0", sha256="e570996037ea42eeca4c9b8b0b77a202d40be1a16068a6245595c551d80bdcad")
    version("6.2.4", sha256="b8a72cb1ed4988b0569817c6387fb2faee4782795a0d8f49b827b32b52572cfd")
    version("6.2.1", sha256="9b062b1d6d945349c31828030c8c1d99fe57d14a1837196ff9aa67bf10ef43f1")
    version("6.2.0", sha256="aec9edc75ae4438aa712192c784e2bed683d2839b502b6aadb18f6012306749b")
    version("6.1.2", sha256="fcfe950f7b87c421565abe090b2de6f463afc1549841002f105ecca7bbbf59e5")
    version("6.1.1", sha256="1e21730ade59b5e32432fa0981383f689a380b1ffc92fe950822722da9521a72")
    version("6.1.0", sha256="90fc2f2c9e11c87e0529e824e4b0561dbc850f8ffa21be6932ae63cbaa27cdf0")
    version("6.0.2", sha256="e281a1a7760fab8c3e0baafe17950cf43c422184e3226e3c14eb06e50c69d421")
    version("6.0.0", sha256="6451b6fdf7f24787628190bbe8f2208c929546b68b692d8355d2f18bea7ca7db")

    amdgpu_targets = ROCmPackage.amdgpu_targets

    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("cmake@3.25.2:", type="build", when="@6.2.0:")
    depends_on("python@3.7:")
    depends_on("python@3.8:3.13.2", when="@6.4:")

    for ver in [
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
    ]:
        depends_on(f"rocm-openmp-extras@{ver}", type="test", when=f"@{ver}")

    for ver in [
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
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")

    for ver in ["6.0.0", "6.0.2", "6.1.0", "6.1.1", "6.1.2", "6.2.0", "6.2.1", "6.2.4"]:
        depends_on(f"hipblas@{ver}", when=f"@{ver}")

    for ver in [
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
        depends_on(f"hipblas-common@{ver}", when=f"@{ver}")
        depends_on(f"rocm-smi-lib@{ver}", when=f"@{ver}")

    for ver in ["6.4.0", "6.4.1", "6.4.2", "6.4.3", "7.0.0", "7.0.2", "7.1.0", "7.1.1", "7.2.0"]:
        depends_on(f"roctracer-dev@{ver}", when=f"@{ver}")

    depends_on("msgpack-c")
    depends_on("py-joblib", type=("build", "link"))
    depends_on("googletest@1.10.0:", type="test")
    depends_on("netlib-lapack@3.7.1:", type="test")
    depends_on("py-pyyaml", type="test")
    depends_on("python-venv", when="@6.4:")
    depends_on("blis", type="test", when="@7.1:")
    depends_on("boost+filesystem", when="@7.1:")
    depends_on("googletest@1.10.0:", when="@7.1:")
    depends_on("py-pyyaml+libyaml", when="@7.1:")
    depends_on("py-packaging", when="@7.1:")
    depends_on("py-msgpack", when="@7.1:")

    # Sets the proper for clang++ and clang-offload-blunder.
    # Also adds hipblas and msgpack include directories
    patch("001_Set_LLVM_Paths_And_Add_Includes.patch", when="@6.0")
    # Below patch sets the proper path for clang++ and clang-offload-blunder.
    # Also adds hipblas and msgpack include directories for 6.1.0 release.
    patch("0001-Set-LLVM_Path-Add-Hiblas-Include-to-CmakeLists-6.1.Patch", when="@6.1:6.2")
    patch("0001-Set-LLVM-Path-6.3.Patch", when="@6.3")
    patch("002-link-roctracer.patch", when="@6.4")
    patch("002-link-roctracer.7.0.patch", when="@7.0")

    patch("003-use-rocm-smi-config.patch", when="@6.4:7.0")
    patch("0004-Set-rocm-smi-ld-path-7.0.patch", when="@7.0")
    # https://github.com/ROCm/rocm-libraries/pull/2115
    patch("005-add-roctracer-include-dir.patch", when="@7.1")
    patch(
        "https://github.com/ROCm/rocm-libraries/commit/841ea340cbf3d7aa0dd37ba2da18a44128602b79.patch?full_index=1",
        sha256="503555b92ccbc33e50a10e2ba1d38e8f3349b93d786c7f6b19aaacb736c9bf7c",
        when="@7.2",
    )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@:6.4"):
            env.set("CXX", self.spec["hip"].hipcc)
        else:
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++")
        if self.spec.satisfies("@6.3.0:6.4"):
            env.set(
                "TENSILE_ROCM_ASSEMBLER_PATH", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++"
            )
        if self.spec.satisfies("@6.3.0:"):
            env.set(
                "TENSILE_ROCM_OFFLOAD_BUNDLER_PATH",
                f"{self.spec['llvm-amdgpu'].prefix}/bin/clang-offload-bundler",
            )
            env.set("ROCM_SMI_PATH", f"{self.spec['rocm-smi-lib'].prefix}/bin/rocm-smi")
            env.set(
                "ROCM_AGENT_ENUMERATOR_PATH",
                f"{self.spec['rocminfo'].prefix}/bin/rocm_agent_enumerator",
            )
        if self.spec.satisfies("@7.0:"):
            env.set("ROCM_LD_PATH", f"{self.spec['llvm-amdgpu'].prefix}/bin/ld.lld")
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang")

        if self.spec.satisfies("@7.1") and self.run_tests:
            env.append_flags("LDFLAGS", "-lstdc++fs")

    def patch(self):
        purelib = self.spec["python"].package.purelib
        joblib_path = os.path.join(self.spec["py-joblib"].prefix, purelib)
        if self.spec.satisfies("@6.3:6.4"):
            filter_file(
                "${rocm_path}/llvm/bin",
                self.spec["llvm-amdgpu"].prefix.bin,
                "tensilelite/Tensile/Ops/gen_assembly.sh",
                string=True,
            )
            filter_file(
                "${rocm_path}/bin/amdclang++",
                f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++",
                "library/src/amd_detail/rocblaslt/src/kernels/compile_code_object.sh",
                string=True,
            )
            filter_file(
                "${rocm_path}/bin/amdclang++",
                f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++",
                "tensilelite/Tensile/Ops/gen_assembly.sh",
                string=True,
            )
        if self.spec.satisfies("@7.0"):
            filter_file(
                "${PROJECT_BINARY_DIR}/lib",
                ":".join(["${PROJECT_BINARY_DIR}/lib", joblib_path]),
                "tensilelite/CMakeLists.txt",
                "tensilelite/Tensile/cmake/TensileConfig.cmake",
                "library/src/amd_detail/rocblaslt/src/extops/CMakeLists.txt",
                string=True,
            )
        if not self.spec["hip"].external:
            if self.spec.satisfies("@6.4:7.0") and self.run_tests:
                filter_file(
                    r"${HIP_CLANG_ROOT}/lib",
                    "{0}/lib".format(self.spec["rocm-openmp-extras"].prefix),
                    "clients/CMakeLists.txt",
                    string=True,
                )
            if self.spec.satisfies("@7.1") and self.run_tests:
                filter_file(
                    r"${HIP_CLANG_ROOT}/lib",
                    "{0}/lib".format(self.spec["rocm-openmp-extras"].prefix),
                    "projects/hipblaslt/clients/CMakeLists.txt",
                    string=True,
                )
        if self.spec.satisfies("@7.1:"):
            yaml_path = os.path.join(self.spec["py-pyyaml"].prefix, purelib)
            packaging_path = os.path.join(self.spec["py-packaging"].prefix, purelib)
            msgpack_path = os.path.join(self.spec["py-msgpack"].prefix, purelib)
            filter_file(
                "${_python_path}",
                ":".join(
                    ["${_python_path}", joblib_path, yaml_path, packaging_path, msgpack_path]
                ),
                "projects/hipblaslt/cmake/hipblaslt_python.cmake",
                string=True,
            )
            filter_file(
                "${PROJECT_BINARY_DIR}/lib",
                ":".join(["${PROJECT_BINARY_DIR}/lib", joblib_path]),
                "projects/hipblaslt/tensilelite/CMakeLists.txt",
                "projects/hipblaslt/tensilelite/Tensile/cmake/TensileConfig.cmake",
                string=True,
            )

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            ver = "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        else:
            ver = None
        return ver

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.1:"):
            return "projects/hipblaslt"
        else:
            return "."

    def cmake_args(self):
        args = [
            self.define("Tensile_CODE_OBJECT_VERSION", "default"),
            self.define("MSGPACK_DIR", self.spec["msgpack-c"].prefix),
            self.define_from_variant("ADDRESS_SANITIZER", "asan"),
            self.define("BUILD_CLIENTS_TESTS", self.run_tests),
        ]
        if "auto" not in self.spec.variants["amdgpu_target"]:
            if self.spec.satisfies("@7.1:"):
                args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
            else:
                args.append(self.define_from_variant("AMDGPU_TARGETS", "amdgpu_target"))
        if self.run_tests:
            args.append(
                self.define("ROCM_OPENMP_EXTRAS_DIR", self.spec["rocm-openmp-extras"].prefix)
            )
        if self.spec.satisfies("@6.4:"):
            args.append(self.define("Python_EXECUTABLE", self.spec["python"].prefix.bin.python3))
            args.append(self.define("Python_ROOT", self.spec["python"].prefix.bin))
        if self.spec.satisfies("@7.0:"):
            args.append(
                self.define(
                    "ROCROLLER_ASSEMBLER_PATH", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++"
                )
            )
            args.append(
                self.define(
                    "Tensile_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++"
                )
            )
        if self.spec.satisfies("@7.1:"):
            args.append(self.define("HIPBLASLT_ENABLE_CLIENT", self.run_tests))
        else:
            args.append(self.define("BUILD_CLIENTS_TESTS", self.run_tests))
        if self.spec.satisfies("@7.1: %gcc@8.0:8.9"):
            args.append(self.define("HIPBLASLT_ENABLE_ROCROLLER", "False"))
        return args
