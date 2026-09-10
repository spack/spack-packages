# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import glob
import os

from spack_repo.builtin.packages.clingo.package import Clingo

from spack.package import *


class ClingoBootstrap(Clingo):
    """Clingo with some options used for bootstrapping"""

    maintainers("alalazo")

    variant("build_type", default="Release", values=("Release",), description="CMake build type")
    variant("apps", default=False, description="build command line applications")

    variant(
        "static_libstdcpp",
        default=False,
        when="platform=linux",
        description="Require a static version of libstdc++",
    )

    variant(
        "optimized",
        default=False,
        description="Enable a series of Spack-specific optimizations (PGO, LTO, mimalloc)",
    )

    # Enable LTO
    conflicts("~ipo", when="+optimized")

    with when("+optimized platform=linux"):
        # Statically linked. Don't use ~override so we don't duplicate malloc/free, they
        # get resolved to Python's libc's malloc in our case anyway.
        depends_on("mimalloc +ipo libs=static ~override", type="build")
        conflicts("~static_libstdcpp", msg="Custom allocator requires static libstdc++")
        # Override new/delete with mimalloc.
        patch("mimalloc.patch", when="@5.5.0:")
        patch("mimalloc-pre-5.5.0.patch", when="@:5.4")
        # ensure we hide libstdc++ with custom operator new/delete symbols
        patch("version-script.patch", when="@spack,5.5:5.6")
        patch("version-script-5.4.patch", when="@5.2:5.4")

    # flat multimap for performance: https://github.com/potassco/clasp/pull/118
    patch(
        "https://github.com/haampie/clasp/commit/0f43ac61e8576404c6a33f25954883d3e51ef0df.patch?full_index=1",
        sha256="0a266a4d475c225af30607ccd2b541cfca0e4b31368219f6de71039c8df156b3",
        working_dir="clasp",
        when="@:5.7 +optimized",
    )
    patch(
        "https://github.com/haampie/clasp/commit/208972863506ecbd85ed0bd78fac580b5e9c9c90.patch?full_index=1",
        sha256="c569fb439a99b709b6e6ac05253b344e4f3055d52223265baa55946db6d44e8b",
        working_dir="clasp",
        when="@5.8: +optimized",
    )

    # CMake at version 3.16.0 or higher has the possibility to force the
    # Python interpreter, which is crucial to build against external Python
    # in environment where more than one interpreter is in the same prefix
    depends_on("cmake@3.16.0:", type="build")
    depends_on("clingo-bootstrap-pgo", type="build", when="+optimized")

    # On Linux we bootstrap with GCC or clang
    requires(
        "%gcc",
        "%clang",
        when="platform=linux",
        msg="GCC or clang are required to bootstrap clingo on Linux",
    )
    conflicts("%gcc@:5", msg="C++14 support is required to bootstrap clingo")

    # On Darwin we bootstrap with Apple Clang
    requires(
        "%apple-clang",
        when="platform=darwin",
        msg="Apple-clang is required to bootstrap clingo on MacOS",
    )

    # Clingo needs the Python module to be usable by Spack
    conflicts("~python", msg="Python support is required to bootstrap Spack")

    cmake_py_shared = False

    @run_before("cmake", when="+optimized")
    def pgo_train(self):
        if self.spec.satisfies("%clang"):
            llvm_profdata = which("llvm-profdata", required=True)
        elif self.spec.satisfies("%apple-clang"):
            llvm_profdata = Executable(
                Executable("xcrun")("-find", "llvm-profdata", output=str).strip()
            )

        # Find the PGO script before starting the build
        script = which_string("clingo-pgo.py", required=True)

        # First configure with PGO flags, and do build apps.
        reports = os.path.abspath("reports")
        sources = os.path.abspath(self.root_cmakelists_dir)
        cmake_options = self.std_cmake_args + self.cmake_args() + [sources]

        # Set PGO flags.
        generate_mods = EnvironmentModifications()
        generate_mods.append_flags("CFLAGS", f"-fprofile-generate={reports}")
        generate_mods.append_flags("CXXFLAGS", f"-fprofile-generate={reports}")
        generate_mods.append_flags("LDFLAGS", f"-fprofile-generate={reports}")

        with working_dir(self.build_directory, create=True):
            cmake(*cmake_options, sources, extra_env=generate_mods)
            make()
            make("install")

        # Clean the reports dir.
        rmtree(reports, ignore_errors=True)

        # Generate profile data.
        env = environment_modifications_for_specs(self.spec, set_package_py_globals=False)
        python(script, extra_env=env)

        # Clean the build dir.
        rmtree(self.build_directory, ignore_errors=True)

        if self.spec.satisfies("%clang") or self.spec.satisfies("%apple-clang"):
            # merge reports
            use_report = join_path(reports, "merged.prof")
            raw_files = glob.glob(join_path(reports, "*.profraw"))
            llvm_profdata("merge", f"--output={use_report}", *raw_files)
            use_flag = f"-fprofile-instr-use={use_report}"
        else:
            use_flag = f"-fprofile-use={reports}"

        # Set PGO use flags for next cmake phase.
        use_mods = EnvironmentModifications()
        use_mods.append_flags("CFLAGS", use_flag)
        use_mods.append_flags("CXXFLAGS", use_flag)
        use_mods.append_flags("LDFLAGS", use_flag)
        cmake.add_default_envmod(use_mods)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if (
            self.spec.satisfies("%gcc") or self.spec.satisfies("%clang")
        ) and "+static_libstdcpp" in self.spec:
            env.append_flags("LDFLAGS", "-static-libstdc++ -static-libgcc -Wl,--exclude-libs,ALL")
