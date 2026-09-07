# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Lo2s(CMakePackage):
    """Linux OTF2 Sampling - A Lightweight Node-Level Performance Monitoring Tool"""

    homepage = "https://tu-dresden.de/zih/forschung/projekte/lo2s"
    url = "https://github.com/tud-zih-energy/lo2s/releases/download/v1.8.0/lo2s-v1.8.0.tar.bz2"

    license("BSD-3-Clause OR GPL-2.0-only OR GPL-3.0-or-later", checked_by="nboelte")

    version("1.8.0", sha256="da0b67b4475507c301a096d2d100ad52ad4e810d1ce641e49807a011921370d4")
    version("1.6.0", sha256="1508438ef75531824db0166693d376245ab76ef0347b8344e67b9ca58ce11a55")
    version("1.5.0", sha256="02aacdb77b90ef806f48d6b989bf918d0dd4db2c88853508923b49720e20a048")
    version("1.4.0", sha256="2f4cfda0b567cb7733d23bea8be94279d1e0b438bb7310136dc5b7f59a7388fb")
    version("1.3.0", sha256="3faa91005c34ca29989f247acc1a542dab8dd3a477bc1b7766801facac021016")
    version("1.2.2", sha256="5193cb86b33ec20d63351aa8fa6d1cf149f442d5a4cf4e2e25432cb35a292035")
    version("1.2.1", sha256="7c2e7fa6cb39b0b0a28f23567084948581a8014a1195e75fc721541890e15dc7")
    version("1.2.0", sha256="8672e63a378d51f44f8b1f6e944af066363209e8b880207f4f11d9e2063125f6")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("elfutils+debuginfod")
    depends_on("libpfm4")
    depends_on("lm-sensors")
    depends_on("otf2@3.1")
