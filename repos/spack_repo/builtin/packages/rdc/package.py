# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import re

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Rdc(CMakePackage):
    """ROCm Data Center Tool"""

    homepage = "https://github.com/ROCm/rdc"
    git = "https://github.com/ROCm/rocm-systems.git"

    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    libraries = ["librdc"]
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/rdc/archive/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-systems/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.1", sha256="201f19174eafbace2f7abf0d1178ebb17db878191276aba6d23f0e1758b0e10f")
    version("7.2.0", sha256="728ea7e9bf16e6ed217a0fd1a8c9afaba2dae2e7908fa4e27201e67c803c5638")
    version("7.1.1", sha256="d16c63fe6609d82d0fcd65e9953f60318d015275b8752d052a6ae20cd634c3e1")
    version("7.1.0", sha256="a77b6ad33dc41917f6b0ed2a26085b96fc7222cf507adb9b90d2eb7976fae5a5")
    version("7.0.2", sha256="1184ef89435063a1d63d6c2d8b6d4f99bb6d5f4d65c241c405b6e550fe285a08")
    version("7.0.0", sha256="2045ed1c57019edc6dd468f7dc092426e4587a413da6ecbff5ccdf45f9a19a0f")
    version("6.4.3", sha256="1a4ba522b780375c8a8b24ceba34d5021d2255dc09fa7f841ae0249eeb96dea1")
    version("6.4.2", sha256="56dcbdf3a0b4e330d7952e790cd6e7bca5fde351189d2f99026c1e4c8ac2fc63")
    version("6.4.1", sha256="8b6d58c6ce30497a9d6b465057a8a39be9e9e4603b75a52b5004335f12310024")
    version("6.4.0", sha256="2ee3def1e90784923f2043220974d30fe9581ec0d54c93628911ed8292fc56c4")
    version("6.3.3", sha256="9be314ea8d7e7af58ac4a24f5720f54d51ba553d3e1751bc9cfc4bff98494fab")
    version("6.3.2", sha256="e0780b8ef46d7b9885eb06a0b9eb56924fdf090ade71a66360a0bee1d9d7295d")
    version("6.3.1", sha256="88a96f13c0010a7f9e63f7a5a5531ae1d57ef1a722bac232c8544cde6245e120")
    version("6.3.0", sha256="419afd9c8e50a872fb0a922e29c8578664ed88e0b79bf558db0a1e864aa8fecf")
    version("6.2.4", sha256="cdebbc0c1a49f067fb8ff17bd91cd92f6f83b2aee142e5b576e5eb1742983a7f")
    version("6.2.1", sha256="63c0cffd772a43d0984505646023485ca2bc8512f5a87ece016f1d381cded075")
    version("6.2.0", sha256="dd12428426a4963d6eb3cfdd818acef7a3c4cddf32504df17f4c1004fa902bef")
    version("6.1.2", sha256="5553b76d4c8b6381d236197613720587377d03d4fd43a5a20bb6a716d49f7dfc")
    version("6.1.1", sha256="c133ebd20bf42e543d13c5b84ea420a7f7c069c77b1d6dcae9680de924e5f539")
    version("6.1.0", sha256="a8ad5d880645c9e95c9c90b0c9026627b22467e3e879525fff38ccd924f36c39")
    version("6.0.2", sha256="00defa3b68c340d7f46b8cb06b37ab0602a7949bfddc884b01c163a1526502f8")
    version("6.0.0", sha256="5e3847a919d5f7efe99d8d76c96e78401659eccd1fb234b1b8cb4304096d6e89")
    version("5.7.1", sha256="5251eb3085f2019246b332e9552dfae1572cf64ddf58306b81cbe7108019ffee")
    version("5.7.0", sha256="924e94f14f6390d7a6ff7863fb4e2085c1ff5f9c12b8bd46471eb31f001c4f14")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3.15:", type="build")
    depends_on("grpc@1.55.0+shared", when="@:6.0")
    depends_on("grpc@1.59.1+shared", when="@6.1")
    depends_on("grpc@1.61.2+shared", when="@6.2:6.4")
    depends_on("grpc@1.67.1 cxxstd=17 +shared", when="@7.0:")
    depends_on("protobuf")
    depends_on("libcap")
    for ver in ["5.7.0", "5.7.1", "6.0.0", "6.0.2", "6.1.0", "6.1.1", "6.1.2"]:
        depends_on(f"rocm-smi-lib@{ver}", type=("build", "link"), when=f"@{ver}")

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
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")

    for ver in [
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
        depends_on(f"amdsmi@{ver}", when=f"@{ver}")

    for ver in [
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
        depends_on(f"rocm-validation-suite@{ver}", when=f"@{ver}")

    def patch(self):
        if self.spec.satisfies("@:6.1"):
            filter_file(r"\${ROCM_DIR}/rocm_smi", "${ROCM_SMI_DIR}", "CMakeLists.txt")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@:7.1"):
            return "."
        else:
            return "projects/rdc"

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            return "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        return None

    def cmake_args(self):
        args = [self.define("GRPC_ROOT", self.spec["grpc"].prefix)]
        if self.spec.satisfies("@:6.1"):
            args.append(self.define("ROCM_SMI_DIR", self.spec["rocm-smi-lib"].prefix))
        if self.spec.satisfies("@:7.1"):
            args.append(
                self.define("CMAKE_MODULE_PATH", f"{self.stage.source_path}/cmake_modules")
            )
        return args
