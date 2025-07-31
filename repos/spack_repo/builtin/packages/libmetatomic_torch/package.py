# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class LibmetatomicTorch(CMakePackage):
    """TorchScript/C++ bindings to metatomic"""

    homepage = "https://docs.metatensor.org/metatomic"
    url = "https://github.com/metatensor/metatomic/releases/download/metatomic-torch-v0.1.2/metatomic_torch-0.1.2.tar.gz"
    git = "https://github.com/metatensor/metatomic.git"

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.1.3", sha256="60a4b651cf6e15f175879af74d18215d45cc4fd5e42a61242a180e2014fe9fd2")
    version("0.1.2", sha256="0d793b16b3d6eee915c89e9b1a385143ec2dbb6dc451bed8feee3a2445b3f63e")
    version("0.1.1", sha256="5b2ea0da270399a315d15551ae09fe80750fc1ef10fcca07fac73bd97bbab9aa")
    version("0.1.0", sha256="7a8a72030361d854e934e9022499c30c457b91df9f3e4e82da842d5a37a913c4")

    depends_on("cmake@3.16:", type="build")
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("libmetatensor-torch@0.7.6:", type=("build", "run"))
    depends_on("py-torch@2.1.0:2.7.0")
