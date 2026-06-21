# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import sys

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class OpenclClhpp(CMakePackage):
    """C++ headers for OpenCL development"""

    homepage = "https://www.khronos.org/registry/OpenCL/"
    url = "https://github.com/KhronosGroup/OpenCL-CLHPP/archive/v2.0.12.tar.gz"
    maintainers("lorddavidiii")

    license("Apache-2.0")

    version(
        "2025.07.22", sha256="c1031afde6e9eb042e6fcfbc17078f4b437a7e8d55482a1ca6e0fa762d262a89"
    )
    version(
        "2024.10.24", sha256="51aebe848514b3bc74101036e111f8ee98703649eec7035944831dc6e05cec14"
    )
    version(
        "2024.05.08", sha256="22921fd23ca72a21ac5592861d64e7ea53cd8a705fccd73905911f8489519a0b"
    )
    version(
        "2023.12.14", sha256="9106700634e79cfa0935ebd67197f64689ced24c42da702acf18fa8435bd8a82"
    )
    version(
        "2023.04.17", sha256="179243843c620ef6f78b52937aaaa0a742c6ff415f9aaefe3c20225ee283b357"
    )
    version(
        "2023.02.06", sha256="2726106df611fb5cb65503a52df27988d80c0b8844c8f0901c6092ab43701e8c"
    )
    version(
        "2022.09.30", sha256="999dec3ebf451f0f1087e5e1b9a5af91434b4d0c496d47e912863ac85ad1e6b2"
    )
    version(
        "2022.09.23", sha256="2427058a8729344138d5251158c7bd76b45628838e1fbcf2732ec19d9a121b01"
    )
    version(
        "2022.05.18", sha256="d29affd740c5037b4499790613f5af0718ffc88c325e793b73cb35b7592fc0f7"
    )
    version("2.0.16", sha256="869456032e60787eed9fceaeaf6c6cb4452bc0ff97e0f5a271510145a1c8f4d4")
    version("2.0.15", sha256="0175806508abc699586fc9a9387e01eb37bf812ca534e3b493ff3091ec2a9246")
    version("2.0.14", sha256="c8821a7638e57a2c4052631c941af720b581edda634db6ab0b59924c958d69b6")
    version("2.0.13", sha256="8ff0d0cd94d728edd30c876db546bf13e370ee7863629b4b9b5e2ef8e130d23c")
    version("2.0.12", sha256="20b28709ce74d3602f1a946d78a2024c1f6b0ef51358b9686612669897a58719")
    version("2.0.11", sha256="ffc2ca08cf4ae90ee55f14ea3735ccc388f454f4422b69498b2e9b93a1d45181")
    version("2.0.10", sha256="fa27456295c3fa534ce824eb0314190a8b3ebd3ba4d93a0b1270fc65bf378f2b")
    version("2.0.9", sha256="ba8ac4977650d833804f208a1b0c198006c65c5eac7c83b25dc32cea6199f58c")

    depends_on("c", type="build", when="@:2")
    depends_on("cxx", type="build")

    depends_on("opencl-c-headers", when="@2022.05.18:")
    depends_on("cmake@3.16:", type="build", when="@2024.10.24:")

    def cmake_args(self):
        # Disable testing the headers
        return [
            "-DBUILD_DOCS=OFF",
            "-DBUILD_TESTS=OFF",
            "-DBUILD_EXAMPLES=OFF",
            "-DBUILD_TESTING=OFF",
        ]

    @run_after("install")
    def post_install(self):
        if sys.platform == "darwin":
            ln = which("ln", required=True)
            ln("-s", prefix.include.CL, prefix.include.OpenCL)
