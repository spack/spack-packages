# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDcm2bids(PythonPackage):
    """Reorganising NIfTI files from dcm2niix into the Brain Imaging Data
    Structure."""

    homepage = "https://github.com/unfmontreal/Dcm2Bids"
    pypi = "dcm2bids/dcm2bids-2.1.9.tar.gz"

    license("GPL-3.0-or-later")

    version("3.3.1", sha256="82b1580c442ed696aa1496a79d8a5ae5fa419acfdd7d784e34c00aa96b2bfd0d")
    version("3.2.0", sha256="f04a6d0fea604901fc71495a91bf78f4acd9cf5d4d9af1d3b51ba47616c02407")
    version("3.1.0", sha256="53a8a177d556df897e19d72bd517fdae0245927a8938bb9fbbd51f9f33f54f84")
    version("2.1.9", sha256="d962bd0a7f1ed200ecb699e8ddb29ff58f09ab2f850a7f37511b79c62189f715")

    with default_args(type="build"):
        depends_on("py-setuptools@61:", when="@3.3:")
        depends_on("py-setuptools")

        # Historical dependencies
        depends_on("py-setuptools-scm", when="@2")

    with default_args(type=("build", "run")):
        depends_on("python@3.8:", when="@3.3:")
        depends_on("python@3.7:")

        depends_on("dcm2niix")

        # Historical dependencies
        depends_on("py-packaging@23.1:", when="@3:3.2")
        depends_on("py-future@0.17.1:", when="@2")
