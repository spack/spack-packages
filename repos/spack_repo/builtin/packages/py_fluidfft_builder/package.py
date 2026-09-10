# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFluidfftBuilder(PythonPackage):
    """Fluidfft plugin dependencies"""

    pypi = "fluidfft-builder/fluidfft_builder-0.0.2.tar.gz"

    maintainers("paugier")
    license("MIT", checked_by="paugier")

    version("0.0.3", sha256="7cd4bb179a17e9f636aabcdc36429a75a16d2122eb507df8c4873aa7a15e71a5")
    version("0.0.2", sha256="c0af9ceca27ae3a00ccf2f160703be9e394d8b886b8a02653b6c0a12a4f54a90")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-flit-core@3.2:3", type="build")
    depends_on("py-cython@3.0:", type="run")
