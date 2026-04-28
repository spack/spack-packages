# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOkadaWrapper(PythonPackage):
    """Python and MATLAB wrappers for the Okada Green's function codes"""

    homepage = "https://github.com/tbenthompson/okada_wrapper"
    pypi = "okada_wrapper/okada_wrapper-18.12.07.3.tar.gz"

    maintainers("snehring")

    license("MIT", checked_by="snehring")

    version("24.6.15", sha256="c19bacfc4336c59d94e3ece3ed378fe2ae3496a165412c47e08164fe8b66f307")
    version(
        "18.12.07.3", sha256="ee296ad6e347c8df400f6f3d1badc371925add8d1af33854634c2fe1a2b2c855"
    )

    depends_on("c", type="build")
    depends_on("fortran", type="build")  # generated

    depends_on("py-meson-python", type="build", when="@24.6.15:")

    # https://github.com/tbenthompson/okada_wrapper/issues/8
    depends_on("python@3:3.11", type=("build", "run"), when="@18.12.07.3")
    depends_on("python@3.8:", type=("build", "run"), when="@24.6.15")

    depends_on("py-setuptools", type="build", when="@18.12.07.3")

    depends_on("py-numpy", type=("build", "run"))
