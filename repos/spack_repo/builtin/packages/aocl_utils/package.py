# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class AoclUtils(CMakePackage):
    """The library AOCL-Utils is intended to provide a uniform interface to all
    AOCL libraries to access CPU features, especially for AMD CPUs. The library
    provides the following features:
    * Core details
    * Flags available/usable
    * ISA available/usable
    * Topology about L1/L2/L3
    AOCL-Utils is designed to be integrated into other AMD AOCL libraries. Each
    project has their own mechanism to identify CPU and provide necessary
    features such as "dynamic dispatch".The main purpose of this library is to
    provide a centralized mechanism to update/validate and provide information
    to the users of this library.

    LICENSING INFORMATION: By downloading, installing and using this software,
    you agree to the terms and conditions of the AMD AOCL-Utils license
    agreement. You may obtain a copy of this license agreement from
    https://www.amd.com/content/dam/amd/en/documents/developer/version-4-2-eulas/utils-elua-4-2.pdf
    """

    _name = "aocl-utils"
    homepage = "https://www.amd.com/en/developer/aocl/utils.html"
    url = "https://github.com/amd/aocl-utils/archive/refs/tags/4.1.tar.gz"
    git = "https://github.com/amd/aocl-utils"

    maintainers("amd-toolchain-support")

    license("BSD-3-Clause")

    version("5.3", sha256="0e29afbbda3b81528380d2dbf7dae1ed6825d8c69e0abfcce53cc6cf90430e69")
    version("5.2", sha256="db0d807170a6eb73fcccd720a65a3e3aa8a787ae656c46479f7d9b4e1f9ed08a")
    version("5.1", sha256="68d75e04013abe90ea8308a9bc99b99532233b6c7f937f35381563f4124c20a5")
    version("5.0", sha256="ee2e5d47f33a3f673b3b6fcb88a7ef1a28648f407485ad07b6e9bf1b86159c59")
    version("4.2", sha256="1294cdf275de44d3a22fea6fc4cd5bf66260d0a19abb2e488b898aaf632486bd")
    version("4.1", sha256="660746e7770dd195059ec25e124759b126ee9f060f43302d13354560ca76c02c")

    variant("doc", default=False, description="enable documentation")
    variant("tests", default=False, description="enable testing")
    variant("shared", default=True, when="@4.2:", description="build shared library")
    variant("examples", default=False, description="enable examples")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.22:", when="@:5.0", type="build")
    depends_on("cmake@3.26:", when="@5.1:", type="build")
    depends_on("doxygen", when="+doc")

    @property
    def libs(self):
        """find aocl-utils libs function"""
        shared = "+shared" in self.spec
        return find_libraries("libaoclutils", root=self.prefix, recursive=True, shared=shared)

    def cmake_args(self):
        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
        ]

        if self.spec.satisfies("@5.0:"):
            args.extend(
                [
                    self.define_from_variant("AU_BUILD_DOCS", "doc"),
                    self.define_from_variant("AU_BUILD_TESTS", "tests"),
                    self.define_from_variant("AU_BUILD_EXAMPLES", "examples"),
                ]
            )
        else:
            args.extend(
                [
                    self.define_from_variant("ALCI_DOCS", "doc"),
                    self.define_from_variant("ALCI_TESTS", "tests"),
                    self.define_from_variant("ALCI_EXAMPLES", "examples"),
                ]
            )

        return args
