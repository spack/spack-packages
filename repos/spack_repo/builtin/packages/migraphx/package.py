# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Migraphx(CMakePackage):
    """AMD's graph optimization engine."""

    homepage = "https://github.com/ROCm/AMDMIGraphX"
    git = "https://github.com/ROCm/AMDMIGraphX.git"
    url = "https://github.com/ROCm/AMDMIGraphX/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    libraries = ["libmigraphx"]

    license("MIT")
    version("7.2.0", sha256="085ea6fcf6197b20fed60917194ca622e5d2c1705237fe063563f988494a8b3d")
    version("7.1.1", sha256="beb9cbf4475d979e8431a983ee0ae8a9f5b75bb24699b7b8dfa2753db9822c4d")
    version("7.1.0", sha256="ffb6e510420e277e30fc1a58635d568197ab2046784ea0c4740aa79ffb17cb70")
    version("7.0.2", sha256="33979c1d8f514d65f823f28b2cd2eb11338477403f295e6367244a3abb0abadd")
    version("7.0.0", sha256="b63634546781af8550395ebc6356e9a3e91a992d82ccb228ea60c719727f5247")
    version("6.4.3", sha256="d3839034d3cbd7762818002e87da730f3c3172cdefca1aab58ade8d2a9889651")
    version("6.4.2", sha256="2c008ce2af0900ce7802ec078c2e69f59d8af980ce5161bee625111aec7d941b")
    version("6.4.1", sha256="25716eb8a7f73cba722cc60ba6a71fbf6459f5491a350c285cf1ec904c339095")
    version("6.4.0", sha256="9041ea3c0ea0a22884e049f2a12559b6221eac897d31b3ebe0cf3e7a5b7d0268")
    version("6.3.3", sha256="a268baa99b145a32fe282e407cf923b1c1022f2ddab36d7178537b860fdfcf8d")
    version("6.3.2", sha256="4e6b9800919e99070c0289616657592c23ff66a55230409f38e5c7e099c0d89b")
    version("6.3.1", sha256="c60df20b3c890c469265ae6f273fb5d43cc13c8c514f76dd7b4d195d9e44ba85")
    version("6.3.0", sha256="21550e5cecf1b26c02e1c4633c7c4c6eb5e37be8758d7a2641f10cfdf4203636")
    version("6.2.4", sha256="849cca3c7c98dc437e42ac17013f86ef0a5fd202cb87b7822778bd9a8f93d293")
    version("6.2.1", sha256="a9479fd6846bae4a888f712c2fecee6a252951ae8979d9990b100450e4cd6c30")
    version("6.2.0", sha256="7b36c1a0c44dd21f31ce6c9c4e7472923281aa7fdc693e75edd2670b101a6d48")
    version("6.1.2", sha256="829f4a2bd9fe3dee130dfcca103ddc7691da18382f5b683aaca8f3ceceaef355")
    version("6.1.1", sha256="e14a62678e97356236b45921e24f28ff430d670fb70456c3e5ebfeeb22160811")
    version("6.1.0", sha256="2ba44146397624845c64f3898bb1b08837ad7a49f133329e58eb04c05d1f36ac")
    version("6.0.2", sha256="13f393f8fdf25275994dda07091a93eec867233cd2f99f9cb0df16fbabd53483")
    version("6.0.0", sha256="7bb3f5011da9b1f3b79707b06118c523c1259215f650c2ffa5622a7e1d88868f")
    version("5.7.1", sha256="3e58c043a5a7d1357ee05725fd6cd41e190b070f1ba57f61300128429902089c")
    version("5.7.0", sha256="14f13554367d2d6490d66f8b5b739203225e7acce25085559e7c4acf29e2a4d5")

    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    conflicts("+asan", when="os=rhel9")
    conflicts("+asan", when="os=centos7")
    conflicts("+asan", when="os=centos8")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    patch("0005-Adding-half-include-directory-path-migraphx.patch", when="@5.7")
    patch("0006-add-option-to-turn-off-ck.patch", when="@5.7")
    patch(
        "https://github.com/ROCm/AMDMIGraphX/commit/728bea3489c97c9e1ddda0a0ae527ffd2d70cb97.patch?full_index=1",
        sha256="3a8afd32208aa4f59fb31f898d243287771ebd409c7af7a4a785c586081e3711",
        when="@6.0",
    )

    patch(
        "https://github.com/ROCm/AMDMIGraphX/commit/624f8ef549522f64fdddad7f49a2afe1890b0b79.patch?full_index=1",
        sha256="410d0fd49f5f65089cd4f540c530c85896708b4fd94c67d15c2c279158aea85d",
        when="@6.0",
    )
    patch("0003-add-half-include-directory-migraphx-6.0.patch", when="@6.0:")

    depends_on("cmake@3.5:", type="build")
    depends_on("protobuf", type="link")
    depends_on("protobuf", type=("build", "link"), when="@7.1:")
    depends_on("blaze", type="build")
    depends_on("nlohmann-json", type="link")
    depends_on("msgpack-c", type="link")
    depends_on("half@2:", when="@:6.2")
    depends_on("half")
    depends_on("python@3.5:", type="build")
    depends_on("py-pybind11@2.6:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("abseil-cpp")

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
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"rocblas@{ver}", when=f"@{ver}")
        depends_on(f"miopen-hip@{ver}", when=f"@{ver}")

    for ver in ["6.0.0", "6.0.2", "6.1.0", "6.1.1", "6.1.2", "6.2.0", "6.2.1", "6.2.4"]:
        depends_on(f"rocmlir@{ver}", when=f"@{ver}")

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
        depends_on(f"rocmlir@{ver}", when=f"@{ver}")
        depends_on(f"hipblas@{ver}", when=f"@{ver}")
        depends_on(f"hipblaslt@{ver}", when=f"@{ver}")

    @property
    def cmake_python_hints(self):
        """Include the python include path to the
        CMake based on current spec
        """
        return [self.define("Python_INCLUDE_DIR", self["python"].config_vars["include"])]

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
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def cmake_args(self):
        spec = self.spec
        abspath = spec["abseil-cpp"].prefix.include
        args = [
            self.define("CMAKE_CXX_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++"),
            self.define("NLOHMANN_JSON_INCLUDE", self.spec["nlohmann-json"].prefix.include),
            self.define("CMAKE_CXX_FLAGS", "-I{0}".format(abspath)),
            self.define("MIGRAPHX_ENABLE_PYTHON", "OFF"),
            self.define("BUILD_TESTING", self.run_tests),
        ]
        if self.spec["cmake"].satisfies("@3.16.0:"):
            args += self.cmake_python_hints
        if "@5.7:" in self.spec:
            args.append(self.define("MIGRAPHX_USE_COMPOSABLEKERNEL", "OFF"))
            args.append(
                self.define("GPU_TARGETS", "gfx906;gfx908;gfx90a;gfx1030;gfx1100;gfx1101;gfx1102")
            )
        if self.spec.satisfies("@6.1:") and self.spec.satisfies("+asan"):
            args.append(
                self.define(
                    "CMAKE_CXX_FLAGS", "-fsanitize=address -shared-libasan -I{0}".format(abspath)
                )
            )
        if self.spec.satisfies("@7.1:"):
            args.append(self.define("PROTOBUF_INCLUDE_DIR", self.spec["protobuf"].prefix.include))

        return args

    def test_unit_tests(self):
        """Run installed UnitTests"""
        unit_tests = which(self.prefix.bin.UnitTests)
        assert unit_tests is not None, "UnitTests is not installed!"
        unit_tests()
