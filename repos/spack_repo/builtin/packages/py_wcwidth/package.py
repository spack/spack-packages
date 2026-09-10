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

    version("0.6.0", sha256="cdc4e4262d6ef9a1a57e018384cbeb1208d8abbc64176027e2c2455c81313159")
    version("0.2.14", sha256="4d478375d31bc5395a3c55c40ccdf3354688364cd61c4f6adacaa9215d0b3605")
    version("0.2.7", sha256="1b6d30a98ddd5ce9bbdb33658191fd2423fc9da203fe3ef1855407dcb7ee4e26")
    version("0.2.5", sha256="c4d647b99872929fdb7bdcaa4fbe7f01413ed3d98077df798530e5b04f116c83")
    version("0.1.7", sha256="3df37372226d6e63e1b1e1eda15c594bca98a22d33a23832a90998faa96bc65e")

    with default_args(type="build"):
        depends_on("py-hatchling", when="@0.3:")

        # Historical dependencies
        depends_on("py-setuptools", when="@:0.2")
