# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRpdsPy(PythonPackage):
    """Python bindings to the Rust rpds crate for persistent data structures."""

    homepage = "https://rpds.readthedocs.io/"
    pypi = "rpds_py/rpds_py-0.20.0.tar.gz"
    git = "https://github.com/crate-py/rpds.git"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("2026.6.3", sha256="1cebd1337c242e4ec2293e541f712b2da849b29f48f0c293684b71c0632625d4")
    version("0.27.1", sha256="26a1c73171d10b7acccbded82bf6a586ab8203601e565badc74bbbf8bc5a10f8")
    version("0.20.0", sha256="d72a210824facfdaf8768cf2d7ca25a042c30320b3020de2fa04640920d4e121")
    version("0.18.1", sha256="dc48b479d540770c811fbd1eb9ba2bb66951863e448efec2e2c102625328e92f")

    with default_args(type="build"):
        depends_on("c")

        depends_on("py-maturin@1.9:1", when="@0.25:")
        depends_on("py-maturin@1.2:1", when="@0.19.1:0.25.1")
        depends_on("py-maturin@1.0:1", when="@:0.19.0")

        # retrieved via cargo msrv
        depends_on("rust@1.85:", when="@0.25:")
        depends_on("rust@1.76:", when="@0.19:")
        depends_on("rust@1.60:")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:", when="@2026.5.1:")
        depends_on("python@3.10:", when="@0.21:")
        depends_on("python@3.9:", when="@0.21:")
        depends_on("python@3.8:", when="@:0.20")
