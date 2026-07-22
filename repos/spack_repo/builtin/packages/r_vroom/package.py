# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RVroom(RPackage):
    """Read and Write Rectangular Text Data Quickly.

    The goal of 'vroom' is to read and write data (like 'csv', 'tsv' and
    'fwf') quickly. When reading it uses a quick initial indexing step, then
    reads the values lazily , so only the data you actually use needs to be
    read. The writer formats the data in parallel and writes to disk
    asynchronously from formatting."""

    cran = "vroom"

    license("MIT")

    version("1.7.1", sha256="7d64f6227fdac3ee64c506654bb1d919e407f92fc2d0d5a2398dbb83001e8790")
    version("1.6.5", sha256="7bdca21e58c9c5049d7445d182f59fd399193cb2f4318d083de0a559ec9b5761")
    version("1.6.1", sha256="eb0e33d53212f9c7e8b38d632c98bd5015365cc13f55dadb15ff0d404b31807c")
    version("1.6.0", sha256="a718ccdf916442693af5392944774d8aec5ce48f417871f9de84dd1089d26ca6")
    version("1.5.7", sha256="d087cb148f71c222fc89199d03df2502689149873414a6d89c2f006d3a109fde")
    version("1.5.5", sha256="1d45688c08f162a3300eda532d9e87d144f4bc686769a521bf9a12e3d3b465fe")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    with default_args(type=("build", "run")):
        depends_on("r@4.1:", when="@1.6.7:")
        depends_on("r@3.6:", when="@1.6.4:")
        depends_on("r@3.4:", when="@1.6.0:")
        depends_on("r@3.1:")

        depends_on("r-bit64")
        depends_on("r-cli@3.2.0:", when="@1.6.0:")
        depends_on("r-cli")
        depends_on("r-crayon")
        depends_on("r-glue")
        depends_on("r-hms")
        depends_on("r-lifecycle@1.0.3:", when="@1.6.1:")
        depends_on("r-lifecycle")
        depends_on("r-rlang@1.1.0:", when="@1.7.0:")
        depends_on("r-rlang@0.4.2:")
        depends_on("r-tibble@2.0.0:")
        depends_on("r-tidyselect")
        depends_on("r-tzdb@0.1.1:")
        depends_on("r-vctrs@0.2.0:")
        depends_on("r-withr")
        depends_on("r-cpp11@0.2.0:")
        depends_on("r-progress@1.2.3:", when="@1.6.6:")
        depends_on("r-progress@1.2.1:")
