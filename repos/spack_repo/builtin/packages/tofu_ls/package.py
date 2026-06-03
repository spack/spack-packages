# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.go import GoPackage

from spack.package import *


class TofuLs(GoPackage):
    """The official OpenTofu language server, provides IDE features to any LSP-compatible editor"""

    homepage = "https://opentofu.org/"
    url = "https://github.com/opentofu/tofu-ls/archive/refs/tags/v0.4.1.tar.gz"

    maintainers("taliaferro")

    license("MPL-2.0", checked_by="taliaferro")

    version("0.4.1", sha256="20a71da45069cc2e28f9f2b58f6aed9da33457760adeb037a10aef94126b77f1")

    depends_on("go@1.25.3:", type="build", when="@0.4.1:")
