# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySetuptoolsScm(PythonPackage):
    """The blessed package to manage your versions by scm tags."""

    homepage = "https://github.com/pypa/setuptools_scm"
    pypi = "setuptools_scm/setuptools_scm-4.1.2.tar.gz"
    tags = ["build-tools"]

    maintainers("RobertMaaskant")

    license("MIT")

    version("9.2.2", sha256="1c674ab4665686a0887d7e24c03ab25f24201c213e82ea689d2f3e169ef7ef57")
    version("8.2.1", sha256="51cfdd1deefc9b8c08d1a61e940a59c4dec39eb6c285d33fa2f1b4be26c7874d")
    version("8.2.0", sha256="a18396a1bc0219c974d1a74612b11f9dce0d5bd8b1dc55c65f6ac7fd609e8c28")
    version("8.1.0", sha256="42dea1b65771cba93b7a515d65a65d8246e560768a66b9106a592c8e7f26c8a7")
    version("8.0.4", sha256="b5f43ff6800669595193fd09891564ee9d1d7dcb196cab4b2506d53a2e1c95c7")
    version("7.1.0", sha256="6c508345a771aad7d56ebff0e70628bf2b0ec7573762be9960214730de278f27")
    version("6.4.2", sha256="6833ac65c6ed9711a4d5d2266f8024cfa07c533a0e55f4c12f6eff280a5a9e30")
    version("6.3.2", sha256="a49aa8081eeb3514eb9728fa5040f2eaa962d6c6f4ec9c32f6c1fba88f88a0f2")
    version("5.0.2", sha256="83a0cedd3449e3946307811a4c7b9d89c4b5fd464a2fb5eeccd0a5bb158ae5c8")
    version("4.1.2", sha256="a8994582e716ec690f33fec70cca0f85bd23ec974e3f783233e4879090a7faa8")
    version("3.5.0", sha256="5bdf21a05792903cafe7ae0c9501182ab52497614fa6b1750d9dbae7b60c1a87")
    version("1.15.6", sha256="49ab4685589986a42da85706b3311a2f74f1af567d39fee6cb1e088d7a75fb5f")

    # Basically a no-op in setuptools_scm 7+, toml support is always built
    variant("toml", default=True, description="Build with TOML support")

    with default_args(type=("build", "run")):
        depends_on("python@3.8:", when="@8:")
        depends_on("python@3.7:", when="@7:")
        depends_on("python@3.6:", when="@6:")
        depends_on("python@2.7:2.8,3.5:", when="@4:")
        depends_on("python@2.7:2.8,3.4:")

        depends_on("python@:3.10", when="@:7.0.5")

        depends_on("py-setuptools@61:", when="@8:")
        depends_on("py-setuptools@45:", when="@6:")
        depends_on("py-setuptools@42:", when="@5:")
        depends_on("py-setuptools@34.4:")

        # use of vendored pkg_resources
        depends_on("py-setuptools@:80", when="@:6")

        depends_on("py-tomli@1:2.0.2", when="@8.2.0: ^python@:3.10")
        depends_on("py-tomli@1:", when="@7.1.0:8.1.0 ^python@:3.10")
        depends_on("py-tomli@1:", when="@7.0.0:7.0.5")
        depends_on("py-tomli@1:", when="+toml @6.3.0:6.4.2")
        depends_on("py-toml", when="+toml @6.1.1:6.2.0")

        depends_on("py-rich", when="@8.0.0:8.0.3")

        depends_on("py-importlib-metadata@4.6:", when="@8.0.0:8.0.2 ^python@:3.9")
        depends_on("py-importlib-metadata", when="@7 ^python@:3.7")

        depends_on("py-typing-extensions", when="@8.1.0: ^python@:3.9")
        depends_on("py-typing-extensions", when="@8.0.4")
        depends_on("py-typing-extensions", when="@8.0.0:8.0.3 ^python@:3.10")
        depends_on("py-typing-extensions", when="@7")

        depends_on("py-packaging@20:", when="@6.3.0:6")
        # https://github.com/pypa/setuptools/issues/4483#issuecomment-2236528158
        depends_on("py-packaging@22:", when="@7: ^py-setuptools@71:")

        depends_on("py-wheel", when="@3.4.0:6.4.2")

        depends_on("git")

    with default_args(type=("run")):
        depends_on("py-typing-extensions", when="@8.1: ^python@:3.10")
        depends_on("py-typing-extensions", when="@7:8.0.4")

        depends_on("py-packaging@20.0:", when="@6.3:")
        depends_on("py-packaging@24:", when="@7.1:")

        depends_on("py-importlib-metadata", when="@7: ^python@:3.7")

    def url_for_version(self, version):
        # setuptools_scm-7.1.0.tar.gz with an underscore became
        # setuptools-scm-8.0.4.tar.gz with a dash
        url = super().url_for_version(version)
        if version >= Version(8):
            return url.replace("_", "-")
        return url
