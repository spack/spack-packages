# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Hipblas(CMakePackage, CudaPackage, ROCmPackage):
    """hipBLAS is a BLAS marshalling library, with multiple
    supported backends"""

    homepage = "https://github.com/ROCm/hipBLAS"
    git = "https://github.com/ROCm/hipBLAS.git"
    url = "https://github.com/ROCm/hipBLAS/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    maintainers("cgmb", "srekolam", "renjithravindrankannath", "haampie", "afzpatel")
    libraries = ["libhipblas"]

    license("MIT")

    version("7.1.1", sha256="4a77f19a6229a6135fc9e2ea8e7694efda984c654a11a8c650fa9480aaf1ca84")
    version("7.1.0", sha256="719c27d839d2008be5c5ec270299d98aab820eaf6aee907b7fa12cecd0cea092")
    version("7.0.2", sha256="af179faab4ff5eec5d5ca3af3640644c72c9a9ca676cfab50591e9d9f3fadf80")
    version("7.0.0", sha256="9500c514cb272f09cba9bea74eaac9873e8a8afc1ed30e9f5b87f795d4eda877")
    version("6.4.3", sha256="75121df09f9b0b3116c19258c9526e0cff3d8845361031305ba0369f140fd8b8")
    version("6.4.2", sha256="f56035ecb60c5244f27fd4b5f5298096212fa301689615bdce833b83bf3da733")
    version("6.4.1", sha256="3fa0a690bf96104afb093d19a4f565012a59ab6df378df8aef5420914e82d91b")
    version("6.4.0", sha256="544a302bdc494af02147dc14c75d088031927e1c3a2f7a349d817497000b1c34")
    version("6.3.3", sha256="8f645a5c9298170e71354437188eeca8272ff2b98077e9f34d1ca0fd7f27b7f8")
    version("6.3.2", sha256="6e86d4f8657e13665e37fdf3174c3a30f4c7dff2c4e2431d1be110cd7d463971")
    version("6.3.1", sha256="77a1845254d738c43a48bc52fa3e94499ed83535b5771408ff476122bc4b7b7c")
    version("6.3.0", sha256="72604c1896e42e65ea2b3e905159af6ec5eede6a353678009c47d0a24f462c92")
    version("6.2.4", sha256="3137ba35e0663d6cceed70086fc6397d9e74803e1711382be62809b91beb2f32")
    version("6.2.1", sha256="b770b6ebd27d5c12ad01827195e996469bfc826e8a2531831df475fc8d7f6b2e")
    version("6.2.0", sha256="33688a4d929b13e1fd800aff7e0833a9f7abf3913754b6b15995595e0d434e94")
    version("6.1.2", sha256="73699892855775a67f48c38beae78169a516078c17f1ed5d67c80abe5d308502")
    version("6.1.1", sha256="087ea82dff13c8162bf93343b174b18f1d58681711bce4fb7c8dc7212020c099")
    version("6.1.0", sha256="5f8193c4ef0508967e608a8adf86d63066a984c5803a4d05dd617021d6298091")
    version("6.0.2", sha256="10c1b6c1deb0f225c0fb6b2bb88398a32cd0d32d3ffce9b5c8df9db2cf88d25c")
    version("6.0.0", sha256="8fbd0c244fe82eded866e06d2399b1d91ab5d43d2ebcb73382c7ce1ae48d9cb3")
    version("5.7.1", sha256="794e9298f48ffbe3bd1c1ab87a5c2c2b953713500155fdec9ef8cbb11f81fc8a")
    version("5.7.0", sha256="8c6cd2ffa4ce6ab03e05feffe074685b5525610870aebe9d78f817b3037f33a4")

    # default to an 'auto' variant until amdgpu_targets can be given a better default than 'none'
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
    variant("rocm", default=True, description="Enable ROCm support")
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")
    conflicts("+cuda +rocm", msg="CUDA and ROCm support are mutually exclusive")
    conflicts("~cuda ~rocm", msg="CUDA or ROCm support is required")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.5:", type="build")

    depends_on("googletest@1.10.0:", type="test")
    depends_on("netlib-lapack@3.7.1:", type="test")
    depends_on("boost@1.64.0:1.76.0 +program_options cxxstd=14", type="test")
    depends_on("py-pyaml", type="test", when="@6.1:")

    patch("remove-hipblas-clients-file-installation.patch", when="@5.7")
    patch("remove-hipblas-clients-file-installation-6.0.patch", when="@6.0:6")
    patch("modify-hipblas-common-dependency.patch", when="@6.3:6")

    depends_on("hip +cuda", when="+cuda")

    for ver in ["5.7.0", "5.7.1"]:
        depends_on(f"rocm-cmake@{ver}", when=f"+rocm @{ver}")
        depends_on(f"rocsolver@{ver}", when=f"+rocm @{ver}")
        depends_on(f"rocblas@{ver}", when=f"+rocm @{ver}")

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
        depends_on(f"rocm-cmake@{ver}", when=f"+rocm @{ver}")
        depends_on(f"rocsolver@{ver}", when=f"+rocm @{ver}")
        depends_on(f"rocblas@{ver}", when=f"+rocm @{ver}")
        depends_on(f"rocm-openmp-extras@{ver}", type="test", when=f"+rocm @{ver}")

    for tgt in ROCmPackage.amdgpu_targets:
        depends_on(f"rocblas amdgpu_target={tgt}", when=f"+rocm amdgpu_target={tgt}")
        depends_on(f"rocsolver amdgpu_target={tgt}", when=f"+rocm amdgpu_target={tgt}")

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
    ]:
        depends_on(f"hipblas-common@{ver}", when=f"@{ver}")

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

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+asan"):
            self.asan_on(env)

    def cmake_args(self):
        args = [
            self.define("BUILD_CLIENTS_SAMPLES", "OFF"),
            self.define("BUILD_CLIENTS_TESTS", self.run_tests),
            self.define_from_variant("USE_CUDA", "cuda"),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]
        # FindHIP.cmake is still used for +cuda
        if self.spec.satisfies("+cuda"):
            args.append(self.define("CMAKE_MODULE_PATH", self.spec["hip"].prefix.lib.cmake.hip))
        if self.spec.satisfies("@:6.3.1"):
            args.append(self.define("BUILD_FILE_REORG_BACKWARD_COMPATIBILITY", True))
        if self.spec.satisfies("@6.1:") and self.run_tests:
            args.append(self.define("LINK_BLIS", "OFF"))

        return args

    def check(self):
        exe = Executable(join_path(self.build_directory, "clients", "staging", "hipblas-test"))
        exe("--gtest_filter=-*known_bug*:_/getrs*:_/getri_batched.solver*")
