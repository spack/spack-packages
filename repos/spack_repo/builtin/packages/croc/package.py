# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Croc(GoPackage):
    """croc is a tool that allows any two computers to simply and securely transfer files and
    folders.
    """

    homepage = "https://schollz.com/software/croc6"
    url = "https://github.com/schollz/croc/archive/refs/tags/v10.2.5.tar.gz"

    maintainers("zzzoom")

    license("MIT", checked_by="zzzoom")

    version("11.5.2", sha256="2ceddb504be8b5912f4a3bfd76dc28bb18afda54191f2bebcf5b0fb24e63f774")
    version("10.2.5", sha256="993e0bb72e79c5168d78db5c14d84f69beeab819ab4d06f4d98fcddd23487207")

    depends_on("go@1.27.0:", type="build", when="@11.2.3:")
    depends_on("go@1.26.0:", type="build", when="@11.1.1:")
    depends_on("go@1.25.0:", type="build", when="@10.4.0:")
    depends_on("go@1.24.0:", type="build", when="@10.2.5:")
