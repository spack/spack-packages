# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Mivisionx(CMakePackage):
    """MIVisionX toolkit is a set of comprehensive computer
    vision and machine intelligence libraries, utilities, and
    applications bundled into a single toolkit."""

    homepage = "https://github.com/ROCm/MIVisionX"
    git = "https://github.com/ROCm/MIVisionX.git"
    url = "https://github.com/ROCm/MIVisionX/archive/rocm-6.4.3.tar.gz"

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    tags = ["rocm"]

    license("MIT")
    version("7.2.1", sha256="cedcb0bcbbe6b8636a36cac0ec3bf9e80da9e24653a8602b6e4f4f3d4d3caff2")
    version("7.2.0", sha256="188dc225d0813f172521e5a2129af5d917ab9e6616488520c0ef27468cc6d89b")
    version("7.1.1", sha256="7a7bd6ccb67e2b858526667decea938cc80c72d6279e7f6d9f3c0bb89ef823d7")
    version("7.1.0", sha256="2fba3aeb970df06f95d465cc2dd5ba5096ec47966e26f2a4544a719e78d43e37")
    version("7.0.2", sha256="ae4f230890f0ddaf0be5ea9a891843312e44c86bd8697c7e663cea142722c4de")
    version("7.0.0", sha256="31a963625e6ab6a85c371c189f265f304d7c75c573189d09882e5b2e7ca131ec")
    version("6.4.3", sha256="a489623d757d8e9825eb7eef7d799f33c84810ba053ee99106bad5f97058ab15")
    version("6.4.2", sha256="efdde57dc1c48936f371c3c548f36040bfce74d835cf1f9816076dfa601ce29e")
    version("6.4.1", sha256="9f1a1a33dc2770ac014e5ea019ebde6cadcca017840753b9cb8cf1598d2d83c8")
    version("6.4.0", sha256="de3902ad2402bf29e4f53617ec10d34188b0c67547fc290390ff0c8ac4ad505a")
    version("6.3.3", sha256="6ab255305b786c6152ffe12211f329d2bc56823bb2192a945b9aa5efe6731b82")
    version("6.3.2", sha256="2e7984e4ef2e6195aa9afa11030b8418aee885bec9befa220b9b53b5229b7fae")
    version("6.3.1", sha256="1f7bd1f6b61401bc642b50e96411344b092b09189534c5d6ba2f4c661d1af0ce")
    version("6.3.0", sha256="bc16881eae11140025b8fbd00bc741763548d41345dbe954c8d8659f4dccfe9e")
    version("6.2.4", sha256="7e65dc83f1b85e089c1218dff57211e64f3586bcb4415bda4798e4a434cba216")
    version("6.2.1", sha256="591fe23ee1e2ab49f29aeeb835b5045e4ba00165c604ddfaa26bd8eb56cb367d")
    version("6.2.0", sha256="ce28ac3aef76f28869c4dad9ffd9ef090e0b54ac58088f1f1eef803641125b51")
    version("6.1.2", sha256="0afa664931f566b7f5a3abd474dd641e56077529a2a5d7c788f5e6700e957ed6")
    version("6.1.1", sha256="3483b5167c47047cca78581cc6c9685138f9b5b25edb11618b720814788fc2a0")
    version("6.1.0", sha256="f18a72c4d12c36ab50f9c3a5c22fc3641feb11c99fed513540a16a65cd149fd1")
    version("6.0.2", sha256="e39521b3109aa0900f652ae95a4421df0fa29fd57e816268cc6602d243c50779")
    version("6.0.0", sha256="01324a12f21ea0e29a4d7d7c60498ba9231723569fedcdd90f28ddffb5e0570e")
    version("5.7.1", sha256="bfc074bc32ebe84c72149ee6abb30b5b6499023d5b98269232de82e35d0505a8")
    version("5.7.0", sha256="07e4ec8a8c06a9a8bb6394a043c9c3e7176acd3b462a16de91ef9518a64df9ba")

    amdgpu_targets = ROCmPackage.amdgpu_targets

    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )

    # Adding variant HIP which HIP as default.

    variant("hip", default=True, description="Use HIP as backend")
    variant("add_tests", default=False, description="add tests and samples folder")
    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    conflicts("+asan", when="os=rhel9")
    conflicts("+asan", when="os=centos7")
    conflicts("+asan", when="os=centos8")

    patch("0001-add-half-include-path-5.6.patch", when="@:6.1")
    patch("0002-add-half-include-path-for-tests.patch", when="@:6.0 +add_tests")
    patch("0002-add-half-include-path-for-tests-6.1.0.patch", when="@6.1 +add_tests")
    patch("0002-add-half-include-path-for-tests-6.2.0.patch", when="@6.2.0: +add_tests")

    def patch(self):
        filter_file(
            r"${ROCM_PATH}/include/miopen/config.h",
            "{0}/include/miopen/config.h".format(self.spec["miopen-hip"].prefix),
            "amd_openvx_extensions/CMakeLists.txt",
            string=True,
        )
        filter_file(
            r"${ROCM_PATH}/llvm/bin/clang++",
            "{0}/bin/clang++".format(self.spec["llvm-amdgpu"].prefix),
            "amd_openvx/openvx/hipvx/CMakeLists.txt",
            "amd_openvx_extensions/amd_nn/nn_hip/CMakeLists.txt",
            string=True,
        )
        if self.spec.satisfies("@:6.1 + hip"):
            filter_file(
                r"${ROCM_PATH}/llvm/bin/clang++",
                "{0}/bin/clang++".format(self.spec["llvm-amdgpu"].prefix),
                "rocAL/rocAL/rocAL_hip/CMakeLists.txt",
                string=True,
            )
        if self.spec.satisfies("@:6.0.0 +add_tests"):
            filter_file(
                r"${ROCM_PATH}/include/mivisionx",
                "{0}/include/mivisionx".format(self.spec.prefix),
                "samples/inference/mv_objdetect/CMakeLists.txt",
                string=True,
            )
            filter_file(
                r"${ROCM_PATH}/lib",
                "{0}/lib".format(self.spec.prefix),
                "samples/inference/mv_objdetect/CMakeLists.txt",
                string=True,
            )
        if self.spec.satisfies("@6.1.0: +add_tests"):
            filter_file(
                r"${ROCM_PATH}/include/mivisionx",
                "{0}/include/mivisionx".format(self.spec.prefix),
                "samples/mv_objdetect/CMakeLists.txt",
                string=True,
            )
            filter_file(
                r"${ROCM_PATH}/lib",
                "{0}/lib".format(self.spec.prefix),
                "samples/mv_objdetect/CMakeLists.txt",
                string=True,
            )

        if self.spec.satisfies("@:6.1 +add_tests"):
            filter_file(
                r"${ROCM_PATH}/${CMAKE_INSTALL_INCLUDEDIR}/mivisionx/rocal",
                "{0}/include/mivisionx/rocal".format(self.spec.prefix),
                "utilities/rocAL/rocAL_unittests/CMakeLists.txt",
                "utilities/rocAL/rocAL_video_unittests/CMakeLists.txt",
                string=True,
            )
            filter_file(
                r"${ROCM_PATH}/lib",
                "{0}/lib".format(self.spec.prefix),
                "utilities/rocAL/rocAL_unittests/CMakeLists.txt",
                "utilities/rocAL/rocAL_video_unittests/CMakeLists.txt",
                string=True,
            )
        if self.spec.satisfies("+add_tests"):
            filter_file(
                r"${ROCM_PATH}/include/mivisionx",
                "{0}/include/mivisionx".format(self.spec.prefix),
                "tests/amd_migraphx_tests/mnist/CMakeLists.txt",
                "tests/amd_migraphx_tests/resnet50/CMakeLists.txt",
                "model_compiler/python/nnir_to_clib.py",
                string=True,
            )
            filter_file(
                r"${ROCM_PATH}/lib",
                "{0}/lib".format(self.spec.prefix),
                "tests/amd_migraphx_tests/mnist/CMakeLists.txt",
                "tests/amd_migraphx_tests/resnet50/CMakeLists.txt",
                string=True,
            )
            filter_file(
                r"/opt/rocm",
                "{0}".format(self.spec.prefix),
                "model_compiler/python/nnir_to_clib.py",
                string=True,
            )
        if self.spec.satisfies("@6.2:"):
            filter_file(
                r"crypto",
                "{0}".format(self.spec["openssl"].libs),
                "utilities/runvx/CMakeLists.txt",
                "utilities/runcl/CMakeLists.txt",
                string=True,
            )

    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.5:", type="build")
    depends_on("ffmpeg@4.4:", type="build")
    depends_on("protobuf@3.12.4:", type="build")
    depends_on(
        "opencv@4.5:"
        "+calib3d+features2d+highgui+imgcodecs+imgproc"
        "+video+videoio+flann+photo+objdetect+png+jpeg",
        type="build",
    )
    depends_on("openssl")
    depends_on("libjpeg-turbo@2.0.6+partial_decoder", type="build", when="@:6.2.0")
    depends_on("lmdb")
    depends_on("py-setuptools")
    depends_on("py-wheel")
    depends_on("py-pybind11")
    depends_on("py-google-api-python-client", when="+add_tests")
    depends_on("py-protobuf@3.20.3", type=("build", "run"), when="+add_tests")
    depends_on("py-future", when="+add_tests")
    depends_on("py-numpy", when="+add_tests")
    depends_on("py-pytz", when="+add_tests")
    depends_on("rapidjson", when="@5.7:")

    with when("+hip"):
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
            depends_on(f"rocm-core@{ver}", when=f"@{ver}")
            depends_on(f"hip@{ver}", when=f"@{ver}")
            for tgt in ROCmPackage.amdgpu_targets:
                depends_on(
                    f"migraphx@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}"
                )
                depends_on(
                    f"miopen-hip@{ver} amdgpu_target={tgt}", when=f"@{ver} amdgpu_target={tgt}"
                )
            depends_on(f"rpp@{ver}", when=f"@{ver}")
            depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
            depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on("python@3.5:", type="build")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("MIVISIONX_MODEL_COMPILER_PATH", self.spec.prefix.libexec.mivisionx.model_compiler)
        if self.spec.satisfies("@6.1:") and not self.spec.external:
            env.prepend_path("LD_LIBRARY_PATH", self.spec["hsa-rocr-dev"].prefix.lib)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@6.1:"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
        if self.spec.satisfies("+asan"):
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def flag_handler(self, name, flags):
        spec = self.spec
        protobuf = spec["protobuf"].prefix.include
        if name == "cxxflags":
            flags.append("-I{0}".format(protobuf))
        return (flags, None, None)

    def cmake_args(self):
        spec = self.spec
        protobuf = spec["protobuf"].prefix.include
        args = [
            self.define("CMAKE_CXX_FLAGS", "-I{0}".format(protobuf)),
            self.define("AMDRPP_LIBRARIES", "{0}/lib/librpp.so".format(spec["rpp"].prefix)),
            self.define("AMDRPP_INCLUDE_DIRS", "{0}/include/rpp".format(spec["rpp"].prefix)),
            self.define("CMAKE_INSTALL_PREFIX_PYTHON", spec.prefix),
        ]
        if self.spec.satisfies("+hip"):
            args.append(self.define("BACKEND", "HIP"))
            args.append(self.define("HSA_PATH", spec["hsa-rocr-dev"].prefix))
            args.append(self.define("HIP_PATH", spec["hip"].prefix))

        if self.spec.satisfies("~hip"):
            args.append(self.define("BACKEND", "CPU"))

        if self.spec.satisfies("@:6.2.0"):
            args.append(
                self.define(
                    "TurboJpeg_LIBRARIES_DIRS", "{0}/lib64".format(spec["libjpeg-turbo"].prefix)
                )
            )
        if "auto" not in self.spec.variants["amdgpu_target"]:
            args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
        return args

    @run_after("install")
    def add_tests(self):
        if self.spec.satisfies("+add_tests"):
            install_tree("tests", self.spec.prefix.tests)
            install_tree("samples", self.spec.prefix.samples)
            install_tree("utilities", self.spec.prefix.utilities)
