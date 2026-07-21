# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLanguageData(PythonPackage):
    """Supplementary data about languages used by the langcodes module"""

    homepage = "https://github.com/georgkrause/language_data"
    pypi = "language_data/language_data-1.3.0.tar.gz"

    license("MIT")

    version("1.3.0", sha256="7600ef8aa39555145d06c89f0c324bf7dab834ea0b0a439d8243762e3ebad7ec")

    depends_on("py-setuptools@60:", type="build")
    depends_on("py-setuptools-scm@8:", type="build")
    depends_on("py-marisa-trie@1.1:", type=("build", "run"))
