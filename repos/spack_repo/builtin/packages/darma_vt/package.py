# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class DarmaVt(CMakePackage):
    """vt : Virtual Transport HPC runtime

    vt is an active messaging layer that utilizes C++ object virtualization to
    manage virtual endpoints with automatic location management. vt is directly
    built on top of MPI to provide efficient portability across different
    machine architectures. Empowered with virtualization, vt can automatically
    perform dynamic load balancing to schedule scientific applications across
    diverse platforms with minimal user input.

    vt abstracts the concept of a node/rank/worker/thread so a program can be
    written in terms of virtual entities that are location independent. Thus,
    they can be automatically migrated and thereby executed on varying hardware
    resources without explicit programmer mapping, location, and communication
    management."""

    homepage = "https://github.com/DARMA-tasking/vt"
    git = "https://github.com/DARMA-tasking/vt.git"

    license("BSD-3-Clause")

    version("develop", branch="develop")
    version("1.7.0", tag="1.7.0")
    version("1.6.0", tag="1.6.0")
    version("1.5.0", tag="1.5.0")
    version("1.4.0", tag="1.4.0")
    version("1.3.0", tag="1.3.0")
    version("1.2.2", tag="1.2.2")

    variant(
        "lb_enabled", default=True, description="Compile with support for runtime load balancing"
    )
    variant("trace_enabled", default=False, description="Compile with support for runtime tracing")
    variant("trace_only", default=False, description="Compile vt in trace-only mode")
    variant(
        "mimalloc_enabled",
        default=False,
        description="Enable mimalloc, an alternative allocator for debugging memory issues",
    )
    variant("asan_enabled", default=False, description="Enable building with address sanitizer")
    variant("werror_enabled", default=False, description="Treat all warnings as errors")
    variant(
        "pool_enabled", default=True, description="Use memory pool in vt for message allocation"
    )
    variant(
        "mpi_guards",
        default=False,
        description="Guards against mis-use of MPI calls in code using vt",
    )
    variant("kokkos", default=False, description="Enable Kokkos support")

    depends_on("mpi")

    depends_on("darma-magistrate@1.7.0", when="@1.7.0")
    depends_on("darma-magistrate@1.6.0", when="@1.6.0")
    depends_on("darma-magistrate@develop", when="@:1.5")
    depends_on("darma-magistrate@develop", when="@develop")

    depends_on("darma-magistrate+kokkos", when="+kokkos")
    depends_on("darma-magistrate~kokkos", when="~kokkos")

    depends_on("fmt@10.2.1:10", when="@1.5.0")
    depends_on("fmt@10.2.1:11", when="@1.6:1.7")
    depends_on("fmt@12", when="@develop")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    sanity_check_is_dir = ["include/vt"]
    sanity_check_is_file = ["cmake/vtConfig.cmake", "cmake/vtTargets.cmake"]

    def cmake_args(self):
        args = [
            "-Dmagistrate_ROOT={}".format(self.spec["darma-magistrate"].prefix),
            "-Dvt_lb_enabled={}".format(int(self.spec.variants["lb_enabled"].value)),
            "-Dvt_trace_enabled={}".format(int(self.spec.variants["trace_enabled"].value)),
            "-Dvt_trace_only={}".format(int(self.spec.variants["trace_only"].value)),
            "-Dvt_mimalloc_enabled={}".format(int(self.spec.variants["mimalloc_enabled"].value)),
            "-Dvt_asan_enabled={}".format(int(self.spec.variants["asan_enabled"].value)),
            "-Dvt_werror_enabled={}".format(int(self.spec.variants["werror_enabled"].value)),
            "-Dvt_pool_enabled={}".format(int(self.spec.variants["pool_enabled"].value)),
            "-Dvt_mpi_guards={}".format(int(self.spec.variants["mpi_guards"].value)),
        ]

        if self.spec.version >= Version("1.5.0"):
            args.append("-Dvt_external_fmt=ON")
            args.append("-Dfmt_ROOT={}".format(self.spec["fmt"].prefix))

        if self.spec.version > Version("1.3.0"):
            args.extend(
                [
                    self.define("vt_build_tests", self.run_tests),
                    self.define("vt_build_examples", self.run_tests),
                ]
            )
        else:
            args.extend(
                [
                    self.define("VT_BUILD_TESTS", self.run_tests),
                    self.define("VT_BUILD_EXAMPLES", self.run_tests),
                ]
            )

        return args

    def check(self):
        with working_dir(self.build_directory):
            ctest("--output-on-failure", "--label-regex", "unit_test|example")
