# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class Talosctl(GoPackage):
    """
    A CLI for out-of-band management of Kubernetes nodes created by Talos.
    """

    homepage = "https://www.talos.dev/"
    url = "https://github.com/siderolabs/talos/archive/refs/tags/v1.12.6.tar.gz"

    maintainers("RobertMaaskant")

    license("MPL-2.0", checked_by="RobertMaaskant")

    version("1.12.6", sha256="bfae01fe1db88cadde1502c552f5bae673524f4dc3512fd99e001c85a86b4515")

    depends_on("go@1.25.5:", type="build", when="@1.12.6:")

    build_directory = "cmd/talosctl"
