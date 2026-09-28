# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPantheonGpu(PythonPackage):
    """Pantheon is a GPU stress-testing and diagnostics suite for NVIDIA CUDA
    and AMD ROCm. It compiles its workloads for the card it finds, runs them
    one subsystem at a time (memory, compute, interconnect, thermals) and
    writes a JSON report of every run."""

    homepage = "https://pantheongpu.com"
    pypi = "pantheon-gpu/pantheon_gpu-1.2.2.tar.gz"
    git = "https://github.com/pantheongpu/pantheon.git"

    maintainers("saqibkh")

    # Pantheon is Apache-2.0. It bundles one header of NVIDIA's Video Codec SDK,
    # nvEncodeAPI.h, which is MIT licensed.
    license("Apache-2.0 AND MIT", checked_by="saqibkh")

    version("1.2.2", sha256="49e3af588a315f1d69f979a4c0217ee98af0d4de24478ca9b0618edfcad51022")

    # The workloads are compiled on the node at first run, for the exact card
    # found there, so the GPU toolchain is needed at run time and not at build.
    variant("cuda", default=False, description="Depend on CUDA, whose nvcc builds the workloads")
    variant("rocm", default=False, description="Depend on HIP, whose hipcc builds the workloads")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@68:", type="build")

    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-nvidia-ml-py", type=("build", "run"))

    depends_on("gmake", type="run")
    depends_on("cuda", when="+cuda", type="run")
    depends_on("hip", when="+rocm", type="run")

    conflicts("platform=darwin", msg="Pantheon runs on Linux")
    conflicts("platform=windows", msg="Pantheon runs on Linux")
