# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyThrottler(PythonPackage):
    """Zero dependency Python package for easy throttling with asyncio support."""

    homepage = "https://github.com/uburuntu/throttler"
    pypi = "throttler/throttler-1.2.1.tar.gz"

    maintainers("charmoniumQ")

    license("MIT")

    version("1.2.3", sha256="d2f5b0b499d62f1fc984dcac8043450b606549b0097753a9c8a707f7427c27e1")
    version("1.2.2", sha256="d54db406d98e1b54d18a9ba2b31ab9f093ac64a0a59d730c1cf7bb1cdfc94a58")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@61:", type="build", when="@1.2.3:")
    depends_on("py-setuptools@:81", type="build", when="@:1.2.2")
