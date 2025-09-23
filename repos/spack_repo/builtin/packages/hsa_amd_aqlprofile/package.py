# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class HsaAmdAqlprofile(CMakePackage):
    """rocm-core is a utility which can be used to get ROCm release version.
    It also provides the Lmod modules files for the ROCm release.
    getROCmVersion function provides the ROCm version."""

    homepage = "https://github.com/ROCm/aqlprofile"
    url = "https://github.com/ROCm/aqlprofile/archive/refs/tags/rocm-7.0.0.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")

    version("7.0.0", sha256="25f040c867e22f4a0b4147317133dc50eccf60e72fc2c91e8d25083fa84c313e")

    for ver in ["7.0.0"]:
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
