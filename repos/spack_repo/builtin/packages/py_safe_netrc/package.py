# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySafeNetrc(PythonPackage):
    """Safe netrc file parser."""

    homepage = "https://git.ligo.org/computing/software/safe-netrc"
    pypi = "safe-netrc/safe-netrc-1.0.1.tar.gz"
    git = "https://git.ligo.org/computing/software/safe-netrc.git"

    maintainers("wdconinc")

    license("GPL-2.0-or-later", checked_by="wdconinc")

    version("1.0.1", sha256="1dcc7263b4d9ce72e0109d8e2bc9ba89c8056ccc618d26c8c94802c6fd753720")

    with default_args(type="build"):
        depends_on("py-setuptools@61:")
        depends_on("py-setuptools-scm@6.2:+toml")
