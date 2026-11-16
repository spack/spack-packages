# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyJaxonnxruntime(PythonPackage):
    """Jaxonnxruntime: JAX based ONNX Runtime."""

    homepage = "https://github.com/google/jaxonnxruntime"
    pypi = "jaxonnxruntime/jaxonnxruntime-0.3.0.tar.gz"

    license("Apache-2.0")

    version("0.3.0", sha256="64340d83f280f725ef068326aedc87489a39f5da67ceebcdbcb24ce777cf8198")

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-setuptools-scm")

    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        depends_on("py-jax")
        depends_on("py-jaxlib")
