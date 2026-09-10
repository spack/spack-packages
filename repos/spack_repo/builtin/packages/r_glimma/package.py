# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class RGlimma(RPackage):
    """Interactive HTML graphics.

    This package generates interactive visualisations for analysis of RNA-
    sequencing data using output from limma, edgeR or DESeq2 packages in an
    HTML page. The interactions are built on top of the popular static
    representations of analysis results in order to provide additional
    information."""

    bioc = "Glimma"

    license("LGPL-3.0-only")

    with default_args(get_full_repo=True):
        version("2.22.1", commit="175f4cddf7aec00054f9519daaf6e6bd1e3f4a03")  # bioc 3.23
        version("2.22.0", commit="a28b515013b9d11b20c07b2501cceb4a2a9c886f")
        version("2.21.0", commit="c7699be21cd052f72182190de09591b8f5c808b5")
        version("2.20.0", commit="73c6c448fdf266c97dcb369eabd1997b155d1dde")  # bioc 3.22
        version("2.19.2", commit="ffb476045d35e5e111233488098b510cec3e21f5")
        version("2.18.0", commit="aa1dad97c09714d7ae502803afd3eb5ab80850c5")  # bioc 3.21
        version("2.17.3", commit="9847590042e575d42674d57b14bf0eb6ce75805b")
        version("2.16.0", commit="3bb40250af316460c7715ea61f7d35666cabb53b")  # bioc 3.20
        version("2.15.2", commit="a1ce2cc0fc64ba55ce974f93e1abd410fab63b02")
        version("2.14.0", commit="498f03d2a52337a41b6d3e6c1ebb0ed81cc22d23")  # bioc 3.19
        version("2.13.0", commit="7636e1b3702fa0830b31075a06b7e54d499203eb")
        version("2.12.0", commit="9ca869e84061bafcdbaeb331453b632e4d88d6db")  # bioc 3.18
        version("2.11.4", commit="27db9e0cf3a75f23368f8822a8966aaa09899dfb")
        version("2.10.0", commit="ea1257614c5fca0cedf5805d5b9a21e8b7d15d18")  # bioc 3.17
        version("2.8.0", commit="09cec82e9af9c6775192570f8c28f050c0df08ac")
        version("2.6.0", commit="23220d9b90476059aab035b5de11b7ce04b331c8")
        version("2.4.0", commit="caa270e44ec6994035d2e915c0f68a14ccbb58db")
        version("2.0.0", commit="40bebaa79e8c87c5686cff7285def4461c11bca9")
        version("1.12.0", commit="d02174239fe0b47983d6947ed42a1a53b24caecb")
        version("1.10.1", commit="ffc7abc36190396598fadec5e9c653441e47be72")
        version("1.8.2", commit="7696aca2c023f74d244b6c908a6e7ba52bfcb34b")
        version("1.6.0", commit="57572996982806aa7ac155eedb97b03249979610")
        version("1.4.0", commit="c613c5334ed7868f36d5716b97fdb6234fb291f8")

    depends_on("r@3.3.0:", type=("build", "run"))
    depends_on("r@3.4.0:", type=("build", "run"), when="@1.6.0:")
    depends_on("r@4.0.0:", type=("build", "run"), when="@2.0.0:")
    depends_on("r-htmlwidgets", type=("build", "run"), when="@2.0.0:")
    depends_on("r-edger", type=("build", "run"))
    # Glimma <= 2.14.0 imports edgeR::decideTestsDGE, removed in edgeR 4.4.0 (Bioc 3.20)
    depends_on("r-edger@:4.2", when="@2.0.0:2.14.0", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"), when="@2.0.0:")
    depends_on("r-limma", type=("build", "run"), when="@2.0.0:")
    depends_on("r-summarizedexperiment", type=("build", "run"), when="@2.0.0:")
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))

    depends_on("r-biobase", type=("build", "run"), when="@1.4.0:1.6.0")
    depends_on("r-scater", type=("build", "run"), when="@1.4.0")
