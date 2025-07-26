# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVesin(PythonPackage):
    """Computing neighbor lists for atomistic system."""

    homepage = "https://luthaf.fr/vesin/latest/index.html"
    pypi = "vesin/vesin-0.3.7.tar.gz"

    import_modules = ["vesin"]

    maintainers("HaoZeke", "luthaf", "rmeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.3.7", sha256="52c11ac0ba775c228f06779877cf8641854edab7ea59036093ef5e8447379de0")

    # pyproject.toml
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-wheel@0.41:", type="build")
    depends_on("cmake@3.16:", type="build")
