# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesTqdm(PythonPackage):
    """Typing stubs for tqdm."""

    homepage = "https://github.com/python/typeshed"
    pypi = "types_tqdm/types_tqdm-4.67.0.20250809.tar.gz"

    license("Apache-2.0")

    version(
        "4.67.0.20250809",
        sha256="02bf7ab91256080b9c4c63f9f11b519c27baaf52718e5fdab9e9606da168d500",
    )

    depends_on("py-setuptools@77.0.3:", type="build")
    depends_on("py-types-requests", type=("build", "run"))
