# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMelissaCore(PythonPackage, CudaPackage):
    """Melissa is a file-avoiding, adaptive, fault-tolerant and elastic
    framework, to run large-scale sensitivity analysis or deep-surrogate
    training on supercomputers.

    This package builds the launcher and server modules.

    **Note:** This package is now unified as `py-melissa-online` from version 3+.
    """

    homepage = "https://gitlab.inria.fr/melissa/melissa"
    git = "https://gitlab.inria.fr/melissa/melissa.git"
    url = "https://gitlab.inria.fr/melissa/melissa/-/archive/v2.0.0/melissa-v2.0.0.tar.gz"
    maintainers("abhishek1297", "raffino")

    license("BSD-3-Clause")

    version(
        "2.4.1",
        sha256="92a8c7f823ef79c8a5eb05b67120e130c9b03bf7fecd635b4ae9501eb32b2fd7",
        deprecated=True,
    )

    # define variants for the deep learning server (torch, tf)
    variant(
        "torch", default=False, description="Install Deep Learning requirements with Pytorch only"
    )
    variant(
        "tf",
        default=True,
        when="~torch",
        description="Install Deep Learning requirements with TensorFlow only",
    )

    # ============================================================
    #                     Base dependencies
    # ============================================================

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")  # generated
    depends_on("py-setuptools@46.4:", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.9:3.12", when="@:2.1.0")
        depends_on("python@3.11:3.12", when="@2.1.1:")

    with default_args(type="run"):
        depends_on("py-pyzmq@22.3.0:")
        depends_on("py-mpi4py@3.1.3:3", when="@:2.3.0")
        depends_on("py-mpi4py@3.1.3:", when="@2.4:")
        depends_on("py-numpy@1.21:1")
        depends_on("py-jsonschema@4.5:")
        depends_on("py-python-rapidjson@1.8:")
        depends_on("py-scipy@1.10.0:1")
        depends_on("py-plotext@5.2.8:")
        depends_on("py-cloudpickle@2.2.0:")
        depends_on("py-iterative-stats@0.1:")
        depends_on("py-psutil@5:")

    # ============================================================
    #                       DL dependencies
    # ============================================================

    for framework in ["+tf", "+torch"]:
        with when(framework):
            conflicts("%gcc@:9", msg=f"GCC must be greater than version 9 when using {framework}")

            with default_args(type="run"):
                depends_on("py-tensorboard@2.10.0:2")
                depends_on("py-matplotlib")
                depends_on("py-pandas")

            depends_on("binutils@2.29:", type="build", when="%gcc")

    # ============================================================
    #                   Frameworks with/out CUDA
    # ============================================================

    with default_args(type="run"):
        # Without CUDA
        with when("~cuda"):
            # WARNING: Do not set tensorflow upper limit above 2.17.
            # Versions >2.17 require AVX-VNNI-INT8 CPU support.
            # Check your CPU flags for 'avxvnniint8' before increasing.
            depends_on("py-tensorflow@2.8.0:2.17 ~cuda", when="+tf")
            depends_on("py-torch@1.12.1:2 ~cuda", when="+torch")

        # With CUDA
        for arch in CudaPackage.cuda_arch_values:
            cuda_specs = f"+cuda cuda_arch={arch}"
            with when(cuda_specs):
                depends_on(f"py-tensorflow@2.8.0:2.17+nccl{cuda_specs}", when="+tf")
                depends_on(f"py-torch@1.12.1:2+cudnn+nccl{cuda_specs}", when="+torch")
