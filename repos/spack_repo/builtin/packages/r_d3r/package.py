# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RD3r(RPackage):
    """Provides a suite of functions to help ease the use of 'd3.js' in R."""

    homepage = "https://github.com/timelyportfolio/d3r"
    url = "https://github.com/timelyportfolio/d3r/archive/refs/tags/v1.1.0.tar.gz"

    license("BSD_3_clause")

    version("1.1.0", sha256="02921d4269381cc5924df3135882a23b5be4438f526527cac0e9b9f26a66f667")
    version("1.0.1", sha256="359bd6ab20839c62801613698ca1d297a073ab54eb3d7fd8bed10c05fd45278a")
    version("1.0.0", sha256="4ee097b1ba149b64696b9447e890a185948c46dbb31002ced87d081ebf6eb3c6")
    version("0.9.0", sha256="292b3e928319e8bc0d4bd3ef1b3973bc99459150540f15536fabff2890960e1a")
    version("0.8.7", sha256="9a0efb95e5782639af22a5a87e9e44565e15cb1062a09ea39a9784fa2c966123")
    version("0.8.6", sha256="f8ca8d5c2ed02acd8e62bc4a6bce034832a0cb7adfa3f09d49dce6ceaad653f4")
    version("0.8.4", sha256="f57817cfd6dd83289021b77bf4e9267e551bfe2a6f40eefd42225e223c36772b")
    version("0.8.2", sha256="45d89aa43ab9f2369ca1dd56d06c9aea6d0f90252eef7de1ba3f5233ea2722fa")
    version("0.8.0", sha256="4fe9a680dc99f69cfce504f11f2c96d854305515520d9d031bf1048e7af8d37c")
    version("0.7.1", sha256="e53c386ff2e15bb3b92dff8724118c6436a0e966bb8d8c222e2eea3140ecd2ef")

    with default_args(type=("build", "run")):
        depends_on("r-dplyr")
        depends_on("r-htmltools")
        depends_on("r-rlang", when="@0.9:1.0")
        depends_on("r-tidyr@0.7:")
        depends_on("r-tidyr@0.8.3:", when="@0.9:")
