# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Elastix(CMakePackage):
    """Welcome to elastix: a toolbox for rigid and nonrigid registration of images.

    elastix is open source software, based on the well-known Insight Segmentation
    and Registration Toolkit (ITK). The software consists of a collection of
    algorithms that are commonly used to solve (medical) image registration problems.
    The modular design of elastix allows the user to quickly configure, test,
    and compare different registration methods for a specific application.
    A command-line interface enables automated processing of large numbers of
    data sets, by means of scripting.
    """

    homepage = "https://www.elastix.dev"
    url = "https://github.com/SuperElastix/elastix/archive/refs/tags/5.2.0.tar.gz"

    maintainers("Markus92")

    license("Apache-2.0", checked_by="Markus92")

    version("5.2.0", sha256="7267d7f2efccc3ddd9529aa83e4d10eeea3707a972de06b2e020fc95d4bec6c1")
    version("5.1.0", sha256="f2e3e33359d1e35cb986bc1eb7a1b0179cdb20a67e410ac8423102a160bfc29e")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("itk@5.4:", when="@5.2:")
    depends_on("itk@5.3:", when="@5.1:")
