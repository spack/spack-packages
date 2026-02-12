# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBlake3(PythonPackage):
    """Python bindings for the BLAKE3 cryptographic hash function"""

    pypi = "blake3/blake3-1.0.5.tar.gz"

    license("BSD-3-Clause")

    version("1.0.5", sha256="7bac73f393a67ea6d5ac32e4a45d39c184487c89c712ab3ed839c1a51ed82259")

    # https://github.com/oconnor663/blake3-py/blob/1.0.5/pyproject.toml
    depends_on("py-maturin@1.0:1", type="build")
