# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyArrayRecord(PythonPackage):
    """ArrayRecord is a file format for IO intensive applications, with
    efficient random access and various compression algorithms."""

    homepage = "https://github.com/google/array_record"
    url = "https://github.com/google/array_record/archive/refs/tags/v0.9.0.tar.gz"

    license("Apache-2.0")

    version("0.9.0", sha256="83656c43987373fbd384f012537baf2df2e89063b41325b041cb209c7d482c77")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type="build"):
        depends_on("bazel@8")
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:")
        depends_on("py-absl-py")
        depends_on("py-etils+epath+epy")

    build_directory = "spack-wheel"

    def patch(self):
        # Use Spack's python instead of the CPython builds rules_python downloads
        python_path = self.spec["python"].command.path
        with open("MODULE.bazel", "a") as f:
            f.write(
                f"""
local_runtime_repo = use_repo_rule(
    "@rules_python//python/local_toolchains:repos.bzl", "local_runtime_repo"
)

local_runtime_toolchains_repo = use_repo_rule(
    "@rules_python//python/local_toolchains:repos.bzl", "local_runtime_toolchains_repo"
)

local_runtime_repo(
    name = "spack_python",
    interpreter_path = "{python_path}",
    on_failure = "fail",
)

local_runtime_toolchains_repo(
    name = "spack_python_toolchains",
    runtimes = ["spack_python"],
)

register_toolchains("@spack_python_toolchains//:all")
"""
            )

    @run_before("install")
    def build_extension(self):
        bazel(
            "--nohome_rc",
            "--nosystem_rc",
            f"--output_user_root={join_path(self.stage.source_path, 'spack-bazel')}",
            # The JVM and Bazel size their thread pools by the number of CPUs
            f"--host_jvm_args=-XX:ActiveProcessorCount={make_jobs}",
            # Don't keep the server running for hours after the build
            "--max_idle_secs=5",
            "build",
            "--color=no",
            f"--jobs={make_jobs}",
            "--verbose_failures",
            "--compilation_mode=opt",
            "--cxxopt=-std=c++17",
            "--host_cxxopt=-std=c++17",
            "//python:array_record_module",
        )

        # Lay out the sources like oss/build_whl.sh does for setup.py
        package = join_path(self.build_directory, "array_record")
        mkdirp(package)
        install("setup.py", self.build_directory)
        install("LICENSE", self.build_directory)
        install("__init__.py", package)
        install("MODULE.bazel", package)
        install_tree("beam", join_path(package, "beam"))
        install_tree("python", join_path(package, "python"))
        install(
            join_path("bazel-bin", "python", "array_record_module.so"),
            join_path(package, "python"),
        )
