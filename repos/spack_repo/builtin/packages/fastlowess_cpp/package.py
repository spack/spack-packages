# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ruff: noqa: UP006
# isort: skip_file

import os
import textwrap
from typing import ClassVar, List  # noqa: UP035

from spack.package import *
from spack_repo.builtin.build_systems.cargo import CargoPackage


class FastlowessCpp(CargoPackage):
    """High-performance LOWESS (Locally Weighted Scatterplot Smoothing)
    C++17 bindings, implemented in Rust. Supports batch, streaming, and online
    smoothing, robust outlier handling, confidence and prediction intervals,
    cross-validation, and parallel execution. Provides shared and static
    libraries with an owning C++ interface and a C-compatible API."""

    homepage = "https://thisisamirv.github.io/lowess-project/cpp/"
    url = "https://github.com/thisisamirv/lowess-project/archive/refs/tags/v5.0.0.tar.gz"
    git = "https://github.com/thisisamirv/lowess-project.git"

    test_requires_compiler = True
    sanity_check_is_file: ClassVar[List[str]] = [
        join_path("include", "fastlowess.hpp"),
        join_path("include", "fastlowess.h"),
    ]
    sanity_check_is_dir: ClassVar[List[str]] = ["include", "lib"]

    maintainers("thisisamirv")

    license("MIT OR Apache-2.0", checked_by="thisisamirv")

    # version() lines below are appended/updated by release-cpp.yml's
    # spack-release job on every release; keep newest first.
    version("5.0.0", sha256="5aaddb050b08d9efa5493c4181dc2d59d02c5a87320dd95b415b726df1884007")
    version(
        "4.1.0",
        sha256="ec0e99ac8f53ad80105eb47891569298e1e02d4068b6be89ab248e56cddbc8fa",
    )
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
    depends_on("cxx", type="build")
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
        version_header = join_path(include_dir, "fastlowess_version.h")
        if os.path.isfile(version_header):
            install(version_header, prefix.include)

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

    def test_cxx_smoke(self):
        """Compile and run a linear fit against the installed C++ library."""
        source = "fastlowess_spack_smoke.cpp"
        with open(source, "w", encoding="utf-8") as stream:
            stream.write(
                textwrap.dedent("""\
                #include <fastlowess.hpp>
                #include <cmath>
                #include <vector>

                int main() {
                    const std::vector<double> x = {1, 2, 3, 4, 5, 6};
                    const std::vector<double> y = {3, 5, 7, 9, 11, 13};
                    fastlowess::LowessOptions options;
                    options.fraction = 1.0;
                    options.iterations = 0;
                    options.parallel = false;
                    options.boundary_policy = "noboundary";
                    fastlowess::Lowess model(options);
                    const auto result = model.fit(x, y).value();
                    if (!result.valid() || result.size() != y.size()) return 1;
                    for (std::size_t index = 0; index < y.size(); ++index) {
                        const double fitted = result.y_value(index);
                        if (!std::isfinite(fitted) ||
                            std::abs(fitted - y[index]) > 1e-8) return 2;
                    }
                    return 0;
                }
                """)
            )

        cxx = which(os.environ["CXX"])
        windows = self.spec.satisfies("platform=windows")
        executable = "fastlowess_spack_smoke.exe" if windows else "fastlowess_spack_smoke"
        compiler_name = os.path.basename(os.environ["CXX"]).lower()
        if compiler_name in ("cl", "cl.exe", "clang-cl", "clang-cl.exe"):
            cxx(
                "/std:c++17",
                "/EHsc",
                f"/I{self.prefix.include}",
                source,
                join_path(self.prefix.lib, "fastlowess_cpp.dll.lib"),
                f"/Fe:{executable}",
            )
        else:
            link_flags = (
                [join_path(self.prefix.lib, "fastlowess_cpp.dll.lib")]
                if windows
                else [
                    f"-L{self.prefix.lib}",
                    "-lfastlowess_cpp",
                    f"-Wl,-rpath,{self.prefix.lib}",
                ]
            )
            cxx(
                "-std=c++17",
                f"-I{self.prefix.include}",
                source,
                *link_flags,
                "-o",
                executable,
            )

        smoke = Executable(join_path(os.getcwd(), executable))
        if windows:
            smoke.add_default_env(
                "PATH",
                os.pathsep.join([str(self.prefix.bin), os.environ.get("PATH", "")]),
            )
        smoke()
