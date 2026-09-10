# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RCurl(RPackage):
    """A Modern and Flexible Web Client for R.

    The curl() and curl_download() functions provide highly configurable
    drop-in replacements for base url() and download.file() with better
    performance, support for encryption (https, ftps), gzip compression,
    authentication, and other libcurl goodies. The core of the package
    implements a framework for performing fully customized requests where data
    can be processed either in memory, on disk, or streaming via the callback
    or connection interfaces. Some knowledge of libcurl is recommended; for a
    more-user-friendly web client see the 'httr' package which builds on this
    package with http specific tools and logic."""

    cran = "curl"

    license("MIT")

    version("7.1.0", sha256="74f079b6306acc18fbe60c18dbaac805703fb6579e6ab398f3437377695fd8a9")
    version("6.2.0", sha256="0399bb6bcad5f31ad2a2a7165ff8c976111707125ca0a9c4b8ccf40bb5eb1635")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("r@3:", type=("build", "run"))
    depends_on("curl")

    # (Jan 2025) MacOS ships a very buggy libcurl 8.7.1 so we avoid this until apple updates it
    # See: https://github.com/jeroen/curl/issues/376
    # from: https://github.com/jeroen/curl/blob/v6.2.0/configure#L18
    depends_on("curl@8.8:", when="platform=darwin")
