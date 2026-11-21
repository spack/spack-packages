# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTruststore(PythonPackage):
    """Verify certificates using native system trust stores"""

    homepage = "https://github.com/sethmlarson/truststore"
    pypi = "truststore/truststore-0.10.5.tar.gz"

    license("MIT")

    version("0.10.5", sha256="30d36967ccaded5cbb38d602c433f53600036c79d502f4533a49b60a03bbefcd")

    depends_on("python@3.10:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-flit-core@3.11:3")
