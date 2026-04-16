# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Rocshmem(CMakePackage):
    """rocSHMEM intra-kernel networking runtime for AMD dGPUs on the ROCm platform."""

    homepage = "https://github.com/ROCm/rocSHMEM"
    url = "https://github.com/ROCm/rocSHMEM/archive/refs/tags/rocm-6.4.0.tar.gz"
    tags = ["rocm"]

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")
    libraries = ["librocshmem"]

    license("MIT")

    version("7.2.0", sha256="22c6851287e635bfa1bf0b23b98d6142440b3ab366d15e2203da362c1497341d")
    version("7.1.1", sha256="610018ac57b5b56954da3ae0d6b5a64fb72fc3228f2e69085c4cd61f901820a8")
    version("7.1.0", sha256="6092bd05976e73262cbb7f48dc55718db389100ad1b36e3baa01db401f0ca222")
    version("7.0.2", sha256="63f5bb31e969c0d38f331e992e7cfd130802a8f66cec9d1fc6bfa73b282ed06a")
    version("7.0.0", sha256="90d9a9915b0ba069b7b6f00b05525c476fa6c4942e4f53d0ba16d911ec68ff94")
    version("6.4.3", sha256="96efeed8640862d9e35e4d8ffe9e6cbfa8efcd9be303e457fd2909f34d776fd8")
    version("6.4.2", sha256="ec070adb6db0622c0c86739db5cb3dcfc40149980bcc49a24b0f5aeea64a0e09")
    version("6.4.1", sha256="35424f49b1060567a63045480eef6c9715ebf9f755f39c2cec2fbf447cce72de")
    version("6.4.0", sha256="fbc8b6a7159901fdeda0d6cc8b97f20740c6cce59ba4a28c2050658cc1eecb81")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    for ver in ["6.4.0", "6.4.1", "6.4.2", "6.4.3", "7.0.0", "7.0.2", "7.1.0", "7.1.1", "7.2.0"]:
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"rocm-cmake@{ver}", when=f"@{ver}")
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on(f"rocprim@{ver}", when=f"@{ver}")
        depends_on(f"rocthrust@{ver}", when=f"@{ver}")
    for ver in ["7.0.0", "7.0.2", "7.1.0", "7.1.1", "7.2.0"]:
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    depends_on("ucx@1.17: +rocm")
    depends_on("openmpi@5.0.6: fabrics=ucx")

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"rocm-(\d+\.\d+\.\d+)", lib)
        if match:
            return match.group(1)
        return cls.version_from_rocm_version_h(lib)

    @classmethod
    def version_from_rocm_version_h(cls, lib):
        """Get ROCm version from <ROCM_PATH>/include/rocm-core/rocm_version.h"""
        libdir = os.path.dirname(os.path.abspath(lib))
        rocm_prefix = os.path.dirname(libdir)
        header = join_path(rocm_prefix, "include", "rocm-core", "rocm_version.h")
        if not os.path.isfile(header):
            return None
        try:
            with open(header, encoding="utf-8", errors="replace") as f:
                text = f.read()
        except OSError:
            return None
        major_m = re.search(r"^\s*#\s*define\s+ROCM_VERSION_MAJOR\s+(\d+)", text, re.MULTILINE)
        minor_m = re.search(r"^\s*#\s*define\s+ROCM_VERSION_MINOR\s+(\d+)", text, re.MULTILINE)
        patch_m = re.search(r"^\s*#\s*define\s+ROCM_VERSION_PATCH\s+(\d+)", text, re.MULTILINE)
        if not major_m or not minor_m or not patch_m:
            return None
        return "{0}.{1}.{2}".format(major_m.group(1), minor_m.group(1), patch_m.group(1))

    def cmake_args(self):
        args = []
        if self.spec.satisfies("@6.4"):
            args.append(self.define("USE_GPU_IB", False))
        if self.spec.satisfies("@7.1:"):
            args.append(self.define("ROCM_PATH", self.spec["rocm-core"].prefix))
        return args
