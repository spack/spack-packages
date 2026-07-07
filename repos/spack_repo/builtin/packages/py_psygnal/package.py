# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPsygnal(PythonPackage):
    """Fast python callback/event system modeled after Qt Signals."""

    homepage = "https://github.com/pyapp-kit/psygnal"
    pypi = "psygnal/psygnal-0.14.0.tar.gz"

    license("BSD-3-Clause")

    version("0.14.2", sha256="588d1a7a0212db8ffc720ef2fb03e849e0280f4f156e5f5922e6b99b13c69689")
    version("0.14.0", sha256="bdd219217d240611af31621a6701505256e245abb6e0dc86d7e4443c3f7d6d41")

    with default_args(type="build"):
        depends_on("py-hatchling@1.8:")
        depends_on("py-hatch-vcs")
