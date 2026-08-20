# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDeepdish(PythonPackage):
    """Flexible HDF5 saving/loading and other data science tools from the
    University of Chicago"""

    homepage = "https://github.com/uchicago-cs/deepdish/"
    pypi = "deepdish/deepdish-0.3.7.tar.gz"

    maintainers("Markus92")

    license("BSD-3-Clause", checked_by="Markus92")

    version("0.3.7", sha256="6aff3abef693cec34438f183f29d1a2d9862aba27bb959d4f24d56e007e41ff3")

    variant("image", default=False, description="Build with skimage support")

    with default_args(type="build"):
        depends_on("py-setuptools")

    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-tables")
        depends_on("py-skimage", when="+image")
