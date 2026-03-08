# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyWcwidth(PythonPackage):
    """Measures number of Terminal column cells of wide-character codes"""

    homepage = "https://github.com/jquast/wcwidth"
    pypi = "wcwidth/wcwidth-0.1.7.tar.gz"

    license("MIT")

    version(
        "0.6.0", sha256="cdc4e4262d6ef9a1a57e018384cbeb1208d8abbc64176027e2c2455c81313159"
    )  # FIXME
    version(
        "0.5.3", sha256="53123b7af053c74e9fe2e92ac810301f6139e64379031f7124574212fb3b4091"
    )  # FIXME
    version(
        "0.5.2", sha256="c022c39a02a0134d1e10810da36d1f984c79648181efcc70a389f4569695f5ae"
    )  # FIXME
    version(
        "0.5.0", sha256="f89c103c949a693bf563377b2153082bf58e309919dfb7f27b04d862a0089333"
    )  # FIXME
    version(
        "0.4.0", sha256="46478e02cf7149ba150fb93c39880623ee7e5181c64eda167b6a1de51b7a7ba1"
    )  # FIXME
    version(
        "0.3.5", sha256="7c3463f312540cf21ddd527ea34f3ae95c057fa191aa7a9e043898d20d636e59"
    )  # FIXME
    version(
        "0.3.4", sha256="73d05c07549b4639b7956cd65a9edd35245d8700c0d3467fa723ad4b16dfe815"
    )  # FIXME
    version(
        "0.3.3", sha256="f8f7d42c8a067d909b80b425342d02c423c5edc546347475e1d402fe3d35bb63"
    )  # FIXME
    version(
        "0.3.2", sha256="d469b3059dab6b1077def5923ed0a8bf5738bd4a1a87f686d5e2de455354c4ad"
    )  # FIXME
    version(
        "0.3.1", sha256="5aedb626a9c0d941b990cfebda848d538d45c9493a3384d080aff809143bd3be"
    )  # FIXME
    version(
        "0.3.0", sha256="af1a2fb0b83ef4a7fc0682a4c95ca2576e14d0280bca2a9e67b7dc9f2733e123"
    )  # FIXME
    version("0.2.14", sha256="4d478375d31bc5395a3c55c40ccdf3354688364cd61c4f6adacaa9215d0b3605")
    version("0.2.7", sha256="1b6d30a98ddd5ce9bbdb33658191fd2423fc9da203fe3ef1855407dcb7ee4e26")
    version("0.2.5", sha256="c4d647b99872929fdb7bdcaa4fbe7f01413ed3d98077df798530e5b04f116c83")
    version("0.1.7", sha256="3df37372226d6e63e1b1e1eda15c594bca98a22d33a23832a90998faa96bc65e")

    depends_on("py-setuptools", type="build")
