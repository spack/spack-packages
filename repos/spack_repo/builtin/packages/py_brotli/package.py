# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBrotli(PythonPackage):
    """Python bindings for the Brotli compression library."""

    homepage = "https://github.com/google/brotli"
    pypi = "brotli/brotli-1.2.0.tar.gz"

    license("MIT")

    version("1.2.0", sha256="e310f77e41941c13340a95976fe66a8a95b01e783d430eeaf7a2f87e0a57dd0a")
    version(
        "1.1.0",
        sha256="81de08ac11bcb85841e440c13611c00b67d3bf82698314928d0b676362546724",
        url="https://files.pythonhosted.org/packages/source/b/Brotli/Brotli-1.1.0.tar.gz",
        deprecated=True,
    )

    def setup_build_environment(self, env):
        env.set("USE_SYSTEM_BROTLI", "1")

    with when("@1.2:"):
        depends_on("brotli@1.2:", type="link")
        depends_on("py-pkgconfig", type="build")

    depends_on("python", type=("build", "link", "run"))
    depends_on("c", type="build")
    depends_on("py-setuptools", type="build")
