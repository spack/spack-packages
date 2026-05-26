# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyF90wrap(PythonPackage):
    """f90wrap is a tool to automatically generate Python extension
    modules which interface to Fortran code that makes use of derived types."""

    homepage = "https://github.com/jameskermode/f90wrap"
    pypi = "f90wrap/f90wrap-0.2.3.tar.gz"

    license("LGPL-3.0-only")

    version("0.3.0", sha256="9c9f08768fe7e9d60de9e913e30909fa1bdc67828f49dffd7149089703d74836")
    version("0.2.6", sha256="e0748eb5e288be7f47829a272fc230373469fb40afccddf91e9973c56da43dd4")
    version("0.2.3", sha256="5577ea92934c5aad378df21fb0805b5fb433d6f2b8b9c1bf1a9ec1e3bf842cff")

    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("py-meson-python@0.12:", type="build")

    # TODO errors with python 3.6 due to UnicodeDecodeError
    depends_on("python@3.9:", type=("build", "run"), when="@0.3:")
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build", when="@:0.2")
    depends_on("py-numpy@2:", type=("build", "run"), when="@0.3:")
    depends_on("py-numpy@1.3:", type=("build", "run"))
