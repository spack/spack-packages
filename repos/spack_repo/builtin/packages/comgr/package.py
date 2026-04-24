# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Comgr(CMakePackage):
    """This provides various Lightning Compiler related services. It currently
    contains one library, the Code Object Manager (Comgr)"""

    homepage = "https://github.com/ROCm/llvm-project"
    git = "https://github.com/ROCm/llvm-project.git"

    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "haampie", "afzpatel")
    libraries = ["libamd_comgr"]
    license("NCSA")

    def url_for_version(self, version):
        if version <= Version("6.0.2"):
            url = "https://github.com/ROCm/ROCm-CompilerSupport/archive/rocm-{0}.tar.gz"
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
    version("6.0.2", sha256="737b110d9402509db200ee413fb139a78369cf517453395b96bda52d0aa362b9")
    version("6.0.0", sha256="04353d27a512642a5e5339532a39d0aabe44e0964985de37b150a2550385800a")
    version("5.7.1", sha256="3b9433b4a0527167c3e9dfc37a3c54e0550744b8d4a8e1be298c8d4bcedfee7c")
    version("5.7.0", sha256="e234bcb93d602377cfaaacb59aeac5796edcd842a618162867b7e670c3a2c42c")

    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.13.4:", type="build")

    depends_on("zlib-api", type="link")
    depends_on("z3", type="link")
    depends_on("ncurses", type="link")

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
        # llvm libs are linked statically, so this *could* be a build dep
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}", when=f"@{ver}", type="build")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@:6.0"):
            return join_path("lib", "comgr")
        else:
            return join_path("amd", "comgr")

    def cmake_args(self):
        args = [
            self.define("BUILD_TESTING", self.run_tests),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]
        if self.spec.satisfies("@5.7:"):
            args.append(self.define_from_variant("ADDRESS_SANITIZER", "asan"))
        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("CMAKE_MODULE_PATH", self.spec["llvm-amdgpu"].prefix.lib.cmake.clang)
        if self.spec.satisfies("@5.7: +asan"):
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
            ver = "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        else:
            ver = None
        return ver
