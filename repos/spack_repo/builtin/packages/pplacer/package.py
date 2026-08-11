# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Pplacer(Package):
    """Pplacer places query sequences on a fixed reference phylogenetic tree
    to maximize phylogenetic likelihood or posterior probability according
    to a reference alignment. Pplacer is designed to be fast, to give
    useful information about uncertainty, and to offer advanced
    visualization and downstream analysis.
    """

    homepage = "https://matsen.fhcrc.org/pplacer/"
    url = "https://github.com/matsen/pplacer/archive/refs/tags/v1.1.alpha22.tar.gz"
    git = "https://github.com/matsen/pplacer.git"

    version(
        "1.1.alpha22", sha256="b1eeb4fd5f4b946f176e4ed8540a035d8a0645c05b4201477ea67d35ebe6b5a1"
    )
    version(
        "1.1.alpha19",
        sha256="9131b45c35ddb927f866385f149cf64af5dffe724234cd4548c22303a992347d",
        url="https://github.com/matsen/pplacer/releases/download/v1.1.alpha19/pplacer-linux-v1.1.alpha19.zip",
    )

    with when("@1.1.alpha22:"):
        with default_args(type="build"):
            depends_on("c")

            depends_on("awk")
            depends_on("gmake")
            depends_on("m4")
            depends_on("opam")
            depends_on("patch")
            depends_on("pkgconf")
        depends_on("gsl")
        depends_on("sqlite@3")
        depends_on("zlib-api")
    with default_args(type="run"):
        depends_on("python@3")
        depends_on("py-biopython")

    resource(
        name="mcl-temp",
        placement="mcl-temp",
        git="https://github.com/fhcrc/mcl.git",
        commit="1f1932b64619e9bd9ecbcb421cb1e3f1eb535e80",
        when="@1.1.alpha22",
    )

    @when("@1.1.alpha22:")
    def setup_build_environment(self, env):
        env.append_path("PATH", join_path(self.stage.source_path, ".opam", "5.2.1", "bin"))

    @when("@1.1.alpha22:")
    def install(self, spec, prefix):
        # resource staging
        copy_tree("mcl-temp", "mcl")
        remove_directory_contents("mcl-temp")

        opam = Executable(self.spec["opam"].prefix.bin.opam)
        opam_root = join_path(self.stage.source_path, ".opam")
        opam("init", "--disable-sandboxing", f"--root={opam_root}", "--compiler=5.2.1")
        opam(
            "repo",
            "add",
            "pplacer-deps",
            "http://matsen.github.io/pplacer-opam-repository",
            f"--root={opam_root}",
        )
        opam("update", "pplacer-deps", f"--root={opam_root}")
        deps = [
            "dune",
            "csv",
            "ounit2",
            "xmlm",
            "batteries",
            "gsl",
            "sqlite3",
            "camlzip",
            "ocamlfind",
        ]
        opam("install", f"--root={opam_root}", "-y", "--assume-depexts", *deps)
        with working_dir("mcl"):
            Executable("./configure")()
            make()
        dune = Executable(join_path(opam_root, "5.2.1", "bin", "dune"))
        dune("build")
        mkdirp(prefix.bin)
        install_tree("scripts", prefix.bin)
        to_remove = [
            "build-common.sh",
            "build-docker.sh",
            "build-linux.sh",
            "build-macos.sh",
            "setup.py",
        ]
        for i in to_remove:
            force_remove(join_path(prefix.bin, i))
        with working_dir(join_path("_build", "default")):
            install("guppy.exe", join_path(prefix.bin, "guppy"))
            install("pplacer.exe", join_path(prefix.bin, "pplacer"))
            install("rppr.exe", join_path(prefix.bin, "rppr"))

    @when("1.1.alpha19")
    def install(self, spec, prefix):
        install_tree("scripts", prefix.bin)
        force_remove(join_path(prefix.bin, "setup.py"))
        install("guppy", prefix.bin)
        install("pplacer", prefix.bin)
        install("rppr", prefix.bin)
