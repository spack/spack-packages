# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cccl(CMakePackage):
    """CUDA Core Compute Libraries (CCCL)

    Welcome to the CUDA Core Compute Libraries (CCCL) where our mission is to make CUDA more
    delightful.

    This repository unifies three essential CUDA C++ libraries into a single, convenient
    repository:

    - Thrust,
    - CUB,
    - libcudacxx

    The goal of CCCL is to provide CUDA C++ developers with building blocks that make it easier to
    write safe and efficient code. Bringing these libraries together streamlines your development
    process and broadens your ability to leverage the power of CUDA C++.

    CCCL is a header-only library.
    """

    homepage = "https://github.com/NVIDIA/cccl"
    url = "https://github.com/NVIDIA/cccl/releases/download/v3.3.4/cccl-src-v3.3.4.tar.gz"
    git = "https://github.com/NVIDIA/cccl"

    supplier = "NVIDIA"

    maintainers("gusser93")

    license(
        "Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSL-1.0 AND LicenseRef-scancode-bsd-unmodified AND BSD-3-Clause",
        checked_by="gusser93",
    )

    version("3.3.4", sha256="9d5ae91a71f971c69a16ec139c6882c2c19f74a862c3d90ceaa3c9e8f327e5a6")
    version("3.3.3", sha256="7aed8bd89049bb75261cc9633e4471e1fcf5fbb5eb5b1aeb3f82ee07e9f60395")
    version("3.3.2", sha256="7bf03b4f3ab4db8b5781613564a01cf19682e50afc58bb06ced53cd049a52965")
    version("3.3.1", sha256="95355e7d492d70604705330c12afef785c76048e1084852ceeb31522e2dbf223")

    depends_on("cmake@3.21:", type="build")
