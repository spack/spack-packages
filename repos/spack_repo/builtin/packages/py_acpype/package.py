# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAcpype(PythonPackage):
    """
    ACPYPE (AnteChamber PYthon Parser interfacE) is a Python wrapper
    that interfaces with Antechamber to generate input files for MD programs.
    """

    homepage = "https://alanwilter.github.io/acpype/"
    pypi = "acpype/acpype-2023.10.27.tar.gz"

    maintainers = "alanwilter"

    version(
        "2023.10.27", sha256="2041ef01031015b6901aabce75cf39c17c6d7e1a034f8b0f4d168f0a6bd06a99"
    )

    # Python version requirement
    depends_on("python@3.9:", type=("build", "run"))

    # Build dependencies
    depends_on("py-setuptools", type="build")

    # Runtime dependencies
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("py-future", type=("build", "run"))
    depends_on("ambertools", type=("build", "run"))
    depends_on("openbabel", type=("build", "run"))
