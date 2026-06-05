# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Pelican(GoPackage):
    """The Pelican command line tool allows one to use a Pelican
    federation as a client and serve datasets through running a
    Pelican origin service."""

    homepage = "https://pelicanplatform.org/"
    url = "https://github.com/PelicanPlatform/pelican/archive/refs/tags/v7.24.3.tar.gz"
    git = "https://github.com/PelicanPlatform/pelican.git"

    maintainers("wdconinc")

    license("Apache-2.0", checked_by="wdconinc")

    version("7.24.3", sha256="fd73d4c9193f3a25d82c696e7269d10f84f4941786e957c8dffa1562d4b605a0")

    variant("server", default=False, description="Also build the pelican-server binary")

    depends_on("go@1.25:", type="build")

    build_directory = "cmd"

    @run_before("build", when="@:7.24")
    def create_frontend_placeholder(self):
        # web_ui/ui.go uses //go:embed frontend/out/*, which requires at least one
        # file to exist. Releases prior to v7.25 did not commit this placeholder,
        # so we create it here to satisfy the embed directive without a full frontend
        # build.
        out_dir = join_path(self.stage.source_path, "web_ui", "frontend", "out")
        mkdirp(out_dir)
        touch(join_path(out_dir, "placeholder"))

    @property
    def ldflags(self):
        return [f"-X github.com/pelicanplatform/pelican/version.version={self.spec.version}"]

    @property
    def build_args(self):
        # Build only the CLI client binary (no web frontend embedded)
        return ["-tags", "forceposix,client"]

    @run_after("build", when="+server")
    def build_server(self):
        args = [*self.std_build_args, "-tags", "forceposix,server"]
        args[args.index("-o") + 1] = "pelican-server"
        with working_dir(self.build_directory):
            go("build", *args)

    @run_after("install", when="+server")
    def install_server(self):
        install(join_path(self.build_directory, "pelican-server"), self.prefix.bin)
