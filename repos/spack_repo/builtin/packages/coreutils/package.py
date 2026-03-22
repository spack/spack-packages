# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.gnu import GNUMirrorPackage

from spack.package import *


class Coreutils(AutotoolsPackage, GNUMirrorPackage):
    """The GNU Core Utilities are the @_y{basic} file, shell and text
    manipulation utilities of the GNU operating system.

    While many operating systems have programs with these names,
    most of the programs in this package have significant advantages over their Unix
    counterparts, such as greater speed, additional options, and fewer
    arbitrary limits.

    These are the @/r{core} utilities which are a necessary component of every operating system.
    """
    docstring_uses_rich_text = True
    docstring_has_extended_text = True

    git = "git://git.sv.gnu.org/coreutils"
    homepage = "https://www.gnu.org/software/coreutils/"
    gnu_mirror_path = "coreutils/coreutils-8.26.tar.xz"

    tags = ["core-packages"]
    maintainers("cosmicexplorer")

    executables = ['^(?:ck|b2|sha224|sha256|sha384|sha512|md5)sum$']

    license("GPL-3.0-or-later")

    # A vast array of extremely significant performance improvements in this release:
    # https://lists.gnu.org/archive/html/info-gnu/2026-04/msg00006.html
    version("9.11", sha256="394024eda0a5955217ceda9cd1201e65dc8fa3aa29c2951135a49521d57c3cc3")

    version("9.10", sha256="16535a9adf0b10037364e2d612aad3d9f4eca3a344949ced74d12faf4bd51d25")
    version("9.7", sha256="e8bb26ad0293f9b5a1fc43fb42ba970e312c66ce92c1b0b16713d7500db251bf")
    version("9.5", sha256="cd328edeac92f6a665de9f323c93b712af1858bc2e0d88f3f7100469470a1b8a")
    version("9.4", sha256="ea613a4cf44612326e917201bbbcdfbd301de21ffc3b59b6e5c07e040b275e52")
    version("9.3", sha256="adbcfcfe899235b71e8768dcf07cd532520b7f54f9a8064843f8d199a904bbaa")
    version("9.2", sha256="6885ff47b9cdb211de47d368c17853f406daaf98b148aaecdf10de29cc04b0b3")
    version("9.1", sha256="61a1f410d78ba7e7f37a5a4f50e6d1320aca33375484a3255eddf17a38580423")
    version("9.0", sha256="ce30acdf4a41bc5bb30dd955e9eaa75fa216b4e3deb08889ed32433c7b3b97ce")
    version("8.32", sha256="4458d8de7849df44ccab15e16b1548b285224dbba5f08fac070c1c0e0bcc4cfa")
    version("8.31", sha256="ff7a9c918edce6b4f4b2725e3f9b37b0c4d193531cac49a48b56c4d0d3a9e9fd")
    version("8.30", sha256="e831b3a86091496cdba720411f9748de81507798f6130adeaef872d206e1b057")
    version("8.29", sha256="92d0fa1c311cacefa89853bdb53c62f4110cdfda3820346b59cbd098f40f955e")
    version("8.26", sha256="155e94d748f8e2bc327c66e0cbebdb8d6ab265d2f37c3c928f7bf6c3beba9a8e")
    version("8.23", sha256="ec43ca5bcfc62242accb46b7f121f6b684ee21ecd7d075059bf650ff9e37b82d")

    version("master", branch="master")
    version("9.9", tag="v9.9", commit="0ae5bdc7a8311efd3efe43363050710d6ea1c367")
    version("arbitrary", commit="6a37187a5f7c0202f7f147257458b1fdf38b0977")

    _version_at_eol = re.compile(r'\s+([0-9]+\.[0-9]+\S*)$')

    @classmethod
    def determine_version(cls, exe):
        exe = Executable(exe)
        m = cls._version_at_eol.search(exe("--version").splitlines()[0])
        if m:
            return m.group(1)
        return None

    depends_on("c", type="build")

    variant("single-binary",
            values=["disabled", "symlinks", "shebangs"],
            default="disabled",
            when="@8.23:",
            description="build all selected programs into a single 'coreutils' binary")
    variant("gprefix", default=False,
            description="prefix commands with 'g', to avoid conflicts with OS utilities "
            "(e.g. 'gsha256sum')")

    variant("crypto", default="builtin",
            values=[
                "builtin",
                conditional("openssl", when="@8.23:"),
                conditional("linux-crypto", when="platform=linux"),
            ],
            description="cryptographic implementation to use. \n"
            "if selected, the fallback will be used for:\n"
            "[MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512]")

    variant("gmp", default=False,
            description="use the GNU Multiple Precision (GMP) library")
    variant("nls", default=False, description="Enable Native Language Support")
    variant("gnulib", default=True,
            when="@9:",
            description="Update from gnulib sources.")
    variant("threads", default=True,
            description="Enable threading. Used in the `sort` command.")

    variant("static", default=False,
            description="Build into statically-linked binaries.")

    with default_args(type="build"):
        depends_on("gnulib", when="+gnulib")
        depends_on("autoconf@2.64:")
        depends_on("automake@1.11.2:")
        depends_on("bison")
        depends_on("git@1.5.5:")
        depends_on("gperf")
        depends_on("gzip")
        depends_on("help2man")
        depends_on("m4")
        depends_on("make")
        depends_on("perl")
        depends_on("tar")
        depends_on("texinfo@6.1:")
        depends_on("wget")
        depends_on("xz")

    depends_on("gmp", when="+gmp")
    depends_on("gettext@0.19.2:", when="+nls")
    depends_on("libiconv", when="+nls")

    depends_on("openssl@3:", type="link", when="crypto=openssl")

    # 84863a1c4dc8cca8fb0f6f670f67779cdd2d543b
    # Author:     Bruno Haible <bruno@clisp.org>
    # AuthorDate: Sat Apr 30 14:09:00 2022 +0200
    #
    # string: Avoid syntax error on glibc systems with GCC 11.
    #
    # Reported by Tom Tromey <tromey@adacore.com> in
    # <https://lists.gnu.org/archive/html/bug-gnulib/2022-04/msg00075.html>
    # and by Satadru Pramanik <satadru@umich.edu> in
    # <https://lists.gnu.org/archive/html/bug-gnulib/2022-04/msg00076.html>.
    #
    # * lib/string.in.h (strndup): Don't rededeclare strndup if it is defined
    # as a macro.
    patch("gnulib-strndup-cpp-syntax.patch", when="@9.1")

    patch(
        "https://src.fedoraproject.org/rpms/coreutils/raw/6b50cb9f/f/coreutils-8.32-ls-removed-dir.patch",
        when="@8.32",
        sha256="5878894375a8fda98150783430b30c0b7104899dc5522034ebcaf8c961183b7e",
    )

    # Avoid symlinking GNUMakefile to GNUMakefile
    build_directory = "spack-build"

    @when("+gnulib")
    def autoreconf(self, spec, prefix):
        bootstrap = Executable("./bootstrap")
        bootstrap("--pull", "--gen", "--bootstrap-sync", "--skip-po")

    def configure_args(self):
        configure_args = []

        if self.spec.satisfies('+gnulib'):
            gnulib = self.spec["gnulib"]
            configure_args.append(f"--with-gnulib-prefix={gnulib.prefix}")

        if self.spec.satisfies('+gprefix'):
            configure_args.append("--program-prefix=g")
        single_binary = self.spec.variants["single-binary"].value
        if single_binary == 'symlinks':
            configure_args.append('--enable-single-binary=symlinks')
        elif single_binary == 'shebangs':
            configure_args.append('--enable-single-binary=shebangs')
        else:
            assert single_binary == 'disabled', single_binary

        # Configure the threading implementation.
        if self.spec.satisfies('+threads'):
            if self.spec.satisfies('platform=windows'):
                configure_args.append("--enable-threads=windows")
            else:
                configure_args.append("--enable-threads=isoc+posix")
        else:
            configure_args.append("--disable-threads")

        # Configure the gmp bignum library.
        if self.spec.satisfies('+gmp'):
            gmp = self.spec["gmp"]
            configure_args.append(f"--with-libgmp-prefix={gmp.prefix}")
        else:
            configure_args.append('--without-libgmp-prefix')

        # Configure language support.
        if self.spec.satisfies('+nls'):
            gettext = self.spec["gettext"]
            libiconf = self.spec["libiconv"]
            configure_args.extend([
                f"--with-libiconv-prefix={libiconv.prefix}",
                f"--with-libintl-prefix={gettext.prefix}",
            ])
        else:
            configure_args.append('--disable-nls')

        # Configure crypto support.
        crypto = self.spec.variants["crypto"].value
        if crypto == "openssl":
            configure_args.append("--with-openssl")
        elif crypto == "linux-crypto":
            configure_args.append("--with-linux-crypto")
        else:
            assert crypto == "builtin", crypto
            configure_args.append("--without-openssl")
            if self.spec.satisfies("platform=linux"):
                configure_args.append("--without-linux-crypto")

        if self.spec.satisfies('+static'):
            configure_args.append('LDFLAGS=-static')

        # TODO: why is this here? is this still necessary?
        if self.spec.satisfies("platform=darwin"):
            configure_args.append("gl_cv_func_ftello_works=yes")

        return configure_args
