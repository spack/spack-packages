# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.pipx import PipxPackage

from spack.package import *


class PipxBlack(PipxPackage):
    """Black is the uncompromising Python code formatter. By using it, you agree to
    cede control over minutiae of hand-formatting. In return, Black gives you
    speed, determinism, and freedom from pycodestyle nagging about formatting.
    """

    homepage = "https://github.com/psf/black"
    pypi = "black/black-23.11.0.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("26.1.0", sha256="d294ac3340eef9c9eb5d29288e96dc719ff269a88e27b396340459dd85da4c58")
    version("25.9.0", sha256="0474bca9a0dd1b51791fcc507a4e02078a1c63f6d4e4ae5544b9848c7adfb619")
    version("25.1.0", sha256="33496d5cd1222ad73391352b4ae8da15253c5de89b93a80b3e2c8d9a19ec2666")
    version("24.8.0", sha256="2500945420b6784c38b9ee885af039f5e7471ef284ab03fa35ecdde4688cd83f")
    version("23.11.0", sha256="4c68855825ff432d197229846f971bc4d6666ce90492e5b02013bcaca4d9ab05")

    depends_on("python@3.10:", when="@26:")
    depends_on("python@3.9:", when="@25:")
    depends_on("python@3.8:", when="@24:")
    depends_on("python@3.7:")
