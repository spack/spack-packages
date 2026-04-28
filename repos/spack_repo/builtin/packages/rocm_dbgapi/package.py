# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RocmDbgapi(CMakePackage):
    """The AMD Debugger API is a library that provides all the support
    necessary for a debugger and other tools to perform low level
    control of the execution and inspection of execution state of
    AMD's commercially available GPU architectures."""

    homepage = "https://github.com/ROCm/ROCdbgapi"
    git = "https://github.com/ROCm/ROCdbgapi.git"
    url = "https://github.com/ROCm/ROCdbgapi/archive/rocm-6.2.1.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    libraries = ["librocm-dbgapi"]

    license("MIT")

    version("7.2.1", sha256="29a5f689e03c176ec562634fb22192309fab538fe4245225a66b25ad6de0fab1")
    version("7.2.0", sha256="3649f1ae9642cdc7f3b172a580388cbe50489dfbea6b245a6a73082a64e06c5b")
    version("7.1.1", sha256="4c31da40e6da3c81fea8a8b0757daae3d6e95dc86ba32ff55484e7044aaa094f")
    version("7.1.0", sha256="334a5bc39f5d1b3e7fe415206f499985156a0f76556b2f91789f528ccbc3e9a2")
    version("7.0.2", sha256="01e154aa8b954beecb420674bc372d6ffe5b252ea393494383a0aad1c928675d")
    version("7.0.0", sha256="f8df0b52e1cd959d2343bbc1eceb18c75d6522e37c125bbf27f89650e55573ff")
    version("6.4.3", sha256="3f0df9d1f350cd6d88ddd41c2e574e4f385c109fcc1524b1de3bd69fce05f5b6")
    version("6.4.2", sha256="fc62c2eb139db9ef454efaf5c18def6736f366c0a1677e8024aac622a5bae8b0")
    version("6.4.1", sha256="c4c16510b691506c3d0e17d6b2f1eb93529e99dee7877c44fa955a8083337463")
    version("6.4.0", sha256="5dcf627245cc9511c7ff22f46410c5e5777187fab97b7cfcd95e03e61069f72c")
    version("6.3.3", sha256="25c8e9f4a22f23004f2fc1998c284095b193591eb6143b47380455754948ab98")
    version("6.3.2", sha256="0e7cea6ae2eb737ad378787d2ef5f6cbaf9dfb483bb5e61e716601a145677adf")
    version("6.3.1", sha256="1843423c91a22cf83bef5f14cb50f55ba333047e03e75296b9f9522facde5822")
    version("6.3.0", sha256="c46ca562fbbac8673c22ee5c92d62ddf6c7dfd7faceeb66d3876cde6beda8872")
    version("6.2.4", sha256="004e9ace3ead840e44f98fc033b621d5489a554965deecfdb7df768482068282")
    version("6.2.1", sha256="40064ca031e41ff3c87bfa31406b7192fa65709ab36734eddad87e0ecc01bb80")
    version("6.2.0", sha256="311811ce0970ee83206791c21d539f351ddeac56ce3ff7efbefc830038748c0c")
    version("6.1.2", sha256="6e55839e3d95c2cfe3ff89e3e31da77aeecc74012a17f5308589e8808df78026")
    version("6.1.1", sha256="425a6cf6a3942c2854c1f5e7717bed906cf6c3753b46c44476f54bfef6188dac")
    version("6.1.0", sha256="0985405b6fd44667a7ce8914aa39a7e651613e037e649fbdbfa2adcf744a2d50")
    version("6.0.2", sha256="39036f083de421f46afd8d3a8799576242ef64002643d7185767ccbba41ae854")
    version("6.0.0", sha256="4e823eba255e46b93aff05fd5938ef2a51693ffd74debebffc1aabfce613805c")
    version("5.7.1", sha256="0ee9c2f083868849f2ea0cec7010e0270c27e7679ccbbadd12072cc0ef6c8a6f")
    version("5.7.0", sha256="285ddded8e7f1981d8861ffc1cd7770b78129e4955da08ad55a4779945699716")

    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    conflicts("+asan", when="os=rhel9")
    conflicts("+asan", when="os=centos7")
    conflicts("+asan", when="os=centos8")

    depends_on("cxx", type="build")  # generated
    depends_on("c", type="build")

    depends_on("cmake@3:", type="build")
    depends_on("hwdata", type="build")
    depends_on("pciutils", type="build")

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
        depends_on(f"hsa-rocr-dev@{ver}", type="build", when=f"@{ver}")
        depends_on(f"comgr@{ver}", type=("build", "link"), when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            return "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        return None

    def patch(self):
        filter_file(
            r"(<INSTALL_INTERFACE:include>)",
            r"\1 {0}/include".format(self.spec["hsa-rocr-dev"].prefix),
            "CMakeLists.txt",
        )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+asan"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def cmake_args(self):
        args = [
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            self.define("PCI_IDS_PATH", self.spec["pciutils"].prefix.share),
        ]
        return args
