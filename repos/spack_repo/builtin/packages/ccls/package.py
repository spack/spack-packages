# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ccls(CMakePackage):
    """C/C++ language server"""

    homepage = "https://github.com/MaskRay/ccls"
    git = "https://github.com/MaskRay/ccls.git"
    url = "https://github.com/MaskRay/ccls/archive/0.20201025.tar.gz"

    maintainers("jacobmerson")

    license("Apache-2.0")

    version(
        "0.20241108", sha256="76224663c3554eef9102dca66d804874d0252312d7c7d02941c615c87dcb68af"
    )
    version(
        "0.20240505", sha256="4ea6d90a9f93d5503e59c3bd0e5568ab262ff3dcf1b7539b50a0ede4a0e32fea"
    )
    version(
        "0.20240202", sha256="355ff7f5eb5f24d278dda05cccd9157e89583272d0559d6b382630171f142d86"
    )
    version(
        "0.20230717", sha256="118e84cc17172b1deef0f9c50767b7a2015198fd44adac7966614eb399867af8"
    )
    version(
        "0.20220729", sha256="af19be36597c2a38b526ce7138c72a64c7fb63827830c4cff92256151fc7a6f4"
    )
    version(
        "0.20210330", sha256="28c228f49dfc0f23cb5d581b7de35792648f32c39f4ca35f68ff8c9cb5ce56c2"
    )

    depends_on("cxx", type="build")
    depends_on("c", type="build")

    depends_on("cmake@3.8:", type="build")
    depends_on("llvm@10:19", when="@=0.20241108")
    depends_on("llvm@7:19", when="@=0.20240505")
    depends_on("llvm@7:18", when="@:0.20240202")
    depends_on("rapidjson")
