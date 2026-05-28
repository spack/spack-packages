# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyExceptiongroup(PythonPackage):
    """A backport of the BaseExceptionGroup and ExceptionGroup classes from Python 3.11."""

    homepage = "https://github.com/agronholm/exceptiongroup"
    pypi = "exceptiongroup/exceptiongroup-1.0.4.tar.gz"

    version("1.3.1", sha256="8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219")
    version("1.1.1", sha256="d484c3090ba2889ae2928419117447a14daf3c1231d5e30d0aae34f354f01785")
    version("1.0.4", sha256="bd14967b79cd9bdb54d97323216f8fdf533e278df937aa2a90089e7d6e06e5ec")

    depends_on("py-flit-scm", type="build")

    depends_on("py-typing-extensions@4.6:", when="@1.3: ^python@:3.12", type=("build", "run"))
