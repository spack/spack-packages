# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libxcrypt(AutotoolsPackage):
    """libxcrypt is a modern library for one-way hashing of passwords."""

    homepage = "https://github.com/besser82/libxcrypt"
    url = "https://github.com/besser82/libxcrypt/releases/download/v4.4.30/libxcrypt-4.4.30.tar.xz"
    tags = ["build-tools"]
    maintainers("haampie")

    license("LGPL-2.1-or-later")

    version("4.4.38", sha256="80304b9c306ea799327f01d9a7549bdb28317789182631f1b54f4511b4206dd6")
    # 4.4.37 requires pkg-config and is not included here
    version("4.4.36", sha256="e5e1f4caee0a01de2aee26e3138807d6d3ca2b8e67287966d1fefd65e1fd8943")
    version("4.4.35", sha256="a8c935505b55f1df0d17f8bfd59468c7c6709a1d31831b0f8e3e045ab8fd455d")

    variant("obsolete_api", default=False, description="Enable all compatibility interfaces")

    patch("truncating-conversion.patch", when="@4.4.30")

    depends_on("c", type="build")  # generated

    # Some distros have incomplete perl installs, +open catches that.
    depends_on("perl@5.14:+open", type="build")

    patch("commit-95d56e0.patch", when="@4.4.35")

    def configure_args(self):
        args = [
            # Disable test dependency on Python (Python itself depends on libxcrypt).
            "ac_cv_path_python3_passlib=not found",
            # Disable -Werror, which breaks with newer compilers
            "--disable-werror",
        ]
        args += self.enable_or_disable("obsolete-api", variant="obsolete_api")
        return args

    @property
    def libs(self):
        return find_libraries("libcrypt", root=self.prefix, recursive=True)
