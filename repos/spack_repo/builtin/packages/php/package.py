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

    version("8.3.12", sha256="d5d4e6ffc6d6b2f02a87c45741623e08045ec6509ade44a1033e0f8bbb374119")
    version("7.4.33", sha256="dfbb2111160589054768a37086bda650a0041c89878449d078684d70d6a0e411")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("bison", type="build")
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
