# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNanobind(PythonPackage):
    """nanobind is a small binding library that exposes C++ types in
    Python and vice versa. It is reminiscent of Boost.Python and pybind11
    and uses near-identical syntax. In contrast to these existing tools,
    nanobind is more efficient: bindings compile in a shorter amount of time,
    produce smaller binaries, and have better runtime performance.
    """

    homepage = "https://nanobind.readthedocs.io"
    pypi = "nanobind/nanobind-2.13.0.tar.gz"
    git = "https://github.com/wjakob/nanobind.git"

    maintainers("chrisrichardson", "garth-wells")

    license("BSD-3-Clause")

    version("master", branch="master", submodules=True)
    version(
        "2.13.0",
        sha256="c7b04d6a6a4cd57985571e605539399b51331ae455d7fce576a5e2fcb89b1dcf",
    )
    version(
        "2.12.0",
        sha256="0ae77c1a88f27153fa57045ee00f7b0a7b06b1cd3df942e95a34b38c5d0a5bee",
    )
    version(
        "2.11.0",
        sha256="6d98d063c61dbbd05a2d903e59be398bfcff9d59c54fbbc9d4488960485d40d0",
    )
    version(
        "2.10.2",
        sha256="08509910ce6d1fadeed69cb0880d4d4fcb77739c6af9bd8fb4419391a3ca4c6b",
    )
    version(
        "2.10.1",
        sha256="66d2c6fea9541401551b0ca6df674758bb769cf4939b11c1bcd73774c1dcc760",
    )
    version(
        "2.9.2",
        sha256="e7608472de99d375759814cab3e2c94aba3f9ec80e62cfef8ced495ca5c27d6e",
    )
    version(
        "2.9.1",
        sha256="8e0f084176bfc4904159475b92d4b6552b781ed7b66f21708f4b471c5be01895",
    )
    version(
        "2.9.0",
        sha256="c8d5154c4f44a52cccbc18fdb824c6e9ce55ee97a2f52e80116b65ef7ca34fd8",
    )
    version(
        "2.8.0",
        sha256="94e7bf6aa1d7dff9566eddc15252aba94fdadbf67a99a169bfab34b708427cd8",
    )
    version(
        "2.7.0",
        sha256="f9f1b160580c50dcf37b6495a0fd5ec61dc0d95dae5f8004f87dd9ad7eb46b34",
    )
    version(
        "2.6.1",
        sha256="e05c6816a844aa699e46408add3bff8c743af9fd3d38eafa307a73633fddf94e",
    )
    version(
        "2.5.0",
        sha256="cc8412e94acffa20a369191382bcdbb6fbfb302e475e87cacff9516d51023a15",
    )
    version(
        "2.4.0",
        sha256="a0392dee5f58881085b2ac8bfe8e53f74285aa4868b1472bfaf76cfb414e1c96",
    )
    version(
        "2.2.0",
        sha256="53fa7a6227bddecaa4a0710e0b8dc18fad4c8ded7a0a31d6eddcf68009ead603",
    )
    version(
        "2.1.0", tag="v2.1.0", commit="9641bb7151f04120013b812789b3ebdfa7e7324f", submodules=True
    )
    version(
        "2.0.0", tag="v2.0.0", commit="8d7f1ee0621c17fa370b704b2100ffa0243d5bfb", submodules=True
    )
    version(
        "1.9.2", tag="v1.9.2", commit="80a30c8efb093b14f0e744bc7f6a9ef34beb3f7f", submodules=True
    )
    version(
        "1.8.0", tag="v1.8.0", commit="1a309ba444a47e081dc6213d72345a2fbbd20795", submodules=True
    )
    version(
        "1.7.0", tag="v1.7.0", commit="555ec7595c89c60ce7cf53e803bc226dc4899abb", submodules=True
    )
    version(
        "1.6.2", tag="v1.6.2", commit="cc5ac7e61def198db2a8b65c6d630343987a9f1d", submodules=True
    )
    version(
        "1.5.2", tag="v1.5.2", commit="b0e24d5b0ab0d518317d6b263a257ae72d4d29a2", submodules=True
    )
    version(
        "1.5.1", tag="v1.5.1", commit="ec6168d06dbf2ab94c31858223bd1d7617222706", submodules=True
    )
    version(
        "1.5.0", tag="v1.5.0", commit="e85a51049db500383808aaa4a77306ff37d96131", submodules=True
    )
    version(
        "1.4.0", tag="v1.4.0", commit="05cba0ef85ba2bb68aa115af4b74c30aa2aa7bec", submodules=True
    )
    version(
        "1.2.0", tag="v1.2.0", commit="ec9350b805d2fe568f65746fd69225eedc5e37ae", submodules=True
    )

    depends_on("cxx", type="build")  # generated

    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-setuptools@42:", when="@:2.0", type="build")
    depends_on("py-scikit-build", when="@:2.0", type="build")
    depends_on("py-typing-extensions", when="@2.0", type="build")
    depends_on("ninja", when="@2.0", type="build")
    depends_on("cmake@3.17:", when="@:2.0", type="build")

    depends_on("py-scikit-build-core+pyproject@0.9:", when="@2.1", type="build")
    depends_on("py-scikit-build-core+pyproject@0.10:", when="@2.2:", type="build")

    @property
    def cmake_prefix_paths(self):
        paths = [join_path(python_platlib, "nanobind", "cmake")]
        return paths
