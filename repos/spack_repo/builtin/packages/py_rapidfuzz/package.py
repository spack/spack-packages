# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyRapidfuzz(PythonPackage):
    """Rapid fuzzy string matching in Python and C++ using the Levenshtein Distance."""

    homepage = "https://github.com/maxbachmann/rapidfuzz"
    pypi = "rapidfuzz/rapidfuzz-1.8.2.tar.gz"

    license("MIT")

    version("3.14.3", sha256="2491937177868bc4b1e469087601d53f925e8d270ccc21e07404b4b5814b7b5f")
    version("3.3.1", sha256="6783b3852f15ed7567688e2e358757a7b4f38683a915ba5edc6c64f1a3f0b450")
    version("2.2.0", sha256="acb8839aac452ec61a419fdc8799e8a6e6cd21bed53d04678cdda6fba1247e2f")
    version("1.8.2", sha256="d6efbb2b6b18b3a67d7bdfbcd9bb72732f55736852bbef823bdf210f9e0c6c90")

    depends_on("cxx", type="build")  # generated

    depends_on("python", type=("build", "link", "run"))
    depends_on("python@3.10:", when="@3.14.3:", type=("build", "link", "run"))
    depends_on("py-setuptools@42:", when="@2:3.3.1", type="build")
    depends_on("py-setuptools", when="@:3.3.1", type="build")
    depends_on("py-scikit-build-core@0.11:", when="@3.14.3:", type="build")
    depends_on("py-scikit-build@0.17", when="@3:3.3.1", type="build")
    depends_on("py-scikit-build@0.13:", when="@2.2:3.3.1", type="build")
    depends_on("py-rapidfuzz-capi@1.0.5", when="@2", type="build")
    depends_on("py-jarowinkler@1.2.0:1", when="@2", type=("build", "run"))

    # CMakeLists.txt
    depends_on("cmake@3.12:", when="@:3.3.1", type="build")
    depends_on("cmake@3.15:3.30", when="@3.14.3:", type="build")
    depends_on("ninja", type="build")
