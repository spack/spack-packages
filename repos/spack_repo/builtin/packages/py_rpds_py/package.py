# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRpdsPy(PythonPackage):
    """Python bindings to the Rust rpds crate for persistent data structures."""

    homepage = "https://rpds.readthedocs.io/"
    pypi = "rpds_py/rpds_py-0.20.0.tar.gz"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version(
        "0.30.0", sha256="dd8ff7cf90014af0c0f787eea34794ebf6415242ee1d6fa91eaba725cc441e84"
    )  # FIXME
    version(
        "0.29.0", sha256="fe55fe686908f50154d1dc599232016e50c243b438c3b7432f24e2895b0e5359"
    )  # FIXME
    version(
        "0.28.0", sha256="abd4df20485a0983e2ca334a216249b6186d6e3c1627e106651943dbdb791aea"
    )  # FIXME
    version("0.27.1", sha256="26a1c73171d10b7acccbded82bf6a586ab8203601e565badc74bbbf8bc5a10f8")
    version("0.20.0", sha256="d72a210824facfdaf8768cf2d7ca25a042c30320b3020de2fa04640920d4e121")
    version("0.18.1", sha256="dc48b479d540770c811fbd1eb9ba2bb66951863e448efec2e2c102625328e92f")

    depends_on("c", type="build")

    depends_on("python@3.10:", type="build", when="@0.28:")
    depends_on("python@3.9:", type="build", when="@0.21:0.27")
    depends_on("python@3.8:", type="build", when="@:0.20")
    depends_on("py-maturin@1.9:1", type="build", when="@0.25:")
    depends_on("py-maturin@1.2:1", type="build", when="@0.19.1:0.25.1")
    depends_on("py-maturin@1.0:1", type="build", when="@:0.19.0")

    # retrieved via cargo msrv
    depends_on("rust@1.85:", type="build", when="@0.25:")
    depends_on("rust@1.76:", type="build", when="@0.19:")
    depends_on("rust@1.60:", type="build")
