# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPreCommitHooks(PythonPackage):
    """A collection of useful pre-commit hooks."""

    homepage = "https://github.com/pre-commit/pre-commit-hooks"
    url = "https://github.com/pre-commit/pre-commit-hooks/archive/refs/tags/v4.5.0.tar.gz"

    maintainers("cedricchevalier19", "claireguilbaud")

    license("MIT")

    version("6.0.0", sha256="5236d2daff61aed8d882ec81463cf27786f6a1f449f05d8c6c3882c3cf2810bb")
    version("5.0.0", sha256="b2fcd00243b7e61b43a3a26d226e295e0a07611f3436818f64846c067a1679d5")
    version("4.6.0", sha256="ebf493781b27929294ff1262763cfd877af1fd33c21fc9d7cd684fdf40204b27")

    depends_on("python@3.8:", when="@4.6:", type=("build", "run"))
    depends_on("python@3.9:", when="@6:", type=("build", "run"))

    # Minimum Python dependencies
    depends_on("py-tomli@1.1.0:", type=("build", "run"), when="^python@:3.10")
    depends_on("py-ruamel-yaml@0.15:", type=("build", "run"))
