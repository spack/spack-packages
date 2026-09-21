# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class FastlowessCpp(CargoPackage):
    """High-performance LOWESS (Locally Weighted Scatterplot Smoothing)
    C++ bindings, implemented in Rust."""

    homepage = "https://github.com/thisisamirv/lowess-project"
    url = "https://github.com/thisisamirv/lowess-project/archive/refs/tags/v4.1.0.tar.gz"
    git = "https://github.com/thisisamirv/lowess-project.git"

    maintainers("thisisamirv")

    license("MIT OR Apache-2.0", checked_by="thisisamirv")

    # version() lines below are appended/updated by release-cpp.yml's
    # spack-release job on every release; keep newest first.
    version("4.1.0", sha256="ec0e99ac8f53ad80105eb47891569298e1e02d4068b6be89ab248e56cddbc8fa")
    version(
        "4.0.0",
        sha256="56f277da4a7f5beeebe822f4827d33d35430087bc68b99e044dae76825d17c90",
    )
    version(
        "3.2.1",
        sha256="418d0620a1fcf9ef81910fc89d891edccb123bebc3dd07b359933e42801043e1",
    )
    version(
        "3.1.0",
        sha256="610a6af65a3e8eaa5483332c256e7ce6c3fe2b7ac3ec0f04e08ecd70bf6abe0f",
    )

    depends_on("c", type="build")
    depends_on("rust@1.89:", type="build")

    @property
    def headers(self):
        return find_headers("fastlowess", root=self.prefix.include, recursive=False)

    @property
    def libs(self):
        return find_libraries("libfastlowess_cpp", root=self.prefix, recursive=True)

    def build(self, spec, prefix):
        # bindings/cpp is a member of the repo's Cargo workspace, so the
        # build output lands in target/release at the workspace root, not
        # under bindings/cpp/target -- build by package name instead of cd'ing.
        cargo("build", "--release", "--lib", "-p", "fastlowess-cpp")

    def install(self, spec, prefix):
        mkdirp(prefix.include)
        mkdirp(prefix.lib)
        include_dir = join_path("bindings", "cpp", "include")
        install(join_path(include_dir, "fastlowess.hpp"), prefix.include)
        install(join_path(include_dir, "fastlowess.h"), prefix.include)

        release_dir = join_path("target", "release")
        if spec.satisfies("platform=windows"):
            mkdirp(prefix.bin)
            install(join_path(release_dir, "fastlowess_cpp.dll"), prefix.bin)
            install(join_path(release_dir, "fastlowess_cpp.dll.lib"), prefix.lib)
        elif spec.satisfies("platform=darwin"):
            install(join_path(release_dir, "libfastlowess_cpp.dylib"), prefix.lib)
        else:
            install(join_path(release_dir, "libfastlowess_cpp.so"), prefix.lib)
        install(join_path(release_dir, "libfastlowess_cpp.a"), prefix.lib)
