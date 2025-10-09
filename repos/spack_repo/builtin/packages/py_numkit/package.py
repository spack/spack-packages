# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNumkit(PythonPackage):
    """Numerical first aid kit (with numpy/scipy)."""

    homepage = "https://github.com/Becksteinlab/numkit"
    pypi = "numkit/numkit-1.3.1.tar.gz"

    maintainers = "orbeckst"

    version("1.3.1", sha256="18fba519ab4714d9426a818c04e4656bc60368169db0f65f5eece2ddae0e3211")

    # Build-system requirements
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-setuptools-scm", type="build", when="@main")

    # Runtime / build deps
    depends_on("py-numpy@1.20:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
