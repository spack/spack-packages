# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmLibrary

from spack.package import *


class Rocminfo(ROCmLibrary, CMakePackage):
    """Radeon Open Compute (ROCm) Runtime rocminfo tool"""

    homepage = "https://github.com/ROCm/rocminfo"
    git = "https://github.com/ROCm/rocm-systems.git"

    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "haampie")
    executables = ["rocminfo"]

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/rocminfo/archive/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-systems/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.3", sha256="e90cfd8694af28a56433c8827a581ee12a4ba835f0d952436741d9e0f3f8685b")
    version("7.2.1", sha256="201f19174eafbace2f7abf0d1178ebb17db878191276aba6d23f0e1758b0e10f")
    version("7.2.0", sha256="728ea7e9bf16e6ed217a0fd1a8c9afaba2dae2e7908fa4e27201e67c803c5638")
    version("7.1.1", sha256="a1ff6d08e0c7ff653bb323964ff2badf6aa1d75aeb2d69248599b0133370fa7e")
    version("7.1.0", sha256="fdf1e08392d3645d64696c5de7c116a1ea7ff3c70f19c0cb46c9eece7c00062c")
    version("7.0.2", sha256="06098e7fa92c618ecd042dca3c980f270617f2085b93d1465a4b7e7cc4d12661")
    version("7.0.0", sha256="fdab0c04941a64f585605b05d4e520fb2261d10175227cc6e9f934e868462eea")
    version("6.4.3", sha256="0aa040963daaa2b5ebbec818a2d53c83612912686336160c223fb664dc0ca92b")
    version("6.4.2", sha256="b559f7e22086db952cec098d5512c77ae844f955a16d2cbbbd088fb3844c8787")
    version("6.4.1", sha256="eabbe4bfb29152900bbde812c6fffd5555b45842259242d85f29e449c00f3249")
    version("6.4.0", sha256="060184e70755cb267017553ec37cc5b36af2c94e6b0643cad4b9fed270199a79")
    version("6.3.3", sha256="08390b2babe6dc832887098c5d3a5253d655430a18751f3446a56c7422b26dd2")
    version("6.3.2", sha256="a98a32bae0e118397b5559b4a584c9363191bb2d1f45fe13b09f502016745e8f")
    version("6.3.1", sha256="30cf7ed537c066e325a8731d0fbe62be2f0f66c8700a06f334e787e9f0f87437")
    version("6.3.0", sha256="40e2ef89e135770196022761cb929af93c80c41869082b3ef80e42b7772267d0")
    version("6.2.4", sha256="14d4b0e22e2314156091ac9ad1646dd20909dba3a43e037584a503a6754e7f9e")
    version("6.2.1", sha256="ae6e08962535e76a81ed872cbd6bf6860c46fa6e4e4bc8f7849c8781359798d8")
    version("6.2.0", sha256="4d9a9051bda3355f8d2050e981435cd02528a04264a7f61162d685e7e1629f73")
    version("6.1.2", sha256="882ebe3db60b6290a81a98e0bac9b8923fbf83966f1706fd24484700b8213bcc")
    version("6.1.1", sha256="ef5e33ad3d0bae462d01e1528ffa9c83c587ccbf7ef5947e096e550480d83819")
    version("6.1.0", sha256="973352210fdc65932f0125e2db68729383727eaf4ebb7f52c88a948c14bbbb73")
    version("6.0.2", sha256="e616d364a48de18eaee661bdce999d095086905f49777663ca99312f40a63da1")
    version("6.0.0", sha256="bc29f1798644b6dea73895353dffada9db7366d0058274e587ebd3291a4d3844")
    version("5.7.1", sha256="642dc2ec4254b3c30c43064e6690861486db820b25f4906ec78bdb47e68dcd0b")
    version("5.7.0", sha256="a5a3c19513bf26f17f163a03ba5288c5c761619ef55f0cb9e15472771748b93e")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3:", type="build")
    extends("python@3:")

    for ver in [
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
    ]:
        depends_on(f"hsakmt-roct@{ver}", when=f"@{ver}")

    for ver in [
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
        "7.2.0",
        "7.2.1",
        "7.2.3",
    ]:
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.2:"):
            return "projects/rocminfo"
        else:
            return "."

    def cmake_args(self):
        return [self.define("ROCM_DIR", self.spec["hsa-rocr-dev"].prefix)]
