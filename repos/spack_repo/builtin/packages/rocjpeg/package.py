# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Rocjpeg(CMakePackage):
    """rocJPEG is a high-performance jpeg decode SDK for decoding jpeg images
    using a hardware-accelerated jpeg decoder on AMD's GPUs."""

    homepage = "https://github.com/ROCm/rocJPEG"
    git = "https://github.com/ROCm/rocJPEG.git"
    url = "https://github.com/ROCm/rocJPEG/archive/refs/tags/rocm-6.4.2.tar.gz"
    tags = ["rocm"]

    maintainers("afzpatel", "srekolam", "renjithravindrankannath")

    license("MIT")
    version("7.1.1", sha256="38ed6ad6aa6de3f830a157297ff239caa1a65010e7b4200891d37b7f31378f4b")
    version("7.1.0", sha256="26ea59dd772c57ae5476a6ba3799bf86981694fbba9b87af882ed76c1b89c639")
    version("7.0.2", sha256="fe1813e333dfb958d74693301ffb70e1baa2601ffd8b8d644f4026e56048164a")
    version("7.0.0", sha256="00dfac45d1776f5e79704fc56bae1b5017fc19326f69e363a49285ebf72bff2e")
    version("6.4.3", sha256="28c95c30603d6a0e39632cd31e8adcbe80786f5d77e15bb88cfef341eaf4eb94")
    version("6.4.2", sha256="543d0a25b7da44885c99845041a54f391f484e0f1e051973c5993f08185d82fa")
    version("6.4.1", sha256="23eed12646409d8f931f6bbdacf68df246c762877a3c0ef723568f89f0f5b40f")
    version("6.4.0", sha256="5488f5ab9c475566716d99ad32fb4c20686ac1bcc00c9242221abdbde2b94ffe")
    version("6.3.3", sha256="65081b20ab3df82337fdcaf3d4e614c75f946656a4ea7bc00ac0d1bbd81e3e83")
    version("6.3.2", sha256="4e1ec9604152e818afa85360f1e0ef9e98bfb8a97ca0989980063e2ece015c16")
    version("6.3.1", sha256="f4913cbc63e11b9b418d33b0f9ba0fec0aa00b23285090acfd435e1ba1c21e42")
    version("6.3.0", sha256="2623b8f8bb61cb418d00c695e8ff0bc5979e1bb2d61d6c327a27d676c89e89cb")

    depends_on("cxx", type="build")

    for ver in [
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
    ]:
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"hip@{ver}", when=f"@{ver}")

    depends_on("libva", type="build", when="@6.2:")
    depends_on("libdrm", type="build", when="@6.4:")
    patch("0001-add-amdgpu-drm-include.patch", when="@6.4")

    def patch(self):
        filter_file(
            r"${ROCM_PATH}/lib/llvm/bin/clang++",
            "{0}/bin/clang++".format(self.spec["llvm-amdgpu"].prefix),
            "CMakeLists.txt",
            string=True,
        )

    def cmake_args(self):
        args = [self.define("LIBVA_INCLUDE_DIR", self.spec["libva"].prefix.include)]
        if self.spec.satisfies("@6.4.0:"):
            args.append(
                self.define("CMAKE_C_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang")
            )
            args.append(
                self.define(
                    "CMAKE_CXX_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++"
                )
            )
        if self.spec.satisfies("@6.4"):
            args.append(self.define("AMDGPU_DRM_INCLUDE_DIRS", self.spec["libdrm"].prefix.include))
        if self.spec.satisfies("@7.0:"):
            args.append(
                self.define("LIBDRM_AMDGPU_INCLUDE_DIR", self.spec["libdrm"].prefix.include)
            )
            args.append(self.define("LIBDRM_AMDGPU_LIBRARY", self.spec["libdrm"].prefix.lib))
        return args
