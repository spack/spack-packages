# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Nsjail(MakefilePackage):
    """Process isolation tool for Linux using namespaces, resource limits,
    and seccomp-bpf syscall filters. Provides sandboxing with cgroup
    management, seccomp filtering via Kafel, and declarative protobuf
    configuration."""

    homepage = "https://nsjail.dev"
    git = "https://github.com/google/nsjail.git"

    license("Apache-2.0")

    version("3.6", tag="3.6", commit="f78475530b46d0186111a9096b30725f816b55fe", submodules=True)
    version("3.5", tag="3.5", commit="402e2b4c13c79731c632c2add4c3884dd1afc25f", submodules=True)
    version("3.4", tag="3.4", commit="079d70dda4aa1edd9512cfd25ff1e47e316dc355", submodules=True)
    version("3.3", tag="3.3", commit="c7c0adfffe79ebebfacca003f3cd8e27ef909185", submodules=True)
    version("3.2", tag="3.2", commit="2e62649b4c98ff5de8f181b3d92fc241518c7435", submodules=True)
    version("3.1", tag="3.1", commit="6483728e2490c1fc497a81bba5682515eb489cf8", submodules=True)
    version("3.0", tag="3.0", commit="7de87aeb7d2f06c0e35efb60d2af58ae0bea7d4d", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Build tools
    depends_on("pkgconfig", type="build")
    depends_on("bison", type="build")
    depends_on("flex", type="build")
    depends_on("autoconf", type="build")  # needed by Kafel's build
    depends_on("libtool", type="build")  # needed by Kafel's build

    # Libraries
    depends_on("protobuf")
    depends_on("libnl")

    # Linux only — nsjail requires kernel namespace support
    conflicts("platform=darwin", msg="nsjail requires Linux namespaces")
    conflicts("platform=windows", msg="nsjail requires Linux namespaces")

    # nsjail 3.x requires C++20
    conflicts("%gcc@:9", msg="nsjail requires C++20 support")

    def install(self, spec, prefix):
        make(f"PREFIX={prefix}", "install")
