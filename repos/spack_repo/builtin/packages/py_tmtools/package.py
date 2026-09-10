# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTmtools(PythonPackage):
    """Python bindings around the TM-align code for structural alignment of proteins."""

    homepage = "https://github.com/jvkersch/tmtools"
    git = "https://github.com/jvkersch/tmtools.git"
    pypi = "tmtools/tmtools-0.2.0.tar.gz"

    maintainers("LydDeb")

    license("GPL-3.0-only", checked_by="LydDeb")

    version("0.2.0", sha256="e2d6422f5af91ee41753fb2e9776140785eb818ec83d7aef8a8b2f296f05e72c")

    depends_on("cxx", type="build")
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-pybind11@2.10.4:2.10", type="build")
    depends_on("py-numpy", type=("build", "run"))
