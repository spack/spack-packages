# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEinopsExts(PythonPackage):
    """Einops extensions."""

    homepage = "https://github.com/lucidrains/einops-exts"
    pypi = "einops-exts/einops-exts-0.0.4.tar.gz"

    license("MIT", checked_by="V-Karch")

    version("0.0.4", sha256="616f145b3411f8e9e3be5da5c968bbe372e55c249de11faa909c7a4b74580a6c")

    depends_on("py-setuptools", type="build")
    # ModuleNotFoundError: No module named 'torch'
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-einops@0.4:", type=("build", "run"))
