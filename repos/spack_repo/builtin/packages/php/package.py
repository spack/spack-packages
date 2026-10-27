# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Php(AutotoolsPackage):
    """
    PHP is a popular general-purpose scripting language that is especially
    suited to web development. Fast, flexible and pragmatic, PHP powers
    everything from your blog to the most popular websites in the world.
    """

    homepage = "https://php.net/"
    url = "https://github.com/php/php-src/archive/php-7.3.13.tar.gz"

    license("PHP-3.01")

    version("8.5.12", sha256="914702592c81f85cb3f6c2bca0cbe4217d3fe5f5a4b8ca34a8f93f74a3575fc7")
    version("8.4.27", sha256="ae5896236c1b5bba6c36dcdd2e30c87ccda595d28650d18e6c007eebb0db68ab")
    version("8.3.36", sha256="132154b55122efe74ed55c6a51486dcf6a7797a2a8df66e5361c2bb6f0f1b527")

    # CVE-2026-109618, CVE-2026-109619
    with default_args(deprecated=True):
        version(
            "8.3.12", sha256="d5d4e6ffc6d6b2f02a87c45741623e08045ec6509ade44a1033e0f8bbb374119"
        )
        version(
            "7.4.33", sha256="dfbb2111160589054768a37086bda650a0041c89878449d078684d70d6a0e411"
        )

    depends_on("c", type="build")

    # buildconf only runs autoconf/autoheader; libtool.m4 is bundled in build/
    depends_on("autoconf@2.68:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("bison@3:", type="build")
    depends_on("re2c", type="build")
    depends_on("bash", type="build")
    depends_on("libiconv", when="@8:")
    depends_on("libxml2")
    depends_on("sqlite")

    patch("sbang-7.patch", when="@7")
    patch("sbang-8.patch", when="@8")

    def patch(self):
        """
        phar sbang is added before build phase.
        Because phar is php script with binary data
        (Not UTF-8 text file) And phar is embeded own sha1 checksum.
        """
        shebang_limit = 127

        if len(self.prefix.bin.php) + 2 <= shebang_limit:
            return

        new_sbang_line = "#!/bin/bash %s" % sbang_install_path()
        original_bang = '-b "$(PHP_PHARCMD_BANG)"'
        makefile = join_path("ext", "phar", "Makefile.frag")
        filter_file(
            original_bang,
            original_bang + ' -z "{0}"'.format(new_sbang_line),
            makefile,
            string=True,
        )

    def autoreconf(self, spec, prefix):
        bash = which("bash", required=True)
        bash("./buildconf", "--force")

    @when("@8:")
    def configure_args(self):
        args = [f"--with-iconv={self.spec['libiconv'].prefix}"]
        return args
