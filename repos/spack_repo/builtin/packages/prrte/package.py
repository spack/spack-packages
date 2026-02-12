# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Prrte(AutotoolsPackage):
    """PRRTE is the Reference RunTime Environment implementation for PMIx.
    It is capable of operating within a host SMS. The reference RTE
    therefore provides an easy way of exploring PMIx capabilities and
    testing PMIx-based applications outside of a PMIx-enabled
    environment."""

    homepage = "https://pmix.org"
    url = "https://github.com/pmix/prrte/releases/download/v1.0.0/prrte-1.0.0.tar.bz2"
    git = "https://github.com/pmix/prrte.git"

    license("BSD-3-Clause-Open-MPI")

    version("develop", branch="master")
    version("4.0.0", sha256="3c2ec961e0ba0c99128c7bf3545f4789d55a85a70ce958e868ae5e3db6ed4de4")
    version("3.0.11", sha256="37af5a82d333a54c0bac358f06c194427b7dbfa7b8b85f2ddd1145acf71cfdd4")
    version("3.0.10", sha256="f5525d88937a5664ab5248a7c05e9ee51389937cd0993398e8270ed5cf53d638")
    version("3.0.9", sha256="29766b5c81faa6320625ab0670a0b24b2b75f5cf1abe4aa7f3bad56487a6a7e1")
    version("3.0.8", sha256="e798192fa0ab38172818a109a6c89bcc37e4b1123ca150d8c115dee5231750de")
    version("3.0.7", sha256="dbcaa3aa9fdcbd20a4320d21d569472b05c0203d0d24aa9c30912e214f758322")
    version("3.0.6", sha256="83b6b37e21b315f069d69faa4686dcec3306225b48fdfe64588dec33e6063e72")
    version("3.0.5", sha256="75ce732b02f3bc7eff5e51b81469e4373f1effc6a42d8445e2935d3670e58c8e")
    version("3.0.4", sha256="7394c2ef9ea548cbc223b62a943f470cfbccf74b3879ac92564d148537f229df")
    version("3.0.3", sha256="25b30a6252ecaeb98d3c2244710493ee5d0bbc31bfa939a42df391bde7293b80")
    version("3.0.2", sha256="1aaa1bb930e8e940251ea682b4a6abc24e4849fa9ffbaaaaf2750a38ba4e474a")
    version("3.0.1", sha256="98fe184b191e78571877492620cc90dd5d46b603a64490fa8356843b39628683")
    version("3.0.0", sha256="0898797e5530e2e37f248a1b32d572828cb3304b0c427b376ea006a1452ba565")
    version("2.0.2", sha256="e724d70caa9b1bbb630181e3b76c7dcc184ed77f9561804fefa7e74bd059d1f2")
    version("2.0.1", sha256="45ab305fe9f9f4e1c58fcf769b612d301662cdec023edd7d0a4763d0f053755c")
    version("2.0.0", sha256="9f4abc0b1410e0fa74ed7b00cfea496aa06172e12433c6f2864d11b534becc25")
    version("1.0.0", sha256="a9b3715e059c10ed091bd6e3a0d8896f7752e43ee731abcc95fb962e67132a2d")

    depends_on("c", type="build")  # generated

    depends_on("pmix")
    depends_on("pmix@6:", when="@4:")
    depends_on("pmix@:5", when="@:3")
    # NOTE: prrte 3.0.1 requires pmix 4.2.4
    # https://github.com/openpmix/prrte/compare/v3.0.0...v3.0.1
    # https://github.com/openpmix/prrte/commit/63370ca00771a7a6004d6b638476ca794b04e4c1
    # -pmix_min_version=4.1.2
    # +pmix_min_version=4.2.4
    depends_on("pmix@4.2.4:", when="@3.0.1:")
    depends_on("libevent")
    depends_on("hwloc")
    depends_on("perl", type=("build"))
    depends_on("m4", type=("build"))
    depends_on("autoconf", type=("build"))
    depends_on("automake", type=("build"))
    depends_on("libtool", type=("build"))
    depends_on("flex", type=("build"))
    depends_on("pkgconfig", type="build")
    depends_on("python@3.7:", type="build", when="@develop")

    # https://github.com/openpmix/openpmix/blob/master/docs/installing-pmix/configure-cli-options/runtime.rst
    SCHEDULERS = ("alps", "lsf", "tm", "slurm", "sge")

    variant(
        "schedulers",
        values=disjoint_sets(("none"), SCHEDULERS).with_non_feature_values("none"),
        description="List of schedulers for which support is enabled",
    )
    depends_on("lsf", when="schedulers=lsf")
    depends_on("pbs", when="schedulers=tm")
    depends_on("slurm", when="schedulers=slurm")

    def url_for_version(self, version):
        if version <= Version("3"):
            # tarballs have a single 'r'
            return f"https://github.com/pmix/prrte/releases/download/v{version}/prte-{version}.tar.bz2"
        else:
            return super().url_for_version(version)

    def autoreconf(self, spec, prefix):
        # If configure exists nothing needs to be done
        if os.path.exists(self.configure_abs_path):
            return
        with working_dir(self.configure_directory):
            perl = spec["perl"].command
            perl("autogen.pl")

    def configure_args(self):
        spec = self.spec
        config_args = ["--enable-shared", "--enable-static", "--disable-sphinx"]

        # libevent
        config_args.append("--with-libevent={0}".format(spec["libevent"].prefix))
        # hwloc
        config_args.append("--with-hwloc={0}".format(spec["hwloc"].prefix))
        # pmix
        config_args.append("--with-pmix={0}".format(spec["pmix"].prefix))

        # schedulers
        # see prte_check_X.m4 files in
        # https://github.com/openpmix/prrte/tree/master/config
        if spec.satisfies("schedulers=alps"):
            config_args.append("--with-alps")

        if spec.satisfies("schedulers=lsf"):
            config_args.append(f"--with-lsf={self.spec['lsf'].prefix}")
            config_args.append(f"--with-lsf-libdir={spec['lsf'].libs.directories[0]}")

        if spec.satisfies("schedulers=sge"):
            config_args.append("--with-sge")

        if spec.satisfies("schedulers=tm"):
            config_args.append(f"--with-tm={self.spec['pbs'].prefix}")

        if spec.satisfies("schedulers=slurm"):
            config_args.append("--with-slurm")

        return config_args
