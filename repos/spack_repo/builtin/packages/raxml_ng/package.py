# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RaxmlNg(CMakePackage):
    """RAxML-NG is a phylogenetic tree inference tool which uses
    maximum-likelihood (ML) optimality criterion.

    Its search heuristic is based on iteratively performing a series
    of Subtree Pruning and Regrafting (SPR) moves,
    which allows to quickly navigate to the best-known ML tree.
    RAxML-NG is a successor of RAxML (Stamatakis 2014) and leverages
    the highly optimized likelihood computation implemented in libpll
    (Flouri et al. 2014)."""

    homepage = "https://github.com/amkozlov/raxml-ng/wiki"
    url = "https://github.com/amkozlov/raxml-ng/archive/2.0.0.tar.gz"
    git = "https://github.com/amkozlov/raxml-ng.git"

    license("AGPL-3.0-only")

    version("2.0.0", submodules=True, commit="e995a54dda83e440ee15e890093c5b2718787043")
    version("1.2.2", submodules=True, commit="805318cef87bd5d67064efa299b5d1cf948367fd")
    version("1.2.1", submodules=True, commit="af74065fa2e03d4eb3efd83881bd50926d07e234")
    version("1.2.0", submodules=True, commit="fd32e7f73c3ee44c526c7555a8d04e84b03bd51c")
    version("1.1.0", submodules=True, commit="9b8150852c21fd0caa764752797e17382fc03aa0")
    version("1.0.3", submodules=True, commit="55aeb1c38cfda54cfd9a416b30a87f08b15a94e5")
    version("1.0.2", submodules=True, commit="411611611793e53c992717d869ca64370f2e4789")
    version("1.0.1", submodules=True, commit="abdd9caff709a73928a8fe06f7934cd442b7a50e")
    version("1.0.0", submodules=True, commit="308ff5cc88d0785fce1308d5953d7b6a644e8cf8")

    variant("mpi", default=True, description="Use MPI")
    variant("vcf", default=True, description="Enable VCF Support", when="@2.0:")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("bison")
    depends_on("flex")
    depends_on("gmp")
    depends_on("mpi", when="+mpi")
    depends_on("htslib ~libcurl", when="+vcf")

    def cmake_args(self):
        return [
            self.define_from_variant("USE_MPI", "mpi"),
            self.define_from_variant("USE_VCF", "vcf"),
        ]
