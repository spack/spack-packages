# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class JacamarCi(GoPackage):
    """Jacamar CI is a HPC focused CI/CD driver for the GitLab custom executor."""

    homepage = "https://gitlab.com/ecp-ci/jacamar-ci"
    url = "https://gitlab.com/ecp-ci/jacamar-ci/-/archive/v0.24.0/jacamar-ci-v0.24.0.tar.gz"
    git = "https://gitlab.com/ecp-ci/jacamar-ci.git"

    maintainers("paulbry")

    license("Apache-2.0 OR MIT")

    version("develop", branch="develop")
    version("0.27.4", sha256="3e9983015340c5e0572a8e64e8740f18386e3eccd7186264817b7e9db56cf6ee")
    version("0.27.1", sha256="15e506eeec62de1adb4a6547135f3fef6496898d8b6773f694c53bba6269614b")
    version("0.27.0", sha256="1a530931bda840a421d361e07b4e956750c3e569c55244981bafdb8436530bf9")
    version("0.26.2", sha256="23e1c7367eb1514ee0c7802123c5fd5559182acc2f84d76cf831b06e5ab39d7f")
    version("0.26.0", sha256="da63c396726af313804da5ec3704ce3754ba3eef5ca267746b594422f542dbea")
    version("0.25.0", sha256="20626ed931f5bf6ba1d5a2dd56af5793efa69a4f355bdac9b8bf742aaf806653")
    version("0.24.2", sha256="d2b8be464b88a92df0ad2ba1e846226b993c4162779432cb8366fb9bca5c40db")
    version("0.24.1", sha256="fe1036fee2e97e38457212bf1246895803eeb6e1a6aa1ecd24eba1d3ea994029")
    version("0.23.0", sha256="796679e13ece5f88dd7d4a4f40a27a87a6f3273085bb07043b258a612a4b43d3")

    conflicts("platform=darwin", msg="Jacamar CI does not support MacOS")

    depends_on("go@1.25:", type="build", when="@0.27.4:")
    depends_on("go@1.24:", type="build", when="@0.27.0:")
    depends_on("go@1.23:", type="build", when="@0.26.0:")
    depends_on("go@1.22.7:", type="build", when="@0.23.0:")
    depends_on("gmake", type="build")
    depends_on("libc", type="link")
    depends_on("libseccomp", type="link")

    executables = ["^jacamar$", "^jacamar-auth$"]
    phases = ["build", "install"]

    def url_for_version(self, version):
        return f"https://gitlab.com/ecp-ci/jacamar-ci/-/archive/v{version}/jacamar-ci-v{version}.tar.gz"

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"Version:\s*(\S+)", output)
        return match.group(1) if match else None

    def build(self, spec, prefix):
        make("VERSION={0}".format(spec.version), "build")

    def install(self, spec, prefix):
        make("PREFIX={0}".format(prefix), "install")
