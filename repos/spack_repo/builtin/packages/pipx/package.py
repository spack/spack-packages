# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Pipx(Package):
    """pipx is a tool to install and run Python applications in isolated environments"""

    homepage = "https://pipx.pypa.io/"
    url = "https://github.com/pypa/pipx/releases/download/1.8.0/pipx.pyz"

    license("MIT")

    maintainers("ebagrenrut")

    with default_args(expand=False):
        version("1.8.0", sha256="b9eabd835dffe0677e36bd99416fc9837c592bd8c079235379bed3dfe043c601")
        version("1.7.1", sha256="1d4f46f86830640f1d7c4e29b280a7a42265d6e8af2c063f40baed4513f03ae8")
        version("1.6.0", sha256="ae4f39e8916e2a0c3699393b1d9c63947388e11ea438d18f7fc51f55f7de1ded")
        version("1.5.0", sha256="d307772eb52df8f4dd7b38523adbe2105a61b5e90c1be34e2f8007be9bd4001f")
        version("1.4.3", sha256="949221fa7128df4641f1e62daff7c85a3dd05e1132a93e53a909e00fc3c9a32c")
        version("1.3.3", sha256="348b59b82b1ba9032513d36c2ea03ad3a34e45805ef8de7638a047673ee8b4cb")
        version("1.2.1", sha256="87fcfde6063d74ca0d5df973d3b9486496880747c808f983fb096a29fd9e07d8")
        version("1.2.0", sha256="93c46f2d254dc17168fa92d413eaabb0fdd050ff04912d8e0f3e03f4bc256b8c")

    conflicts("platform=windows")

    depends_on("python@3.9:", when="@1.8:", type="run")
    depends_on("python@3.8:", when="@1.3:", type="run")
    depends_on("python@3.7:", type="run")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(self.stage.archive_file, join_path(prefix.bin, "pipx"))
        set_executable(join_path(prefix.bin, "pipx"))

    # ========================================================================
    # Set up environment to make install easier for pipx-installed packages
    # ========================================================================
    def setup_dependent_package(self, module, dependent_spec):
        """Called before Pipx modules' install() method."""
        # Pipx builds can have a global `pipx` executable function
        module.pipx = Executable(join_path(self.spec.prefix.bin, "pipx"))
