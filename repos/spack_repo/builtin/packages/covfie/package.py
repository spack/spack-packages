# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Covfie(CMakePackage, CudaPackage, ROCmPackage):
    """Covfie is a library for compositional descriptions of storage methods for
    vector fields and other structured multi-dimensional data."""

    homepage = "https://github.com/acts-project/covfie"
    url = "https://github.com/acts-project/covfie/archive/refs/tags/v0.13.0.tar.gz"
    git = "https://github.com/acts-project/covfie.git"
    list_url = "https://github.com/acts-project/covfie/tags"

    maintainers("stephenswat", "sethrj")

    license("MPL-2.0")

    version("main", branch="main")
    version("0.15.6", sha256="ed22408f981692398408ffe04ff8e6230c022288552a83dbc2ad34b96003a84e")
    version("0.15.5", sha256="1b2b34e3a968f24a2c1adb495bff5b8f943c0f72c729c199d8881cb4d0fc2dc0")
    version("0.15.4", sha256="9a69f57c4a48acefedc7e8bc2cb38f688584a0535d79bb7eab9c0cc5c8c7290c")
    version("0.15.3", sha256="72da1147c44731caf9163f3931de78d7605a44f056f22a2f6ea024ad02a1ba71")
    version("0.15.2", sha256="6eff65e05118d3007c689e3529a62bb1674348ac1b0f0f32afd953c62d1b8890")
    version("0.15.1", sha256="809f1207ee9c96c6065fc9da796abfe9bdeab1bb987526da787f26b1d628ce7a")
    version("0.15.0", sha256="16a0e781ae5c38585573316813f57562752734639c8c24193f37a8588e120bd7")
    version("0.14.0", sha256="b4d8afa712c6fc0e2bc6474367d65fad652864b18d0255c5f2c18fd4c6943993")
    version("0.13.0", sha256="e9cd0546c7bc9539f440273bbad303c97215ccd87403cedb4aa387a313938d57")
    version("0.12.1", sha256="c33d7707ee30ab5fa8df686a780600343760701023ac0b23355627e1f2f044de")
    version("0.12.0", sha256="e35e94075a40e89c4691ff373e3061577295d583a2546c682b2d652d9fce7828")
    version("0.11.0", sha256="39fcd0f218d3b4f3aacc6af497a8cda8767511efae7a72b47781f10fd4340f4f")
    version("0.10.0", sha256="d44142b302ffc193ad2229f1d2cc6d8d720dd9da8c37989ada4f23018f86c964")

    depends_on("c", type="build", when="@:0.13")
    depends_on("cxx", type="build")

    depends_on("cmake@3.21:", type="build", when="@0.11:")
    depends_on("cmake@3.18:", type="build")

    # requirements for examples
    depends_on("boost@1.71: +log +program_options", type="test")

    def cmake_args(self):
        args = [
            self.define("COVFIE_PLATFORM_CPU", True),
            self.define_from_variant("COVFIE_PLATFORM_CUDA", "cuda"),
            self.define_from_variant("COVFIE_PLATFORM_HIP", "rocm"),
            self.define("COVFIE_QUIET", True),
            self.define("COVFIE_BUILD_EXAMPLES", self.run_tests),
            self.define("COVFIE_BUILD_TESTS", self.run_tests),
        ]

        return args
