# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SaltFm(CMakePackage):
    """SALT-FM: A next generation LLVM-based Source Analysis Toolkit for performance 
    instrumentation of HPC applications"""

    homepage = "https://github.com/ParaToolsInc/SALT-FM"
    url = "https://github.com/ParaToolsInc/SALT-FM/archive/refs/tags/v0.4.1.tar.gz"
    git = "https://github.com/ParaToolsInc/SALT-FM.git"

    maintainers("zbeekman", "wspear")

    license("Apache-2.0", checked_by="wspear")

    version("master", branch="master")

    version("0.4.1", sha256="fe251f28cd44eeb71640b03d01d6201c935485b4794ba7bc2d92e7988a13d237")
    version("0.4.0", sha256="3c322326f0dfaa9f00f283d4d9be8c8fb991d1f081aca1c86451ceb92f2c9c4f")

    version("0.3.0", sha256="7df4c060c292ed625d4c1cc8c0e794cd4380a263df63693b648b3c8e0cf51ccf")
    version("0.2.0", sha256="55c80f9d0591752b1e5b40e924718dc28f928ee0a3c7008adec3feab1280c57f")

    depends_on("cxx", type="build")
    depends_on("c", type="build")

    variant(
        "flang", default=True, description="Build the Flang frontend plugin for Fortran support"
    )

    depends_on("cmake@3.23:", type="build")

    depends_on("llvm+clang+flang@19", type=("build", "link", "run"), when="@:0.3.0")

    depends_on("llvm@19:22 +clang", type=("build", "link", "run"), when="@0.4.0:")
    depends_on("llvm@19:22 +clang", type=("build", "link", "run"), when="@master")

    with when("+flang"):
        depends_on("llvm +flang", type=("build", "link", "run"))
