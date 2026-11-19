# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyQuarto(PythonPackage):
    """Quarto is an open-source scientific and technical publishing system built on Pandoc."""

    homepage = "https://quarto.org"
    pypi = "quarto-cli/quarto_cli-1.10.19.tar.gz"

    license("MIT")

    version("1.10.19", sha256="e4b14f3aeb38ea536672428a402c413c962bd4ba9d0b9805f416779226eb53e2")

    depends_on("py-setuptools", type="build")

    depends_on("py-jupyter", type=("build", "run"))
    depends_on("py-nbclient", type=("build", "run"))
