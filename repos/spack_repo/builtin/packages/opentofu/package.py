# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Opentofu(GoPackage):
    """
    OpenTofu is an infrastructure as code tool that lets you define both cloud and on-prem
    resources in human-readable configuration files that you can version, reuse, and share.
    It serves as a drop-in replacement for Terraform, preserving your existing workflows and
    configurations.
    """

    homepage = "https://opentofu.org/"
    url = "https://github.com/opentofu/opentofu/archive/refs/tags/v1.11.6.tar.gz"

    maintainers("taliaferro")

    license("MPL-2.0", checked_by="taliaferro")

    version("1.11.6", sha256="4c16aaac1c8db7386488abb13226f93fed4141698d0ebc02711029e6d6676a82")

    depends_on("go@1.25.9:", type="build", when="@1.11.6")

    def install(self, spec: Spec, prefix: Prefix) -> None:
        mkdirp(prefix.bin)
        install("tofu", prefix.bin)

    @property
    def build_args(self):
        return [
            "-p",
            str(make_jobs),
            "-modcacherw",
            "-ldflags",
            f"-X main.version={ self.version } -X github.com/opentofu/opentofu/version.dev=no ",
            "-o", "tofu",
            "./cmd/tofu"
        ]
