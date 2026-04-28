# Copyright Spack Project Developers. See COPYRIGHT file for details.
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyImutils(PythonPackage):
    """A series of convenience functions to make basic image processing
    functions such as translation, rotation, resizing, skeletonization,
    displaying Matplotlib images, sorting contours, detecting edges, and much
    more easier with OpenCV and both Python 2.7 and Python 3."""

    homepage = "https://github.com/jrosebr1/imutils"
    pypi = "imutils/imutils-0.5.4.tar.gz"

    license("MIT", checked_by="alex391")

    version("0.5.4", sha256="03827a9fca8b5c540305c0844a62591cf35a0caec199cb0f2f0a4a0fb15d8f24")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("opencv+python3+imgcodecs", type=("build", "run"))
