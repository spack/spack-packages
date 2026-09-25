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

    version("0.4.3", sha256="03ddab6936dbdcdda8d211bde32cad9abe51603f010fc6f4a8264160c4c2f84a")
    version("0.4.2", sha256="996fffc4877c9664228679d566a5ebfd49a87648547d3bca1bb2905033e83421")

    depends_on("python@3.6.1:3.13", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-six")
        depends_on("py-numpy@1.21:")
        depends_on("py-numpy@2.3:", when="^python@3.14:")
        depends_on("py-scipy")
        depends_on("pil")
        depends_on("py-matplotlib")
        depends_on("py-scikit-image@0.18:")
        depends_on("opencv+python3")
        depends_on("py-imageio")
        depends_on("py-shapely")
        depends_on("py-imagecorruptions-imaug@1.1.3:")
        depends_on("py-imagecorruptions-imaug@1.1.5:", when="@0.4.3:")

    # ModuleNotFoundError: No module named 'pkg_resources'
    conflicts("py-setuptools@82:", when="@:0.4.2")
