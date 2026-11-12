# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RLanguageserver(RPackage):
    """An implementation of the Language Server Protocol for R."""

    cran = "languageserver"

    license("MIT")

    version("0.3.18", sha256="747fdeaa4474e9424189544ce84622d146ab0cc09eaf6667000d3c8d88f079d9")

    depends_on("c", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@3.4:")

        depends_on("curl")
        depends_on("openssl")
        depends_on("libxml2")
        depends_on("libuv")

        depends_on("r-callr@3:")
        depends_on("r-collections@0.3:")
        depends_on("r-digest@0.3:")
        depends_on("r-fs@1.3.1:")
        depends_on("r-jsonlite@1.6:")
        depends_on("r-lintr@3:")
        depends_on("r-r6@2.4.1:")
        depends_on("r-roxygen2@7:")
        depends_on("r-stringi@1.1.7:")
        depends_on("r-styler@1.5.1:")
        depends_on("r-xml2@1.2.2:")
        depends_on("r-xmlparsedata@1.0.3:")
