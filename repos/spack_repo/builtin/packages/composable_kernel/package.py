# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class ComposableKernel(CMakePackage):
    """Composable Kernel: Performance Portable Programming Model
    for Machine Learning Tensor Operators."""

    homepage = "https://github.com/ROCm/composable_kernel"
    git = "https://github.com/ROCm/rocm-libraries.git"

    tags = ["rocm"]
    maintainers("srekolam", "afzpatel")
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/composable_kernel/archive/refs/tags/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-libraries/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.1", sha256="bc5140deec3b1c93c13796a8a6d2cb7e50aa87fd89f60f87c8d801d66f2fd156")
    version("7.2.0", sha256="8ad5f4a11f1ed8a7b927f2e65f24083ca6ce902a42021a66a815190a91ccb654")
    version("7.1.1", sha256="e1174a4b6faa12ef31dac0324547fd49aca09fee380bd89ecd49a44bb34b72cc")
    version("7.1.0", sha256="03c7fffcad2aed373486315266fdf9dd400a280d383b543ff48ebd3acb3f985f")
    version("7.0.2", sha256="b7293e3451750f606ab845585b3dd4eb4e185d4dda4a22290d73e8874a45a26b")
    version("7.0.0", sha256="20593d704608f39edfdfe0075ca030471b7df32ae594a5f4d8762a59bb012108")
    version("6.4.3", sha256="70d9a2da51d7967e95329884dbd0154753b3ffaecd7272501c59e951bb5160cc")
    version("6.4.2", sha256="6e2acd889d7558f3be88915f249496394a690dd5d7675c36e4053e3856b51567")
    version("6.4.1", sha256="6db4d36673da6506ca52625b3bd40c29d3b376d31a224fd221ffe60cf97564bf")
    version("6.4.0", sha256="8dbfea0bdc4950ca60e8d1ea43edf1f515c4a34e47ead951415c49a0669a3baf")
    version("6.3.3", sha256="b7102efba044455416a6127af1951019fe8365a653ea7eb0b1d83bb4542c9309")
    version("6.3.2", sha256="875237fe493ff040f8f63b827cddf2ff30a8d3aa18864f87d0e35323c7d62a2d")
    version("6.3.1", sha256="3e8c8c832ca3f9ceb99ab90f654b93b7db876f08d90eda87a70bc629c854052a")
    version("6.3.0", sha256="274f87fc27ec2584c76b5bc7ebdbe172923166b6b93e66a24f98475b44be272d")
    version("6.2.4", sha256="5598aea4bce57dc95b60f2029831edfdade80b30a56e635412cc02b2a6729aa6")
    version("6.2.1", sha256="708ff25218dc5fa977af4a37105b380d7612a70c830fa7977b40b3df8b8d3162")
    version("6.2.0", sha256="4a3024f4f93c080db99d560a607ad758745cd2362a90d0e8f215331686a6bc64")
    version("6.1.2", sha256="54db801e1c14239f574cf94dd764a2f986b4abcc223393d55c49e4b276e738c9")
    version("6.1.1", sha256="f55643c6eee0878e8f2d14a382c33c8b84af0bdf8f31b37b6092b377f7a9c6b5")
    version("6.1.0", sha256="355a4514b96b56aa9edf78198a3e22067e7397857cfe29d9a64d9c5557b9f83d")
    version("6.0.2", sha256="f648a99388045948b7d5fbf8eb8da6a1803c79008b54d406830b7f9119e1dcf6")
    version("6.0.0", sha256="a8f736f2f2a8afa4cddd06301205be27774d85f545429049b4a2bbbe6fcd67df")
    version("5.7.1", sha256="75f66e023c2e31948e91fa26366eaeac72d871fc2e5188361d4465179f13876e")
    version("5.7.0", sha256="d9624dbaef04e0138f9f73596c49b4fe9ded69974bae7236354baa32649bf21a")

    amdgpu_targets = ROCmPackage.amdgpu_targets
    variant(
        "amdgpu_target",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
        description="set gpu targets",
    )

    depends_on("cxx", type="build")  # generated

    depends_on("python", type="build")
    depends_on("z3", type="build")
    depends_on("zlib", type="build")
    depends_on("ncurses+termlib", type="build")
    depends_on("bzip2", type="build")
    depends_on("sqlite", type="build")
    depends_on("half", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("cmake@3.16:", type="build")

    generator("ninja")

    for ver in [
        "7.2.1",
        "7.2.0",
        "7.1.1",
        "7.1.0",
        "7.0.2",
        "7.0.0",
        "6.4.3",
        "6.4.2",
        "6.4.1",
        "6.4.0",
        "6.3.3",
        "6.3.2",
        "6.3.1",
        "6.3.0",
        "6.2.4",
        "6.2.1",
        "6.2.0",
        "6.1.2",
        "6.1.1",
        "6.1.0",
        "6.0.2",
        "6.0.0",
        "5.7.1",
        "5.7.0",
    ]:
        depends_on("hip+rocm@" + ver, when="@" + ver)
        depends_on("llvm-amdgpu@" + ver, when="@" + ver)
        depends_on("rocm-cmake@" + ver, when="@" + ver, type="build")

    # Build is breaking on warning, -Werror, -Wunused-parameter. The patch is part of:
    # https://github.com/ROCm/composable_kernel/commit/959073842c0db839d45d565eb260fd018c996ce4
    patch("0001-mark-kernels-maybe-unused.patch", when="@6.2")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.2:"):
            return "projects/composablekernel"
        else:
            return "."

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("CXX", self.spec["hip"].hipcc)

    def cmake_args(self):
        spec = self.spec
        args = [
            self.define(
                "CMAKE_CXX_COMPILER", "{0}/bin/clang++".format(spec["llvm-amdgpu"].prefix)
            ),
            self.define("CMAKE_C_COMPILER", "{0}/bin/clang".format(spec["llvm-amdgpu"].prefix)),
            self.define("CMAKE_BUILD_TYPE", "Release"),
            self.define("CMAKE_POSITION_INDEPENDENT_CODE", "ON"),
        ]
        if "auto" not in self.spec.variants["amdgpu_target"]:
            args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
        else:
            args.append(self.define("INSTANCES_ONLY", "ON"))
        if self.run_tests:
            args.append(self.define("BUILD_TESTING", "ON"))
        elif self.spec.satisfies("@:6.1"):
            args.append(self.define("INSTANCES_ONLY", "ON"))
        if self.spec.satisfies("@:5.7"):
            args.append(self.define("CMAKE_CXX_FLAGS", "-O3"))
        if self.spec.satisfies("@6.2:"):
            args.append(self.define("BUILD_DEV", "OFF"))
        return args
