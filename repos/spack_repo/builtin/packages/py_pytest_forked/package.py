# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPytestForked(PythonPackage):
    """Run tests in isolated forked subprocesses."""

    homepage = "https://github.com/pytest-dev/pytest-forked"
    pypi = "pytest-forked/pytest_forked-1.7.5.tar.gz"

    license("MIT")

    version("1.7.5", sha256="00f2bee51612f29b8e6b81eed2c3b2975e824c2693394f5bdaf7a1369078ba5f")
    version("1.6.0", sha256="4dafd46a9a600f65d822b8f605133ecf5b3e1941ebb3588e943b4e3eb71a5a3f")
    version("1.5.0", sha256="2933c4da9d058231b79788d6e731ff460bd541dddc1d63649ff2c147a4e23335")
    version("1.4.0", sha256="8b67587c8f98cbbadfdd804539ed5455b6ed03802203485dd2f53c1422d7440e")
    version("1.3.0", sha256="6aa9ac7e00ad1a539c41bec6d21011332de671e938c7637378ec9710204e37ca")
    version("1.2.0", sha256="65f96334863d9cbe53d21f73e8febc4dd61b8d1fdcac7b487d9af07a5d02a938")
    version("1.1.3", sha256="1805699ed9c9e60cb7a8179b8d4fa2b8898098e82d229b0825d8095f0f261100")
    version("1.1.2", sha256="6d1c9052f5dd766a7cb2f8947fef7d32b6bbaf9aaea8cd971a1f84d257253498")
    version("1.1.1", sha256="e2d46f319c8063a3a0536b18f9cdea6eea3bc9fe2cb16c94e1d6fad3abc37300")

    depends_on("python@3.10:", type=("build", "run"), when="@1.7:")
    depends_on("python@3.7:", type=("build", "run"), when="@1.5:1.6")
    depends_on("python@3.6:", type=("build", "run"), when="@1.4")
    depends_on("python@2.7:2.8,3.5:", type=("build", "run"), when="@1.2:1.3")
    depends_on("python@2.7:2.8,3.4:", type=("build", "run"), when="@:1.1")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@41.4:", type="build", when="@1.1.2:")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-setuptools-scm@3.3:", type="build", when="@1.1.2:")

    depends_on("py-pytest@7:", type=("build", "run"), when="@1.7.4:")
    depends_on("py-pytest@3.10:", type=("build", "run"), when="@1.3:")
    depends_on("py-pytest@3.1.0:", type=("build", "run"))
    depends_on("py-py", type=("build", "run"), when="@1.3:1.6")

    def url_for_version(self, version):
        if version < Version("1.7"):
            return super().url_for_version(version).replace("_", "-")
        return super().url_for_version(version)
