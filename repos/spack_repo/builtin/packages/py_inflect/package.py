# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyInflect(PythonPackage):
    """inflect.py - Correctly generate plurals, singular nouns, ordinals,
    indefinite articles; convert numbers to words."""

    homepage = "https://github.com/jaraco/inflect"
    pypi = "inflect/inflect-5.0.2.tar.gz"

    license("MIT")

    version("7.5.0", sha256="faf19801c3742ed5a05a8ce388e0d8fe1a07f8d095c82201eb904f5d27ad571f")
    version("6.0.2", sha256="f1a6bcb0105046f89619fde1a7d044c612c614c2d85ef182582d9dc9b86d309a")
    version("5.0.2", sha256="d284c905414fe37c050734c8600fe170adfb98ba40f72fc66fed393f5b8d5ea0")

    with default_args(type="build"):
        depends_on("py-setuptools@61.2:", when="@7.2.1:")
        depends_on("py-setuptools@56:", when="@6.0.2:")
        depends_on("py-setuptools@42:")
        depends_on("py-setuptools-scm+toml@3.4.1:")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:", when="@7.5:")
        depends_on("python@3.7:", when="@6.0.2:")
        depends_on("python@3.6:")

        depends_on("py-more-itertools@8.5.0:", when="@7.3.1:")
        depends_on("py-typeguard@4.0.1:", when="@7.2:")
        depends_on("py-typing-extensions", when="@7.3: ^python@:3.8")

        # Historical dependencies
        depends_on("py-pydantic@1.9.1:", when="@6.0.2:7.1")
