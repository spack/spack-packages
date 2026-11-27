# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDetectInstaller(PythonPackage):
    """Detect how a Python package was installed and get the correct upgrade command."""

    homepage = "https://github.com/patrick91/detect-installer"
    pypi = "detect_installer/detect_installer-0.2.1.tar.gz"

    version("0.2.1", sha256="85f889d4d19c1caf5bef89ef389eb920cd8c6c2a868e1eeceec24527b93021e7")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-uv-build@0.9.8:0.9", type="build")
