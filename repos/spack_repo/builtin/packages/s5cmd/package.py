# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class S5cmd(GoPackage):
    """
    s5cmd is a very fast S3 and local filesystem execution tool. It comes with support
    for a multitude of operations including tab completion and wildcard support for
    files, which can be very handy for your object storage workflow while working with
    large numbers of files.
    """

    homepage = "https://github.com/peak/s5cmd"
    url = "https://github.com/peak/s5cmd/archive/refs/tags/v2.3.0.tar.gz"

    maintainers("ebagrenrut")

    license("MIT")

    version("2.3.0", sha256="6910763a7320010aa75fe9ef26f622e440c2bd6de41afdbfd64e78c158ca19d4")

    depends_on("go@1.20:", type="build")

    @run_after("install")
    def install_completions(self):
        s5cmd = Executable(self.prefix.bin.s5cmd)

        extra_env = EnvironmentModifications()

        extra_env.set("SHELL", "bash")
        bash_comp_path = bash_completion_path(self.prefix)
        mkdirp(bash_comp_path)
        with open(bash_comp_path / self.name, "w") as file:
            s5cmd("--install-completion", extra_env=extra_env, output=file)

        extra_env.set("SHELL", "zsh")
        zsh_comp_path = zsh_completion_path(self.prefix)
        mkdirp(zsh_comp_path)
        with open(zsh_comp_path / f"_{self.name}", "w") as file:
            s5cmd("--install-completion", extra_env=extra_env, output=file)
