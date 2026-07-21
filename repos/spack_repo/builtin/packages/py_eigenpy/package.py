# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class PyEigenpy(CMakePackage):
    """Efficient bindings between Numpy and Eigen using Boost.Python"""

    homepage = "https://github.com/stack-of-tasks/eigenpy"
    git = "https://github.com/stack-of-tasks/eigenpy.git"

    maintainers("nim65s")

    license("BSD-2-Clause", checked_by="nim65s")

    version("develop", branch="devel")
    version("3.12.0", "8564b96c1f7d5a53d4330b0e9ecbf9e0815319bbe43cdf9e9488a4e9b9aa7ce6")

    depends_on("cxx", type="build")
    depends_on("eigen")
    depends_on("boost+python")
    depends_on("py-numpy")
    extends("python")

    # fixes for Eigen 5. Merged upstream.
    patch(
        "https://github.com/stack-of-tasks/eigenpy/commit/0bb71c7da9c297a334f2de419df13ba2c7a67312.patch?full_index=1",
        sha256="812274fc7fa68e3af3ede5324590aa2e7ae06f264ac1927989dfe6e324374791",
        when="@:3.12.0 ^eigen@5:",
    )
    patch(
        "https://github.com/stack-of-tasks/eigenpy/commit/a64334c3ddbdd9ffd9f3b65a0b9c1e0d1d2b8c96.patch?full_index=1",
        sha256="2110114b6467e5e2889ea55b9e3b2ef5f8cc965a914bfd62d2335e526551d421",
        when="@:3.12.0 ^eigen@5:",
    )
    patch(
        "https://github.com/stack-of-tasks/eigenpy/commit/2a4adb8af92eebd1dac321010db040797100b91d.patch?full_index=1",
        sha256="ef47a99123a391c6d3a7be683d5667b3d2f94562d1b4a6c8284c8acc1928b4c2",
        when="@:3.12.0 ^eigen@5:",
    )

    def url_for_version(self, version):
        return f"https://github.com/stack-of-tasks/eigenpy/archive/refs/tags/v{version}.tar.gz"

    def cmake_args(self):
        return [
            self.define("BUILD_TESTING", self.run_tests),
            self.define("BUILD_TESTING_SCIPY", False),
        ]
