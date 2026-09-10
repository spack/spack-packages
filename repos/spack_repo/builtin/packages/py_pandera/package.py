# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPandera(PythonPackage):
    """
    A light-weight and flexible data validation and testing tool for statistical data objects.
    """

    homepage = "https://www.union.ai/pandera"
    git = "https://github.com/unionai-oss/pandera.git"
    pypi = "pandera/pandera-0.24.0.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("0.29.0", sha256="06bc4fc1e4ff02534dd44482a9bc704fb2e58fe3fbb11be906aa714f7f5ec801")
    version("0.24.0", sha256="154231780643bc73b121bd976b0ada9dcebb3e065c622954fd099dc299cf44bd")

    depends_on("python@3.10:", type=("build", "run"), when="@0.29.0:")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@61.0:", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-packaging@20.0:", type=("build", "run"))
    depends_on("py-pydantic", type=("build", "run"))
    depends_on("py-typeguard", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-typing-inspect@0.6.0:", type=("build", "run"))
