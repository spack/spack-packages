# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDrawsvg(PythonPackage):
    """
    A Python 3 library for programmatically generating SVG (vector) images and animations. Drawsvg
    can also render to PNG, MP4, and display your drawings in Jupyter notebook and Jupyter lab.
    """

    homepage = "https://github.com/cduck/drawsvg"
    pypi = "drawsvg/drawsvg-2.4.2.tar.gz"

    supplier = "Person: Casey Duckering"

    maintainers("LydDeb")

    version("2.4.2", sha256="5efd8bcdc2c2400425e7fb71b4b80d8fdd83b1dc810f790f58a165df33ddd303")

    with default_args(type="build"):
        depends_on("py-setuptools")
