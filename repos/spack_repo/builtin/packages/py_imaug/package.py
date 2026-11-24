# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyImaug(PythonPackage):
    """Image augmentation library for deep neural networks. Fork of py-imgaug"""

    homepage = "https://github.com/imaug/imaug"
    pypi = "imaug/imaug-0.4.2.tar.gz"

    license("MIT")

    version("0.4.2", sha256="996fffc4877c9664228679d566a5ebfd49a87648547d3bca1bb2905033e83421")

    depends_on("python@3.6.1:3.13", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-six")
        depends_on("py-numpy@1.21:")
        depends_on("py-scipy")
        depends_on("pil")
        depends_on("py-matplotlib")
        depends_on("py-scikit-image@0.18:")
        depends_on("opencv+python3")
        depends_on("py-imageio")
        depends_on("py-shapely")
        depends_on("py-imagecorruptions-imaug@1.1.3:")
