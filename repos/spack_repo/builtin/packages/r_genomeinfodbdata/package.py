# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGenomeinfodbdata(RPackage):
    """for mapping between NCBI taxonomy ID and species. Used by functions
    in the GenomeInfoDb package."""

    bioc = "GenomeInfoDbData"
    url = "https://bioconductor.org/packages/release/data/annotation/src/contrib/GenomeInfoDbData_0.99.0.tar.gz"

    version(
        "1.2.15",
        url="https://bioconductor.org/packages/3.22/data/annotation/src/contrib/GenomeInfoDbData_1.2.15.tar.gz",
        sha256="aef012d96075c729ff1b859a6701e220f010c83f4e15d85707fbc3fa1a7a2ad8",
    )

    version(
        "1.2.14",
        url="https://bioconductor.org/packages/3.21/data/annotation/src/contrib/GenomeInfoDbData_1.2.14.tar.gz",
        sha256="23e2fec59d4d286c5539eb679924fa69092154a0cd36c4947664884895b850d9",
    )

    version(
        "1.2.13",
        url="https://bioconductor.org/packages/3.20/data/annotation/src/contrib/GenomeInfoDbData_1.2.13.tar.gz",
        sha256="51a33c432e65261ef81a7c2039b17cbdf7a0b417376fdb7ada4d618566f7074e",
    )

    version(
        "1.2.12",
        url="https://bioconductor.org/packages/3.19/data/annotation/src/contrib/GenomeInfoDbData_1.2.12.tar.gz",
        sha256="f7556dc1a0e7b8c33ae7b86519f3f4af15d77c3e2a7be2f6e4a291bf0a95a355",
    )

    version(
        "1.2.11",
        url="https://bioconductor.org/packages/3.18/data/annotation/src/contrib/GenomeInfoDbData_1.2.11.tar.gz",
        sha256="311fe287842e6161f24fc1faaa824a6d5ce88afcbf4c0203f5e309456e667bc2",
    )

    version(
        "1.2.10",
        url="https://bioconductor.org/packages/3.17/data/annotation/src/contrib/GenomeInfoDbData_1.2.10.tar.gz",
        sha256="74c5db556d163e8f512d55f5c0d8ce315fb13ac822d31b4b030c20036d58f864",
    )
    version(
        "1.2.9",
        url="https://bioconductor.org/packages/3.16/data/annotation/src/contrib/GenomeInfoDbData_1.2.9.tar.gz",
        sha256="e63a719a8eceefeda39fc95de83e7aa41caad39705efc712a44ab4021adc45fa",
    )
    version(
        "1.2.8",
        url="https://bioconductor.org/packages/3.15/data/annotation/src/contrib/GenomeInfoDbData_1.2.8.tar.gz",
        sha256="576750330a011c1eccb47c7154ca1b40ae4cd473fd7973f6c2955237a0729eb4",
    )
    version(
        "1.2.7",
        url="https://bioconductor.org/packages/3.14/data/annotation/src/contrib/GenomeInfoDbData_1.2.7.tar.gz",
        sha256="217cbad0dd3ed8f0da6b21c7d35df5737bcbd21e317ca71d2fb6ec4c316b1987",
    )
    version(
        "1.2.1",
        url="https://bioconductor.org/packages/3.9/data/annotation/src/contrib/GenomeInfoDbData_1.2.1.tar.gz",
        sha256="75e6d683a29b8baeec66ba5194aa59a6aa69b04fae5a9c718a105c155fb41711",
    )
    version(
        "1.1.0",
        url="https://bioconductor.org/packages/3.7/data/annotation/src/contrib/GenomeInfoDbData_1.1.0.tar.gz",
        sha256="6efdca22839c90d455843bdab7c0ecb5d48e3b6c2f7b4882d3210a6bbad4304c",
    )
    version("0.99.0", sha256="457049804bbd70f218c1c84067a23e83bdecb7304a3e4d8b697fee0b16dc1888")

    depends_on("r@3.5:", type=("build", "run"), when="@1.2.1:")
    depends_on("r@3.3:", type=("build", "run"), when="@0.99.0:1.1.0")
    depends_on("r@3.5.0:", type=("build", "run"), when="@1.2.10:")
