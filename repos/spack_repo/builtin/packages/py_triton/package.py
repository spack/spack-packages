# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems import python as pybs
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTriton(PythonPackage):
    """A language and compiler for custom Deep Learning operations."""

    homepage = "https://github.com/triton-lang/triton"
    url = "https://github.com/triton-lang/triton/archive/refs/tags/v2.1.0.tar.gz"
    git = "https://github.com/triton-lang/triton.git"

    license("MIT")

    version("main", branch="main")
    version("3.4.0", sha256="a96e87a911794c907fab30e0c7a3f96ef4e9e8fdc8812cd8bbc6f0457619072f")
    version("3.3.1", sha256="9dc77d9205933bf2fc05eb054f4f1d92acd79a963826174d57fe9cfd58ba367b")
    version("3.2.0", sha256="04eb07e2ff1b87bf4b26e132d696177248bfb9c71cecd4864e561a9c103de9b3")
    version("2.1.0", sha256="4338ca0e80a059aec2671f02bfc9320119b051f378449cf5f56a1273597a3d99")

    variant(
        "build-custom-llvm",
        default=False,
        description="Build and use an in-prefix llvm-project for Triton",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Build-time requirements
    with default_args(type="build"):
        depends_on("cmake@3.18:3")
        depends_on("ninja@1.11.1:")
        depends_on("py-setuptools@40.8.0:")
        depends_on("py-pybind11@2.13.1:")
        depends_on("py-lit")
        depends_on("nlohmann-json")
        depends_on("git", when="+build-custom-llvm")

    # Runtime/additional deps
    depends_on("py-setuptools@40.8.0:", type="run", when="@3.2.0")
    depends_on("py-filelock", type=("build", "run"))
    depends_on("zlib-api", type="link")
    conflicts("^openssl@3.3.0")
    depends_on("cuda")

    def setup_run_environment(self, env):
        cuda = self.spec["cuda"].prefix
        cuda_bin = os.path.join(str(cuda), "bin")
        cuda_inc = os.path.join(str(cuda), "include")
        cupti_path = self.spec["cuda"].prefix.extras.CUPTI

        env.set("TRITON_PTXAS_PATH", os.path.join(cuda_bin, "ptxas"))
        env.set("TRITON_CUOBJDUMP_PATH", os.path.join(cuda_bin, "cuobjdump"))
        env.set("TRITON_NVDISASM_PATH", os.path.join(cuda_bin, "nvdisasm"))
        env.set("TRITON_CUDACRT_PATH", cuda_inc)
        env.set("TRITON_CUDART_PATH", cuda_inc)
        env.set("TRITON_CUPTI_INCLUDE_PATH", os.path.join(cupti_path, "include"))
        env.set("TRITON_CUPTI_LIB_PATH", os.path.join(cupti_path, "lib64"))


class PythonPipBuilder(pybs.PythonPipBuilder):

    def _build_llvm(self, pkg: PythonPackage):
        repo_root = pkg.stage.source_path

        # Find LLVM commit hash
        env_hash = os.environ.get("LLVM_COMMIT_HASH")
        hash_file = os.path.join(repo_root, "cmake", "llvm-hash.txt")
        if env_hash:
            llvm_commit_hash = env_hash.strip()
        elif os.path.exists(hash_file):
            with open(hash_file) as f:
                llvm_commit_hash = f.read().strip()
        else:
            raise InstallError(
                "Could not determine LLVM commit hash. "
                f"Set LLVM_COMMIT_HASH or provide {hash_file}."
            )
        if not llvm_commit_hash:
            raise InstallError("LLVM commit hash is empty.")

        llvm_project_path = os.environ.get(
            "LLVM_PROJECT_PATH", os.path.join(repo_root, "llvm-project")
        )
        llvm_build_path = os.environ.get(
            "LLVM_BUILD_PATH", os.path.join(llvm_project_path, "build")
        )
        llvm_install_path = os.environ.get(
            "LLVM_INSTALL_PATH", os.path.join(str(pkg.prefix), "triton-llvm")
        )
        llvm_targets = os.environ.get("LLVM_TARGETS", "Native;NVPTX;AMDGPU")
        llvm_projects = os.environ.get("LLVM_PROJECTS", "mlir;llvm;lld")
        llvm_btype = os.environ.get("LLVM_BUILD_TYPE", "Release")
        llvm_url = os.environ.get("LLVM_PROJECT_URL", "https://github.com/llvm/llvm-project")

        git, cmake, ninja = which("git"), which("cmake"), which("ninja")

        if os.environ.get("LLVM_CLEAN") and os.path.exists(llvm_project_path):
            Executable("rm")("-rf", llvm_project_path)

        if not os.path.exists(llvm_project_path):
            git("clone", llvm_url, llvm_project_path)

        git("-C", llvm_project_path, "fetch", "origin", llvm_commit_hash)
        git("-C", llvm_project_path, "reset", "--hard", llvm_commit_hash)

        mkdirp(llvm_build_path)
        mkdirp(llvm_install_path)

        cmake(
            "-G",
            "Ninja",
            f"-DCMAKE_BUILD_TYPE={llvm_btype}",
            "-DCMAKE_BUILD_WITH_INSTALL_RPATH=ON",
            "-DLLVM_CCACHE_BUILD=OFF",
            "-DLLVM_ENABLE_ASSERTIONS=ON",
            "-DLLVM_BUILD_TOOLS=ON",
            "-DLLVM_INSTALL_TOOLS=ON",
            "-DLLVM_INSTALL_UTILS=ON",
            "-DLLVM_OPTIMIZED_TABLEGEN=ON",
            f"-DLLVM_TARGETS_TO_BUILD={llvm_targets}",
            "-DCMAKE_EXPORT_COMPILE_COMMANDS=1",
            f"-DLLVM_ENABLE_PROJECTS={llvm_projects}",
            f"-DCMAKE_INSTALL_PREFIX={llvm_install_path}",
            "-B",
            llvm_build_path,
            os.path.join(llvm_project_path, "llvm"),
        )
        ninja("-C", llvm_build_path, f"-j{make_jobs}")
        ninja("-C", llvm_build_path, "install", f"-j{make_jobs}")

        libdir = os.path.join(llvm_install_path, "lib")
        if not os.path.isdir(libdir):
            libdir = os.path.join(llvm_install_path, "lib64")

        return llvm_install_path, os.path.join(llvm_install_path, "include"), libdir

    def install(self, pkg: PythonPackage, spec: Spec, prefix: Prefix) -> None:

        env_map = os.environ.copy()

        if "+build-custom-llvm" in spec:
            llvm_syspath, llvm_include_dir, llvm_library_dir = self._build_llvm(self.pkg)
            env_map["LLVM_INCLUDE_DIRS"] = llvm_include_dir
            env_map["LLVM_LIBRARY_DIR"] = llvm_library_dir
            env_map["LLVM_SYSPATH"] = llvm_syspath

        cuda = self.pkg.spec["cuda"].prefix
        cuda_bin = os.path.join(str(cuda), "bin")
        cuda_include = os.path.join(str(cuda), "include")
        cupti_path = self.pkg.spec["cuda"].prefix.extras.CUPTI

        env_map["CUDA_HOME"] = str(cuda)
        env_map["CUDA_PATH"] = str(cuda)
        env_map["CUDAToolkit_ROOT"] = str(cuda)
        env_map["CUDA_TOOLKIT_ROOT_DIR"] = str(cuda)
        env_map["TRITON_PTXAS_PATH"] = os.path.join(cuda_bin, "ptxas")
        env_map["TRITON_CUOBJDUMP_PATH"] = os.path.join(cuda_bin, "cuobjdump")
        env_map["TRITON_NVDISASM_PATH"] = os.path.join(cuda_bin, "nvdisasm")
        env_map["TRITON_CUDACRT_PATH"] = cuda_include
        env_map["TRITON_CUDART_PATH"] = cuda_include
        env_map["TRITON_CUPTI_INCLUDE_PATH"] = f"{cupti_path}/include"
        env_map["TRITON_CUPTI_LIB_PATH"] = f"{cupti_path}/lib64"

        cmake_args_list = [
            "-DCMAKE_BUILD_WITH_INSTALL_RPATH=ON",
            f"-DCMAKE_CXX_FLAGS=-I{cuda_include}",
        ]
        env_map["TRITON_APPEND_CMAKE_ARGS"] = " ".join(cmake_args_list)

        triton_home = f"{self.build_directory}/.triton_home"
        env_map["TRITON_HOME"] = triton_home

        env_map["PYBIND11_SYSPATH"] = self.pkg.spec["py-pybind11"].prefix
        env_map["JSON_SYSPATH"] = self.pkg.spec["nlohmann-json"].prefix

        env_map["MAX_JOBS"] = str(make_jobs)

        pip = spec["python"].command
        pip.add_default_arg("-m", "pip")

        args = type(self).std_args(pkg) + [f"--prefix={prefix}"]

        for setting in pybs._flatten_dict(self.config_settings(spec, prefix)):
            args.append(f"--config-settings={setting}")
        for option in self.install_options(spec, prefix):
            args.append(f"--install-option={option}")
        for option in self.global_options(spec, prefix):
            args.append(f"--global-option={option}")

        if pkg.stage.archive_file and pkg.stage.archive_file.endswith(".whl"):
            args.append(pkg.stage.archive_file)
        else:
            args.append(".")

        with working_dir(self.build_directory):
            pip(*args, env=env_map)

    @property
    def build_directory(self):
        # Triton changed layout in 3.4.0
        return "." if self.spec.satisfies("@3.4.0:") else "python"
