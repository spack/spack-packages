# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyIgwnAuthUtils(PythonPackage):
    """Authorisation utilities for IGWN."""

    homepage = "https://git.ligo.org/computing/igwn-auth-utils"
    pypi = "igwn_auth_utils/igwn_auth_utils-1.4.0.tar.gz"
    git = "https://git.ligo.org/computing/igwn-auth-utils.git"

    maintainers("wdconinc")

    license("BSD-3-Clause", checked_by="wdconinc")

    version("1.4.0", sha256="8ebd331a1d6de16e843e94cde2dc0a09d07a7fbc089bc525fa0eabddd89ea187")

    with default_args(type="build"):
        depends_on("py-setuptools@70:")
        depends_on("py-setuptools-scm@3.4.3:+toml")

    with default_args(type=("build", "run")):
        depends_on("py-cryptography@44.0.1:")
        depends_on("py-requests@2.32:")
        depends_on("py-safe-netrc@1:")
        depends_on("py-scitokens@1.8:")
