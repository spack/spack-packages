# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHssm(PythonPackage):
    """Bayesian inference for hierarchical sequential sampling models."""

    homepage = "https://lnccbrown.github.io/HSSM/"
    pypi = "hssm/hssm-0.5.0.tar.gz"
    git = "https://github.com/lnccbrown/HSSM.git"

    license("custom")

    version("0.5.0", sha256="e3dda827d7e6c61ab524e3cadfbd6b4cf67f7c58c7d8043d51e3849467ea1278")

    with default_args(type="build"):
        depends_on("py-uv-build@0.11.21:0.11")

    with default_args(type=("build", "run")):
        depends_on("python@3.12:3.14")

        depends_on("py-absl-py@2.5:")
        depends_on("py-bambi@0.19:")
        depends_on("py-h5netcdf@1.8.1:")
        depends_on("py-h5py@3.16:")
        depends_on("py-hddm-wfpt@0.1.6:")
        depends_on("py-huggingface-hub@1.17:")
        depends_on("py-jaxonnxruntime@0.3:")
        depends_on("py-numpy@2.4")
        depends_on("py-numpyro@0.20:")
        depends_on("py-onnx@1.16:")
        depends_on("py-scipy@1.10:")
        depends_on("py-ssm-simulators@0.14:")
