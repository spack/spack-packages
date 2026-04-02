# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAiohttp(PythonPackage):
    """Supports both client and server side of HTTP protocol.
    Supports both client and server Web-Sockets out-of-the-box and
    avoids Callbacks.  Provides Web-server with middlewares and
    plugable routing."""

    homepage = "https://github.com/aio-libs/aiohttp"
    pypi = "aiohttp/aiohttp-3.8.1.tar.gz"

    license("Apache-2.0 AND MIT", when="@3.13:")
    license("Apache-2.0", when="@:3.12")

    version("3.13.5", sha256="9d98cc980ecc96be6eb4c1994ce35d28d8b1f5e5208a23b421187d1209dbb7d1")
    with default_args(deprecated=True):
        # https://www.cvedetails.com/cve/CVE-2025-69230/
        # https://www.cvedetails.com/cve/CVE-2025-69229/
        # https://www.cvedetails.com/cve/CVE-2025-69228/
        # https://www.cvedetails.com/cve/CVE-2025-69227/
        # https://www.cvedetails.com/cve/CVE-2025-69226/
        # https://www.cvedetails.com/cve/CVE-2025-69225/
        # https://www.cvedetails.com/cve/CVE-2025-69224/
        # https://www.cvedetails.com/cve/CVE-2025-69223/
        version(
            "3.12.15", sha256="4fc61385e9c98d72fcdf47e6dd81833f47b2f77c114c29cd64a361be57a763a2"
        )
        # https://www.cvedetails.com/cve/CVE-2025-53643/
        version(
            "3.11.16", sha256="16f8a2c9538c14a557b4d309ed4d0a7c60f0253e8ed7b6c9a2859a7582f8b1b8"
        )
        # https://www.cvedetails.com/cve/CVE-2024-52304/
        # https://www.cvedetails.com/cve/CVE-2024-52303/
        # https://www.cvedetails.com/cve/CVE-2024-42367/
        version("3.9.5", sha256="edea7d15772ceeb29db4aff55e482d4bcfb6ae160ce144f2682de02f6d693551")
        version("3.9.4", sha256="6ff71ede6d9a5a58cfb7b6fffc83ab5d4a63138276c771ac91ceaaddf5459644")
        # https://www.cvedetails.com/cve/CVE-2024-30251/
        # https://www.cvedetails.com/cve/CVE-2024-27306/
        # https://www.cvedetails.com/cve/CVE-2024-23829/
        # https://www.cvedetails.com/cve/CVE-2024-23334/
        version("3.9.0", sha256="09f23292d29135025e19e8ff4f0a68df078fe4ee013bca0105b2e803989de92d")
        # https://www.cvedetails.com/cve/CVE-2023-49081/
        # https://www.cvedetails.com/cve/CVE-2023-47627/
        # https://www.cvedetails.com/cve/CVE-2023-37276/
        version("3.8.4", sha256="bf2e1a9162c1e441bf805a1fd166e249d574ca04e03b34f97e2928769e91ab5c")
        version("3.8.1", sha256="fc5471e1a54de15ef71c1bc6ebe80d4dc681ea600e68bfd1cbce40427f0b7578")
        version("3.8.0", sha256="d3b19d8d183bcfd68b25beebab8dc3308282fe2ca3d6ea3cb4cd101b3c279f8d")
        # https://www.cvedetails.com/cve/CVE-2023-37276/
        version("3.7.4", sha256="5d84ecc73141d0a0d61ece0742bb7ff5751b0657dab8405f899d3ceb104cc7de")

    with default_args(type="build"):
        depends_on("c")
        depends_on("pkgconfig", when="@3.12:")
        depends_on("py-setuptools@67:", when="@3.13.1:")
        depends_on("py-setuptools@46.4:")

    with default_args(type=("build", "run")):
        depends_on("py-aiohappyeyeballs@2.5:", when="@3.12:")
        depends_on("py-aiohappyeyeballs@2.3:", when="@3.10:")
        depends_on("py-aiosignal@1.4.0:", when="@3.12:")
        depends_on("py-aiosignal@1.1.2:", when="@3.8.1:")
        depends_on("py-async-timeout@4:5", when="@3.8: ^python@:3.10")
        depends_on("py-async-timeout@3", when="@:3.7.4 ^python@:3.10")
        depends_on("py-attrs@17.3:")
        depends_on("py-frozenlist@1.1.1:", when="@3.8.1:")
        depends_on("py-multidict@4.5:6", when="@3.6.3:")
        depends_on("py-propcache@0.2:", when="@3.11:")
        depends_on("py-yarl@1.17:1", when="@3.11:")
        depends_on("py-yarl@1")

        # Historical dependencies
        depends_on("py-chardet@2.0:3", when="@:3.7")
        depends_on("py-charset-normalizer@2:3", when="@3.8.4:3.12")
        depends_on("py-charset-normalizer@2", when="@3.8.0:3.8.3")
        depends_on("py-typing-extensions@3.6.5:", when="@3.7")
