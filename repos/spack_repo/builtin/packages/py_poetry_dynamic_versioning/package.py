# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPoetryDynamicVersioning(PythonPackage):
    """Plugin for Poetry to enable dynamic versioning based on VCS tags."""

    homepage = "https://github.com/mtkennerly/poetry-dynamic-versioning"
    pypi = "poetry_dynamic_versioning/poetry_dynamic_versioning-1.4.0.tar.gz"

    license("MIT")

    version("1.10.0", sha256="52bf9ed57f2d60f4250a1dfe43db7b8144541df2f3ae6e712d12b43ecda71f47")
    version("1.9.1", sha256="d6e7b9df817aa2ca4946cd695c6c89e1379d2e6c640f008a9b6170d081a9da48")
    version("1.4.0", sha256="725178bd50a22f2dd4035de7f965151e14ecf8f7f19996b9e536f4c5559669a7")
    version("0.19.0", sha256="a11a7eba6e7be167c55a1dddec78f52b61a1832275c95519ad119c7a89a7f821")

    depends_on("py-poetry-core@1:", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.7:3")

        depends_on("py-dunamai@1.26", when="@1.10:")
        depends_on("py-dunamai@1.25", when="@1.9")
        depends_on("py-dunamai@1.21", when="@1.3:1.7")
        depends_on("py-dunamai@1.12", when="@:0.19")
        depends_on("py-tomlkit@0.4:")
        depends_on("py-jinja2@2.11.1:3")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/p/{0}/{0}-{1}.tar.gz"
        if version >= Version("1"):
            letter = "poetry_dynamic_versioning"
        else:
            letter = "poetry-dynamic-versioning"
        return url.format(letter, version)
