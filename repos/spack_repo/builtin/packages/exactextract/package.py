# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.python import PythonExtension, PythonPipBuilder

from spack.package import *


class Exactextract(CMakePackage, PythonExtension):
    """exactextract is a library for extracting and summarizing the
    values in the portion of a raster dataset that is covered by a polygon,
    often referred to as zonal statistics."""

    homepage = "https://isciences.github.io/exactextract/index.html"
    git = "https://github.com/isciences/exactextract.git"
    url = "https://github.com/isciences/exactextract/archive/refs/tags/v0.3.0.tar.gz"

    maintainers("Chrismarsh")

    license("Apache-2.0")

    version("0.3.0", sha256="0f825bb27daa184c822ff155c8462ec69cac34a0ca1cc95b2f3a02ebb99b7e65")

    variant("python", default=False, description="Enable Python support")
    variant("tbb", default=False, description="Enable TBB parallel support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.8:", type="build")

    # header only
    depends_on("cli11", type="build")

    depends_on("geos@3.5:", type=("build", "run"))
    depends_on("gdal@2:", type=("build", "run"))
    depends_on("intel-oneapi-tbb", type=("build", "run"), when="+tbb")

    with when("+python"):
        extends("python", type=("build", "link", "run"))
        depends_on("py-pip")
        depends_on("py-scikit-build-core", type="build")
        depends_on("py-pybind11")

    def cmake_args(self):
        cmake_args = [
            self.define_from_variant("BUILD_PYTHON", "python"),
            self.define_from_variant("BUILD_PARALLEL_TBB", "tbb"),
        ]

        return cmake_args

    @run_after("install")
    def install_python(self):
        if self.spec.satisfies("+python"):
            # build the python library
            pip(*PythonPipBuilder.std_args(self), f"--prefix={self.prefix}", ".")
