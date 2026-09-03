# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTorchaudio(PythonPackage):
    """An audio package for PyTorch."""

    homepage = "https://github.com/pytorch/audio"
    git = "https://github.com/pytorch/audio.git"
    submodules = True

    license("BSD-2-Clause")
    maintainers("adamjstewart")

    version("main", branch="main")
    version("2.11.0", tag="v2.11.0", commit="34c52a67e8941bbd8e6adaca0eb0b9eabec11d78")
    version("2.10.0", tag="v2.10.0", commit="27b7ebdebd2d2e4d34a2f5c05b0fb26efbd1da63")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "link", "run")):
        # Based on PyPI wheel availability
        depends_on("python@3.10:")

        depends_on("py-torch@main", when="@main")
        depends_on("py-torch@2.11:", when="@2.11.0")
        depends_on("py-torch@2.10:", when="@2.10.0")

    # CMakelists.txt
    depends_on("cmake@3.18:", type="build")
    depends_on("ninja", type="build")

    # setup.py
    depends_on("py-setuptools", type="build")
    depends_on("py-pybind11", type=("build", "link"))
    depends_on("pkgconfig", type="build")

    def patch(self):
        # Add missing rpaths, which requires patching due to hardcoded cmake_args
        rpaths = [f"{python_platlib}/torchaudio/lib", f"{python_platlib}/torio/lib"]
        cmake_args = [
            f"-DCMAKE_INSTALL_RPATH={';'.join(rpaths)}",
            "-DCMAKE_INSTALL_RPATH_USE_LINK_PATH=ON",
        ]
        cmake_str = ", ".join(f"'{arg}'" for arg in cmake_args)
        filter_file(
            "cmake_args = [",
            f"cmake_args = [{cmake_str},",
            "tools/setup_helpers/extension.py",
            string=True,
        )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if "+cuda" in self.spec["py-torch"]:
            env.set("USE_CUDA", "1")
        else:
            env.set("USE_CUDA", "0")

        if "+rocm" in self.spec["py-torch"]:
            env.set("USE_ROCM", "1")
        else:
            env.set("USE_ROCM", "0")
