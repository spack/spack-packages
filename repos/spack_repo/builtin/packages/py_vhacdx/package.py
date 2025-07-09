# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVhacdx(PythonPackage):
    """Generates an approximate convex decomposition of a triangle mesh."""

    homepage = "https://github.com/trimesh/vhacdx"
    pypi = "vhacdx/vhacdx-0.0.8.post2.tar.gz"

    maintainers("moloney")

    license("MIT", checked_by="moloney")

    version("0.0.8.post2", sha256="aa27c5ef19ed4aba428fa9408dccc37f2b7a6bbfaddc48b06a8cea9faaf93156")

    depends_on("cxx", type="build")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pybind11", type="build")

    depends_on("py-numpy", type=("build", "run"))
