# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *

VERSIONS = {
    "0.1.10": "a221154d789d7c03ba2e06da9653301fb1954f92d9c2608e8c19fd33dde84d2d",
    # 0.1.9 is skipped because it is partially broken
    "0.1.8": "8bb19a487d112ca6fe73a75fd28440e35b29f1d599a36fc41dc0f05fca783353",
    "0.1.7": "bd8cc1638e5e2bb14f9db57c634bb9794b6530796041a698cb8b47d7ad67c9ab",
    "0.1.6": "cb1a966bd69e13234b02289f984705ecdbf5eb3cbcb050c1e103741adc708d50",
    "0.1.5": "fb9680cd4cbac4348833af9cb2d196bcfbffb02da623397168e3f96c9a9e0e32",
    "0.1.4": "c593bbc0fa3a410bd19d4a4a8d0008d5bd1c31a9faaca85b9d6b655ee1133bde",
    "0.1.3": "60a4b651cf6e15f175879af74d18215d45cc4fd5e42a61242a180e2014fe9fd2",
}


class PyMetatomicTorch(PythonPackage):
    """Torchscript bindings for metatomic"""

    homepage = "https://docs.metatensor.org/metatomic"
    pypi = "metatomic-torch/metatomic_torch-0.0.0.tar.gz"

    import_modules = ["metatomic.torch"]

    maintainers("HaoZeke", "Luthaf", "RMeli")
    license("BSD-3-Clause", checked_by="HaoZeke")

    for ver, sha256 in VERSIONS.items():
        version(ver, sha256=sha256)
        depends_on(f"libmetatomic-torch@={ver}", when=f"@{ver}")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("python@3.10:", type=("build", "run"), when="@0.1.6:")
    # python/metatomic_torch/setup.py
    depends_on("py-torch@2.1:", type=("build", "run"))
    depends_on("py-vesin", type=("build", "run"))
    depends_on("py-vesin@0.5.1:", type=("build", "run"), when="@0.1.10:")
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
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Fix build when torch looks for a CUDA compiler
    patch(
        "https://github.com/metatensor/metatomic/commit/256f9f96eb36620e42228c25d7b3062d544a11c0.patch?full_index=1",
        sha256="4e958c83e1a2b5684984f6db38c948a86cca6b5477f8e0a849496d235f81d628",
        when="@0.1.3",
        level=3,
    )

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("METATOMIC_TORCH_PYTHON_USE_EXTERNAL_LIB", "ON")
