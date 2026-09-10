# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLangcodes(PythonPackage):
    """Tools for labeling human languages with IETF language tags"""

    homepage = "https://github.com/rspeer/langcodes"
    pypi = "langcodes/langcodes-3.3.0.tar.gz"

    license("MIT")

    version("3.5.1", sha256="40bff315e01b01d11c2ae3928dd4f5cbd74dd38f9bd912c12b9a3606c143f731")
    version("3.5.0", sha256="1eef8168d07e51e131a2497ffecad4b663f6208e7c3ae3b8dc15c51734a6f801")
    version("3.3.0", sha256="794d07d5a28781231ac335a1561b8442f8648ca07cd518310aeb45d6f0807ef6")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.9:", type=("build", "run"), when="@3.5:")
    depends_on("py-setuptools@60:", type="build", when="@3.5:")
    depends_on("py-setuptools-scm@8:", type="build", when="@3.5:")
    depends_on("py-poetry-core@1:", type="build", when="@:3.4")
    depends_on("py-language-data@1.2:", type=("build", "run"), when="@3.5:")
