# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNpe2(PythonPackage):
    """The napari plugin engine version 2, npe2 extends the functionality of
    napari's core. The plugin ecosystem offers user additional functionality
    for napari as well as specific support for different scientific domains."""

    homepage = "github.com/napari/npe2"
    pypi = "npe2/npe2-0.7.9.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.7.9", sha256="b6d2f20c87c12bcf60294cab9b1645889c12d68c5338ff7abd66f2742e675ad4")

    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-pyyaml")
        depends_on("py-platformdirs")
        depends_on("py-build@1")
        depends_on("py-psygnal@0.3.0:")
        depends_on("py-pydantic")
        depends_on("py-tomli-w")
        depends_on("py-tomli", when="^python@:3.10")
        depends_on("py-rich")
        depends_on("py-typer")
