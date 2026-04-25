# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNapariSvg(PythonPackage):
    """A plugin for writing svg files with napari."""

    homepage = "https://github.com/napari/napari-svg"
    pypi = "napari_svg/napari_svg-0.2.1.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.2.1", sha256="031f13b34b0948afbdcb11eb00728fe32ef7e4e3aa3905f923001d6871a08ad9")

    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-setuptools@56:", type="build")
    depends_on("py-setuptools-scm@8: +toml", type="build")

    depends_on("py-imageio@2.5.0:", type=("build", "run"))
    depends_on("py-numpy@1.16:", type=("build", "run"))
    depends_on("py-vispy@0.6.4:", type=("build", "run"))
