# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMorphosamplers(PythonPackage):
    """A library for sampling image data along morphological objects such as
    splines and surfaces."""

    homepage = "https://github.com/morphometrics/morphosamplers"
    pypi = "morphosamplers/morphosamplers-0.0.16.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.0.16", sha256="82097605e42f2129445ef4ac2235430ac10d1ec6dced918bfacc58d913377f58")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@45:", type="build")
    depends_on("py-setuptools-scm@6.2:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-einops")
        depends_on("py-numpy")
        depends_on("py-psygnal")
        depends_on("py-pydantic")
        depends_on("py-pydantic-compat")
        depends_on("py-scipy")
        depends_on("py-typing-extensions")
