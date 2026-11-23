# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPackageurlPython(PythonPackage):
    """Python library to parse and build "purl" a.k.a. Package URLs."""

    homepage = "https://github.com/package-url/packageurl-python"
    pypi = "packageurl_python/packageurl_python-0.17.6.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("0.17.6", sha256="1252ce3a102372ca6f86eb968e16f9014c4ba511c5c37d95a7f023e2ca6e5c25")

    variant(
        "django",
        default=False,
        description="Enable Django abstract model mixin to use Package URLs in Django",
    )
    variant(
        "sqlalchemy",
        default=False,
        description="Enable SQLAlchemy declarative mixin to use Package URLs in SQLAlchemy models",
    )

    depends_on("py-setuptools", type="build")

    depends_on("python@3.8:", type=("build", "run"))

    with default_args(type="run"):
        depends_on("py-django", when="+django")
        depends_on("py-sqlalchemy@2:", when="+sqlalchemy")
