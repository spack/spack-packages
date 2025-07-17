# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin import build_systems
from spack_repo.builtin.build_systems.python import CudaPackage, PythonPackage

import llnl.util.filesystem as fs

from spack.package import *


class PyTriton(PythonPackage, CudaPackage):
    """A language and compiler for custom Deep Learning operations."""

    homepage = "https://github.com/triton-lang/triton"
    url = "https://github.com/triton-lang/triton/archive/refs/tags/v2.1.0.tar.gz"
    git = "https://github.com/triton-lang/triton.git"

    license("MIT")

    version("main", branch="main")
    version("3.3.1", sha256="9dc77d9205933bf2fc05eb054f4f1d92acd79a963826174d57fe9cfd58ba367b")
    version("3.2.0", sha256="04eb07e2ff1b87bf4b26e132d696177248bfb9c71cecd4864e561a9c103de9b3")
    version("2.1.0", sha256="4338ca0e80a059aec2671f02bfc9320119b051f378449cf5f56a1273597a3d99")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    with default_args(type="build"):
        # avoid bdist_whell.dist_info_dir problems:
        # pypa used to contain `bdist_wheel` but it is part of setuptools as of v70.1
        # see https://github.com/pypa/wheel/pull/631
        # and https://github.com/pypa/setuptools/pull/4684
        depends_on("py-setuptools@40.8:70.0")

        # https://github.com/triton-lang/triton/blob/v3.3.1/python/requirements.txt
        depends_on("cmake@3.18:3")
        depends_on("ninja@1.11.1:")
        depends_on("py-pybind11@2.13.1:")
        depends_on("py-lit")

    depends_on("py-filelock", type=("build", "run"))
    depends_on("zlib-api", type="link")
    conflicts("^openssl@3.3.0")


# override pip install to use python subdirectory from parent directory
class PythonPipBuilder(build_systems.python.PythonPipBuilder):
    def install(self, pkg, spec, prefix):
        pip = spec["python"].command
        pip.add_default_arg("-m", "pip")
        args = build_systems.python.PythonPipBuilder.std_args(pkg) + [f"--prefix={prefix}"]
        # build directory specified manually as additional argument to pip install
        args.append("./python")
        with fs.working_dir(self.build_directory):
            pip(*args)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        """Set environment variables used to control the build"""
        if self.spec.satisfies("%clang"):
            env.set("TRITON_BUILD_WITH_CLANG_LLD", "True")
        # set number of concurrent build jobs
        env.set("MAX_JOBS", make_jobs)
        # add a directory for triton's downloads
        triton_home = f"{self.build_directory}/.triton_home"
        env.set("TRITON_HOME", triton_home)
        # use spack installed dependencies
        env.set("PYBIND11_SYSPATH", self.spec["py-pybind11"].prefix)
        if self.spec.satisfies("+cuda"):
            env.set("TRITON_PTXAS_PATH", self.spec["cuda"].prefix)
            env.set("TRITON_CUOBJDUMP_PATH", self.spec["cuda"].prefix)
            env.set("TRITON_NVDISASM_PATH", self.spec["cuda"].prefix)
            env.set("TRITON_CUDACRT_PATH", self.spec["cuda"].prefix)
            env.set("TRITON_CUDART_PATH", self.spec["cuda"].prefix)
            cupti_path = self.spec["cuda"].prefix.extras.CUPTI
            env.set("TRITON_CUPTI_INCLUDE_PATH", f"{cupti_path}/include")
            env.set("TRITON_CUPTI_LIB_PATH", f"{cupti_path}/lib64")

    # build_directory does not work since apparently one needs to call pip from
    # the parent directory
    # build_directory = "python"
