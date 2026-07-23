# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Professor(Package):
    """Professor Monte-Carlo tuning package"""

    homepage = "https://professor.hepforge.org/"
    url = "https://professor.hepforge.org/downloads/?f=Professor-2.3.3.tar.gz"
    git = "https://gitlab.com/hepcedar/professor"
    list_url = "https://professor.hepforge.org/downloads/"

    maintainers("mjk655")

    version("2.5.6", sha256="7537f23078bd56f00e67e1f96c7a24026b255cc26907ad5d5234b8371e49b3c7")
    version("2.3.3", sha256="60c5ba00894c809e2c31018bccf22935a9e1f51c0184468efbdd5d27b211009f")

    variant(
        "interactive",
        default=True,
        description="Install prof-I (Interactive parametrization explorer)",
    )

    depends_on("cxx", type="build")  # generated
    depends_on("gmake", type="build")
    depends_on("py-pip", type="build")

    depends_on("yoda")
    depends_on("eigen")
    depends_on("py-cython")
    depends_on("py-iminuit")
    depends_on("py-iminuit@2:", when="@2.4:")
    depends_on("py-matplotlib")
    depends_on("py-matplotlib backend=wx", when="+interactive")
    depends_on("root")

    extends("python")

    def patch(self):
        filter_file("PROF_ROOT=$(PWD)", "PROF_ROOT=$(CURDIR)", "Makefile", string=True)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("PROF_VERSION", str(self.spec.version))
        if self.spec["eigen"].satisfies("@5:"):
            env.set("CXXSTD", "c++14")

    @run_before("install", when="@2.5.0:")
    def configure(self):
        with working_dir(self.stage.source_path):
            configure = Executable("./configure")
            configure(f"--prefix={self.prefix}", f"--with-eigen={self.spec['eigen'].prefix}")

    def install(self, spec, prefix):
        with working_dir(self.stage.source_path):
            make()
            make("PREFIX={0}".format(prefix), "install")
        if self.spec.satisfies("~interactive"):
            os.remove(join_path(prefix.bin, "prof2-I"))
