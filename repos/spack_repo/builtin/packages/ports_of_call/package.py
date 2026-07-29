# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class PortsOfCall(CMakePackage):
    """Ports of Call: Performance Portability Utilities"""

    homepage = "https://github.com/lanl/ports-of-call"
    url = "https://github.com/lanl/ports-of-call/archive/refs/tags/v3.0.0.tar.gz"
    git = "https://github.com/lanl/ports-of-call.git"

    maintainers("rbberger", "Yurlungur")

    license("BSD-3-Clause")

    version("main", branch="main")
    version("3.0.0", commit="8af8ca7c4f5c720ef3e814423d02d59d2f0f9f37", tag="v3.0.0")
    version("2.1.0", commit="4caf262ca5d0b4ba7fbca86fd6f67532388309d9", tag="v2.1.0")
    version("2.0.1", commit="a284b6b2d42e70afeb99babb23522c869200d6ea", tag="v2.0.1")
    version("2.0.0", commit="3349de8995868ec4c6125acdb5aefa4fa9a999c5", tag="v2.0.0")
    version("1.7.1", commit="0b1e73b93799cc635ac1c3f8c54f3d9d09f17221", tag="v1.7.1")
    version("1.7.0", commit="7841f2b311dc6d23acb41f27e7570e96a3e6da08", tag="v1.7.0")
    version("1.6.0", commit="58ce1181b2d835bd32673ad70550c9130381f91b", tag="v1.6.0")
    version("1.5.2", commit="5f83ece2b203efb3737cf7c89f3daa29c2642765", tag="v1.5.2")
    version("1.5.1", commit="caf672277b47f0aea15e77fffae8548c6e521ae4", tag="v1.5.1")
    version("1.4.1", commit="603e5cdf87f0760d6ee90843d304a427d9617ba4", tag="v1.4.1")
    version("1.4.0", commit="b2b2a0af10ba9b9d76e50dd02eda06199cee958c", tag="v1.4.0")
    version("1.3.0", commit="4c3d3f7534f6c3d0d303286c936f89b75dbba005", tag="v1.3.0")

    variant("test", default=False, description="Build tests")
    variant(
        "test_portability_strategy",
        description="Portability strategy used by tests",
        values=("Kokkos", "Cuda", "None"),
        multi=False,
        default="None",
        when="@1.7.0: +test",
    )

    depends_on("c", type="build", when="@:1.7.1")
    depends_on("cxx", type="build")

    depends_on("cmake@3.12:", type="build")
    depends_on("catch2@3.0.1:", when="+test", type=("build", "test"))
    depends_on("kokkos", when="+test test_portability_strategy=Kokkos", type=("build", "test"))

    def cmake_args(self):
        args = [
            self.define_from_variant("PORTS_OF_CALL_BUILD_TESTING", "test"),
            self.define_from_variant(
                "PORTS_OF_CALL_TEST_PORTABILITY_STRATEGY", "test_portability_strategy"
            ),
        ]
        if self.spec.satisfies("test_portability_strategy=Kokkos ^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
            args.append(self.define("CMAKE_C_COMPILER", self.spec["hip"].hipcc))
        if self.spec.satisfies("test_portability_strategy=Kokkos ^kokkos+cuda"):
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))
        return args
