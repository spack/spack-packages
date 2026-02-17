# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Sqlcipher(AutotoolsPackage):
    """SQLCipher is an SQLite extension that provides 256 bit AES encryption
    of database files.
    """

    homepage = "https://www.zetetic.net/sqlcipher/"
    url = "https://github.com/sqlcipher/sqlcipher/archive/v4.4.1.tar.gz"
    git = "https://github.com/sqlcipher/sqlcipher.git"

    maintainers("rmsds")

    license("BSD-3-Clause")

    version("4.6.1", sha256="d8f9afcbc2f4b55e316ca4ada4425daf3d0b4aab25f45e11a802ae422b9f53a3")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("openssl")
    depends_on("tcl", type="build")
    depends_on("zlib-api")

    def configure_args(self):
        args = []
        args.append("--enable-tempstore=yes")
        args.append("CFLAGS=-DSQLITE_HAS_CODEC")
        return args
