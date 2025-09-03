# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class GoSh(GoPackage):
    """A shell parser, formatter, and interpreter. Supports POSIX
    Shell, Bash, and mksh. Requires Go 1.23 or later."""

    homepage = "https://github.com/mvdan/sh"
    url = "https://github.com/mvdan/sh/archive/refs/tags/v3.12.0.tar.gz"

    maintainers("mcmehrtens")
    license("BSD-3-Clause", checked_by="mcmehrtens")

    version("3.12.0", sha256="ac15f42feeba55af29bd07698a881deebed1cd07e937effe140d9300e79d5ceb")

    depends_on("go@1.23:", type="build", when="@3.12.0:")

    variant("shfmt", default=True, description="Build and install shfmt")
    variant("gosh", default=False, description="Build and install gosh")
    conflicts("~shfmt~gosh", msg="One of shfmt or gosh must be specified")

    @property
    def sanity_check_is_file(self):
        files = []
        if self.spec.satisfies("+shfmt"):
            files.append(join_path("bin", "shfmt"))
        if self.spec.satisfies("+gosh"):
            files.append(join_path("bin", "gosh"))
        return files

    def build(self, spec: Spec, prefix: Prefix) -> None:
        """Runs ``go build`` in the source directory for the specified
        variants."""
        common_flags = (
            "-p",
            str(make_jobs),
            "-modcacherw",
            "-ldflags",
            f"-s -w -X main.version={spec.version}",
        )
        with working_dir(self.build_directory):
            if spec.satisfies("+shfmt"):
                go("build", "-o", "shfmt", *common_flags, "cmd/shfmt/main.go")
            if spec.satisfies("+gosh"):
                go("build", "-o", "gosh", *common_flags, "cmd/gosh/main.go")

    def install(self, spec: Spec, prefix: Prefix) -> None:
        """Install built binaries into prefix bin."""
        with working_dir(self.build_directory):
            mkdirp(prefix.bin)
            if spec.satisfies("+shfmt"):
                install("shfmt", prefix.bin)
            if spec.satisfies("+gosh"):
                install("gosh", prefix.bin)
