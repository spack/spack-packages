# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBleach(PythonPackage):
    """An easy whitelist-based HTML-sanitizing tool."""

    homepage = "https://github.com/mozilla/bleach"
    pypi = "bleach/bleach-3.1.0.tar.gz"

    license("Apache-2.0")

    version("6.4.0", sha256="4202482733d85cedd04e59fcb2f89f4e4c7c385a78d3c3c23c30446843a37452")
    with default_args(deprecated=True):
        # https://github.com/mozilla/bleach/security/advisories/GHSA-g75f-g53v-794x
        # https://github.com/mozilla/bleach/security/advisories/GHSA-gj48-438w-jh9v
        version("6.3.0", sha256="6f3b91b1c0a02bb9a78b5a454c92506aa0fdf197e1d5e114d2e00c6f64306d22")
        version("6.2.0", sha256="123e894118b8a599fd80d3ec1a6d4cc7ce4e5882b1317a7e1ba69b56e95f991f")
        version("6.0.0", sha256="1a1a85c1595e07d8db14c5f09f09e6433502c51c595970edc090551f0db99414")
        version("5.0.1", sha256="0d03255c47eb9bd2f26aa9bb7f2107732e7e8fe195ca2f64709fcf3b0a4a085c")
        version("4.1.0", sha256="0900d8b37eba61a802ee40ac0061f8c2b5dee29c1927dd1d233e075ebf5a71da")
        version("4.0.0", sha256="ffa9221c6ac29399cc50fcc33473366edd0cf8d5e2cbbbb63296dc327fb67cc8")
        version("3.3.1", sha256="306483a5a9795474160ad57fce3ddd1b50551e981eed8e15a582d34cef28aafa")
        # https://github.com/mozilla/bleach/security/advisories/GHSA-vv2x-vrpj-qqpq
        # https://github.com/mozilla/bleach/security/advisories/GHSA-vqhp-cxgc-6wmm
        # https://github.com/mozilla/bleach/security/advisories/GHSA-m6xf-fq7q-8743
        # https://github.com/mozilla/bleach/security/advisories/GHSA-q65m-pv3f-wr5r
        version("3.1.0", sha256="3fdf7f77adcf649c9911387df51254b813185e32b2c6619f690b593a617e19fa")
        version("1.5.0", sha256="978e758599b54cd3caa2e160d74102879b230ea8dc93871d0783721eef58bc65")

    variant("css", default=False, when="@5:", description="Add css support")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@6.3:")
        depends_on("python@3.9:", when="@6.2:")
        depends_on("python@3.8:", when="@6.1:")
        depends_on("python@3.7:", when="@5:")
        depends_on("py-webencodings")

        with when("+css"):
            depends_on("py-tinycss2@1.1:", when="@6.4:")
            depends_on("py-tinycss2@1.1:1.4", when="@6.2:6.3")
            depends_on("py-tinycss2@1.1:1.2", when="@6.1")
            depends_on("py-tinycss2@1.1", when="@:6.0")

        # Historical dependencies
        depends_on("py-six@1.9.0:", when="@:6.1")
        depends_on("py-packaging", when="@3.1.5:4")
