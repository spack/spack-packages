# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTokenizers(PythonPackage):
    """Fast and Customizable Tokenizers."""

    homepage = "https://github.com/huggingface/tokenizers"
    pypi = "tokenizers/tokenizers-0.6.0.tar.gz"

    version("0.22.1", sha256="61de6522785310a309b3407bac22d99c4db5dba349935e99e4d15ea2226af2d9")
    version("0.21.0", sha256="ee0894bf311b75b0c03079f33859ae4b2334d675d4e93f5a4132e1eae2834fe4")
    version("0.20.4", sha256="db50ac15e92981227f499268541306824f49e97dbeec05d118ebdc7c2d22322c")
    version("0.19.1", sha256="ee59e6680ed0fdbe6b724cf38bd70400a0c1dd623b07ac729087270caeac88e3")
    version("0.15.0", sha256="10c7e6e7b4cabd757da59e93f5f8d1126291d16f8b54f28510825ef56a3e5d0e")
    version("0.13.3", sha256="2e546dbb68b623008a5442353137fbb0123d311a6d7ba52f2667c8862a75af2e")
    version("0.13.1", sha256="3333d1cee5c8f47c96362ea0abc1f81c77c9b92c6c3d11cbf1d01985f0d5cf1d")
    version("0.10.3", sha256="1a5d3b596c6d3a237e1ad7f46c472d467b0246be7fd1a364f12576eb8db8f7e6")

    depends_on("python@3.9:", type=("build", "run"), when="@0.22.1:")

    # TODO: This package currently requires internet access to install.
    depends_on("py-maturin@1:", when="@0.14:", type="build")
    depends_on("rust", when="@0.14:", type="build")
    depends_on("py-huggingface-hub@0.16.4:0", when="@0.15:0.21.0", type=("build", "run"))
    depends_on("py-huggingface-hub@0.16.4:1", when="@0.22.1:", type=("build", "run"))

    # cargo resolves dependencies, which includes openssl-sys somewhere, which needs
    # system pkgconfig and openssl.
    depends_on("pkgconfig", type="build")
    depends_on("openssl")

    # Historical dependencies
    depends_on("py-setuptools", when="@:0.13", type="build")
    depends_on("py-setuptools-rust", when="@:0.13", type="build")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
