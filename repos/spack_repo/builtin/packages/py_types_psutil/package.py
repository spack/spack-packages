# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTypesPsutil(PythonPackage):
    """Typing stubs for psutil."""

    homepage = "https://github.com/python/typeshed"
    pypi = "types_psutil/types_psutil-7.0.0.20251001.tar.gz"

    license("Apache-2.0")

    version(
        "7.2.2.20260408", sha256="e8053450685965b8cd52afb62569073d00ea9967ae78bb45dff5f606847f97f2"
    )
    version(
        "7.0.0.20251001", sha256="60d696200ddae28677e7d88cdebd6e960294e85adefbaafe0f6e5d0e7b4c1963"
    )
    version("5.9.5.16", sha256="4e9b219efb625d3d04f6bf106934f87cab49aa41a94b0a3b3089403f47a79228")
    version("5.9.5.5", sha256="4f26fdb2cb064b274cbc6359fba4abf3b3a2993d7d4abc336ad0947568212c62")

    with default_args(type="build"):
        depends_on("py-setuptools@82.0.1:", when="@7.2.2.20260404:")
        depends_on("py-setuptools@77.0.3:", when="@7.0.0.20250516:")
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@7.2.2.20260404:")
        depends_on("python@3.9:", when="@7.0.0.20250218:")

    def url_for_version(self, version):
        if self.spec.satisfies("@6.1.0.20241221:"):
            name = "types_psutil"
        else:
            name = "types-psutil"
        return f"https://files.pythonhosted.org/packages/source/{name[0]}/{name}/{name}-{version}.tar.gz"
