# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScimba(PythonPackage):
    """This library implements some common tools for scientific machine learning."""

    homepage = "https://www.scimba.org"
    pypi = "scimba/scimba-1.3.4.tar.gz"

    maintainers("tpadioleau", "boileaum")

    license("MIT", checked_by="tpadioleau")

    version("1.4.2", sha256="b689fc75074aa6ffbb483d6296e0490eac1c06ff160c4888c450136d14c513b3")
    version("1.4.1", sha256="91ce62810b828837544291c4fc81b1ebdef59dc7455d03167ff60a719bea9d15")
    version("1.3.4", sha256="7b555633c577c043b73417f86a85ca2c71837e4310fc114de7ada31a1f60a755")

    variant("torch", default=True, description="Enable PyTorch backend", when="@1.4.1:")
    variant("jax", default=False, description="Install the experimental JAX backend", when="@:1.3")
    variant("jax", default=True, description="Enable JAX backend", when="@1.4.1:")
    variant("mesh", default=False, description="Enable GMSH and meshio support", when="@1.4.1:")

    depends_on("py-setuptools@61.2:", type="build")

    depends_on("python@3.11:", when="@1.4.1:", type=("build", "run"))
    depends_on("python@3.10:", when="@1.0.0:", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))

    depends_on("py-torch@2.9:", type=("build", "run"), when="@:1.3")
    depends_on("py-torch@2.9:", type=("build", "run"), when="@1.4.1: +torch")

    with when("+jax"):
        depends_on("py-jax@0.6.2:", type=("build", "run"))
        depends_on("py-equinox@0.13:", type=("build", "run"), when="@:1.3")
        depends_on("py-optax", type=("build", "run"), when="@:1.3")
        depends_on("py-orbax-checkpoint", type=("build", "run"), when="@1.4.1:")
        depends_on("py-jax-tqdm", type=("build", "run"))

    with when("+mesh"):
        depends_on("py-meshio", type=("build", "run"))
        depends_on("py-gmsh", type=("build", "run"))

    @property
    def skip_modules(self):
        skipped = []
        if self.spec.satisfies("@1.4.1: ~torch"):
            skipped.append("scimba_torch")
        if not self.spec.satisfies("+jax"):
            skipped.append("scimba_jax")
        if not self.spec.satisfies("+mesh"):
            skipped.append("scimba_jax.mapping.macro_mesh")
        return skipped
