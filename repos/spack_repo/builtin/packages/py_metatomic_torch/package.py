# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMetatomicTorch(PythonPackage):
    """Torchscript bindings for metatomic"""

    homepage = "https://docs.metatensor.org/metatomic"
    pypi = "metatomic-torch/metatomic_torch-0.0.0.tar.gz"

    import_modules = ["metatomic.torch"]

    maintainers("HaoZeke", "Luthaf", "RMeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    version("0.1.6", sha256="cb1a966bd69e13234b02289f984705ecdbf5eb3cbcb050c1e103741adc708d50")
    version("0.1.5", sha256="fb9680cd4cbac4348833af9cb2d196bcfbffb02da623397168e3f96c9a9e0e32")
    version("0.1.4", sha256="c593bbc0fa3a410bd19d4a4a8d0008d5bd1c31a9faaca85b9d6b655ee1133bde")
    version("0.1.3", sha256="60a4b651cf6e15f175879af74d18215d45cc4fd5e42a61242a180e2014fe9fd2")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"), when="@0.1.6:")
    # python/metatomic_torch/setup.py
    depends_on("py-torch@2.1:", type=("build", "run"))
    depends_on("py-vesin", type=("build", "run"))
    depends_on("py-metatensor-torch@0.8.0:0.8", type=("build", "run"), when="@0.1.4:")
    depends_on("py-metatensor-torch@0.7.0:0.7", type=("build", "run"), when="@0.1.3")
    depends_on("py-metatensor-operations@0.4.0:0.4", type=("build", "run"), when="@0.1.6:")
    depends_on("py-metatensor-operations@0.3.0:0.3", type=("build", "run"), when="@:0.1.5")
    # pyproject.toml
    depends_on("py-setuptools@77:", type="build")
    depends_on("py-packaging@23:", type="build")
    # CMakeLists.txt
    depends_on("cmake@3.16:", type="build")
    depends_on("cmake@3.22:", type="build", when="@0.1.5:")

    # Fix build when torch looks for a CUDA compiler
    patch(
        "https://github.com/metatensor/metatomic/commit/256f9f96eb36620e42228c25d7b3062d544a11c0.patch?full_index=1",
        sha256="4e958c83e1a2b5684984f6db38c948a86cca6b5477f8e0a849496d235f81d628",
        when="@0.1.3",
        level=3,
    )
