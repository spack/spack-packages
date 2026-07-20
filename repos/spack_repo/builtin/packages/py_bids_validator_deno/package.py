# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBidsValidatorDeno(PythonPackage):
    """Typescript implementation of the BIDS validator."""

    homepage = "https://github.com/bids-standard/bids-validator"
    pypi = "bids_validator_deno/bids_validator_deno-2.0.7.tar.gz"

    license("MIT")

    version("2.4.1", sha256="a79b4af2818a200ff5a597715a3c1050ae93be7cb523bcfef54b93af057d8466")
    version("2.4.0", sha256="78cd6bc4d43aa6b17555185181c74b22e2ccaea8c3494175b6524807b467aa94")
    version("2.0.7", sha256="55a46dc9e134c2996ecb077896aad65e5320f3c864b41c47e108011f8fd1e2d1")

    depends_on("py-pdm-backend", type="build")
    depends_on("deno", type=("build", "run"))
