# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "0.9.0": {
        "darwin-x86_64": "7d3730694707605d6e60cec4efcb79a0632d61babc035aa16cda1b897536acf5",
        "linux-aarch64": "179c579ef3481317d130adebede74a34dbbc2df961a70916dd4039ebf0735fae",
        "linux-armv6hf": "03deed9ded9dd66434ccf9649815bcde7d275d6c9f6dcf665b83391673512c75",
        "linux-x86_64": "700324c6dd0ebea0117591c6cc9d7350d9c7c5c287acbad7630fa17b1d4d9e2f",
    },
    "0.10.0": {
        "darwin-aarch64": "bbd2f14826328eee7679da7221f2bc3afb011f6a928b848c80c321f6046ddf81",
        "linux-aarch64": "324a7e89de8fa2aed0d0c28f3dab59cf84c6d74264022c00c22af665ed1a09bb",
        "linux-armv6hf": "1c89cb51e1412b580d7ba8aac240251ffb0b829788f83d2daa4a82da42d275e4",
        "linux-riscv64": "be1f2028951783424c7a5dc744ac0bab8d5b181189e80f640cc56f481f1e371e",
        "linux-x86_64": "6c881ab0698e4e6ea235245f22832860544f17ba386442fe7e9d629f8cbedf87",
    },
    "0.11.0": {
        "darwin-aarch64": "56affdd8de5527894dca6dc3d7e0a99a873b0f004d7aabc30ae407d3f48b0a79",
        "linux-aarch64": "12b331c1d2db6b9eb13cfca64306b1b157a86eb69db83023e261eaa7e7c14588",
        "linux-armv6hf": "8afc50b302d5feeac9381ea114d563f0150d061520042b254d6eb715797c8223",
        "linux-riscv64": "693c987777e7b524dd311d9b8c704885a39c889c9804bb1ef1fd29b48567b0b3",
        "linux-x86_64": "8c3be12b05d5c177a04c29e3c78ce89ac86f1595681cab149b65b97c4e227198",
    },
}


class Shellcheck(Package):
    """ShellCheck is a GPLv3 tool that gives warnings and suggestions for bash/sh shell scripts.

    Note: Spack does not have a Haskell toolchain, so a ShellCheck binary is downloaded instead of
    being compiled from source.
    """

    homepage = "https://www.shellcheck.net"
    url = "https://github.com/koalaman/shellcheck/releases/download/v0.9.0/shellcheck-v0.9.0.linux.x86_64.tar.xz"

    maintainers("aphedges")

    # The following installs the binaries for shellcheck. The reason for
    # installing binaries is that shellcheck is a Haskell package and the
    # Haskell framework is not yet in Spack. See #1408 for a discussion of the
    # challenges with Haskell, and see the pandoc package for a precedent of
    # downloading a Haskell-derived binary.

    license("GPL-3.0")

    for ver, packages in _versions.items():
        system = platform.system().lower()
        machine = platform.machine().lower()
        key = "{0}-{1}".format(system, machine)
        pkg_hash = packages.get(key)
        if pkg_hash:
            url = (
                "https://github.com/koalaman/shellcheck/releases/download"
                "/v{0}/shellcheck-v{0}.{1}.{2}.tar.xz".format(ver, system, machine)
            )
            version(ver, sha256=pkg_hash, url=url)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("shellcheck", prefix.bin)
