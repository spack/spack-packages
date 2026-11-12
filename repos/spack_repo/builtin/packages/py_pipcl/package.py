# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPipcl(PythonPackage):
    """Python packaging operations, including PEP-517 support,
    for use by a setup.py script."""

    homepage = "https://github.com/ArtifexSoftware/pipcl"
    pypi = "pipcl/pipcl-4.tar.gz"

    license("AGPL-3.0", checked_by="V-Karch")

    version("4", sha256="872af57ed3be4cfce9ffe16861514f8774675f8ddbc5df91b2d9ff283bb33f8c")
