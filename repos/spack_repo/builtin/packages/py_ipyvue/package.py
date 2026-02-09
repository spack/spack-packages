# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIpyvue(PythonPackage):
    """
    Jupyter widgets base for Vue libraries.
    """

    homepage = "https://github.com/widgetti/ipyvue"
    pypi = "ipyvue/ipyvue-1.10.1.tar.gz"

    license("MIT")

    maintainers("jeremyfix")

    version("1.10.2", sha256="a9973586fa2e296510d9a24b935a22a2450acca057b5de9f0bab66ecb1c33ab4")
    version("1.10.1", sha256="20615ce86ba516cf0b7aad84cc607e4e2c9104232e954cd0eccbf33530a5e1d4")

    depends_on("py-setuptools", type="build")

    depends_on("py-ipywidgets@7:", type=("build", "run"))
