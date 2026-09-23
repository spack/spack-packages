# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyKrakenBiom(PythonPackage):
    """Create BIOM-format tables from Kraken output"""

    homepage = "https://github.com/smdabdoub/kraken-biom"
    url = "https://github.com/smdabdoub/kraken-biom/archive/refs/tags/v1.2.tar.gz"

    license("MIT", checked_by="V-Karch")

    version("1.2", sha256="64b37c06800c768616b1a27d44c0216e14140fedecef7a8800286f97f56bfc68")

    depends_on("py-setuptools", type="build")
    depends_on("py-biom-format@2.1.5:", type=("build", "run"))
