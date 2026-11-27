# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyYetAnotherImodWrapper(PythonPackage):
    """A simple API for automated tilt-series alignment using IMOD."""

    homepage = "https://github.com/teamtomo/yet-another-imod-wrapper"
    pypi = "yet-another-imod-wrapper/yet_another_imod_wrapper-0.1.2.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause")

    version("0.1.2", sha256="47e61ab00adf584db6067acbf716029e4a7cafdfbca6c90b86646b879d3faea4")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    # PyPI sdist ships PKG-INFO with the version already resolved, so this
    # isn't strictly needed, but set it anyway in case a future version's
    # build hook requires it (same mechanism py-relion uses for setuptools-scm).
    def setup_build_environment(self, env):
        env.set("SETUPTOOLS_SCM_PRETEND_VERSION", str(self.spec.version))

    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        depends_on("py-mrcfile@1.4.0:")
        depends_on("py-starfile")
        depends_on("py-pandas")
        depends_on("py-packaging")
        depends_on("py-typer")
        depends_on("py-rich")

    depends_on("imod@4.11.0:", type="run")
