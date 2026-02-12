# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class HdfEos2(AutotoolsPackage):
    """HDF-EOS (Hierarchical Data Format - Earth Observing System) is a
    self-describing file format based upon HDF for standard data products
    that are derived from EOS missions.  HDF-EOS2 is based upon HDF4.
    """

    homepage = "https://hdfeos.org"
    url = "https://git.earthdata.nasa.gov/projects/DAS/repos/hdfeos"

    maintainers("climbfuji", "danrosen25")

    # Archives are committed to a branch related to the version
    # but the branch name and archive name are subject to change
    # from version to version
    version_list = [
        {
            "version": "3.0",
            "branch": "HDFEOS2_3.0",
            "archive": "hdf-eos2-3.0-src.tar.gz",
            "sha256": "3a5564b4d69b541139ff7dfdad948696cf31d9d1a6ea8af290c91a4c0ee37188",
        },
        {
            "version": "2.20v1.00",
            "branch": "HDFEOS2.20",
            "archive": "HDF-EOS2.20v1.00.tar.Z",
            "sha256": "cb0f900d2732ab01e51284d6c9e90d0e852d61bba9bce3b43af0430ab5414903",
        },
        {
            "version": "2.19v1.00",
            "branch": "HDFEOS2.19",
            "archive": "HDF-EOS2.19v1.00.tar.Z",
            "sha256": "3fffa081466e85d2b9436d984bc44fe97bbb33ad9d8b7055a322095dc4672e31",
        },
        {
            "version": "2.19b",
            "branch": "HDFEOS2.19",
            "archive": "hdfeos2_19b.zip",
            "sha256": "a69993508dbf5fa6120bac3c906ab26f1ad277348dfc2c891305023cfdf5dc9d",
            "deprecated": True,
        },
    ]

    for vrec in version_list:
        ver = vrec["version"]
        sha256 = vrec["sha256"]
        deprecated = vrec.get("deprecated", False)
        version(ver, sha256=sha256, deprecated=deprecated)

    variant(
        "shared", default=True, description="Build shared libraries (can be used with +static)"
    )
    variant(
        "static", default=True, description="Build static libraries (can be used with +shared)"
    )
    variant("fortran", default=False, description="Enable Fortran support")

    conflicts("~static", when="~shared", msg="At least one of +static or +shared must be set")
    conflicts("%gcc@14:", when="@:2", msg="GCC 14+ is only supported for version 3.0+")

    depends_on("c", type="build")
    depends_on("fortran", type="build", when="+fortran")

    # Build dependencies
    depends_on("hdf")
    # Because hdf always depends on zlib and jpeg in spack, the tests below in configure_args
    # (if self.spec.satisfies("^jpeg"):) always returns true and hdf-eos2 wants zlib and jpeg, too.
    depends_on("zlib-api", when="^hdf")
    depends_on("jpeg", when="^hdf")
    depends_on("szip", when="^hdf +szip")

    # Fix some problematic logic in stock configure script
    # test succeeds, but then script aborts due to env variable not being set
    patch("hdf-eos2.configure.patch", when="@2:3.0")

    # The standard Makefile.am, etc. add a --single_module flag to LDFLAGS
    # to pass to the linker.
    # That appears to be only recognized by the Darwin linker, remove it
    # if we are not running on darwin/
    if sys.platform != "darwin":
        patch("hdf-eos2.nondarwin-no-single_module.patch", when="@2")

    def url_for_version(self, version):
        vrec = [x for x in self.version_list if x["version"] == version.dotted.string]
        if vrec:
            branch = vrec[0]["branch"]
            archive = vrec[0]["archive"]
            myurl = f"{self.url}/raw/{archive}?at=refs%2Fheads%2F{branch}"
            return myurl
        else:
            sys.exit(
                "ERROR: cannot generate URL for version {0};"
                "version/checksum not found in version_list".format(version)
            )

    @run_before("configure")
    def fix_configure(self):
        # spack patches the configure file unless autoconf is run,
        # and this fails because configure has the wrong permissions (644)
        if not self.force_autoreconf:
            os.chmod(join_path(self.stage.source_path, "configure"), 0o755)

        # The configure script as written really wants you to use h4cc.
        # This causes problems because h4cc differs when HDF is built with
        # autotools vs cmake, and we lose all the nice flags from the
        # Spack wrappers.  These filter operations allow us to use the
        # Spack wrappers again
        filter_file("\\$CC -show &> /dev/null", "true", "configure")
        filter_file("CC=./\\$SZIP_CC", "", "configure")

    def flag_handler(self, name, flags):
        if name == "cflags":
            flags.append(self.compiler.cc_pic_flag)
            if (
                self.spec.satisfies("%clang@16:")
                or self.spec.satisfies("%apple-clang@15:")
                or self.spec.satisfies("%oneapi")
                or self.spec.satisfies("%gcc@14:")
            ):
                flags.append("-Wno-error=implicit-function-declaration")
                flags.append("-Wno-error=implicit-int")

        return flags, None, None

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # Add flags to LDFLAGS for any dependencies that need it
        extra_ldflags = []
        # hdf might have link dependency on rpc, if so need to add flags
        if self.spec.satisfies("^libtirpc"):
            tmp = self.spec["libtirpc"].libs.ld_flags
            extra_ldflags.append(tmp)
        # Set LDFLAGS
        env.set("LDFLAGS", " ".join(extra_ldflags))
        # Use h4cc compiler wrapper and flags
        if self.spec.satisfies("^hdf"):
            env.set("CC", os.path.join(self.spec["hdf"].prefix.bin, "h4cc"))
            if (
                self.spec.satisfies("%clang@16:")
                or self.spec.satisfies("%apple-clang@15:")
                or self.spec.satisfies("%oneapi")
                or self.spec.satisfies("%gcc@14:")
            ):
                env.set(
                    "CFLAGS", "-Wno-error=implicit-function-declaration -Wno-error=implicit-int"
                )

    def configure_args(self):
        extra_args = []

        # We always build PIC code
        extra_args.append("--with-pic")
        extra_args.append("--enable-install_include")

        # Set shared/static appropriately
        extra_args.extend(self.enable_or_disable("shared"))
        extra_args.extend(self.enable_or_disable("static"))

        # Set fortran
        extra_args.extend(self.enable_or_disable("fortran"))

        # Provide config args for dependencies
        if self.spec.satisfies("^hdf"):
            tmp = self.spec["hdf"].libs.directories
            if tmp:
                extra_args.append("--with-hdf4={0}".format(tmp[0]))
        if self.spec.satisfies("^jpeg"):
            # Allow handling whatever provider of jpeg are using
            tmp = self.spec["jpeg"].libs.directories
            if tmp:
                extra_args.append("--with-jpeg={0}".format(tmp[0]))
        if self.spec.satisfies("^szip"):
            tmp = self.spec["szip"].libs.directories
            if tmp:
                extra_args.append("--with-szlib={0}".format(tmp[0]))
        if self.spec.satisfies("^zlib-api"):
            # Allow handling whatever provider of zlib-api are using
            tmp = self.spec["zlib-api"].libs.directories
            if tmp:
                extra_args.append("--with-zlib={0}".format(tmp[0]))

        return extra_args
