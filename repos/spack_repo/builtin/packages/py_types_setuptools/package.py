# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesSetuptools(PythonPackage):
    """Typing stubs for setuptools."""

    homepage = "https://github.com/python/typeshed"
    pypi = "types-setuptools/types_setuptools-80.9.0.20250529.tar.gz"

    license("Apache-2.0")

    version(
        "82.0.0.20260210",
        sha256="d9719fbbeb185254480ade1f25327c4654f8c00efda3fec36823379cebcdee58",
    )
    version(
        "81.0.0.20260209",
        sha256="2c2eb64499b41b672c387f6f45678a28d20a143a81b45a5c77acbfd4da0df3e1",
    )
    version(
        "80.10.0.20260124",
        sha256="1b86d9f0368858663276a0cbe5fe5a9722caf94b5acde8aba0399a6e90680f20",
    )
    version(
        "80.9.0.20251223",
        sha256="d3411059ae2f5f03985217d86ac6084efea2c9e9cacd5f0869ef950f308169b2",
    )
    version(
        "80.9.0.20251221",
        sha256="05da599f5a062bbee3e83d60318576ba23111a768b7a2e46aa11644109c5d17f",
    )
    version(
        "80.9.0.20250822",
        sha256="070ea7716968ec67a84c7f7768d9952ff24d28b65b6594797a464f1b3066f965",
    )
    version(
        "80.9.0.20250809",
        sha256="e986ba37ffde364073d76189e1d79d9928fb6f5278c7d07589cde353d0218864",
    )
    version(
        "80.9.0.20250801",
        sha256="e1e92682fa07226415396bb4e2d31f116a16ffbe583b05b01f9910fcdea3b7e8",
    )
    version(
        "80.9.0.20250822",
        sha256="070ea7716968ec67a84c7f7768d9952ff24d28b65b6594797a464f1b3066f965",
    )
    version(
        "80.9.0.20250529",
        sha256="79e088ba0cba2186c8d6499cbd3e143abb142d28a44b042c28d3148b1e353c91",
    )
    version("68.2.0.0", sha256="a4216f1e2ef29d089877b3af3ab2acf489eb869ccaf905125c69d2dc3932fd85")
    version("65.5.0.3", sha256="17769171f5f2a2dc69b25c0d3106552a5cda767bbf6b36cb6212b26dae5aa9fc")

    depends_on("python@3.9:", type=("build", "run"), when="@75.8.0.20250210:")

    depends_on("py-setuptools@77.0.3:", type="build", when="@79.0.0.20250422:")
    depends_on("py-setuptools", type="build")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/t/types-setuptools/{}-{}.tar.gz"
        if version >= Version("75.5.0.20241121"):
            name = "types_setuptools"
        else:
            name = "types-setuptools"
        return url.format(name, version)
