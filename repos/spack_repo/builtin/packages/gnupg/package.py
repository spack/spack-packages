# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Gnupg(AutotoolsPackage):
    """GNU Pretty Good Privacy (PGP) package."""

    homepage = "https://gnupg.org/index.html"
    url = "https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.3.4.tar.bz2"

    maintainers("alalazo")

    license("GPL-3.0-or-later")

    version("2.5.20", sha256="6461266e99c308419a379abe6c356d54c214136c4589bd65951091138989ffc6")
    version("2.4.9", sha256="dd17ab2e9a04fd79d39d853f599cbc852062ddb9ab52a4ddeb4176fd8b302964")
    version("2.3.8", sha256="540b7a40e57da261fb10ef521a282e0021532a80fd023e75fb71757e8a4969ed")
    version("2.2.40", sha256="1164b29a75e8ab93ea15033300149e1872a7ef6bdda3d7c78229a735f8204c28")

    with default_args(deprecated=True):
        version(
            "2.5.17", sha256="2c1fbe20e2958fd8fb53cf37d7c38e84a900edc0d561a1c4af4bc3a10888685d"
        )
        version(
            "2.5.16", sha256="05144040fedb828ced2a6bafa2c4a0479ee4cceacf3b6d68ccc75b175ac13b7e"
        )
        version(
            "2.5.12", sha256="48d7b15474d330c571128a49eb32ae2332c086ce7945fb94d4c5491b07985e09"
        )
        version(
            "2.5.11", sha256="5f765ec1eb605dce9e9c48679cd43b5818d4d4b84c8ea4c0c60eb5dca13c405c"
        )
        version("2.5.6", sha256="377f9d79af0ce494c0946dbe7c92197425bb522d7edd6f54acbc9869695131a8")
        version("2.5.3", sha256="23128b136aed4e5121e793d1b6c60ee50c8007a9d926c1313e524d05386b54ac")
        version("2.5.2", sha256="7f404ccc6a58493fedc15faef59f3ae914831cff866a23f0bf9d66cfdd0fea29")
        version("2.5.1", sha256="8a34bb318499867962c939e156666ada93ed81f01926590ac68f3ff79178375e")
        version("2.5.0", sha256="2222c827d4e7087f15e7f72739d004abc1d05c6c5f0a5a12b24c6a6cc5d173fb")
        version("2.4.7", sha256="7b24706e4da7e0e3b06ca068231027401f238102c41c909631349dcc3b85eb46")
        version("2.4.6", sha256="95acfafda7004924a6f5c901677f15ac1bda2754511d973bb4523e8dd840e17a")
        version("2.4.5", sha256="f68f7d75d06cb1635c336d34d844af97436c3f64ea14bcb7c869782f96f44277")
        version("2.4.4", sha256="67ebe016ca90fa7688ce67a387ebd82c6261e95897db7b23df24ff335be85bc6")
        version("2.4.3", sha256="a271ae6d732f6f4d80c258ad9ee88dd9c94c8fdc33c3e45328c4d7c126bd219d")
        version("2.4.2", sha256="97eb47df8ae5a3ff744f868005a090da5ab45cb48ee9836dbf5ee739a4e5cf49")
        version("2.4.1", sha256="76b71e5aeb443bfd910ce9cbc8281b617c8341687afb67bae455877972b59de8")
        version("2.4.0", sha256="1d79158dd01d992431dd2e3facb89fdac97127f89784ea2cb610c600fb0c1483")
        version("2.3.7", sha256="ee163a5fb9ec99ffc1b18e65faef8d086800c5713d15a672ab57d3799da83669")

    depends_on("c", type="build")

    depends_on("npth@1.2:")

    depends_on("libgpg-error@1.24:")
    depends_on("libgpg-error@1.41:", when="@2.3:")
    depends_on("libgpg-error@1.46:", when="@2.4:")
    # https://github.com/gpg/gnupg/commit/d78131490edd7f7db142702b8144bc30e65dbd8d
    depends_on("libgpg-error@1.50:", when="@2.5:")
    # https://github.com/gpg/gnupg/commit/c3bab200d97460028d842d76484b4c08fb947fef
    depends_on("libgpg-error@1.51:", when="@2.5.2:")
    # https://github.com/gpg/gnupg/commit/39cc15029017ba5fd6d04f710e5a3125ed3b30a8
    depends_on("libgpg-error@1.56:", when="@2.5.13:")

    depends_on("libgcrypt@1.7.0:")
    depends_on("libgcrypt@1.9.1:", when="@2.3:")
    # https://github.com/gpg/gnupg/commit/f305e703d51079a17bcfc15d54f4c5f591dcff56
    depends_on("libgcrypt@1.11:", when="@2.5:")

    depends_on("libksba@1.3.4:")
    depends_on("libksba@1.6.3:", when="@2.4:")

    depends_on("libassuan@:2", when="@:2.4.3")
    depends_on("libassuan@2.5:", when="@2.2.15:")
    # https://github.com/gpg/gnupg/commit/0d20b79ab79819f6177737a61e886d4820e475e2
    depends_on("libassuan@3:", when="@2.5.0:")

    depends_on("pinentry", type="run")
    depends_on("iconv")
    depends_on("zlib-api")

    # note: perl and curl are gnupg1 dependencies when keyserver support is
    # requested, but we disable that.

    executables = ["^gpg$", "^gpg-agent$"]

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"gpg \(GnuPG\) (\S+)", output)
        return match.group(1) if match else None

    @run_after("install")
    def add_gpg2_symlink(self):
        if self.spec.satisfies("@2.0:2"):
            symlink("gpg", self.prefix.bin.gpg2)

    def configure_args(self):
        args = [
            "--disable-nls",
            "--disable-bzip2",
            "--disable-ldap",
            "--disable-regex",
            f"--with-zlib={self.spec['zlib-api'].prefix}",
            "--without-tar",
            "--without-readline",
        ]

        if self.spec.satisfies("@2:"):
            args.extend(
                [
                    "--disable-sqlite",
                    "--disable-ntbtls",
                    "--disable-gnutls",
                    f"--with-pinentry-pgm={self.spec['pinentry'].command.path}",
                    f"--with-libgpg-error-prefix={self.spec['libgpg-error'].prefix}",
                    f"--with-libgcrypt-prefix={self.spec['libgcrypt'].prefix}",
                    f"--with-libassuan-prefix={self.spec['libassuan'].prefix}",
                    f"--with-ksba-prefix={self.spec['libksba'].prefix}",
                    f"--with-npth-prefix={self.spec['npth'].prefix}",
                ]
            )
            if self.spec["iconv"].name == "libiconv":
                args.append(f"--with-libiconv-prefix={self.spec['iconv'].prefix}")
            else:
                args.append("--without-libiconv-prefix")

        if self.run_tests:
            args.append("--enable-all-tests")

        return args
