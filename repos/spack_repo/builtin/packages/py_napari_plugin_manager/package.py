# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNapariPluginManager(PythonPackage):
    """The napari plugin manager provides a graphical user interface for
    installing napari plugins."""

    homepage = "https://github.com/napari/napari-plugin-manager"
    pypi = "napari_plugin_manager/napari_plugin_manager-0.1.7.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.1.7", sha256="858adeacfc65bb8ed92e875659999a51c06188a6c813ebef54f5248e27dd5a74")

    depends_on("python@3.10:", type=("build", "run"))

    depends_on("py-setuptools@77:", type="build")
    depends_on("py-setuptools-scm +toml", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-npe2")
        depends_on("py-qtpy")
        depends_on("py-superqt")
        depends_on("py-packaging")
        depends_on("py-pip")
        # Other dependencies include napari - but that'd be circular

    patch("clean_pyproject_toml.patch")
