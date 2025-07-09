# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGlooey(PythonPackage):
    """An object-oriented GUI library for pyglet."""

    homepage = "https://glooey.readthedocs.io/en/latest/"
    pypi = "glooey/glooey-0.3.6.tar.gz"

    maintainers("moloney")

    license("MIT", checked_by="moloney")

    version("0.3.6", sha256="c025aca6c0e8d73f99793cb7b15aa547195da5499a11384379f2d3446f864520")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-flit", type="build")
    with default_args(type=("build", "run")):
        depends_on("py-pyglet")
        depends_on("py-more-itertools")
        depends_on("py-pyyaml")
