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
