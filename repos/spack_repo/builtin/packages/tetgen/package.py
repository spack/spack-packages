# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import glob
import os

from spack_repo.builtin.build_systems import makefile, cmake

from spack.package import *

class Tetgen(makefile.MakefilePackage, cmake.CMakePackage):
    """TetGen is a program and library that can be used to generate
    tetrahedral meshes for given 3D polyhedral domains. TetGen
    generates exact constrained Delaunay tetrahedralizations,
    boundary conforming Delaunay meshes, and Voronoi paritions.
    """

    homepage = "https://wias-berlin.de/software/tetgen/"

    license("AGPL-3.0-only")

    version(
        "1.6.0",
        sha256="87b5e61ebd3a471fc4f2cdd7124c2b11dd6639f4feb1f941a5d2f5110d05ce39",
        url="http://www.tetgen.org/1.5/src/tetgen1.6.0.tar.gz",
    )
    version(
        "1.5.1",
        sha256="e46a4434a3e7c00044c8f4f167e18b6f4a85be7d22838c8f948ce8cc8c01b850",
        url="http://www.tetgen.org/1.5/src/tetgen1.5.1.tar.gz",
        preferred=True,
    )
    version(
        "1.5.0",
        sha256="4d114861d5ef2063afd06ef38885ec46822e90e7b4ea38c864f76493451f9cf3",
        url="http://www.tetgen.org/1.5/src/tetgen1.5.0.tar.gz",
    )
    version(
        "1.4.3",
        sha256="952711bb06b7f64fd855eb24c33f08e3faf40bdd54764de10bbe5ed5b0dce034",
        url="http://www.tetgen.org/files/tetgen1.4.3.tar.gz",
    )

    build_system("makefile", "cmake", default="makefile")

    with when("build_system=makefile"):
      variant("debug", default=False, description="Builds the library in debug mode.")

      depends_on("gmake", type="build")

    with when("build_system=cmake"):
      variant("build_type", default="Release",
          description="CMake build type",
          values=("Debug", "Release", "RelWithDebInfo", "MinSizeRel"))
      variant("shared", default=True, description="Enables the build of shared libraries.")

    variant("pic", default=True, description="Builds the library in pic mode.")
    variant(
        "except",
        default=False,
        description="Replaces asserts with exceptions for better C++ compatibility.",
        when="@:1.5.0",
    )

    patch("tetgen-1.5.0-free.patch", when="@1.5.0")

    depends_on("cxx", type="build")

    def patch(self):
      if "+except" in self.spec:
          hff = FileFilter("tetgen.h")
          hff.filter(r"(\b)(throw)(\b)(.*);", r"\1assert_throw(false);")
          hff.filter(
              r"^(#define\s*tetgenH\s*)$",
              r"\1{0}".format(
                  """\n
#include <stdexcept>

inline void assert_throw(bool assertion)
{
  if(!assertion)
    throw std::runtime_error("Tetgen encountered a problem (assert failed)!");
}\n"""
                ),
            )

      sff = FileFilter(*(glob.glob("*.cxx")))
      sff.filter(r"(\b)(assert)(\b)", r"\1assert_throw\3")

class MakefileBuilder(makefile.MakefileBuilder):
    def build(self, pkg, spec, prefix):
      make("tetgen", "tetlib")

    def install(self, pkg, spec, prefix):
      mkdirp(prefix.bin)
      install("tetgen", prefix.bin)

      mkdirp(prefix.include)
      install("tetgen.h", prefix.include)

      mkdirp(prefix.lib)
      install("libtet.a", prefix.lib)
  
class CMakeBuilder(cmake.CMakeBuilder):
    def cmake_args(self):
      args = [
          self.pkg.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
          self. pkg.define_from_variant("BUILD_SHARED_LIBS", "shared"),
      ]

      return args

    @run_before("cmake")
    def run_before_cmake_is_invoked(self) -> None:
      print("self is", dir(self))
      with open(join_path(os.path.dirname(__file__), "CMakeLists.txt.in"), 'r') as file:
        cmakelists_content = file.read()

      cmakelists_content = cmakelists_content.replace("%VERSION%", str(self.pkg.version))

      with open("CMakeLists.txt", "w") as file:
        file.write(cmakelists_content)

      copy(join_path(os.path.dirname(__file__), "tetgen-config.cmake.in"), "tetgen-config.cmake.in")
