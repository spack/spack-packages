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

    version("3.1.0", sha256="384e36fc1e8d4bd361bdb3672841faae7a345b3f708aae9895d074c878332551")

    depends_on("py-flit-core@3.7:3", type="build")
