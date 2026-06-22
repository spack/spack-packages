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
        sha256="0ae77c1a88f27153fa57045e00f7b0a7b06b1cd3df942e95a34b38c5d0a5bee",
    )
    version(
        "2.11.0",
        sha256="6d98d063c1dbbd05a2d903e59be398bfcff9d59c54fbbc9d4488960485d40d0",
    )
    version(
        "2.10.2",
        sha256="08509910ce6d1fadeed69cb0880d4d4fcb77739c6af9bd8fb4419391a3ca4c6b",
    )
    version(
        "2.10.1",
        sha256="66d2c6fea9541401551b0ca6df674758bb769cf4939b11c1bcd73774cdcc760",
    )
    version(
        "2.9.2",
        sha256="7608472de99d375759814cab3e2c94aba3f9ec80e62cfef8ced495ca5c27d6e",
    )
    version(
        "2.9.1",
        sha256="8e0f084176bfc4904159475b92d4b6552b781ed7b66f21708f4b4715be01895",
    )
    version(
        "2.9.0",
        sha256="c8d5154c4f44a52cccbc18fdb824c69ce55ee97a2f52e80116b65ef7ca34fd8",
    )
    version(
        "2.8.0",
        sha256="94e7b6aa1d7dff9566eddc15252aba94fdadbf67a99a169bfab34b708427cd8",
    )
    version(
        "2.7.0",
        sha256="f9f1b160580c50dcf37b6495a0fd5ec61dc0d95dae5f8004f87dd9ad7eb4b34",
    )
    version(
        "2.6.1",
        sha256="e05c6816a844aa699e46408add3bff8c743f9fd3d38eafa307a73633fddf94e",
    )
    version(
        "2.5.0",
        sha256="cc8412e94acffa20a369191382bcdbbfbfb302e475e87cacff9516d51023a15",
    )
    version(
        "2.4.0",
        sha256="a0392de5f58881085b2ac8bfe8e53f74285aa4868b1472bfaf76cfb414e1c96",
    )
    version(
        "2.2.0",
        sha256="53fa7a6227bddecaa4a0710e0b8dc18fad4c8ded7a0a31d6eddcf68009eadc03",
    )
    version(
        "2.1.0",
        sha256="a613a2ce750fee63f03dc8a36593be2bdc2929cb4cea56b38fafeb74b85c3a5f",
    )
    version(
        "2.0.0",
        sha256="9e4f4383ad83a72ce46ba5e9395dc67fadb8d53e5230aecdfc90ffdcd08d1a70",
    )
    version(
        "1.9.2",
        sha256="137ba9e75cc6b2e5d92c2acb9810beaa079b9c8e5d68c581b4f90d626d79358c",
    )
    version(
        "1.8.0",
        sha256="c9b069f408660124b12565ca026834d146154a3965efcd2bcf749eefb99b4873",
    )
    version(
        "1.7.0",
        sha256="a368b8121d3c1ec384a2dab0cb2b556924ceafc84ed80b0d1e211e3997576dae",
    )
    version(
        "1.6.2",
        sha256="27b62eae0134cd60563a4026e5f347d88fcae6d6357b11683b470eb4c51efe9f",
    )
    version(
        "1.5.2",
        sha256="34515bf2c0675d6d1c7be17ae8c7a1361439cb0a98dcde15899f23a63ef1b55f",
    )
    version(
        "1.5.1",
        sha256="e408ca6bcd424cb4555c6217cf7624d334862a6d497c549b01b9bc509e25b21e",
    )
    version(
        "1.5.0",
        sha256="0e2343bdc7246c332eb4bd477b89b53482490457a12d7b084a9b410f122770b8",
    )
    version(
        "1.4.0",
        sha256="0eeded0d1868e2b575714dc620e85631ffe03eb719f8d629101abb2c09668d8f",
    )
    version(
        "1.2.0",
        sha256="949332ba8653a7dedf1ebb2485a4479116e7774478240213a00493db3c49e9d5",
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
