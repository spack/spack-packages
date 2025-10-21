# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Casper(MakefilePackage):
    """CASPER (Context-Aware Scheme for Paired-End Read) is state-of-the art
    merging tool in terms of accuracy and robustness. Using this
    sophisticated merging method, we could get elongated reads from the
    forward and reverse reads."""

    homepage = "http://best.snu.ac.kr/casper/index.php?name=main"
    url = "http://best.snu.ac.kr/casper/program/casper_v0.8.2.tar.gz"
    git = "https://github.com/skwonPNU/casper.git"

    version("20220916", commit="08655cad5af7e801f05fdb9e643dcd859f823cba")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")

    depends_on("jellyfish@2.2.3:")
    depends_on("boost+exception")

    conflicts("%gcc@7.1.0")

    def install(self, spec, prefix):
        install_tree(".", prefix)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("PATH", self.spec.prefix)
