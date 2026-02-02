# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Libgeopm(AutotoolsPackage):
    """The Global Extensible Open Power Manager (GEOPM) Runtime is designed to
    enhance energy efficiency of applications through active hardware
    configuration."""

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
    variant("overhead", default=False, description="Track time spent in GEOPM API calls")
    variant("beta", default=False, description="Enable beta features")
    variant("mpi", default=True, description="Enable MPI dependent components")
    variant("fortran", default=True, description="Build fortran interface")
    variant("openmp", default=True, description="Build with OpenMP")
    variant("ompt", default=True, description="Use OpenMP Tools Interface")
    variant("gnu-ld", default=False, description="Assume C compiler uses gnu-ld")
    variant("intel-mkl", default=True, description="Build with Intel MKL support")
    variant(
        "checkprogs",
        default=False,
        description='Build tests (use with "devbuild" or "install --keep-stage")',
    )

    conflicts("%gcc@:7.2", msg="Requires C++17 support")
    conflicts("%clang@:4", msg="Requires C++17 support")
    conflicts("%gcc", when="+ompt")

    conflicts("platform=darwin", msg="Darwin is not supported")
    conflicts("platform=windows", msg="Windows is not supported")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    # Autotools dependencies
    depends_on("automake", type="build")
    depends_on("autoconf", type="build")
    depends_on("libtool", type="build")
    depends_on("file")

    # Other dependencies
    for ver in ["3.1.0", "3.2.0", "3.2.1", "3.2.2", "develop"]:
        depends_on(f"libgeopmd@{ver}", type=("build", "run"), when=f"@{ver}")

    depends_on("py-setuptools-scm@6.4.2:", when="@develop", type="build")  # Used in autogen.sh
    depends_on("bash-completion")
    depends_on("unzip")
    depends_on("mpi@2.2:", when="+mpi")
    depends_on("libelf")

    # Intel dependencies
    depends_on("intel-oneapi-mkl%oneapi", when="+intel-mkl")

    configure_directory = "libgeopm"

    @property
    def install_targets(self):
        target = ["install"]
        if self.spec.satisfies("+checkprogs"):
            target += ["checkprogs"]
        return target

    def autoreconf(self, spec, prefix):
        bash = which("bash")
        with working_dir(self.configure_directory):
            if not spec.version.isdevelop():
                version_file = "VERSION"
                # Required to workaround missing VERSION files
                # from GitHub generated source tarballs
                with open(version_file, "w") as fd:
                    fd.write(f"{spec.version}")
            bash("./autogen.sh")

    def configure_args(self):
        args = ["--disable-geopmd-local", f"--with-geopmd={self.spec['libgeopmd'].prefix}"]

        args += self.enable_or_disable("debug")
        args += self.enable_or_disable("overhead")
        args += self.enable_or_disable("beta")
        args += self.enable_or_disable("mpi")
        args += self.enable_or_disable("fortran")
        args += self.enable_or_disable("openmp")
        args += self.enable_or_disable("ompt")
        args += self.with_or_without("gnu-ld")

        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        # Required to ensure libgeopm.so
        # can be used with LD_PRELOAD
        if os.path.isdir(self.prefix.lib64):
            lib_dir = self.prefix.lib64
        else:
            lib_dir = self.prefix.lib
        env.prepend_path("LD_LIBRARY_PATH", lib_dir)

        if self.spec.satisfies("+checkprogs"):
            env.set("GEOPM_SOURCE", self.stage.source_path)
            env.prepend_path("PYTHONPATH", self.stage.source_path)
        env.set("GEOPM_INSTALL", self.prefix)
