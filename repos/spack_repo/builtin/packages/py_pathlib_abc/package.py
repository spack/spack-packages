# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPathlibAbc(PythonPackage):
    """Backport of pathlib ABCs."""

    homepage = "https://github.com/barneygale/pathlib-abc"
    pypi = "pathlib_abc/pathlib_abc-0.5.2.tar.gz"

    license("PSF-2.0")

    version("0.5.2", sha256="fcd56f147234645e2c59c7ae22808b34c364bb231f685ddd9f96885aed78a94c")

    with default_args(type="build"):
        depends_on("py-hatchling")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:")
