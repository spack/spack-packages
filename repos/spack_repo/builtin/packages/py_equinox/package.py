# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEquinox(PythonPackage, CudaPackage):
    """Equinox is your one-stop [JAX](https://github.com/google/jax) library,
    for everything you need that isn't already in core JAX:
    - neural networks (or more generally any model), with easy-to-use PyTorch-like syntax;
    - filtered APIs for transformations;
    - useful PyTree manipulation routines;
    - advanced features like runtime errors;

    and best of all, Equinox isn't a framework: everything you write in Equinox is compatible
    with anything else in JAX or the ecosystem."""

    homepage = "https://docs.kidger.site/equinox/"
    pypi = "equinox/equinox-0.13.1.tar.gz"

    maintainers("abhishek1297")
    license("Apache-2.0", checked_by="abhishek1297")

    version("0.13.2", sha256="509ad744ff99b7c684d45230d6890f9e78eac1a556d7a06db1eff664a3cac74f")
    version("0.13.1", sha256="e90f11cfe66b2f73f5c172260a17c48851794a0f243dd2cbe4ea70f4c90cbd07")
    version("0.13.0", sha256="d59615be722373e9d66e0ba78462964e6357fb76a8b1b98c2c6027961b778a69")
    version("0.12.2", sha256="648e4206bbc53b228922e8f18cd3cffe543ddda1172c0002f8954e484bab0023")
    version("0.12.1", sha256="7ed4b84553cb59d4930185f87ac2c1121aab2b38999be9499c021e7583a7ed0d")
    version("0.12.0", sha256="6a99877376cfc168cfe44220a734740926bf23eb9c0cd0d7fdc49adfec4d78ca")
    version("0.11.12", sha256="bee22aabaf7ee0cde6f2ae58cf3b981dea73d47e297361a0203e299208ef1739")
    version("0.11.11", sha256="648072c1384adc3528930a3bf089246fd77aa873310a19f1f21c08e7681f95a7")
    version("0.11.10", sha256="f3e7d5545b71e427859a28050526d09adb6b20285c47476a606328a0b96c9509")
    version("0.11.9", sha256="e0f0fa5ea597949492d201ab4d08b05c2d5b4020c65a1778aedf6ad76c2c4fe7")
    version("0.11.8", sha256="d1e91a05e41bb9538db72a8e15d26daf958348c26714533434c88c5ec0c0b0ef")
    version("0.11.7", sha256="96e0216a9d822ec4b1465b0cbfbab14a36fb7e7d62c55f521287db3aaaa251be")
    version("0.11.6", sha256="e237c25e446960ed479f086df240d4dd779bb0917bafc76811d341ccac76b712")
    version("0.11.5", sha256="5e0ca252eeb20cc5eece225d3d35137c7e57f998a1c6422a1972db9e5c68b7f6")
    version("0.11.4", sha256="0033d9731083f402a855b12a0777a80aa8507651f7aa86d9f0f9503bcddfd320")
    version("0.11.3", sha256="a1273cc28c60d3131ac596f8a0f5c7dd384729e6cddae86e7be05f026880e8e0")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.10:3.12", type=("build", "run"))

    with default_args(type="run"):
        for arch in CudaPackage.cuda_arch_values:
            cuda_specs = f"+cuda cuda_arch={arch}"
            with when(cuda_specs):
                depends_on(f"py-jaxlib@0.4.13:0.4.26 {cuda_specs}", when="@:0.11.10")
                depends_on(f"py-jaxlib@0.4.38:0.5 {cuda_specs}", when="@0.11.11:0.11.12")
                depends_on(f"py-jaxlib@0.4.38: {cuda_specs}", when="@0.12:")

        depends_on("py-jax@0.4.13:0.4.26", when="@:0.11.10")
        depends_on("py-jax@0.4.38:0.5", when="@0.11.11:0.11.12")
        depends_on("py-jax@0.4.38:", when="@0.12:")

        depends_on("py-jaxtyping@0.2.20:")
        depends_on("py-typing-extensions@4.5.0:")
        depends_on("py-wadler-lindig@0.1.0:")

    conflicts("^py-jaxlib@0.7.0:0.7.1", when="@0.12:")
    conflicts("^py-jax@0.7.0:0.7.1", when="@0.12:")
