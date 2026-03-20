# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBoostHistogram(PythonPackage):
    """The Boost::Histogram Python wrapper."""

    homepage = "https://github.com/scikit-hep/boost-histogram"
    pypi = "boost_histogram/boost_histogram-1.2.1.tar.gz"

    license("BSD-3-Clause")

    version("1.7.1", sha256="6ed3d7d2688fa32889dd441a7ef4920d60d696137d2abc3ab14eb9bd3b455b19")
    version("1.6.1", sha256="cbe67507f62063590395cc9fe177bf979f26a53c0574365f8241b883b9a6f756")
    version("1.5.2", sha256="51e42e830b848f08ad4d28de2ade18ded6e9a2fa4e6038becc9c72592e484e5c")
    version("1.4.1", sha256="97146f735f467d506976a047f3f237ce59840a952fd231f5f431f897fb006cdd")
    version("1.3.2", sha256="e175efbc1054a27bc53fbbe95472cac9ea93999c91d0611840d776b99588d51a")
    version("1.3.1", sha256="31cd396656f3a37834e07d304cdb84d9906bc2172626a3d92fe577d08bcf410f")
    version("1.2.1", sha256="a27842b2f1cfecc509382da2b25b03056354696482b38ec3c0220af0fc9b7579")

    depends_on("cxx", type="build")  # generated

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"), when="@1.4")
    depends_on("python@3.8:", type=("build", "run"), when="@1.5")
    depends_on("python@3.9:", type=("build", "run"), when="@1.6")
    depends_on("python@3.10:", type=("build", "run"), when="@1.7:")

    with when("@1.5:"):
        depends_on("py-scikit-build-core@0.11:", type="build")
        depends_on("py-pybind11@2.13.3:", type="build")
        depends_on("py-pybind11@3:", type="build", when="@1.6:")
        # pyproject.toml:
        # [tool.scikit-build]
        # metadata.version.provider = "scikit_build_core.metadata.setuptools_scm"
        depends_on("py-setuptools-scm", type="build")
    with when("@:1.4"):
        depends_on("py-setuptools@45:", type="build")
        depends_on("py-setuptools-scm@4.1.2:+toml", type="build")

    depends_on("py-numpy@1.13.3:", type=("build", "run"))
    depends_on("py-numpy@1.21.3:", type=("build", "run"), when="@1.7:")
    # https://github.com/numpy/numpy/issues/26191#issuecomment-2179127999
    depends_on("py-numpy@:1", when="@:1.4.0", type=("build", "run"))
    depends_on("py-typing-extensions", when="^python@:3.7", type=("build", "run"))
