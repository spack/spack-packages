# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Openssl(Package):  # Uses Fake Autotools, should subclass Package
    """OpenSSL is an open source project that provides a robust, commercial-grade, and
    full-featured toolkit for the Transport Layer Security (TLS) and Secure Sockets Layer (SSL)
    protocols. It is also a general-purpose cryptography library."""

    homepage = "https://www.openssl.org"

    url = "https://www.openssl.org/source/openssl-1.1.1d.tar.gz"
    list_url = "https://www.openssl.org/source/old/"
    list_depth = 1

    maintainers("AlexanderRichert-NOAA")

    tags = ["core-packages", "windows"]

    executables = ["openssl"]

    license("Apache-2.0")

    version("3.6.0", sha256="b6a5f44b7eb69e3fa35dbf15524405b44837a481d43d81daddde3ff21fcbb8e9")
    version("3.5.4", sha256="967311f84955316969bdb1d8d4b983718ef42338639c621ec4c34fddef355e99")
    version("3.4.3", sha256="fa727ed1399a64e754030a033435003991aee36bda9a5b080995cb2ac5cf7f37")
    version("3.3.5", sha256="9d62c00a5a6903740c8703f0e006257f429d565d3b91ac1a9bd4a4c700002e01")
    version("3.2.6", sha256="89681a9ddaa9ed7cf25ea8ef61338db805200bae47d00510490623547380c148")
    version("3.0.18", sha256="d80c34f5cf902dccf1f1b5df5ebb86d0392e37049e5d73df1b3abae72e4ffe8b")

    with default_args(deprecated=True):
        version("3.4.1", sha256="002a2d6b30b58bf4bea46c43bdd96365aaf8daa6c428782aa4feee06da197df3")
        version("3.3.3", sha256="712590fd20aaa60ec75d778fe5b810d6b829ca7fb1e530577917a131f9105539")
        version("3.2.4", sha256="b23ad7fd9f73e43ad1767e636040e88ba7c9e5775bfa5618436a0dd2c17c3716")
        version("3.1.8", sha256="d319da6aecde3aa6f426b44bbf997406d95275c5c59ab6f6ef53caaa079f456f")
        version(
            "3.0.16", sha256="57e03c50feab5d31b152af2b764f10379aecd8ee92f16c985983ce4a99f7ef86"
        )

    # On Cray DVS mounts, we can't make symlinks to /etc/ssl/openssl.cnf,
    # either due to a bug or because DVS is not intended to be POSIX compliant.
    # Therefore, stick to system agnostic certs=mozilla.
    variant(
        "certs",
        default="mozilla",
        values=("mozilla", "system", "none"),
        multi=False,
        description=(
            "Use certificates from the ca-certificates-mozilla package, symlink system "
            "certificates, or use none, respectively. The default is `mozilla`, since it is "
            "system agnostic. Instead of picking certs=system, one can mark openssl as an "
            "external package, to avoid compiling openssl entirely."
        ),
    )
    variant("docs", default=False, description="Install docs and manpages")
    variant("shared", default=True, description="Build shared library version")
    with when("platform=windows"):
        variant("dynamic", default=False, description="Link with MSVC's dynamic runtime library")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")

    depends_on("zlib-api")
    depends_on("perl@5.14.0:", type=("build", "test"))
    depends_on("ca-certificates-mozilla", type="build", when="certs=mozilla")
    depends_on("nasm", when="platform=windows")

    depends_on("gmake", type="build", when="platform=linux")
    depends_on("gmake", type="build", when="platform=darwin")

    @classmethod
    def determine_version(cls, exe):
        output = Executable(exe)("version", output=str, error=str)
        match = re.search(r"OpenSSL.(\S+)*", output)
        return match.group(1) if match else None

    @property
    def libs(self):
        return find_libraries(
            ["libssl", "libcrypto"],
            root=self.prefix,
            recursive=True,
            shared=self.spec.variants["shared"].value,
            runtime=False,
        )

    def handle_fetch_error(self, error):
        tty.warn(
            "Fetching OpenSSL failed. This may indicate that OpenSSL has "
            "been updated, and the version in your instance of Spack is "
            "insecure. Consider updating to the latest OpenSSL version."
        )

    def install(self, spec, prefix):
        # OpenSSL uses these variables in its Makefile or config scripts. If any of them
        # happen to be set in the environment, then this will override what is set in
        # the script or Makefile, leading to build errors.
        for v in ("APPS", "BUILD", "RELEASE", "MACHINE", "SYSTEM"):
            env.pop(v, None)

        if str(spec.target.family) in ("x86_64", "ppc64"):
            # This needs to be done for all 64-bit architectures (except Linux,
            # where it happens automatically?)
            env["KERNEL_BITS"] = "64"

        options = ["zlib"]
        # clang does not support the .arch directive in assembly files.
        if "clang" in self["c"].cc and spec.target.family == "aarch64":
            options.append("no-asm")
        elif "%nvhpc" in spec:
            # Last tested on nvidia@22.3 for x86_64:
            # nvhpc segfaults NVC++-F-0000-Internal compiler error.
            # gen_llvm_expr(): unknown opcode       0  (crypto/rsa/rsa_oaep.c: 248)
            options.append("no-asm")
        elif spec.satisfies("%oneapi"):
            # Last tested on oneapi@2023.1.0 for x86_64:
            # crypto/md5/md5-x86_64.s:684:31: error: expected string
            options.append("no-asm")

        # The default glibc provided by CentOS 7 does not provide proper
        # atomic support when using the NVIDIA compilers
        if self.spec.satisfies("os=centos7 %nvhpc"):
            options.append("-D__STDC_NO_ATOMICS__")

        # Make a flag for shared library builds
        base_args = [
            "--prefix=%s" % prefix,
            "--openssldir=%s" % join_path(prefix, "etc", "openssl"),
        ]
        if spec.satisfies("platform=windows"):
            base_args.extend([f"CC={self.compiler.cc}", f"CXX={self.compiler.cxx}", "VC-WIN64A"])
        else:
            base_args.extend(
                [
                    "-I{0}".format(self.spec["zlib-api"].prefix.include),
                    "-L{0}".format(self.spec["zlib-api"].prefix.lib),
                ]
            )
            base_args.extend(options)

        if spec.satisfies("~shared"):
            base_args.append("no-shared")
        else:
            base_args.append("shared")

        # On Windows, we use perl for configuration and build through MSVC
        # nmake.
        if spec.satisfies("platform=windows"):
            # The configure executable requires that paths with spaces
            # on Windows be wrapped in quotes
            Executable("perl")("Configure", *base_args, ignore_quotes=True)
        else:
            Executable("./config")(*base_args)

        # Remove non-standard compiler options if present. These options are
        # present e.g. on Darwin. They are non-standard, i.e. most compilers
        # (e.g. gcc) will not accept them.
        filter_file(r"-arch x86_64", "", "Makefile")

        if spec.satisfies("platform=windows"):
            host_make = nmake
            make_args = {}
        else:
            host_make = make
            make_args = {"parallel": False}

        host_make()

        if self.run_tests:
            host_make("test", **make_args)  # 'VERBOSE=1'

        install_tgt = "install" if self.spec.satisfies("+docs") else "install_sw"

        # See https://github.com/openssl/openssl/issues/7466#issuecomment-432148137
        host_make(install_tgt, **make_args)

    @run_after("install")
    def link_system_certs(self):
        if self.spec.variants["certs"].value != "system":
            return

        system_dirs = [
            # CentOS, Fedora, RHEL
            "/etc/pki/tls",
            # Ubuntu
            "/usr/lib/ssl",
            # OpenSUSE
            "/etc/ssl",
        ]

        pkg_dir = join_path(self.prefix, "etc", "openssl")

        mkdirp(pkg_dir)

        for directory in system_dirs:
            # Link configuration file
            sys_conf = join_path(directory, "openssl.cnf")
            pkg_conf = join_path(pkg_dir, "openssl.cnf")
            if os.path.exists(sys_conf) and not os.path.exists(pkg_conf):
                symlink(sys_conf, pkg_conf)

            sys_cert = join_path(directory, "cert.pem")
            pkg_cert = join_path(pkg_dir, "cert.pem")
            # If a bundle exists, use it. This is the preferred way on Fedora,
            # where the certs directory does not work.
            if os.path.exists(sys_cert) and not os.path.exists(pkg_cert):
                symlink(sys_cert, pkg_cert)

            sys_certs = join_path(directory, "certs")
            pkg_certs = join_path(pkg_dir, "certs")
            # If the certs directory exists, symlink it into the package.
            # We symlink the whole directory instead of all files because
            # the directory contents might change without Spack noticing.
            if os.path.isdir(sys_certs) and not os.path.islink(pkg_certs):
                if os.path.isdir(pkg_certs):
                    os.rmdir(pkg_certs)
                symlink(sys_certs, pkg_certs)

    @run_after("install")
    def copy_mozilla_certs(self):
        if self.spec.variants["certs"].value != "mozilla":
            return

        pkg_dir = join_path(self.prefix, "etc", "openssl")
        mkdirp(pkg_dir)

        mozilla_pem = self.spec["ca-certificates-mozilla"].pem_path
        pkg_cert = join_path(pkg_dir, "cert.pem")
        install(mozilla_pem, pkg_cert)

    def patch(self):
        if self.spec.satisfies("%nvhpc"):
            # Remove incompatible preprocessor flags
            filter_file("-MF ", "", "Configurations/unix-Makefile.tmpl", string=True)
            filter_file(r"-MT \$\@ ", "", "Configurations/unix-Makefile.tmpl", string=True)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("PERL", self.spec["perl"].prefix.bin.perl)
