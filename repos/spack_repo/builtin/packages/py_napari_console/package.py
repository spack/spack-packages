# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNapariConsole(PythonPackage):
    """This napari plugin adds a console to napari"""

    homepage = "https://github.com/napari/napari-console"
    pypi = "napari_console/napari_console-0.1.3.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.1.3", sha256="ba4f7e1cdca65a7924631372a5e58884e2e35a2b9092c79b98acb9c2dfe1254f")

    depends_on("python@3.9:", type="run")

    depends_on("py-setuptools@42:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")

    depends_on("py-ipython@7.7.0:", type=("build", "run"))
    depends_on("py-ipykernel@5.2.0:", type=("build", "run"))
    depends_on("py-qtpy@1.7.0:", type=("build", "run"))

    depends_on("py-qtconsole@4.5.1:", type=("build", "run"))
    conflicts("^py-qtconsole@4.7.6")
    conflicts("^py-qtconsole@5.4.2")

    depends_on("py-napari-plugin-engine@0.1.9:", type=("build", "run"))
