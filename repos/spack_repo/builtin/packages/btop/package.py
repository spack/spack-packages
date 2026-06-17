# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems import cmake, makefile
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Btop(MakefilePackage, CMakePackage):
    """Resource monitor that shows usage and stats for processor,
    memory, disks, network and processes.
    """

    homepage = "https://github.com/aristocratos/btop#documents"
    url = "https://github.com/aristocratos/btop/archive/refs/tags/v1.2.13.tar.gz"

    maintainers("alalazo")

    license("Apache-2.0")

    version("1.4.7", sha256="933de2e4d1b2211a638be463eb6e8616891bfba73aef5d38060bd8319baeefc6")
    version("1.4.6", sha256="4beb90172c6acaac08c1b4a5112fb616772e214a7ef992bcbd461453295a58be")
    with default_args(deprecated=True):
        version("1.4.4", sha256="98d464041015c888c7b48de14ece5ebc6e410bc00ca7bb7c5a8010fe781f1dd8")
        version("1.4.3", sha256="81b133e59699a7fd89c5c54806e16452232f6452be9c14b3a634122e3ebed592")
        version("1.4.0", sha256="ac0d2371bf69d5136de7e9470c6fb286cbee2e16b4c7a6d2cd48a14796e86650")
        version("1.3.2", sha256="331d18488b1dc7f06cfa12cff909230816a24c57790ba3e8224b117e3f0ae03e")
        version("1.3.0", sha256="375e078ce2091969f0cd14030620bd1a94987451cf7a73859127a786006a32cf")
        version(
            "1.2.13", sha256="668dc4782432564c35ad0d32748f972248cc5c5448c9009faeb3445282920e02"
        )

    build_system("makefile", conditional("cmake", when="@1.3.0:"), default="cmake")

    variant("gpu", default=False, description="Enable GPU support", when="build_system=cmake")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.24:", type="build", when="@1.3.0: build_system=cmake")
    depends_on("cmake@3.25:", type="build", when="@1.4.1: build_system=cmake")
    depends_on("googletest@1.17:", type="test", when="@1.4.6: build_system=cmake")

    # Fix linking GPU support, by adding an explicit "target_link_libraries" to ${CMAKE_DL_LIBS}
    patch("link-dl.patch", when="+gpu @:1.4.0")
    # gcc does not define _GNU_SOURCE by default, making asprintf undeclared in the bundled
    # intel_gpu_top C code. See https://github.com/aristocratos/btop/issues/1565
    patch("gnu-source.patch", when="+gpu @1.3.0:")

    requires("%gcc@11:", "%clang@16:", policy="one_of", msg="C++ 20 is required")
    requires("%gcc@14:", "%clang@19:", policy="one_of", msg="C++ 23 is required", when="@1.4.6:")


class MakefileBuilder(makefile.MakefileBuilder):
    build_targets = ["STATIC=true", "VERBOSE=true"]

    @property
    def install_targets(self):
        return [f"PREFIX={self.prefix}", "install"]


class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
        return [
            self.define_from_variant("BTOP_GPU", "gpu"),
            self.define("BUILD_TESTING", self.pkg.run_tests),
        ]
