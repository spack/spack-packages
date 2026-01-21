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
    """

    homepage = "https://gitlab.inria.fr/melissa/melissa"
    git = "https://gitlab.inria.fr/melissa/melissa.git"
    url = "https://gitlab.inria.fr/melissa/melissa/-/archive/v2.0.0/melissa-v2.0.0.tar.gz"
    maintainers("abhishek1297", "raffino")

    license("BSD-3-Clause")

    version("develop", branch="develop", preferred=True)
    version("2.3.0", sha256="f356e05082e4bb26a210cd11ccfa78a783ebe07be2bd75d5e51ed10da3b58997")
    version("2.2.0", sha256="e805c9ac08de5aa666768d5d92bfc680f064bd9108415a911dfd08ad7b0a3cf3")
    version("2.1.1", sha256="6b92852429f13b144860edc37c7914723addabb0ec0bd108929ff567334d3f71")
    version("2.1.0", sha256="cf0f105ed5b1da260cc7476aec23df084470b50a61df997c0e457c38948bed93")
    version("2.0.1", sha256="a7ff4df75ea09af435b0c28c3fa3cab9335c1c76e1c48757facce36786b4962c")
    version("2.0.0", sha256="75957d1933cd9c228a6e8643bc855587162c31f3b0ca94c3f5e0e380d01775dd")

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
        depends_on("py-mpi4py@3.1.3:3")
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
