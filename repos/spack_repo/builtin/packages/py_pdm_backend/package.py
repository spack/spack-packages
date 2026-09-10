# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPdmBackend(PythonPackage):
    """The build backend used by PDM that supports latest packaging standards"""

    homepage = "https://backend.pdm-project.org/"
    pypi = "pdm_backend/pdm_backend-2.3.0.tar.gz"
    git = "https://github.com/pdm-project/pdm-backend.git"

    license("MIT", checked_by="matz-e")

    version("2.4.7", sha256="a509d083850378ce919d41e7a2faddfc57a1764d376913c66731125d6b14110f")
    version("2.4.5", sha256="56c019c440308adad5d057c08cbb777e65f43b991a3b0920749781258972fe5b")
    version("2.4.3", sha256="dbd9047a7ac10d11a5227e97163b617ad5d665050476ff63867d971758200728")
    version("2.3.0", sha256="e39ed2da206d90d4a6e9eb62f6dce54ed4fa65ddf172a7d5700960d0f8a09e09")

    depends_on("python@3.9:", type=("build", "run"), when="@2.4.4:")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-importlib-metadata@3.6:", type=("build", "run"), when="^python@:3.9")
