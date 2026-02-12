# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libgcrypt(AutotoolsPackage):
    """Cryptographic library based on the code from GnuPG."""

    homepage = "https://gnupg.org/software/libgcrypt/index.html"
    url = "https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.8.5.tar.bz2"

    maintainers("alalazo")

    license("LGPL-2.1-or-later AND GPL-2.0-or-later")

    version("1.12.0", sha256="0311454e678189bad62a7e9402a9dd793025efff6e7449898616e2fc75e0f4f5")
    version("1.11.2", sha256="6ba59dd192270e8c1d22ddb41a07d95dcdbc1f0fb02d03c4b54b235814330aac")
    version("1.11.1", sha256="24e91c9123a46c54e8371f3a3a2502f1198f2893fbfbf59af95bc1c21499b00e")
    version("1.10.3", sha256="8b0870897ac5ac67ded568dcfadf45969cfa8a6beb0fd60af2a9eadc2a3272aa")

    depends_on("c", type="build")

    depends_on("libgpg-error@1.27:")
    depends_on("libgpg-error@1.49:", when="@1.11:")
    depends_on("libgpg-error@1.56:", when="@1.12:")

    def flag_handler(self, name, flags):
        # https://dev.gnupg.org/T7634
        if name == "ldflags" and self.spec.satisfies("@1.11.1 platform=linux"):
            flags.append("-lpthread")

        # We should not inject optimization flags through the wrapper, because
        # the jitter entropy code should never be compiled with optimization
        # flags, and the build system ensures that
        return (None, flags, None)

    patch("o_flag_munging-1.10.patch", when="@1.10")

    def check(self):
        # Without this hack, `make check` fails on macOS when SIP is enabled
        # https://bugs.gnupg.org/gnupg/issue2056
        # https://github.com/Homebrew/homebrew-core/pull/3004
        if self.spec.satisfies("platform=darwin"):
            old = self.prefix.lib.join("libgcrypt.20.dylib")
            new = join_path(self.stage.source_path, "src", ".libs", "libgcrypt.20.dylib")
            filename = "tests/.libs/random"

            install_name_tool = Executable("install_name_tool")
            install_name_tool("-change", old, new, filename)

        make("check")
