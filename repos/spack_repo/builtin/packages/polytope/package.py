# Copyright Spack Project Developers. See COPYRIGHT file for details.

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Polytope(CMakePackage, CudaPackage, ROCmPackage):
    """C++ library for generating polygonal and polyhedral meshes"""

    homepage = "https://github.com/llnl/polytope"
    url = "https://github.com/llnl/polytope/archive/refs/tags/v0.7.5.tar.gz"
    git = "https://github.com/llnl/polytope.git"

    maintainers("jmikeowen", "ldowen")
    license("BSD-2-Clause")

    version("master", branch="master", submodules=True)
    version("0.7.5", sha256="ee249cfbb38632a704d177bb3269124ab7b227d29a6c36c9857e822cf4df0430")
    version("0.7.4", sha256="a1901b0feaf3c4d3660766e8a6c325c0fe1fcaeb236b5ae95c8d139c386147c8")
    version("0.7.3", sha256="f32817b44d2a3b98407531980b89d0a31b0c14b8b30de37a6a7bc6ec91e48bf1")
    version("0.7.2", sha256="94a42ac30226da28ec07ad06b745101235c6aa45e8e8e1d218c8e991837b6867")
    version("0.7.1", sha256="83b12db2a2dc419488e986e40f32b085824ca0345f2958a48e66547f2e4f60fa")
    version("0.7.0", sha256="e7be5a5d06a95309b9100f02ab80c2f3401c11ac6304a3204fb1f25052efd77e")
    version("0.6.2", sha256="e9ed18c3ebc7b4b231a0563235cc032c26daa7de88839c64141975170e55bcfd")
    version("0.6.1", sha256="f4f35e327d788305f7f7b95f90eda928f6632c58fc1a272bc5d208e54ba2a27f")
    version("0.6.0", sha256="25b10759d784de2f2ea0b93200194b69319079b68c73785d1aaa397cacce2eea")
    version("0.5.24", sha256="ff45624cfc522d62f21c69ac8aa90477bf00d6ee472f4e0a07b508702304fa57")

    variant("shared", default=False, description="Enable share lib build")
    variant("boost", default=False, description="Enable Boost support")

    with default_args(type="build"):
        depends_on("cmake@3.1.0:")
        depends_on("c")
        depends_on("cxx")

    depends_on("boost", when="+boost")

    def url_for_version(self, version):
        if version >= Version("1.7.5"):
            url = "https://github.com/llnl/polytope/archive/refs/tags/v{0}.tar.gz"
        else:
            url = "https://github.com/llnl/polytope/archive/refs/tags/{0}.tar.gz"
        return url.format(version)

    def cmake_args(self):
        args = [
            self.define("TESTING", "OFF"),
            self.define("ENABLE_MPI", "OFF"),  # MPI support is currently broken
            self.define_from_variant("USE_BOOST", "boost"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
        ]
        return args
