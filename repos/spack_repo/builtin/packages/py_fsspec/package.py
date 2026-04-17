# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFsspec(PythonPackage):
    """A specification for pythonic filesystems."""

    homepage = "https://github.com/intake/filesystem_spec"
    pypi = "fsspec/fsspec-0.4.4.tar.gz"

    license("BSD-3-Clause")

    # Requires pytest
    skip_modules = ["fsspec.tests"]

    version("2026.3.0", sha256="1ee6a0e28677557f8c2f994e3eea77db6392b4de9cd1f5d7a9e87a0ae9d01b41")
    version("2025.9.0", sha256="19fd429483d25d28b65ec68f9f4adc16c17ea2c7c7bf54ec61360d478fb19c19")
    version("2024.10.0", sha256="eda2d8a4116d4f2429db8550f2457da57279247dd930bb12f821b58391359493")
    version("2024.5.0", sha256="1d021b0b0f933e3b3029ed808eb400c08ba101ca2de4b3483fbc9ca23fcee94a")
    version("2024.3.1", sha256="f39780e282d7d117ffb42bb96992f8a90795e4d0fb0f661a70ca39fe9c43ded9")
    version("2024.2.0", sha256="b6ad1a679f760dda52b1168c859d01b7b80648ea6f7f7c7f5a8a91dc3f3ecb84")
    version("2023.10.0", sha256="330c66757591df346ad3091a53bd907e15348c2ba17d63fd54f5c39c4457d2a5")
    version("2023.1.0", sha256="fbae7f20ff801eb5f7d0bedf81f25c787c0dfac5e982d98fa3884a9cde2b5411")
    version("2022.11.0", sha256="259d5fd5c8e756ff2ea72f42e7613c32667dc2049a4ac3d84364a7ca034acb8b")
    version("2021.7.0", sha256="792ebd3b54de0b30f1ce73f0ba0a8bcc864724f2d9f248cb8d0ece47db0cbde8")
    version("2021.4.0", sha256="8b1a69884855d1a8c038574292e8b861894c3373282d9a469697a2b41d5289a6")
    version("0.9.0", sha256="3f7a62547e425b0b336a6ac2c2e6c6ac824648725bc8391af84bb510a63d1a56")
    version("0.8.0", sha256="176f3fc405471af0f1f1e14cffa3d53ab8906577973d068b976114433c010d9d")
    version("0.7.3", sha256="1b540552c93b47e83c568e87507d6e02993e6d1b30bc7285f2336c81c5014103")
    version("0.4.4", sha256="97697a46e8bf8be34461c2520d6fc4bfca0ed749b22bb2b7c21939fd450a7d63")

    variant("http", default=False, description="HTTPFileSystem support", when="@0.8.1:")

    with default_args(type="build"):
        depends_on("python@3.10:", when="@2025.12:")
        depends_on("python@3.9:", when="@2025.3.2:")

        depends_on("py-hatchling@1.27:", when="@2025.9:")
        depends_on("py-hatchling", when="@2024.5:")
        depends_on("py-hatch-vcs", when="@2024.5:")

        # Historical dependencies
        depends_on("py-setuptools", when="@:2024.4")

    with default_args(type=("build", "run")):
        depends_on("py-aiohttp", when="+http")

        # Historical dependencies
        depends_on("py-requests", when="@:2023+http")
