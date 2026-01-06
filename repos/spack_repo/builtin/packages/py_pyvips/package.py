# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyvips(PythonPackage):
    """Python binding for the libvips image processing library."""

    homepage = "https://github.com/libvips/pyvips"
    pypi = "pyvips/pyvips-3.1.1.tar.gz"

    version("3.1.1", sha256="84fe744d023b1084ac2516bb17064cacd41c7f8aabf8e524dd383534941b9301")

    depends_on("py-setuptools@61:", type="build")
    depends_on("py-pkgconfig@1.5:", type="build")  # needed to enable API mode
    depends_on("py-cffi@1:", type=("build", "run"))

    depends_on("libvips +fftw +jpeg +tiff +png +poppler", type=("run", "build", "link"))
