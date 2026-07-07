# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsBuilder, AutotoolsPackage
from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage

from spack.package import *


class Dssp(CMakePackage, AutotoolsPackage):
    """'mkdssp' utility. (dictionary of protein secondary structure)"""

    homepage = "https://pdb-redo.eu/dssp"
    url = "https://github.com/PDB-REDO/dssp/archive/refs/tags/v4.5.8.tar.gz"

    license("GPL-3.0-or-later", when="@2.3.0:3.1.4")
    license("BSD-2-Clause", when="@4:")

    build_system(
        conditional("autotools", when="@:3.1.4"), conditional("cmake", when="@4:"), default="cmake"
    )

    version("4.6.1", sha256="5ddb8274f03ac0338adffcd661989f515fffb95d40afca404cf2677024256ae3")
    version("4.5.8", sha256="634bf8d8dd96954bd680da90f3dcb66b87189c13b12b52b61de8af9d597b74ac")
    version(
        "3.1.4",
        sha256="496282b4b5defc55d111190ab9f1b615a9574a2f090e7cf5444521c747b272d4",
        url="https://github.com/cmbi/dssp/archive/refs/tags/2.3.0.tar.gz",
    )
    version(
        "2.3.0",
        sha256="4c95976d86dc64949cb0807fbd58c7bee5393df0001999405863dc90f05846c6",
        url="https://github.com/cmbi/dssp/archive/refs/tags/3.1.4.tar.gz",
    )

    # pdb data download.
    # 1ALK.pdb - PDB (protein data bank) : https://www.rcsb.org/
    resource(
        name="pdb_data",
        url="https://files.rcsb.org/download/1ALK.pdb",
        sha256="99f4cd7ab63b35d64eacc85dc1491af5a03a1a0a89f2c9aadfb705c591b4b6c9",
        expand=False,
        placement="pdb",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated

    with when("build_system=autotools"):
        depends_on("autoconf", type="build")
        depends_on("automake", type="build")
        depends_on("libtool", type="build")
        depends_on("m4", type="build")
    depends_on(
        "boost@1.48:1.84+date_time+system+filesystem+iostreams+program_options+thread+test\
                cxxstd=11",
        when="@:3.1.4",
    )

    # header only library (at this time)
    depends_on("libmcfp@1.4.2", type="build", when="@4.5.8:")
    depends_on("libcifpp@9.0.6", when="@4.5.8")
    depends_on("libcifpp@10.0.3", when="@4.6.1")
    depends_on("fmt", when="@4.5.8 %gcc@:12")
    depends_on("sqlite@3:", when="@4.6:")

    extends("python", when="+python")
    depends_on("boost@1.86:+python", when="+python")
    with when("@4.6.1:"):
        conflicts("%gcc@:12", msg="Requires gcc@13:")
        conflicts("%clang@:13", msg="Requires llvm@14:")

    variant("python", default=False, description="build python module", when="@4:")

    def patch(self):
        # <format> unavailable until gcc13
        if self.spec.satisfies("@4.5.8 %gcc@:12"):
            # do evil things
            filter_file(
                "#include <format>",
                "#include <fmt/format.h>",
                join_path("libdssp", "src", "dssp-io.cpp"),
                string=True,
            )
            filter_file(
                "std::format",
                "fmt::format",
                join_path("libdssp", "src", "dssp-io.cpp"),
                string=True,
            )
            filter_file(r"(find_package\(Threads\))", "\\1\nfind_package(fmt)", "CMakeLists.txt")
            filter_file(
                r"(target_link_libraries\(mkdssp .*dssp::dssp)\)",
                r"\1 fmt::fmt)",
                "CMakeLists.txt",
            )

    @run_after("install")
    def cache_test_sources(self):
        """Save off the pdb sources for stand-alone testing."""
        cache_extra_test_sources(self, "pdb")

    def test_mkdssp(self):
        """calculate structure for example"""
        pdb_path = self.test_suite.current_test_cache_dir.pdb
        mkdssp = which(self.prefix.bin.mkdssp, required=True)
        with working_dir(pdb_path):
            mkdssp("1ALK.pdb", "1alk.dssp")


class CMakeBuilder(CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define("INSTALL_LIBRARY", True),
            self.define_from_variant("BUILD_PYTHON_MODULE", "python"),
        ]

        return args


class AutotoolsBuilder(AutotoolsBuilder):
    def configure_args(self):
        args = ["--with-boost=%s" % self.spec["boost"].prefix]
        return args

    @run_after("configure")
    def edit(self):
        makefile = FileFilter(join_path(self.stage.source_path, "Makefile"))
        makefile.filter(".*-Werror .*", "                    -Wno-error \\")
