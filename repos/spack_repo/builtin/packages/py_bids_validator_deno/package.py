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

    version("2.0.11", sha256="c6724949dae74f82964d0db4af6b3fe933a22717f6f32139ccd991acb6826e5b")
    version("2.0.7", sha256="55a46dc9e134c2996ecb077896aad65e5320f3c864b41c47e108011f8fd1e2d1")

    depends_on("py-pdm-backend", type="build")
    depends_on("deno", type=("build", "run"))
