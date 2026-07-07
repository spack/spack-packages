# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRomanNumerals(PythonPackage):
    """Manipulate well-formed Roman numerals."""

    homepage = "https://github.com/AA-Turner/roman-numerals/"
    pypi = "roman_numerals/roman_numerals-3.1.0.tar.gz"

    license("0BSD OR CC0-1.0")

    version("4.1.0", sha256="1af8b147eb1405d5839e78aeb93131690495fe9da5c91856cb33ad55a7f1e5b2")
    version("3.1.0", sha256="384e36fc1e8d4bd361bdb3672841faae7a345b3f708aae9895d074c878332551")

    with default_args(type="build"):
        depends_on("py-flit-core@3.12:3", when="@4:")
        depends_on("py-flit-core@3.7:3", when="@:3")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@4:")
        depends_on("python@3.9:")
