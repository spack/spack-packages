# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RocmDeviceLibs(CMakePackage):
    """set of AMD specific device-side language runtime libraries"""

    homepage = "https://github.com/ROCm/llvm-project"
    git = "https://github.com/ROCm/llvm-project.git"

    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "haampie", "afzpatel")

    def url_for_version(self, version):
        if version <= Version("6.0.2"):
            url = "https://github.com/ROCm/ROCm-Device-Libs/archive/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/llvm-project/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.1", sha256="4d3449d758e3f79b336248b0207a394eda04ba5cdd48a4088e135ddf769127fa")
    version("7.2.0", sha256="e86138d2a63fbcbdf64668d55573b26ae944d0f0ae5a3f5bb59bf7bdb3124d3f")
    version("7.1.1", sha256="d76a16db4a56914383029e241823f7bc2a3d645f2967dd22230f11c11cfe189e")
    version("7.1.0", sha256="87f5532b8b653bd18541cdf6e59923cbd340b300d8ec5046d3e4288d9e5195c0")
    version("7.0.2", sha256="fd612fa750bebd0c3be0ea642b2cae8ff5c7e00a2280b22b9ea16ee86a11d763")
    version("7.0.0", sha256="3d479a2aa615b6bb35cd3521122fbff34188dc0cc52d8b0acda59f9f55198211")
    version("6.4.3", sha256="7a484b621d568eef000ee8c4d2d46d589e5682b950f1f410ce7215031f1f3ad7")
    version("6.4.2", sha256="9f42cb73d90bd4561686c0366f60f6e58cfd32ff24b094c69e8259fb5d177457")
    version("6.4.1", sha256="460ad28677092b9eb86ffdc49bcb4d01035e32b4f05161d85f90c9fa80239f50")
    version("6.4.0", sha256="dca1c145a23f05229d5d646241f9d1d3c5dbf1d745b338ae020eabe33beb965c")
    version("6.3.3", sha256="4df9aba24e574edf23844c0d2d9dda112811db5c2b08c9428604a21b819eb23d")
    version("6.3.2", sha256="1f52e45660ea508d3fe717a9903fe27020cee96de95a3541434838e0193a4827")
    version("6.3.1", sha256="e9c2481cccacdea72c1f8d3970956c447cec47e18dfb9712cbbba76a2820552c")
    version("6.3.0", sha256="79580508b039ca6c50dfdfd7c4f6fbcf489fe1931037ca51324818851eea0c1c")
    version("6.2.4", sha256="7af782bf5835fcd0928047dbf558f5000e7f0207ca39cf04570969343e789528")
    version("6.2.1", sha256="4840f109d8f267c28597e936c869c358de56b8ad6c3ed4881387cf531846e5a7")
    version("6.2.0", sha256="12ce17dc920ec6dac0c5484159b3eec00276e4a5b301ab1250488db3b2852200")
    version("6.1.2", sha256="300e9d6a137dcd91b18d5809a316fddb615e0e7f982dc7ef1bb56876dff6e097")
    version("6.1.1", sha256="f1a67efb49f76a9b262e9735d3f75ad21e3bd6a05338c9b15c01e6c625c4460d")
    version("6.1.0", sha256="6bd9912441de6caf6b26d1323e1c899ecd14ff2431874a2f5883d3bc5212db34")
    version("6.0.2", sha256="c6d88b9b46e39d5d21bd5a0c1eba887ec473a370b1ed0cebd1d2e910eedc5837")
    version("6.0.0", sha256="198df4550d4560537ba60ac7af9bde31d59779c8ec5d6309627f77a43ab6ef6f")
    version("5.7.1", sha256="703de8403c0bd0d80f37c970a698f10f148daf144d34f982e4484d04f7c7bbef")
    version("5.7.0", sha256="0f8780b9098573f1c456bdc84358de924dcf00604330770a383983e1775bf61e")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.13.4:", type="build")

    depends_on("zlib-api", type="link")
    depends_on("texinfo", type="link")

    depends_on("rocm-cmake@3.5.0:", type="build")

    # Make sure llvm is not built with rocm-device-libs (that is, it's already
    # built with rocm-device-libs as an external project).
    depends_on("llvm-amdgpu ~rocm-device-libs")

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
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@:6.0"):
            return "."
        else:
            return join_path("amd", "device-libs")

    def cmake_args(self):
        spec = self.spec
        return [
            self.define("LLVM_DIR", spec["llvm-amdgpu"].prefix),
            self.define("CMAKE_C_COMPILER", spec["llvm-amdgpu"].prefix.bin.clang),
        ]
