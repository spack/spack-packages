# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMlDtypes(PythonPackage):
    """A stand-alone implementation of several NumPy dtype extensions
    used in machine learning libraries."""

    homepage = "https://github.com/jax-ml/ml_dtypes"
    pypi = "ml_dtypes/ml_dtypes-0.3.1.tar.gz"
    git = "https://github.com/jax-ml/ml_dtypes.git"

    license("Apache-2.0")

    version("0.5.1", tag="v0.5.1", commit="560866cfbb44990c9c68b82e878bf8ee7972a595")
    version("0.4.0", tag="v0.4.0", commit="9fc7e6773acb66fa496ed8d476a008a489a4da49")
    version("0.3.1", tag="v0.3.1", commit="bbeedd470ecac727c42e97648c0f27bfc312af30")
    version("0.2.0", tag="v0.2.0", commit="5b9fc9ad978757654843f4a8d899715dbea30e88")

    # ml_dtypes depends on eigen, but the build system relies on a submodule vendor
    # patch that out so Spack can supply an eigen
    # in 0.6.0 ml_dtypes added CMake support so the patch target changes
    patch("third-party-eigen.patch", when="@0.2.0:0.5.1")

    depends_on("cxx", type="build")

    depends_on("python@3.9:", when="@0.3:", type=("build", "link", "run"))
    depends_on("py-numpy@1.21:", type=("build", "link", "run"))
    # https://github.com/jax-ml/ml_dtypes/pull/143
    depends_on("py-numpy@:1", when="@:0.3", type=("build", "link", "run"))
    # Build dependencies are overconstrained, older versions work just fine
    depends_on("py-pybind11", when="@:0.3.1", type=("build", "link"))
    depends_on("py-setuptools", when="@:0.5", type="build")

    # upstream vendors an unreleased snapshot, but requires features
    # from 5.0
    depends_on("eigen@5.0:", type="build")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@:0.5"):
            env.set("EIGEN_DIR", self.spec["eigen"].prefix.include.eigen3)
