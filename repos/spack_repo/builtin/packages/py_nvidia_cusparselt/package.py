# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import platform

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvidiaCusparselt(PythonPackage):
    """A high-performance CUDA library dedicated to general matrix-matrix operations
    in which at least one operand is a structured sparse matrix with 50% sparsity ratio."""

    homepage = "https://docs.nvidia.com/cuda/cusparselt/"

    skip_version_audit = ["platform=darwin", "platform=windows"]

    maintainers("thomas-bouvier")

    system = platform.system().lower()
    arch = platform.machine()
    if "linux" in system and arch == "x86_64":
        version(
            "0.8.1-cuda130",
            sha256="786ce87568c303fadb5afcc7102d454cd3040d75f6f8626f5db460d1871f4dd0",
            url="https://files.pythonhosted.org/packages/34/7d/2661f2fb3ac4302f3a246f5fc030213ac60c1fe0bce84f9783dbd831dbb7/nvidia_cusparselt_cu13-0.8.1-py3-none-manylinux2014_x86_64.whl",
        )
        version(
            "0.8.1-cuda120",
            sha256="cd1b1dc9e1ad31ea3353c1f985e2bd6f9e7ae0e797d7e6ce879d7b2ace5e80e8",
            url="https://files.pythonhosted.org/packages/bb/14/e46964290aa587cb9fb7df20efdc60528ddd00d291ccffec47617fb06ca3/nvidia_cusparselt_cu12-0.8.1-py3-none-manylinux2014_x86_64.whl",
        )
    elif "linux" in system and arch == "aarch64":
        version(
            "0.8.1-cuda130",
            sha256="4dca476c50bf4780d46cd0bfbd82e2bc10a08e4fef7950917ce8d7578d22a23f",
            url="https://files.pythonhosted.org/packages/46/e1/cdc1797eadf82d3a9a575a19b33fdc871a97edbec42c00b5b5e914f4aff4/nvidia_cusparselt_cu13-0.8.1-py3-none-manylinux2014_aarch64.whl",
        )
        version(
            "0.8.1-cuda120",
            sha256="5c72f727722f74762380e5f8755557c788b26d8fdcc49df1641c1b08e16d256c",
            url="https://files.pythonhosted.org/packages/fd/f8/a809966c96e824b92df09ee3b7032442f5e975d873d7dadfef818d527f48/nvidia_cusparselt_cu12-0.8.1-py3-none-manylinux2014_aarch64.whl",
        )

    cuda130_versions = ("@0.8.1-cuda130",)
    cuda120_versions = ("@0.8.1-cuda120",)

    for v in cuda130_versions:
        depends_on("cuda@13", when=v, type=("build", "run"))
    for v in cuda120_versions:
        depends_on("cuda@12", when=v, type=("build", "run"))

    depends_on("python@3.8:", type=("build", "run"))
