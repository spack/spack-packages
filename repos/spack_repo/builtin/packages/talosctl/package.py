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

    version("1.13.7", sha256="2694a289d868ecb5ab2b0fcfbf61c452dfbc6540fab1c6b49f52d451755b5c8a")
    version("1.13.6", sha256="8e08a279ef826c50e98ce8953dcc140d66f40c59922ab794d67b3e39f938f1f7")
    version("1.13.5", sha256="d3457377cf574d843f7aa4efb7f1263830ff150a153bd3e21ec93795f8c43f76")
    version("1.13.3", sha256="f0f42d68db52cec6f5e6f4da3994f7f4c9dca700e05b690184ea588251f92aca")
    version("1.12.6", sha256="bfae01fe1db88cadde1502c552f5bae673524f4dc3512fd99e001c85a86b4515")

    depends_on("go@1.26.5:", type="build", when="@1.13.6:")
    depends_on("go@1.26.3:", type="build", when="@1.13.1:")
    depends_on("go@1.25.5:", type="build", when="@1.12.6:")

    build_directory = "cmd/talosctl"
