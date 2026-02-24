# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libgeopmd(AutotoolsPackage):
    """The Global Extensible Open Power Manager (GEOPM) Service provides a
    user interface for accessing hardware telemetry and settings securely.

    Note: GEOPM interfaces with hardware using Model Specific Registers (MSRs).
    For proper usage make sure MSRs are made available via the msr or
    msr-safe kernel modules by your administrator."""

    homepage = "https://geopm.github.io"
    git = "https://github.com/geopm/geopm.git"
    url = "https://github.com/geopm/geopm/tarball/v3.2.2"

    maintainers("bgeltz", "cmcantalupo")
    license("BSD-3-Clause")
    tags = ["e4s"]

    version("develop", branch="dev", get_full_repo=True)
    version("3.2.2", sha256="715383060187a84b0d4022a823805b158709ec9225d2f35dba94af63cd260afe")
    version(
        "3.2.1",
        sha256="9177da3af335256592c4ea8ae0dd4f8f9c8fb4caf65965af6216e7975d094b99",
        deprecated=True,
    )
    version(
        "3.2.0",
        sha256="b708233e1bfda66408c500f2ac0cbaf042140870bffdced12dd7cabbd18e0025",
        deprecated=True,
    )
    version(
        "3.1.0",
        sha256="2d890cad906fd2008dc57f4e06537695d4a027e1dc1ed92feed4d81bb1a1449e",
        deprecated=True,
    )

    variant("debug", default=False, description="Enable debug")
    variant("systemd", default=True, description="Enable use of systemd/DBus")
    variant("grpc", default=False, when="@3.2:", description="Enable gRPC support")
    variant("liburing", default=True, description="Enables the use of liburing for batch I/O")
    variant(
        "libcap", default=True, description="Enables the use of libcap to do capabilities checks"
    )
    variant("gnu-ld", default=False, description="Assume C compiler uses gnu-ld")

    variant("level_zero", default=False, description="Enables the use of oneAPI Level Zero loader")
    variant("nvml", default=False, description="Enable NVML support")

    variant(
        "rawmsr",
        default=True,
        description="Enable direct use of standard msr device driver",
        when="@3.2:",
    )

    conflicts(
        "+nvml", when="@3.1.0+level_zero", msg="LevelZero and NVML support are mutually exclusive"
    )

    conflicts("%gcc@:7.2", msg="Requires C++17 support")
    conflicts("%clang@:4", msg="Requires C++17 support")

    conflicts("platform=darwin", msg="Darwin is not supported")
    conflicts("platform=windows", msg="Windows is not supported")

    patch("nvml-v3.1+.patch", when="@3.1: +nvml")
    patch("libtool.patch", when="@3.2.0")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    # Autotools dependencies
    depends_on("automake", type="build")
    depends_on("autoconf", type="build")
    depends_on("libtool", type="build")
    depends_on("file")

    # Other dependencies
    depends_on("py-setuptools-scm@6.4.2:", when="@develop", type="build")  # Used in autogen.sh
    depends_on("bash-completion")
    depends_on("unzip")
    depends_on("systemd", when="+systemd")
    depends_on("libcap", when="+libcap")
    depends_on("liburing", when="+liburing")
    depends_on("oneapi-level-zero", when="+level_zero")
    depends_on("cuda", when="+nvml")
    depends_on("grpc+shared", when="+grpc")
    depends_on("protobuf", when="+grpc")
    depends_on("pkgconfig", when="+grpc")

    configure_directory = "libgeopmd"

    def autoreconf(self, spec, prefix):
        bash = which("bash", required=True)
        with working_dir(self.configure_directory):
            if not spec.version.isdevelop():
                version_file = "VERSION"
                # Required to workaround missing VERSION files
                # from GitHub generated source tarballs
                with open(version_file, "w") as fd:
                    fd.write(f"{spec.version}")
            bash("./autogen.sh")

    def configure_args(self):
        args = [
            *self.enable_or_disable("debug"),
            *self.enable_or_disable("systemd"),
            *self.enable_or_disable("io-uring", variant="liburing"),
            *self.with_or_without("liburing", activation_value="prefix"),
            *self.enable_or_disable("libcap"),
            *self.with_or_without("gnu-ld"),
            *self.enable_or_disable("levelzero", variant="level_zero"),
            *self.enable_or_disable("nvml"),
            *self.enable_or_disable("rawmsr"),
            *self.enable_or_disable("grpc"),
        ]

        if self.spec.satisfies("+nvml"):
            args += [
                "--with-nvml="
                + join_path(
                    self.spec["cuda"].prefix, "targets", f"{self.spec.target.family}-linux"
                )
            ]

        if self.spec.satisfies("@develop") and self.spec.target.family != "x86_64":
            args.append("--disable-cpuid")
        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # Required to ensure geopmdpy can load
        # libgeopmd.so.2 via CFFI
        if os.path.isdir(self.prefix.lib64):
            lib_dir = self.prefix.lib64
        else:
            lib_dir = self.prefix.lib
        env.prepend_path("LD_LIBRARY_PATH", lib_dir)
