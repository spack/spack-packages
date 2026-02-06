# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class HsaAmdAqlprofile(CMakePackage):
    """Architected Queuing Language Profiling Library
    AQLprofile is an open source library that enables advanced
    GPU profiling and tracing on AMD platforms"""

    homepage = "https://github.com/ROCm/aqlprofile"
    url = "https://github.com/ROCm/aqlprofile/archive/refs/tags/rocm-7.0.0.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    version("7.1.1", sha256="0137f429a551c431a81f613e114b247d7e269ab9201154d6c87fe7fc86987a66")
    version("7.1.0", sha256="19964494662243773a89c8f20e78a6903b5c886fdb472703b6c9f5bec36d3120")
    version("7.0.2", sha256="1c56781bf40e7195b1dd670b8f05ecc0b2007c57c0a0b80fea97dfaa9999e8e3")
    version("7.0.0", sha256="25f040c867e22f4a0b4147317133dc50eccf60e72fc2c91e8d25083fa84c313e")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    for ver in ["7.0.0", "7.0.2", "7.1.0", "7.1.1"]:
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
