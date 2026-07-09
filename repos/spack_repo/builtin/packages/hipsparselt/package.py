# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Hipsparselt(CMakePackage, ROCmPackage):
    """hipSPARSELt is a SPARSE marshalling library, with multiple supported backends.
    It sits between the application and a 'worker' SPARSE library, marshalling inputs into
    the backend library and marshalling results back to the application. hipSPARSELt exports
    an interface that does not require the client to change, regardless of the chosen backend.
    Currently, hipSPARSELt supports rocSPARSELt and cuSPARSELt v0.4 as backends."""

    homepage = "https://github.com/ROCm/hipsparselt"
    git = "https://github.com/ROCm/rocm-libraries.git"

    tags = ["rocm"]
    maintainers("srekolam", "afzpatel", "renjithravindrankannath")
    libraries = ["libhipsparselt"]
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.0.2"):
            url = "https://github.com/ROCm/hipsparselt/archive/refs/tags/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-libraries/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.3", sha256="300cc50720d40bad7c7ed1f6d67e8c5ebecaba62c07a6ea1cc5813c0ea2e41b5")
    version("7.2.1", sha256="bc5140deec3b1c93c13796a8a6d2cb7e50aa87fd89f60f87c8d801d66f2fd156")
    version("7.2.0", sha256="8ad5f4a11f1ed8a7b927f2e65f24083ca6ce902a42021a66a815190a91ccb654")
    version("7.1.1", sha256="2c00694c6131192354b0e785e4dcb06a302e4b7891ec50ca30927e05ba7b368b")
    version("7.1.0", sha256="d9e138a15e8195a7e9b5e15240e50c557b830d50a2bafa27db14dad3884dbfd8")
    version("7.0.2", sha256="04bb529fa656624f8875b726aa5ef1699207fdc5de4b3446986eafc4890ef708")
    version("7.0.0", sha256="317f035fe13f3fa008d567f9553978483821ab34ca8108ecc11fbb2b47bd99e0")
    version("6.4.3", sha256="2255b2732a9101a7b4fb51f4d11810be64dc3999728c77850a3918cabcf5cb50")
    version("6.4.2", sha256="5148b05436e8f7ceffdb31a01da53adc061019055cecf9b71051103045656dc8")
    version("6.4.1", sha256="74836c789e912e61532aacf275efb053ac6d0818b3da360e7b236e1b82b3152b")
    version("6.4.0", sha256="3950f424c5623bdf764e23c263f3a63de62e3690f491251b88054e27560dc604")
    version("6.3.3", sha256="6b756e20fddb37b8c1237ef8e124452c9bdd46acad8a40699d10b609d0d2ebfc")
    version("6.3.2", sha256="a0b30b478eff822dd7fa1c116ad99dcdf14ece1c33aae04ac71b594efd4d9866")
    version("6.3.1", sha256="403d4c0ef47f89510452a20be6cce72962f21761081fc19a7e0e27e7f0c4ccfd")
    version("6.3.0", sha256="f67ed4900101686596add37824d0628f1e71cf6a30d827a0519b3c3657f63ac3")
    version("6.2.4", sha256="7b007b346f89fac9214ad8541b3276105ce1cac14d6f95a8a504b5a5381c8184")
    version("6.2.1", sha256="a23287bc759442aebaccce0306f5e3938865240e13553847356c25c54214a0d4")
    version("6.2.0", sha256="a25a3ce0ed3cc616b1a4e38bfdd5e68463bb9fe791a56d1367b8a6373bb63d12")
    version("6.1.2", sha256="a5a01fec7bc6e1f4792ccd5c8eaee7b42deac315c54298a7ce5265e5551e8640")
    version("6.1.1", sha256="ca6da099d9e385ffce2b68404f395a93b199af1592037cf52c620f9148a6a78d")
    version("6.1.0", sha256="66ade6de4fd19d144cab27214352faf5b00bbe12afe59472efb441b16d090265")
    version("6.0.2", sha256="bdbceeae515f737131f0391ee3b7d2f7b655e3cf446e4303d93f083c59053587")
    version("6.0.0", sha256="cc4c7970601edbaa7f630b7ea24ae85beaeae466ef3e5ba63e11eab52465c157")

    amdgpu_targets = ROCmPackage.amdgpu_targets
    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=disjoint_sets(("auto",), amdgpu_targets)
        .with_default("auto")
        .with_error(
            "the values 'auto' and 'none' are mutually exclusive with any of the other values"
        )
        .with_non_feature_values("auto", "none"),
        sticky=True,
    )
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

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
        depends_on(f"rocm-openmp-extras@{ver}", when=f"@{ver}", type="test")

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
        "7.2.1",
        "7.2.3",
    ]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"hipsparse@{ver}", when=f"@{ver}")
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")

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
        "7.2.1",
        "7.2.3",
    ]:
        depends_on(f"rocm-smi-lib@{ver}", when=f"@{ver}")

    for ver in ["7.0.0", "7.0.2"]:
        depends_on(f"roctracer-dev@{ver}", when=f"@{ver}")

    for ver in ["7.1.0", "7.1.1", "7.2.0", "7.2.1", "7.2.3"]:
        depends_on(f"roctracer-dev@{ver}", when=f"@{ver}")
        depends_on(f"hipblas-common@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}", when=f"@{ver}")

    depends_on("cmake@3.5:", type="build")
    depends_on("msgpack-c@3:")
    depends_on("python@3.6:")
    depends_on("py-virtualenv")
    depends_on("py-wheel")
    depends_on("py-pip")
    depends_on("py-pyyaml", type="test")
    depends_on("py-joblib")
    depends_on("googletest@1.10.0:", type="test")
    depends_on("netlib-lapack@3.7.1:", type="test")
    depends_on("amdblis", type="test", when="@7.2:")
    depends_on("python-venv", when="@7.0:")
    depends_on("py-pyyaml+libyaml", when="@7.1:")
    depends_on("py-packaging", when="@7.1:")
    depends_on("py-msgpack", when="@7.1:")

    for t_version, t_commit in [
        ("7.0.2", "7fc3631478ce7887f3cfdba3adb149240ac539db"),
        ("7.0.0", "7fc3631478ce7887f3cfdba3adb149240ac539db"),
    ]:
        resource(
            name="hipblaslt",
            git="https://github.com/ROCm/hipBLASLt.git",
            commit=t_commit,
            when=f"@{t_version}",
        )
    patch("0001-update-llvm-path-add-hipsparse-include-dir-for-spack.patch", when="@6.0")
    # Below patch sets the proper path for clang++,lld and clang-offload-blunder inside the
    # tensorlite subdir of hipblas . Also adds hipsparse and msgpack include directories
    # for 6.1.0 release.
    patch("0001-update-llvm-path-add-hipsparse-include-dir-for-spack-6.1.patch", when="@6.1")
    patch("0001-update-llvm-path-add-hipsparse-include-dir-for-spack-6.2.patch", when="@6.2")
    patch("0001-update-llvm-path-add-hipsparse-include-dir-for-spack-6.3.patch", when="@6.3")
    patch("0002-add-hipsparse-include.patch", when="@6.4")
    patch("0003-add-roctracer-inc-dir.patch", when="@7.2")

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

    def patch(self):
        purelib = self.spec["python"].package.purelib
        joblib_path = os.path.join(self.spec["py-joblib"].prefix, purelib)
        if not self.spec["hip"].external:
            if self.spec.satisfies("@6.4:7.1") and self.run_tests:
                filter_file(
                    r"${HIP_CLANG_ROOT}/lib",
                    "{0}/lib".format(self.spec["rocm-openmp-extras"].prefix),
                    "clients/CMakeLists.txt",
                    string=True,
                )
        if self.spec.satisfies("@7.0"):
            filter_file(
                "${PROJECT_BINARY_DIR}/lib",
                ":".join(["${PROJECT_BINARY_DIR}/lib", joblib_path]),
                "hipBLASLt/tensilelite/CMakeLists.txt",
                "hipBLASLt/tensilelite/Tensile/cmake/TensileConfig.cmake",
                "hipBLASLt/library/src/amd_detail/rocblaslt/src/extops/CMakeLists.txt",
                string=True,
            )
        if self.spec.satisfies("@7.1:"):
            filter_file(
                "${PROJECT_BINARY_DIR}/lib",
                ":".join(["${PROJECT_BINARY_DIR}/lib", joblib_path]),
                "projects/hipblaslt/tensilelite/CMakeLists.txt",
                "projects/hipblaslt/tensilelite/Tensile/cmake/TensileConfig.cmake",
                string=True,
            )
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

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@7.1:"):
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++")
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang")
        else:
            env.set("CXX", self.spec["hip"].hipcc)
        if self.spec.satisfies("+asan"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
        env.set("TENSILE_ROCM_ASSEMBLER_PATH", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
        env.set(
            "TENSILE_ROCM_OFFLOAD_BUNDLER_PATH",
            f"{self.spec['llvm-amdgpu'].prefix}/bin/clang-offload-bundler",
        )
        env.set(
            "ROCM_AGENT_ENUMERATOR_PATH",
            f"{self.spec['rocminfo'].prefix}/bin/rocm_agent_enumerator",
        )
        if self.spec.satisfies("@6.3:"):
            env.set("ROCM_SMI_PATH", f"{self.spec['rocm-smi-lib'].prefix}/bin/rocm-smi")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.1:"):
            return "projects/hipsparselt"
        else:
            return "."

    def cmake_args(self):
        args = [
            self.define("Tensile_CODE_OBJECT_VERSION", "default"),
            self.define("MSGPACK_DIR", self.spec["msgpack-c"].prefix),
            self.define_from_variant("BUILD_ADDRESS_SANITIZER", "asan"),
            self.define("BUILD_SHARED_LIBS", "ON"),
        ]
        if "auto" not in self.spec.variants["amdgpu_target"]:
            args.append(self.define_from_variant("AMDGPU_TARGETS", "amdgpu_target"))
        if self.spec.satisfies("@7.0"):
            args.append(
                self.define(
                    "Tensile_TEST_LOCAL_PATH", f"{self.stage.source_path}/hipBLASLt/tensilelite"
                )
            )
        if self.spec.satisfies("@7.0:"):
            args.append(self.define("Python_EXECUTABLE", self.spec["python"].prefix.bin.python3))
            args.append(self.define("Python_ROOT", self.spec["python"].prefix.bin))
        if self.spec.satisfies("@7.1"):
            args.append(self.define("BUILD_USE_LOCAL_TENSILE", "OFF"))
        if self.spec.satisfies("@7.2:"):
            args.append(self.define("BUILD_TESTING", self.run_tests))
            args.append(self.define("HIPSPARSELT_ENABLE_CLIENT", self.run_tests))
            args.append(self.define("HIPSPARSELT_ENABLE_SAMPLES", "OFF"))
            args.append(self.define("HIPSPARSELT_ENABLE_BENCHMARKS", "OFF"))
            args.append(self.define("HIPSPARSELT_ENABLE_BLIS", self.run_tests))
        else:
            args.append(self.define("BUILD_CLIENTS_TESTS", self.run_tests))
            args.append(self.define("BUILD_CLIENTS_SAMPLES", "OFF"))
            if self.run_tests:
                args.append(
                    self.define("ROCM_OPENMP_EXTRAS_DIR", self.spec["rocm-openmp-extras"].prefix)
                )
        return args
