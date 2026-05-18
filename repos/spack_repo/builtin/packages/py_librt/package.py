# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLibrt(PythonPackage):
    """Mypyc runtime library."""

    homepage = "https://github.com/mypyc/librt"
    pypi = "librt/librt-0.6.3.tar.gz"

    license("MIT AND PSF-2.0")

    version("0.9.0", sha256="a0951822531e7aee6e0dfb556b30d5ee36bbe234faf60c20a16c01be3530869d")
    version("0.6.3", sha256="c724a884e642aa2bbad52bb0203ea40406ad742368a5f90da1b220e970384aae")

    depends_on("python@3.9:3.14", type=("build", "link", "run"))
    depends_on("c", type="build")
    depends_on("py-setuptools@77.0.3:", type="build")
