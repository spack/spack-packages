# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Hipfort(CMakePackage):
    """Radeon Open Compute Parallel Primitives Library"""

    homepage = "https://github.com/ROCm/hipfort"
    git = "https://github.com/ROCm/hipfort.git"
    url = "https://github.com/ROCm/hipfort/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    license("MIT")

    maintainers("cgmb", "srekolam", "renjithravindrankannath", "afzpatel")
    version("7.2.1", sha256="a908ed8a3f871581e55166fdbfdd24ab97d1a5ff91573b552ed3cae89607c298")
    version("7.2.0", sha256="0e59a7fd503ed4a76db89b3c679658108d3f0a7e6730ecfb7555087b203805c8")
    version("7.1.1", sha256="4e1e1aafc6eec9cabed3c90777591a15b033b8f9a58cacbaadf92cc21fcd896f")
    version("7.1.0", sha256="b4e74b92919e59cbccbc0baf611f49d50e7d160d2fda86e6eb2aed78ff20f89c")
    version("7.0.2", sha256="25de35f1d261f82a6022b0eb0322167398971bde3d48483f8936f3341b510ab2")
    version("7.0.0", sha256="7b6f7033ec4b73934bd1b04a396f9e920eac5f5a2c17d06fc2a74aeb38b2f27f")
    version("6.4.3", sha256="6cfd4f704ee4f156d15afa30b8e029a4af336a6cb60fe4f6ca6fb85c86a266bd")
    version("6.4.2", sha256="28f83c278bffb5a07469466061a4e6a76dce1030bcb7d16aa73da803181e532b")
    version("6.4.1", sha256="4981ab58a59da29b79bb038cd3438e84bf5a7f246b1de4c41d3fec6a11d37294")
    version("6.4.0", sha256="a2e4c10f1c6561789208ba5a41a00b562c8048ec503339cb4eed236ee3cf6131")
    version("6.3.3", sha256="dacb7d5a30689e6a8f81ec251daaa4a74b40f1d28145953c7d42ccd29cecee7c")
    version("6.3.2", sha256="d2438971199637eb2e09519c1f2300cdd7a84b4d948034a7cd1ce3e441faf5de")
    version("6.3.1", sha256="8141bf3d05ab4f91c561815134707123e3d06486bf775224b9a3a4cc8ee8f56f")
    version("6.3.0", sha256="9e7f4420c75430cdb9046c0c4dbe656f22128b0672b2e261d50a6e92e47cc6d3")
    version("6.2.4", sha256="32daa4ee52c2d44790bff7a7ddde9d572e4785b2f54766a5e45d10228da0534b")
    version("6.2.1", sha256="5258f2dd63aeebe29ce566e654c47b8e2e1f5eb8ca3da92af09c54517b259f32")
    version("6.2.0", sha256="7f6db61a0ac7771e5c4604a6113b36736f6c7f05cabd7e1df8e832c98b87311d")
    version("6.1.2", sha256="f60d07fa3e5b09246c8908b2876addf175a91e91c8b0fac85b000f88b6743c7c")
    version("6.1.1", sha256="646f7077399db7a70d7102fda8307d0a11039f616399a4a06a64fd824336419f")
    version("6.1.0", sha256="70d3ccc9f3536f62686e73934f5972ed011c4df7654ed1f8e6d2d42c4289f47e")
    version("6.0.2", sha256="b60ada7474b71c1d82c700b0159bc0756dbb2808375054903710280b1677f199")
    version("6.0.0", sha256="151cf11648885db799aade0d00a7882589e7195643b02beaa251f1b2a43aceed")
    version("5.7.1", sha256="859fac509e195f3ab97c555b5f63afea325a61aae0f281cb19a970a1b533dead")
    version("5.7.0", sha256="57b04d59f61683a1b141d6d831d10c9fdecea483991ec02d14c14e441e935c05")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3.0.2:", type="build")

    depends_on("rocm-cmake@3.8.0:", type="build")

    depends_on("binutils", when="%cce")

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
    ]:
        depends_on(f"hip@{ver}", type="build", when=f"@{ver}")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CXX", self.spec["hip"].hipcc)

    def cmake_args(self):
        args = ["-DHIPFORT_COMPILER={}".format(env["SPACK_FC"])]

        if self.spec.satisfies("^cmake@3.21.0:3.21.2"):
            args.append(self.define("__skip_rocmclang", "ON"))

        if self.spec.satisfies("%cce"):
            args.append("-DHIPFORT_AR=" + join_path(self.spec["binutils"].prefix.bin, "ar"))
            args.append(
                "-DHIPFORT_RANLIB=" + join_path(self.spec["binutils"].prefix.bin, "ranlib")
            )
            args.append("-DHIPFORT_COMPILER_FLAGS='-ffree -eT'")
        elif self.spec.satisfies("%gcc"):
            args.append("-DHIPFORT_COMPILER_FLAGS='-ffree-form -cpp -ffree-line-length-none'")

        return args
