# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyImagecorruptionsImaug(PythonPackage):
    """This package provides a set of image corruptions."""

    homepage = "https://github.com/imaug/imagecorruptions"
    pypi = "imagecorruptions_imaug/imagecorruptions_imaug-1.1.3.tar.gz"

    license("Apache-2.0")

    version("1.1.3", sha256="dd103a5b7a1d1d8d173aec26fe8b4be93ef83de122bea4ad88c08695daa76d00")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-numpy@1.16:", type=("build", "run"))
    depends_on("pil@5.4.1:", type=("build", "run"))
    depends_on("py-scikit-image@0.15:", type=("build", "run"))
    depends_on("opencv@3.4.5:+python3", type=("build", "run"))
    depends_on("py-scipy@1.2.1:", type=("build", "run"))
    depends_on("py-numba@0.53:", type=("build", "run"))
