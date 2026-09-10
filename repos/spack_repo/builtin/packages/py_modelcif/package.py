# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyModelcif(PythonPackage):
    """Package for handling ModelCIF mmCIF and BinaryCIF files."""

    homepage = "https://github.com/ihmwg/python-modelcif"
    git = "https://github.com/ihmwg/python-modelcif.git"
    pypi = "modelcif/modelcif-1.4.tar.gz"

    maintainers("LydDeb")

    license("MIT", checked_by="LydDeb")

    version("1.6", sha256="b1bf0751f0e2d1ea6da7a0a8a92efd2754428ae50bc3bfbff8e015183e978b19")
    version("1.4", sha256="fca5c1da5eb25fff3c9cd61b618fa247569f8e90cbb64774740601155d4add6e")

    depends_on("py-setuptools", type="build")
    depends_on("py-ihm@2.6:", type=("build", "run"))
