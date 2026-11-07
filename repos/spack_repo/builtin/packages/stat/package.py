# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


class Stat(AutotoolsPackage):
    """Library to create, manipulate, and export graphs Graphlib."""

    homepage = "https://paradyn.org/STAT/STAT.html"
    url = "https://github.com/LLNL/STAT/archive/v2.0.0.tar.gz"
    git = "https://github.com/llnl/stat.git"
    maintainers("lee218llnl")

    tags = ["e4s"]

    version("develop", branch="develop")
    version(
        "4.3.0",
        sha256="f65d110e944a016b52c9af16fedd6823fb2db2da1607c8f540c114c0a71aa231",
        url="https://github.com/llnl/STAT/releases/download/v4.3.0/stat-4.3.0.tar.gz",
    )
    version(
        "4.2.3",
        sha256="cec7824e43d4c1f2cd24bdf074ef27b47d89ce9abda2b5bc37eed6396c4adf37",
        url="https://github.com/LLNL/STAT/releases/download/v4.2.3/stat-4.2.3.tar.gz",
    )
    version(
        "4.2.2",
        sha256="e12b5d1d0be1e7e485b5a4baba901ce508102a63deb5d2c9ca045b63bf6463d6",
        url="https://github.com/LLNL/STAT/releases/download/v4.2.2/stat-4.2.2.tar.gz",
    )
    version(
        "4.2.1",
        sha256="137529889ec5b5f9b9bae3a0864a385c5814e989d0074228dd3500e3e713801d",
        url="https://github.com/LLNL/STAT/releases/download/v4.2.1/stat-4.2.1.tar.gz",
    )
    version(
        "4.2.0",
        sha256="d244d53585b0949e308354eb024f7a89ee3467fd2866b818e8aa6c8b5d372ced",
        url="https://github.com/LLNL/STAT/releases/download/v4.2.0/stat-4.2.0.tar.gz",
    )
    version(
        "4.1.0",
        sha256="1d5b00afd563cf3bd9dd40818c44a03d7d4b13356216881513c058566c3b0080",
        url="https://github.com/LLNL/STAT/files/6193568/stat-4.1.0.tar.gz",
    )
    version(
        "4.0.2",
        sha256="9ece10dde8e1579c9db469ac8d2391b26e59498c0947dbb271c2d01d7ef0a65d",
        url="https://github.com/LLNL/STAT/releases/download/v4.0.2/stat-4.0.2.tar.gz",
    )

    # TODO: dysect requires Dyninst patch for version 3.0.0b
    variant("dysect", default=False, description="enable DySectAPI")
    variant("examples", default=False, description="enable examples")
    variant("fgfs", default=True, description="enable file broadcasting")
    variant("gui", default=True, description="enable GUI")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("dyninst", when="@4.2.1:")
    depends_on("dyninst@:11.9", when="~dysect @:4.2.0")
    depends_on("dyninst +stat_dysect", when="+dysect")
    # we depend on fgfs@master to avoid seg faults with fgfs 1.1
    depends_on("fast-global-file-status@1.1.1:", when="+fgfs")
    depends_on("graphlib@3.0.0")
    depends_on("graphviz", type=("build", "link", "run"))
    # we depend on mpa@master for bug fixes since launchmon 1.0.2
    depends_on("launchmon@1.2.0:")
    depends_on("mrnet")
    depends_on("python", when="@4.3.0:")
    depends_on("python@:3.11", when="@:4.2.3")
    depends_on("py-xdot@1.6:", when="+gui @4.3.0:", type=("run"))
    depends_on("py-xdot@1.0", when="+gui @:4.2.3", type=("run"))
    depends_on("py-pygments", when="+gui", type=("run"))
    depends_on("pango", when="+gui", type=("run"))
    depends_on("swig@4.0:", when="^python@3.12:")
    depends_on("swig", type=("build"))
    depends_on("mpi", when="+examples")
    depends_on("glib", type=("build", "run"), when="+gui")
    depends_on("gtkplus", type=("build", "run"), when="+gui")

    # TODO: replace this with an explicit list of components of Boost,
    # for instance depends_on('boost +filesystem')
    # See https://github.com/spack/spack/pull/22303 for reference
    depends_on(Boost.with_default_variants)

    # No Mac support due to dependencies like dyninst, elf etc.
    conflicts("platform=darwin", msg="macOS is not supported")

    def configure_args(self):
        spec = self.spec

        # we need to find all the dependent python site-package directories
        # for STAT's configuration so they can be added to PYTHONPATH in the
        # STAT executable scripts
        stat_python_path = ""
        py_version = self.spec["python"].version.up_to(2)
        platlib = "lib64/python%s/site-packages" % py_version
        purelib = "lib/python%s/site-packages" % py_version
        for dep in spec.traverse(deptype=("run")):
            site_packages = {dep.prefix.join(platlib), dep.prefix.join(purelib)}
            for sp in site_packages:
                if os.path.exists(sp):
                    stat_python_path += sp + ":"

        args = [
            "--with-launchmon=%s" % spec["launchmon"].prefix,
            "--with-mrnet=%s" % spec["mrnet"].prefix,
            "--with-graphlib=%s" % spec["graphlib"].prefix,
            "--with-stackwalker=%s" % spec["dyninst"].prefix,
            "--with-python=%s" % spec["python"].command.path,
            "--with-boost=%s" % spec["boost"].prefix,
        ]
        if (spec.satisfies("@4.3.0:") or spec.satisfies("@develop")) and spec.satisfies("+gui"):
            args.append("--with-python-path=%s" % stat_python_path)
        if (spec.satisfies("@4.2.2:") or spec.satisfies("@develop")) and spec["glib"].satisfies("@2.0:2.99"):
            args.append(
                "STAT_GSETTINGS_SCHEMA_DIR=%s"
                % spec["gtkplus"].prefix.join("share/glib-2.0/schemas")
            )

        if "+fgfs" in spec:
            args.append("--with-fgfs=%s" % spec["fast-global-file-status"].prefix)
        if "+dysect" in spec:
            args.append("--enable-dysectapi")
        if "~gui" in spec:
            args.append("--disable-gui")
        if "~examples" in spec:
            args.append("--disable-examples")
        return args
