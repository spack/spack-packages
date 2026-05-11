# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyrodigalGv(PythonPackage):
    """A Pyrodigal extension to predict genes in giant viruses and
    viruses with alternative genetic code."""

    homepage = "https://github.com/althonos/pyrodigal-gv"
    pypi = "pyrodigal_gv/pyrodigal_gv-0.3.2.tar.gz"

    license("GPL-3.0", checked_by="V-Karch")

    version("0.3.2", sha256="aeeff43daec2c4aec7830ae2400799aa90bf273bcca86656ef239bee8d7e5ea5")

    depends_on("py-setuptools@46.4:", type="build")
    depends_on("py-wheel@0.23:", type="build")

    depends_on("py-pyrodigal", type=("build", "run"))
