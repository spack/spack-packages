# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNumba(PythonPackage):
    """Compiling Python code using LLVM.

    Numba is an open source, NumPy-aware optimizing compiler for Python sponsored by Anaconda, Inc.
    It uses the LLVM compiler project to generate machine code from Python syntax.
    """

    homepage = "https://numba.pydata.org/"
    pypi = "numba/numba-0.35.0.tar.gz"
    git = "https://github.com/numba/numba.git"

    skip_modules = ["numba.core.rvsdg_frontend"]

    license("BSD-2-Clause")

    version("0.63.0", sha256="27e525ce6f9f727c4f61e89b9d453d4a7d0aabbbf110278988334f43cbd70fdc")
    version("0.62.1", sha256="7b774242aa890e34c21200a1fc62e5b5757d5286267e71103257f4e2af0d5161")
    version(
        "0.62.0rc2",
        sha256="4f9a4a9c61e1b1a8a75ef862c4fc265599c32d760b30b29b58442a0da384e30f",
        deprecated=True,
    )
    version("0.61.2", sha256="8750ee147940a6637b80ecf7f95062185ad8726c8c28a2295b8ec1160a196f7d")
    version("0.61.0", sha256="888d2e89b8160899e19591467e8fdd4970e07606e1fbc248f239c89818d5f925")
    version("0.60.0", sha256="5df6158e5584eece5fc83294b949fd30b9f1125df7708862205217e068aabf16")
    version("0.59.1", sha256="76f69132b96028d2774ed20415e8c528a34e3299a40581bae178f0994a2f370b")
    version("0.58.1", sha256="487ded0633efccd9ca3a46364b40006dbdaca0f95e99b8b83e778d1195ebcbaa")
    version("0.57.0", sha256="2af6d81067a5bdc13960c6d2519dbabbf4d5d597cf75d640c5aeaefd48c6420a")
    version("0.56.4", sha256="32d9fef412c81483d7efe0ceb6cf4d3310fde8b624a9cecca00f790573ac96ee")
    version("0.56.0", sha256="87a647dd4b8fce389869ff71f117732de9a519fe07663d9a02d75724eb8e244d")
    version("0.55.2", sha256="e428d9e11d9ba592849ccc9f7a009003eb7d30612007e365afe743ce7118c6f4")
    version("0.55.1", sha256="03e9069a2666d1c84f93b00dbd716fb8fedde8bb2c6efafa2f04842a46442ea3")
    version("0.54.0", sha256="bad6bd98ab2e41c34aa9c80b8d9737e07d92a53df4f74d3ada1458b0b516ccff")

    variant("tbb", default=False, description="Build with Intel Threading Building Blocks")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")

    with default_args(type=("build", "link", "run")):
        # See min/max_*_version in setup.py
        # Upper bounds are exclusive
        depends_on("python@3.10:3.14", when="@0.63:")
        depends_on("python@3.10:3.13", when="@0.61:0.62")
        depends_on("python@3.9:3.12", when="@0.59:0.60")
        depends_on("python@3.8:3.11", when="@0.57:0.58")
        depends_on("python@3.7:3.10", when="@0.55:0.56")
        depends_on("python@3.7:3.9", when="@0.54")

    with default_args(type=("build", "run")):
        # Use min_numpy_run_version, not min_numpy_build_version
        # min_numpy_build_version may be higher to ensure backwards-compatibility of wheels,
        # but this doesn't matter for Spack which always guarantees compatibility
        depends_on("py-numpy@1.22:2.3", when="@0.62:")
        depends_on("py-numpy@1.24:2.2", when="@0.61.1:0.61.2")
        depends_on("py-numpy@1.24:2.1", when="@0.61.0")
        depends_on("py-numpy@1.22:2.0", when="@0.60")
        depends_on("py-numpy@1.22:1.26", when="@0.58.1:0.59")
        depends_on("py-numpy@1.21:1.25", when="@0.58.0")
        depends_on("py-numpy@1.21:1.24", when="@0.57")
        depends_on("py-numpy@1.18:1.23", when="@0.56.1:0.56.4")
        depends_on("py-numpy@1.18:1.22", when="@0.55.2:0.56.0")
        depends_on("py-numpy@1.18:1.21", when="@0.55.0:0.55.1")
        depends_on("py-numpy@1.17:1.20", when="@0.54")

        depends_on("py-llvmlite@0.46", when="@0.63")
        depends_on("py-llvmlite@0.45", when="@0.62")
        depends_on("py-llvmlite@0.44", when="@0.61")
        depends_on("py-llvmlite@0.43", when="@0.60")
        depends_on("py-llvmlite@0.42", when="@0.59")
        depends_on("py-llvmlite@0.41", when="@0.58")
        depends_on("py-llvmlite@0.40", when="@0.57")
        depends_on("py-llvmlite@0.39", when="@0.56")
        depends_on("py-llvmlite@0.38", when="@0.55")
        depends_on("py-llvmlite@0.37", when="@0.54")

        # Always a build requirement
        # Run-time requirement prior to 0.57, still required for pycc but technically optional
        depends_on("py-setuptools")

    depends_on("tbb", when="+tbb")
    # Version 6.0.0 of llvm had a hidden symbol which breaks numba at runtime.
    # See https://reviews.llvm.org/D44140
    conflicts("^llvm@6.0.0")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("~tbb"):
            env.set("NUMBA_DISABLE_TBB", "yes")
