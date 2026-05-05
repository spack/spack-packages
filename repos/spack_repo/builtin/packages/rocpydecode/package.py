# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Rocpydecode(CMakePackage):
    """rocPyDecode is a set of Python bindings to rocDecode C++ library which provides
    full HW acceleration for video decoding on AMD GPUs."""

    homepage = "https://github.com/ROCm/rocPyDecode"
    url = "https://github.com/ROCm/rocPyDecode/archive/refs/tags/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")

    version("7.2.1", sha256="68736587beff68ab10e591b80c02804b104a16f54b0f3069a8a01e364171be35")
    version("7.2.0", sha256="e91a48734df8d4ce769b8979f2a1350a86705d38035c29618dff674471c9d026")
    version("7.1.1", sha256="8946730b6159350b896f9704b3ed485fa376e502d9b68f0cef68d09ab8260fab")
    version("7.1.0", sha256="7e9feeb0dd7d975f04364730cdf2b194d8e8d6bcc62aa983bc99509d9c6366d1")
    version("7.0.2", sha256="fa8215316966198086ff24c1ba7646e69d105b8bd1df1f90b829a6ca3b8f383e")
    version("7.0.0", sha256="f4245da75ba7bd27d3dbd39ecae89255e6d2b8c2096e579f812708f28b08716d")
    version("6.4.3", sha256="d9dc540ab8d6cfd979016abeab9cfc79063e81647a32d9eeffd834a9d008f1e3")
    version("6.4.2", sha256="d51f2dde62c6e581b0d3676fbd74b36802b4f97bbfc3f82baee76097affca685")
    version("6.4.1", sha256="2b74cb18d2f54664dbf1fa2063c7957e3c849fe6673e279d14aefe3712e187ff")
    version("6.4.0", sha256="c7fd47f98dc0ef005a0fda0dc73e71e1d5318901d038489ba69f51473b7aca6a")
    version("6.3.3", sha256="df45b4a64ed3e550229fd91bcf7896d1a8fe377dd1ff88d2e6a71897b981180d")
    version("6.3.2", sha256="c1b4dba9f8a28299279ad4e4aeb0c857c3a9772d016fcc0f164940f22faa6dee")
    version("6.3.1", sha256="77ed22ee23409b004676fb1a11b963324b878e786dae0a56fdef58375716c9eb")
    version("6.3.0", sha256="4d0d969fb32328d8277b5cc451ee875428f58c12c1d4b3ff33247774ecc6caf8")
    version("6.2.4", sha256="9cdb8bdc65b54b2c02d6c950dd34cd702ec50d903aa4d252d1eb1f8cae8c0afb")
    version("6.2.1", sha256="34c595cfe40ad74fcec2f52e7cc7be3ad8c8334030b0e98eb36305b6f63edc0d")
    version("6.2.0", sha256="e465254cd3e96bbb59208e90293d7c6b7744b0fbcd928ef278ec568c83e63ff3")

    depends_on("py-pybind11")
    depends_on("ffmpeg@4.4:6")
    depends_on("dlpack")

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
        depends_on(f"rocdecode@{ver}", when=f"@{ver}")
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")

    for ver in ["7.0.0", "7.0.2", "7.1.0", "7.1.1", "7.2.0", "7.2.1"]:
        depends_on(f"rocjpeg@{ver}", when=f"@{ver}")

    def patch(self):
        filter_file(
            r"${ROCM_PATH}/llvm/bin/clang++",
            "{0}/bin/clang++".format(self.spec["llvm-amdgpu"].prefix),
            "CMakeLists.txt",
            string=True,
        )
        filter_file(
            r"${ROCM_PATH}/lib/llvm/bin/clang++",
            "{0}/bin/clang++".format(self.spec["llvm-amdgpu"].prefix),
            "CMakeLists.txt",
            string=True,
        )
        filter_file(
            r"${ROCM_PATH}/share/rocdecode/utils",
            "{0}/share/rocdecode/utils".format(self.spec["rocdecode"].prefix),
            "CMakeLists.txt",
            string=True,
        )
        if self.spec.satisfies("@7.0:"):
            filter_file(
                r"${ROCM_PATH}/include/rocdecode",
                self.spec["rocdecode"].prefix.include.rocdecode,
                "CMakeLists.txt",
                string=True,
            )

    def cmake_args(self):
        args = [
            self.define("rocDecode_PATH", self.spec["rocdecode"].prefix),
            self.define("FFMPEG_INCLUDE_DIR", self.spec["ffmpeg"].prefix.include),
            self.define("CMAKE_INSTALL_PREFIX_PYTHON", self.spec.prefix),
            self.define(
                "CMAKE_CXX_FLAGS",
                "-DUSE_AVCODEC_GREATER_THAN_58_134 -I{0}".format(
                    self.spec["dlpack"].prefix.include
                ),
            ),
        ]
        if self.spec.satisfies("@6.4.0:"):
            args.append(
                self.define("CMAKE_C_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang")
            )
            args.append(
                self.define(
                    "CMAKE_CXX_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++"
                )
            )
        return args
