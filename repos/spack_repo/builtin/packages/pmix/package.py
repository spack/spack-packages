# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import platform

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Pmix(AutotoolsPackage):
    """The Process Management Interface (PMI) has been used for quite some
    time as a means of exchanging wireup information needed for
    interprocess communication. However, meeting the significant
    orchestration challenges presented by exascale systems requires
    that the process-to-system interface evolve to permit a tighter
    integration between the different components of the parallel
    application and existing and future SMS solutions.

    PMI Exascale (PMIx) addresses these needs by providing an extended
    version of the PMI definitions specifically designed to support
    exascale and beyond environments by: (a) adding flexibility to the
    functionality expressed in the existing APIs, (b) augmenting the
    interfaces with new APIs that provide extended capabilities, (c)
    forging a collaboration between subsystem providers including
    resource manager, fabric, file system, and programming library
    developers, (d) establishing a standards-like body for maintaining
    the definitions, and (e) providing a reference implementation of the
    PMIx standard that demonstrates the desired level of scalability
    while maintaining strict separation between it and the standard
    itself."""

    homepage = "https://openpmix.github.io/"
    url = "https://github.com/openpmix/openpmix/releases/download/v5.0.3/pmix-5.0.3.tar.bz2"
    git = "https://github.com/openpmix/openpmix.git"

    license("BSD-3-Clause-Open-MPI")

    version("master", branch="master", submodules=True)
    version("6.0.0", sha256="bfe969966d0ce82e032739cac286239bd5ad74a831d7adae013284919f125318")
    version("5.0.8", sha256="bf5f0a341d0ec7f465627a7570f4dcda3b931bc859256428a35f6c72f13462d0")
    version("5.0.7", sha256="b9e6ad482fcdcb58c9b9553ae56956b6d7df875d5605b6ecb96adaff16b2b07a")
    version("5.0.6", sha256="ea51baa0fdee688d54bc9f2c11937671381f00de966233eec6fd88807fb46f83")
    version("5.0.5", sha256="a12e148c8ec4b032593a2c465a762e93c43ad715f3ceb9fbc038525613b0c70d")
    version("5.0.4", sha256="f72d50a5ae9315751684ade8a8e9ac141ae5dd64a8652d594b9bee3531a91376")
    version("5.0.3", sha256="474ebf5bbc420de442ab93f1b61542190ac3d39ca3b0528a19f586cf3f1cbd94")
    version("5.0.2", sha256="28227ff2ba925da2c3fece44502f23a91446017de0f5a58f5cea9370c514b83c")
    version("5.0.1", sha256="d4371792d4ba4c791e1010100b4bf9a65500ababaf5ff25d681f938527a67d4a")
    version("5.0.0", sha256="92a85c4946346816c297ac244fbaf4f723bba87fb7e4424a057c2dabd569928d")
    version("4.2.9", sha256="6b11f4fd5c9d7f8e55fc6ebdee9af04b839f44d06044e58cea38c87c168784b3")
    version("4.2.8", sha256="09b442878e233f3d7f11168e129b32e5c8573c3ab6aaa9f86cf2d59c31a43dc9")
    version("4.2.7", sha256="ac9cf58a0bf01bfacd51d342100234f04c740ec14257e4492d1dd0207ff2a917")
    version("4.2.6", sha256="10b0d5a7fca70272e9427c677557578ac452cea02aeb00e30dec2116d20c3cd0")
    version("4.2.5", sha256="a89c2c5dc69715a4df1e76fdc4318299386c184623a1d0d5eb1fb062e14b0d2b")
    version("4.2.4", sha256="c4699543f2278d3a78bdac72b4b2da9cd92d11d18478d66522b8991764b021c8")
    version("4.2.3", sha256="c3d9d6885ae39c15627a86dc4718e050baf604acda71b8b9e2ee3b12ad5c2d2a")
    version("4.2.2", sha256="935b2f492e4bc409017f1425a83366aa72a7039605ea187c9fac7bb1371cd73c")
    version("4.2.1", sha256="3c992fa0d653b56e0e409bbaec9de8fc1b82c948364dbb28545442315ed2a179")

    variant("docs", default=False, when="@master", description="Build documentation")
    variant("munge", default=False, description="Enable MUNGE support")
    variant("python", default=False, description="Enable Python bindings")
    variant(
        "restful",
        default=False,
        when="@4:5.0.4",
        description="Allow a PMIx server to request services from a system-level REST server",
    )

    depends_on("c", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("m4", type="build", when="@master")
    depends_on("autoconf@2.69:", type="build", when="@master")
    depends_on("automake@1.13.4:", type="build", when="@master")
    depends_on("libtool@2.4.2:", type="build", when="@master")
    depends_on("flex@2.5.39:", type="build", when="@master")
    depends_on("perl", type="build", when="@master")
    depends_on("python@3.7:", type="build", when="+docs")
    depends_on("py-sphinx@5:", type="build", when="+docs")
    depends_on("py-recommonmark", type="build", when="+docs")
    depends_on("py-docutils", type="build", when="+docs")
    depends_on("py-sphinx-rtd-theme", type="build", when="+docs")

    depends_on("libtool@2.4.2:", type="build")

    depends_on("libevent@2.0.20:")
    depends_on("hwloc@1.11:")
    depends_on("zlib-api")
    depends_on("curl", when="+restful")
    depends_on("jansson@2.11:", when="+restful")
    depends_on("python", when="+python")
    depends_on("py-cython", when="+python")
    depends_on("py-setuptools", when="+python")
    depends_on("munge", when="+munge")

    def autoreconf(self, spec, prefix):
        """Only needed when building from git checkout"""
        # If configure exists nothing needs to be done
        if os.path.exists(self.configure_abs_path):
            return
        # Else bootstrap with autotools
        perl = which("perl")
        perl("./autogen.pl")

    def find_external_lib_path(self, pkg_name, path_match_str=""):
        spec = self.spec
        tgt_libpath = ""
        dir_list = spec[pkg_name].libs
        for entry in dir_list:
            if path_match_str == "" or (path_match_str != "" and path_match_str in entry):
                tgt_libpath = entry
                break
        path_list = tgt_libpath.split(os.sep)
        del path_list[-1]
        return (os.sep).join(path_list)

    def configure_args(self):
        spec = self.spec

        config_args = ["--enable-shared", "--enable-static"]

        if spec.satisfies("~docs") or spec.satisfies("@4.2.3:5"):
            config_args.append("--disable-sphinx")

        config_args.append("--with-zlib=" + spec["zlib-api"].prefix)

        config_args.append("--with-libevent=" + spec["libevent"].prefix)
        config_args.append("--with-hwloc=" + spec["hwloc"].prefix)

        # As of 09/22/22 pmix build does not detect the hwloc version
        # for 32-bit architecture correctly. Since, we have only been
        # able to test on 64-bit architecture, we are keeping this
        # check for "64" in place. We will need to re-visit this when we
        # have the fix in Pmix for 32-bit library version detection
        if "64" in platform.machine():
            if spec["libevent"].external_path:
                dep_libpath = self.find_external_lib_path("libevent", "64")
                config_args.append("--with-libevent-libdir=" + dep_libpath)
            if spec["hwloc"].external_path:
                dep_libpath = self.find_external_lib_path("hwloc", "64")
                config_args.append("--with-hwloc-libdir=" + dep_libpath)

        config_args.extend(self.enable_or_disable("python-bindings", variant="python"))

        if spec.satisfies("+munge"):
            config_args.append("--with-munge=" + spec["munge"].prefix)
        else:
            config_args.append("--without-munge")

        if spec.satisfies("+restful"):
            config_args.append("--with-curl=" + spec["curl"].prefix)
            config_args.append("--with-jansson=" + spec["jansson"].prefix)

        return config_args
