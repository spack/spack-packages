# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class HpnSsh(AutotoolsPackage):
    """HPN-SSH : a version of OpenSSH optimised for high-speed transfers and high-latency networks."""

    homepage = "https://psc.edu/hpn-ssh-home/"
    git = "https://github.com/rapier1/hpn-ssh.git"

    version("18.12.0", tag="hpn-18.12.0")
    version("18.11.1", tag="hpn-18.11.1")

    variant("zlib", default=True, description="Enable transport compression support")
    variant("pam", default=False, description="Enable PAM support")
    variant("libedit", default=False, description="Enable libedit support for sftp")
    variant("kerberos", default=False, description="Enable Kerberos/GSSAPI support")
    variant("selinux", default=False, description="Enable SELinux support")
    variant(
        "security-key",
        default=False,
        description="Enable built-in U2F/FIDO2 security key support (requires libfido2)",
    )

    depends_on("c", type="build")

    # Building from git: the configure script must be generated
    force_autoreconf = True
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("pkgconfig", type="build")

    # Upstream strongly recommends OpenSSL 3.0 or higher
    depends_on("openssl@3:")
    depends_on("zlib-api", when="+zlib")
    depends_on("linux-pam", when="+pam")
    depends_on("libedit", when="+libedit")
    depends_on("krb5", when="+kerberos")

    def configure_args(self):
        spec = self.spec
        args = [f"--with-ssl-dir={spec['openssl'].prefix}"]

        if spec.satisfies("+zlib"):
            args.append(f"--with-zlib={spec['zlib-api'].prefix}")
        else:
            args.append("--without-zlib")

        if spec.satisfies("+pam"):
            args.append("--with-pam")
        if spec.satisfies("+libedit"):
            args.append(f"--with-libedit={spec['libedit'].prefix}")
        if spec.satisfies("+kerberos"):
            args.append(f"--with-kerberos5={spec['krb5'].prefix}")
        if spec.satisfies("+selinux"):
            args.append("--with-selinux")

        return args
