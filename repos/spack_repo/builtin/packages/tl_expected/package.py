# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class TlExpected(CMakePackage):
    """C++11/14/17 std::expected with functional-style extensions."""

    homepage = "https://tl.tartanllama.xyz/en/latest/"
    url = "https://github.com/TartanLlama/expected/archive/refs/tags/v1.0.0.tar.gz"
    git = "https://github.com/TartanLlama/expected.git"

    maintainers("charmoniumQ")

    license("CC0-1.0", checked_by="wdconinc")

    version("1.2.0", sha256="f5424f5fc74e79157b9981ba2578a28e0285ac6ec2a8f075e86c41226fe33386")
    version("1.1.0", sha256="1db357f46dd2b24447156aaf970c4c40a793ef12a8a9c2ad9e096d9801368df6")
    version("1.0.0", sha256="8f5124085a124113e75e3890b4e923e3a4de5b26a973b891b3deb40e19c03cee")

    depends_on("cxx", type="build")
