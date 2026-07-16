# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Cccl(CMakePackage, CudaPackage):
    """CUDA Core Compute Libraries (CCCL)
    CCCL provide the following header-only CUDA libraries: Thrust, CUB, and libcudacxx.
    """

    homepage = "https://github.com/NVIDIA/cccl"
    url = "https://github.com/NVIDIA/cccl/releases/download/v3.3.4/cccl-src-v3.3.4.tar.gz"
    git = "https://github.com/NVIDIA/cccl"

    supplier = "NVIDIA"

    maintainers("gusser93")

    license(
        "Apache-2.0 AND"  # Thrust
        "Apache-2.0 WITH LLVM-exception AND"  # libcu++
        "BSL-1.0 AND"  # Parts of Thrust
        "LicenseRef-scancode-bsd-unmodified AND"  # Portions of thrust::complex
        "BSD-3-Clause",  # CUB
        checked_by="gusser93",
    )

    version("3.4.0", sha256="7d3f36c6236b4a9fd6e40a0520aa516e0dcbe157aa6345966eb25f35bc4cdc77")
    version("3.3.4", sha256="9d5ae91a71f971c69a16ec139c6882c2c19f74a862c3d90ceaa3c9e8f327e5a6")
    version("3.3.3", sha256="7aed8bd89049bb75261cc9633e4471e1fcf5fbb5eb5b1aeb3f82ee07e9f60395")
    version("3.3.2", sha256="7bf03b4f3ab4db8b5781613564a01cf19682e50afc58bb06ced53cd049a52965")
    version("3.3.1", sha256="95355e7d492d70604705330c12afef785c76048e1084852ceeb31522e2dbf223")

    variant("cuda", default=True, description="Build with CUDA")

    depends_on("cmake@3.21:", type="build")
    depends_on("cxx", type="build")

    # CCCL version X needs CUDA version >= X+9
    depends_on("cuda@12:", type=("build", "link"), when="@3")

    requires("+cuda")
