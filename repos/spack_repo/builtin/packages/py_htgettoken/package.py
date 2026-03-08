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
    version("2.5", sha256="a5fd9d81883d7bc3bcd192ee5e0e477e71b3297a25da063b97bc6779309eb67a")
    version("2.4", sha256="0178e6ae14a9768c981f66bc9e68b99164a094ecf3120854eb23a5a9cef1763d")
    version("2.3", sha256="73f7be0bca09c668928286c05d6786e841783ee87cdede5111bf0445620fd30a")
    version("2.2-2", sha256="47fc2a416f4cca97546d4faa3b471a162692c274ab126ceb05dc4982cd4e6bf7")
    version("2.2", sha256="5c323a7f8f04df558cd4e7b879a7a5e1d660f6a54904e914f799032c4c01139b")
    version("2.1", sha256="eafd54ae81dc19390a2b9f8f5e93a64fa0ef407fa38416194a7179f8c093e294")
    version("2.0-2", sha256="80b1b15cc4957f9d1cb5e71a1fbdc5d0ac82de46a888aeb7fa503b1465978b13")
    # The following versions refer to setuptools-buildable commits after 1.16;
    # they are special reproducible version numbers from `git describe`
    version("1.16-33-g3788bb4", commit="3788bb4733e5e8f856cee51566df9a36cbfe097d")
    version("1.16-20-g8b72f48", commit="8b72f4800ef99923dac99dbe0756a26266a27886")

    # Older versions do not have a python build system

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
