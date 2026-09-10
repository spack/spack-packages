# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPywinpty(PythonPackage):
    """Pseudoterminals for Windows in Python."""

    homepage = "https://github.com/andfoy/pywinpty"
    pypi = "pywinpty/pywinpty-3.0.3.tar.gz"
    git = "https://github.com/andfoy/pywinpty.git"

    maintainers("wdconinc")

    license("MIT", checked_by="wdconinc")

    version("3.0.3", sha256="523441dc34d231fb361b4b00f8c99d3f16de02f5005fd544a0183112bcc22412")

    requires("platform=windows")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", type="build")

    with default_args(type="build"):
        depends_on("py-maturin@1.1:1")
