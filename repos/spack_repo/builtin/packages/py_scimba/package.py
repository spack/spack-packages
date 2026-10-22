# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScimba(PythonPackage):
    """This library implements some common tools for scientific machine learning."""

    homepage = "https://www.scimba.org"
    pypi = "scimba/scimba-1.3.4.tar.gz"

    maintainers("tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("1.3.4", sha256="7b555633c577c043b73417f86a85ca2c71837e4310fc114de7ada31a1f60a755")

    variant("jax", default=False, description="Install the experimental JAX backend")

    depends_on("py-setuptools@61.2:", type="build")

    depends_on("python@3.10:", when="@1.0.0:", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-torch@2.9:", type=("build", "run"))

    with when("+jax"):
        depends_on("py-jax@0.6.2:", type=("build", "run"))
        depends_on("py-equinox@0.13:", type=("build", "run"))
        depends_on("py-optax", type=("build", "run"))
        depends_on("py-jax-tqdm", type=("build", "run"))
