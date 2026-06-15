# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHtgettoken(PythonPackage):
    """htgettoken gets OIDC authentication tokens for High Throughput Computing
    via a Hashicorp vault server."""

    homepage = "https://github.com/fermitools/htgettoken"

    # htgettoken is not available on PyPi
    url = "https://github.com/fermitools/htgettoken/archive/refs/tags/v1.16.tar.gz"
    git = "https://github.com/fermitools/htgettoken.git"

    maintainers("wdconinc")

    license("BSD-3-Clause")

    version("2.6", sha256="d553d40b8b1ad794d4fa36e4a88e4c6343f12bc4498b3143d297d1c60d1877b4")
    version("2.0-2", sha256="80b1b15cc4957f9d1cb5e71a1fbdc5d0ac82de46a888aeb7fa503b1465978b13")
    version("1.16-33-g3788bb4", commit="3788bb4733e5e8f856cee51566df9a36cbfe097d", deprecated=True)
    version("1.16-20-g8b72f48", commit="8b72f4800ef99923dac99dbe0756a26266a27886", deprecated=True)

    depends_on("py-setuptools@30.3:", type="build")

    depends_on("py-gssapi", type=("build", "run"))
    depends_on("py-paramiko", type=("build", "run"))
    depends_on("py-urllib3", type=("build", "run"))

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        dir = os.environ.get("XDG_RUNTIME_DIR", "/tmp")
        uid = os.environ.get("UID", str(os.geteuid()))
        file = join_path(dir, "bt_u" + uid)
        env.set("BEARER_TOKEN", file)
        env.set("BEARER_TOKEN_FILE", file)
