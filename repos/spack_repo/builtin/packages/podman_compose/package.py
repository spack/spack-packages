# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install podman-compose
#
# You can edit this file again by typing:
#
#     spack edit podman-compose
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------
import sys

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *
class PodmanCompose(PythonPackage):
    """An container composition tool for Podman"""
    homepage = "https://podman.io"
    url = "https://github.com/containers/podman-compose/archive/refs/tags/v1.4.0.tar.gz"
    maintainers("scothalverson")
    license("Apache-2.0")
    version("1.4.0", sha256="167860361357f32e09660342756442ac6f9adf182f00ade1309b550de48ed494")
    depends_on("podman")
    depends_on("py-setuptools")
    depends_on("py-pyyaml")
    depends_on("py-python-dotenv")

