# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Rocrand(CMakePackage):
    """The rocRAND project provides functions that generate
    pseudo-random and quasi-random numbers."""

    homepage = "https://github.com/ROCm/rocRAND"
    git = "https://github.com/ROCm/rocm-libraries.git"

    tags = ["rocm"]
    maintainers("cgmb", "srekolam", "renjithravindrankannath", "afzpatel")
    libraries = ["librocrand"]
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/rocRAND/archive/refs/tags/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-libraries/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.3", sha256="300cc50720d40bad7c7ed1f6d67e8c5ebecaba62c07a6ea1cc5813c0ea2e41b5")
    version("7.2.1", sha256="bc5140deec3b1c93c13796a8a6d2cb7e50aa87fd89f60f87c8d801d66f2fd156")
    version("7.2.0", sha256="8ad5f4a11f1ed8a7b927f2e65f24083ca6ce902a42021a66a815190a91ccb654")
    version("7.1.1", sha256="15c33c595aa8e4de1d8b3736df9eaf2ceba7914ffebe718f0997b0da28215d9e")
    version("7.1.0", sha256="616c2f61a4e05d8f07e4f95a26c1f031e66092cbf45354fe64c62becc9dcb751")
    version("7.0.2", sha256="ee0fee0ee7d3b59aafba8f9935c28c528363f941b42eea05045023c27e61938d")
    version("7.0.0", sha256="b8539339d1538d1aae69b7b77e62eee00c8586001b996f1c8af0c7579e85a9a6")
    version("6.4.3", sha256="6d174b679c1829e1740d8cb2a59bb43b7a34bd42e9234026860762ead90cccf9")
    version("6.4.2", sha256="43b370e7f4acb44a0eb4a403f658a3b3db2f748dbf5d9582014c20cb3ba8329c")
    version("6.4.1", sha256="690f8edc7789719876cf6119e58aa1335b4ca17b775a753dffb9a07000af9df7")
    version("6.4.0", sha256="689bc7de81741a0b3feb9f4415a55c2cf1ae58a378fbd9b1a33769caf62bbf95")
    version("6.3.3", sha256="d55be9d367af28d87d983d649329b7ef04641e74d39064b98aeee4b9980af4eb")
    version("6.3.2", sha256="57f364806369ddb80761ce44187920075cf446de527dd1fbc6adbb4b4b3e9bb8")
    version("6.3.1", sha256="80d86c31ec9cb40f5c5532281b42cf99fbc8a81e3ffd3bc8b3bbe4a7e509bf5f")
    version("6.3.0", sha256="396d2dc842c64d29f577365c348fbccd6260a11431eec61f233fdb0f38b7625d")
    version("6.2.4", sha256="94a2ea2413623b427ddf69365b3996c18721456965024c0dfac506a13c8dc547")
    version("6.2.1", sha256="ed07f638b5e30199251ddda6dd9ee53ee0ec49bcf37cc571a3de85c3a9833248")
    version("6.2.0", sha256="7f5318e9c9eb36fb3660392e97520268920c59af3a51af19633aabe5046ef1af")
    version("6.1.2", sha256="ac3c858c0f76188ac50574591aa6b41b27bda2af5925314451a44242319f28c8")
    version("6.1.1", sha256="d6302d014045694be85385cdc683ea75476e23fd92ae170079c261c0b041764b")
    version("6.1.0", sha256="ea80c5d657fa48b1122a47986239a04118977195ee4826d2b14b8bfe0fabce6e")
    version("6.0.2", sha256="51d66c645987cbfb593aaa6be94109e87fe4cb7e9c70309eb3c159af0de292d7")
    version("6.0.0", sha256="cee93231c088be524bb2cb0e6093ec47e62e61a55153486bebbc2ca5b3d49360")
    version("5.7.1", sha256="885cd905bbd23d02ba8f3f87d5c0b79bc44bd020ea9af190f3959cf5aa33d07d")
    version("5.7.0", sha256="d6053d986821e5cbc6cfec0778476efb1411ef943f11e7a8b973b1814a259dcf")

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
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.10.2:", type="build")

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
        "7.2.3",
    ]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}:", type="build", when=f"@{ver}")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.2:"):
            return "projects/rocrand"
        else:
            return "."

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CXX", self.spec["hip"].hipcc)
        if self.spec.satisfies("+asan"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            return "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        return None

    def cmake_args(self):
        args = [self.define("BUILD_BENCHMARK", "OFF"), self.define("BUILD_TEST", self.run_tests)]

        if "auto" not in self.spec.variants["amdgpu_target"]:
            if self.spec.satisfies("@7.1:"):
                args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
            else:
                args.append(self.define_from_variant("AMDGPU_TARGETS", "amdgpu_target"))

        if self.spec.satisfies("^cmake@3.21.0:3.21.2"):
            args.append(self.define("__skip_rocmclang", "ON"))
        if self.spec.satisfies("@:5.7"):
            args.append(self.define("BUILD_HIPRAND", "OFF"))

        return args
