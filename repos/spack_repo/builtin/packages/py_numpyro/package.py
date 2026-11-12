# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNumpyro(PythonPackage):
    """Probabilistic programming with NumPy powered by JAX for autograd and
    JIT compilation to GPU/TPU/CPU."""

    homepage = "https://github.com/pyro-ppl/numpyro"
    pypi = "numpyro/numpyro-0.22.0.tar.gz"

    license("Apache-2.0")

    version("0.22.0", sha256="d428b688f7c6d1f9089b730c242a3817452609e3672bd62bbc1b02ce17f069bb")

    with default_args(type="build"):
        depends_on("py-setuptools@61:")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:")

        depends_on("py-jax@0.7:")
        depends_on("py-jaxlib@0.7:")
        depends_on("py-multipledispatch")
        depends_on("py-numpy")
        depends_on("py-tqdm")
