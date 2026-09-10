# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIniconfig(PythonPackage):
    """
    iniconfig: brain-dead simple parsing of ini files
    """

    pypi = "iniconfig/iniconfig-1.1.1.tar.gz"

    license("MIT")

    version("2.1.0", sha256="3abbd2e30b36733fee78f9c7f7308f2d0050e88f0087fd25c2645f63c773e1c7")
    version("2.0.0", sha256="2d91e135bf72d31a410b17c16da610a82cb55f6b0477d1a902134b24a455b8b3")
    version("1.1.1", sha256="bc3af051d7d14b2ee5ef9969666def0cd1a000e121eaea580d4a313df4b37f32")

    depends_on("python@3.8:", when="@2.1:", type=("build", "run"))
    depends_on("python@3.7:", when="@2:", type=("build", "run"))
    depends_on("py-hatchling@1.26:", when="@2.1:", type="build")
    depends_on("py-hatchling", when="@2", type="build")
    depends_on("py-hatch-vcs", when="@2", type="build")

    # Historical dependencies
    depends_on("py-setuptools@41.2:", when="@1", type="build")
    depends_on("py-setuptools-scm@4:", when="@1", type="build")
