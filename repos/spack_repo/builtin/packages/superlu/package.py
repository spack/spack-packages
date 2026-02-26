# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Superlu(CMakePackage):
    """SuperLU is a general purpose library for the direct solution of large,
    sparse, nonsymmetric systems of linear equations on high performance
    machines. SuperLU is designed for sequential machines."""

    homepage = "https://portal.nersc.gov/project/sparse/superlu/"
    url = "https://github.com/xiaoyeli/superlu/archive/refs/tags/v5.3.0.tar.gz"

    tags = ["e4s"]

    test_requires_compiler = True

    license("BSD-3-Clause")

    version("7.0.1", sha256="86dcca1e086f8b8079990d07f00eb707fc9ef412cf3b2ce808b37956f0de2cb8")
    version("7.0.0", sha256="d7b91d4e0bb52644ca74c1a4dd466a694ddf1244a7bbf93cb453e8ca1f6527eb")
    version("6.0.1", sha256="6c5a3a9a224cb2658e9da15a6034eed44e45f6963f5a771a6b4562f7afb8f549")
    version("6.0.0", sha256="5c199eac2dc57092c337cfea7e422053e8f8229f24e029825b0950edd1d17e8e")
    version("5.3.0", sha256="3e464afa77335de200aeb739074a11e96d9bef6d0b519950cfa6684c4be1f350")

    requires("build_system=cmake", when="platform=windows")

    variant("pic", default=True, description="Build with position independent code")
    variant("fortran", default=True, description="Build fortran interface")

    depends_on("c", type="build")
    depends_on("fortran", type="build", when="+fortran")
    depends_on("metis", when="@6:")

    depends_on("blas")
    conflicts(
        "@:5.2.1",
        when="%apple-clang@12:",
        msg="Older SuperLU is incompatible with newer compilers",
    )

    examples_src_dir = "EXAMPLE"

    def test_example(self):
        """build and run test example"""
        test_dir = join_path(self.test_suite.current_test_cache_dir, self.examples_src_dir)
        test_exe = "superlu"
        test_src = f"{test_exe}.c"

        if not os.path.isfile(join_path(test_dir, test_src)):
            raise SkipTest(f"Cached {test_src} is missing")

        with working_dir(test_dir):
            args = []
            if self.version < Version("5.2.2"):
                args.append("HEADER=" + self.prefix.include)
            args.append(test_exe)

            make = which("make", required=True)
            make(*args)

            superlu = which(test_exe, required=True)
            superlu()

    def cmake_args(self):
        args = [
            self.define("enable_internal_blaslib", False),
            self.define("CMAKE_INSTALL_LIBDIR", self.prefix.lib),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            self.define("enable_tests", self.run_tests),
            self.define_from_variant("enable_fortran", "fortran"),
        ]

        if self.spec.satisfies("@6:"):
            args.extend(
                [
                    self.define("TPL_ENABLE_METISLIB", True),
                    self.define("TPL_METIS_INCLUDE_DIRS", self.spec["metis"].prefix.include),
                    self.define("TPL_METIS_LIBRARIES", self.spec["metis"].libs),
                ]
            )

        return args

    @run_after("install")
    def setup_standalone_tests(self):
        """Set up and copy example source files after the package is installed
        to an install test subdirectory for use during `spack test run`."""
        makefile = join_path(self.examples_src_dir, "Makefile")

        if self.spec.satisfies("@5.2.2:"):
            # Include dir was hardcoded in 5.2.2
            filter_file(
                r"INCLUDEDIR  = -I\.\./SRC", "INCLUDEDIR = -I" + self.prefix.include, makefile
            )

        # Create the example makefile's include file and ensure the new file
        # is the one use.
        filename = "make.inc"
        config_args = []
        if self.spec.satisfies("@5:"):
            lib = "libsuperlu.a"
        else:
            config_args.append("PLAT       = _x86_64")
            lib = f"libsuperlu_{self.spec.version}.a"
        config_args.extend(self._make_hdr_for_test(lib))

        with open(join_path(self.examples_src_dir, filename), "w") as inc:
            for option in config_args:
                inc.write(f"{option}\n")

        # change the path in the example's Makefile to the file written above
        filter_file(r"include \.\./" + filename, "include ./" + filename, makefile)

        # Cache the examples directory for use by stand-alone tests
        cache_extra_test_sources(self, self.examples_src_dir)

    def _make_hdr_for_test(self, lib):
        """Standard configure arguments for make.inc"""
        ranlib = "ranlib" if which("ranlib") else "echo"
        return [
            f"SuperLUroot = {self.prefix}",
            f"SUPERLULIB = {self.prefix.lib}/{lib}",
            f"BLASLIB    = {self.spec['blas'].libs.ld_flags}",
            "TMGLIB     = libtmglib.a",
            "LIBS       = $(SUPERLULIB) $(BLASLIB)",
            "ARCH       = ar",
            "ARCHFLAGS  = cr",
            f"RANLIB     = {ranlib}",
            f"CC         = {env['CC']}",
            f"FORTRAN    = {env['FC']}",
            f"LOADER     = {env['CC']}",
            "CFLAGS     = -O3 -DNDEBUG -DUSE_VENDOR_BLAS -DPRNTlevel=0 -DAdd_",
            "NOOPTS     = -O0",
        ]
