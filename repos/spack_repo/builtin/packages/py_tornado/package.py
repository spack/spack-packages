# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTornado(PythonPackage):
    """Tornado is a Python web framework and asynchronous networking library."""

    homepage = "https://github.com/tornadoweb/tornado"
    pypi = "tornado/tornado-6.1.tar.gz"

    license("Apache-2.0")

    version("6.5.7", sha256="66c513a76cda70d53907bc27cf1447557699c2e95aa48ba27a442ff61c3ddfc2")
    with default_args(deprecated=True):
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-pw6j-qg29-8w7f
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-cx3h-4qpv-8hc9
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-mgf9-4vpg-hj56
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-3x9g-8vmp-wqvf
        version("6.5.5", sha256="192b8f3ea91bd7f1f50c06955416ed76c6b72f96779b962f07f911b91e8d30e9")
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-78cv-mqj4-43f7
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-qjxf-f2mg-c6mc
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-jhmp-mqwm-3gq8
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-c98p-7wgm-6p64
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-pr2v-jx2c-wg9f
        version("6.5.2", sha256="ab53c8f9a0fa351e2c0741284e06c7a45da86afb544133201c5cc8578eb076a0")
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-7cx3-6m66-7c5m
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-8w49-h785-mj3c
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-w235-7p84-xx57
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-753j-mpmx-qq6g
        version("6.3.3", sha256="e7d8db41c0181c80d76c982aacc442c0783a2c54d6400fe028954201a2e032fe")
        # https://github.com/tornadoweb/tornado/security/advisories/GHSA-qppv-j76h-2rpx
        version("6.2", sha256="9b630419bde84ec666bfd7ea0a4cb2a8a651c2d5cccdbdd1972a0c859dfc3c13")
        version("6.1", sha256="33c6e81d7bd55b468d2e793517c909b139960b6c790a60b7991b9b6b76fb9791")
        version("6.0.3", sha256="c845db36ba616912074c5b1ee897f8e0124df269468f25e4fe21fe72f6edd7a9")
        version("5.1.1", sha256="4e5158d97583502a7e2739951553cbd88a72076f152b4b11b64b9a10c4c49409")
        version("4.4", sha256="3176545b6cb2966870db4def4f646da6ab7a0c19400576969c57279a7561ab02")

    with default_args(type=("build", "link", "run")):
        depends_on("python@3.9:", when="@6.5:")
        depends_on("python@3.8:", when="@6.3:")

    with default_args(type="build"):
        depends_on("c")
        depends_on("py-setuptools")
