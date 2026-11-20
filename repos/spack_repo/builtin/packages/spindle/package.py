# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Spindle(AutotoolsPackage):
    """Spindle improves the library-loading performance of dynamically
    linked HPC applications.  Without Spindle large MPI jobs can
    overload on a shared file system when loading dynamically
    linked libraries, causing site-wide performance problems.
    """

    homepage = "https://computing.llnl.gov/projects/spindle"
    url = "https://github.com/hpc/Spindle/archive/v1.0rc1.tar.gz"

    maintainers = ["mplegendre", "nchaimov", "rountree"]
    license("LGPL-2.1-or-later")

    version("devel", git="https://github.com/llnl/spindle", branch="devel")
    version("1.0rc1", sha256="a9d130864539ef8802fd45d22a6ef2e5a11ecd245f363ebdccdeba3d00356956")
    version("0.12", sha256="3fd9d0afefa9072fffdf2cfd80a0b5e557e201a0b0eb02e7379eae65e64eb1f2")
    version("0.8.1", sha256="c1e099e913faa8199be5811dc7b8be0266f0d1fd65f0a3a25bb46fbc70954ed6")

    variant("tests", default=False, description="Build testsuite")
    variant("numa", default=True, description="Enables libnuma support")
    variant("munge", default=True, description="Use munge for connection authentication")
    variant(
        "rm",
        default="slurm",
        values=("serial", "slurm", "flux"),
        multi=True,
        description="Resource managers supported",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("mpi", when="rm=slurm +tests")
    depends_on("mpi", when="rm=flux +tests")

    depends_on("slurm@23-11-0-1:", when="rm=slurm")
    depends_on("flux-core", when="rm=flux")
    depends_on("munge", when="rm=flux")
    depends_on("munge", when="rm=slurm")
    depends_on("munge", when="+munge")

    depends_on("numactl", when="+numa")

    when("@1.0rc1:")

    def configure_args(self):
        args = []
        if "+tests" in self.spec:
            # If we're building tests, then what should be the default RM to run tests
            if "rm=slurm" in self.spec:
                args.append("--with-testrm=slurm")
            if "rm=flux" in self.spec:
                args.append("--with-testrm=flux")
            else:
                args.append("--with-testrm=serial")
        else:
            args.append("--disable-testsuite")

        if "rm=slurm" in self.spec:
            args.append("--enable-slurm")
            args.append("--enable-slurm-plugin")
        if "rm=flux" in self.spec:
            args.append("--enable-flux-plugin")
        if "+numa" in self.spec:
            args.append("--enable-numa")

        if "munge" in self.spec:
            args.append("--enable-sec-munge")
        else:
            # Spindle security disabled. You don't want this for production deployments.
            args.append("--enable-sec-none")
        args.append("--enable-crash-dedup")
        return args

    # Workaround for:
    # spindle_logd.cc:65:76: error: narrowing conversion of '255' from 'int' to 'char'
    # spindle_logd.cc:65:76: error: narrowing conversion of '223' from 'int' to 'char'
    # spindle_logd.cc:65:76: error: narrowing conversion of '191' from 'int' to 'char'
    @when("@0.8.1 %gcc")
    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.append_flags("CPPFLAGS", "-Wno-narrowing")
