# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class HipblasCommon(CMakePackage):
    """Common files shared by hipBLAS and hipBLASLt"""

    homepage = "https://github.com/ROCm/hipBLAS-common"
    url = "https://github.com/ROCm/hipBLAS-common/archive/refs/tags/rocm-6.3.0.tar.gz"
    git = "https://github.com/ROCm/rocm-libraries.git"

    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/hipBLAS-common/archive/refs/tags/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-libraries/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.0", sha256="8ad5f4a11f1ed8a7b927f2e65f24083ca6ce902a42021a66a815190a91ccb654")
    version("7.1.1", sha256="1baedf7562c7afdca5f688b9117949941082b30cd5ea8630b30e9ac299cf56ea")
    version("7.1.0", sha256="6c00bb9335ad2ad3d4730eb41ebc704b0207162d5f98da1cdce3eea1087c3944")
    version("7.0.2", sha256="7b8007784831d895fb0a432f366388bc7d212443a25ea9f14eb2aa0a7b4ad5d7")
    version("7.0.0", sha256="a20e4770a5758e931b7a79c5e0f2a061a1b11195217f74d512cdc764124fc564")
    version("6.4.3", sha256="a6a0ad9b12fb104e96d19556e576bb2a8ddb630acf6209f171a61707eed1d6c8")
    version("6.4.2", sha256="2212ebede73269864d5303fec94f4d0774c196f68dc9afe50af4014f82f1e073")
    version("6.4.1", sha256="ba3cb314ceab9183aeac851e536c5d143933986f3099533edd327ffeb4b48e9b")
    version("6.4.0", sha256="8953bcf13ba1aa03cb29481bd90eaef373bf0e41cadff68e567ecd2ec0b07363")
    version("6.3.3", sha256="b2b77abb5c851674839b583dc313684b5f6aa676e8186ff0a5696b6962c2b4da")
    version("6.3.2", sha256="29aa1ac1a0f684a09fe2ea8a34ae8af3622c27708c7df403a7481e75174e1984")
    version("6.3.1", sha256="512e652483b5580713eca14db3fa633d0441cd7c02cdb0d26e631ea605b9231b")
    version("6.3.0", sha256="240bb1b0f2e6632447e34deae967df259af1eec085470e58a6d0aa040c8530b0")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.2:"):
            return "projects/hipblas-common"
        else:
            return "."
