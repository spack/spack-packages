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
    git = "https://github.com/ROCm/rocm-systems"
    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "afzpatel")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/aqlprofile/archive/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-systems/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.1", sha256="201f19174eafbace2f7abf0d1178ebb17db878191276aba6d23f0e1758b0e10f")
    version("7.2.0", sha256="728ea7e9bf16e6ed217a0fd1a8c9afaba2dae2e7908fa4e27201e67c803c5638")
    version("7.1.1", sha256="0137f429a551c431a81f613e114b247d7e269ab9201154d6c87fe7fc86987a66")
    version("7.1.0", sha256="19964494662243773a89c8f20e78a6903b5c886fdb472703b6c9f5bec36d3120")
    version("7.0.2", sha256="1c56781bf40e7195b1dd670b8f05ecc0b2007c57c0a0b80fea97dfaa9999e8e3")
    version("7.0.0", sha256="25f040c867e22f4a0b4147317133dc50eccf60e72fc2c91e8d25083fa84c313e")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    for ver in ["7.0.0", "7.0.2", "7.1.0", "7.1.1", "7.2.0", "7.2.1"]:
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@:7.1"):
            return "."
        else:
            return "projects/aqlprofile"
