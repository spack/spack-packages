# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Proteowizard(Package):
    """ProteoWizard: A set of software libraries and tools for rapid development of mass
    spectrometry and proteomic data analysis software."""

    homepage = "https://proteowizard.sourceforge.io"
    git = "https://github.com/ProteoWizard/pwiz.git"

    # 17.05.2026
    version(
        "3.0.26136-56ef25d",
        url="http://github.com/ProteoWizard/pwiz/tarball/56ef25de24d72f23a3b247ce53abacb25f2f0886",
        sha256="5141427765444a934130e4e63c2f02cd17235b1676da829e96ef75bab4107710",
    )

    # 13.04.2026
    version(
        "3.0.26102-0783ec5",
        url="http://github.com/ProteoWizard/pwiz/tarball/0783ec56810626af7888a80d7b32fb3e47d02d52",
        sha256="8ed54d324d1d30db074046cfa017dd94ed40437007f51bd1b06d715042bf8f5c",
    )

    license("Apache-2.0")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def determine_toolset(self, spec):
        toolsets = {"%gcc": "gcc", "%oneapi": "intel", "%clang": "clang", "%nvhpc": "pgi"}

        for cc, toolset in toolsets.items():
            if spec.satisfies(cc):
                return toolset

        raise InstallError("Unable to match compiler with b2 configuration file")

    def install(self, spec, prefix):
        with working_dir("libraries/boost-build/src/engine"):
            bootstrap_b2 = Executable("./build.sh")
            bootstrap_b2()

        b2_path = join_path(self.stage.source_path, "libraries/boost-build/src/engine", "b2")
        b2 = Executable(b2_path)

        b2_toolset = self.determine_toolset(spec)

        args = [f"-j{make_jobs}", f"toolset={b2_toolset}", "address-model=64", "executables"]
        env["BOOST_BUILD_PATH"] = join_path(self.stage.source_path, "libraries/boost-build")
        b2(*args, env=env)

        build_path = join_path(self.stage.source_path, "build-linux-x86_64")
        dist_path = join_path(build_path, f"{b2_toolset}-release-x86_64")

        mkdirp(prefix.bin)

        with working_dir(dist_path):
            for file in glob.glob("*"):
                if file == "readme.txt":
                    continue

                install(file, prefix.bin)
