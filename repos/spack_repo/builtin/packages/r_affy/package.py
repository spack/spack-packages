# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RAffy(RPackage):
    """Methods for Affymetrix Oligonucleotide Arrays.

    The package contains functions for exploratory oligonucleotide array
    analysis. The dependence on tkWidgets only concerns few convenience
    functions. 'affy' is fully functional without it."""

    bioc = "affy"

    with default_args(get_full_repo=True):
        version("1.90.0", commit="7ed56e774351b32c16e0f1a6314faa2b0a79f36c")  # bioc 3.23
        version("1.88.0", commit="229aef42785482d8d06d102327bd0a389ebe8f8d")  # bioc 3.22
        version("1.86.0", commit="263e70742f3085699839b7762b99f7dfe734a573")  # bioc 3.21
        version("1.84.0", commit="1174adf7e83ee46603189397cd557044802cda01")  # bioc 3.20
        version("1.82.0", commit="fb130de33532f6d15fe99ba02ff35cce07922308")  # bioc 3.19
        version("1.80.0", commit="a0d64dfdadfff1a1d7a4c39ba73e843e5e3fc6da")  # bioc 3.18
        version("1.78.2", commit="affc14023640f4bf369ec5ec7fa35bf94be1cf83")  # bioc 3.17
        version("1.78.0", commit="cc7eac358b6e10ee86a7a93d2e436758f6fbd9b5")
        version("1.76.0", commit="3bb309388d5d6402c356d4a5270ee83c5b88942f")  # bioc 3.16
        version("1.74.0", commit="2266c4a46eda7e5b64f7f3e17e8b61e7b85579ff")
        version("1.72.0", commit="3750b4eb8e5224b19100f6c881b67e568d8968a2")

    depends_on("c", type="build")

    depends_on("r-biocgenerics@0.1.12:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-affyio@1.13.3:", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-preprocesscore", type=("build", "run"))

    depends_on("r-zlibbioc", type=("build", "run"), when="@:1.85.0")
