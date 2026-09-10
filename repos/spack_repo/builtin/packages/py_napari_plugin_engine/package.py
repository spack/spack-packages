# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNapariPluginEngine(PythonPackage):
    """napari-plugin-engine is a fork of pluggy modified by the napari team for
    use in napari."""

    homepage = "https://napari-plugin-engine.readthedocs.io/en/latest/"
    pypi = "napari-plugin-engine/napari-plugin-engine-0.2.0.tar.gz"

    maintainers("Markus92")

    license("MIT", checked_by="github_user1")

    version("0.2.0", sha256="fa926f869d70e0d652c005661948cd0c7fee5508ae17d437937f34f5287590b3")

    depends_on("py-setuptools@42:", type="build")
    depends_on("py-setuptools-scm@3.4: +toml", type="build")
