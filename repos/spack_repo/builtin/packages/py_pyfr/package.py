# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.python import PythonPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class PyPyfr(PythonPackage, CudaPackage, ROCmPackage):
    """PyFR is an open-source Python based framework for solving
    advection-diffusion type problems on streaming architectures
    using the Flux Reconstruction approach of Huynh."""

    homepage = "https://www.pyfr.org/"
    pypi = "pyfr/pyfr-1.13.0.tar.gz"
    git = "https://github.com/PyFR/PyFR/"
    maintainers("MichaelLaufer")

    license("BSD-3-Clause")

    # git branches
    version("develop", branch="develop")
    version("master", branch="master")

    # pypi releases
    version(
        "3.1",
        sha256="a41d183f6d1499a2e0f65ca8b231032b23ae3166acb278201b9dadfeb6ec63ef",
        preferred=True,
    )
    version("3.0", sha256="719db2bb69accb1c7744a7d7b97a128d664c7eab9e73f2687036cad22dcd76d9")
    version("2.1", sha256="9da6c66cf7322a2242efd46c679dc9de43d134b2fce4076f44d7951ed6dff665")
    version("2.0.3", sha256="1fd2ca377596ab541d929d2c7b2d27e376e21b5dd6c4c0e7653bbb53864dee61")
    version("2.0.2", sha256="2c6bf460ffec446a933451792c09d3cd85d6703f14636d99810d61823b8d92c7")
    version("1.15.0", sha256="6a634b9d32447f45d3c24c9de0ed620a0a0a781be7cc5e57b1c1bf44a4650d8d")

    variant("metis", default=False, when="@:1.15.0", description="Metis for mesh partitioning")
    variant("scotch", default=True, description="Scotch for mesh partitioning")
    variant("kahip", default=False, when="@3:", description="KaHIP for mesh partitioning")
    variant("tinytc", default=False, when="@2.1:", description="TinyTC for OpenCL backend")
    variant("cuda", default=False, description="CUDA backend support")
    variant("hip", default=False, description="HIP backend support")
    variant("libxsmm", default=True, description="LIBXSMM for OpenMP backend")

    # Required dependencies
    depends_on("python@3.9:", when="@:1.15.0", type=("build", "run"))
    depends_on("python@3.10:", when="@2.0.2:2.1", type=("build", "run"))
    depends_on("python@3.11:", when="@3:", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-gimmik@3", when="@1.15.0", type=("build", "run"))
    depends_on("py-gimmik@3.2.1:", when="@2.0.2:", type=("build", "run"))
    depends_on("py-h5py@2.10:", type=("build", "run"))
    depends_on("py-mako@1.0.0:", type=("build", "run"))
    depends_on("py-mpi4py@3.1.0:", when="@:2.1", type=("build", "run"))
    depends_on("py-mpi4py@4.0.0:", when="@3:", type=("build", "run"))
    depends_on("py-numpy@1.20:", when="@:1.15.0", type=("build", "run"))
    depends_on("py-numpy@1.26.4:", when="@2.0.2:2.1", type=("build", "run"))
    depends_on("py-numpy@2.4.2:", when="@3:", type=("build", "run"))
    depends_on("py-platformdirs@2.2.0:", type=("build", "run"))
    depends_on("py-pytools@2016.2.1:", type=("build", "run"))
    depends_on("py-rtree@1.0.1:", when="@2.0.2:2.1", type=("build", "run"))
    depends_on("py-rtree@1.4.1:", when="@3:", type=("build", "run"))

    # Optional dependencies
    depends_on("metis@5.0.0:5.1.0", when="@:1.15.0 +metis", type=("run"))
    depends_on("scotch@7.0.1: +link_error_lib", when="+scotch", type=("run"))
    depends_on("kahip@3.10:", when="@3: +kahip", type=("run"))
    depends_on("tiny-tensor-compiler@0.3.1:+opencl+shared", when="@2.1: +tinytc", type=("run"))
    depends_on("cuda@11.4.0: +allow-unsupported-compilers", when="@1.15.0: +cuda", type=("run"))
    depends_on("rocblas@5.2.0:", when="@:1.15.0 +hip", type=("run"))
    depends_on("rocblas@6.0.0:", when="@2.0.2:2.1 +hip", type=("run"))
    depends_on("rocblas@6.4.1:", when="@3: +hip", type=("run"))
    depends_on("libxsmm@1.17-pyfr+shared blas=0", when="@:2.1 +libxsmm", type=("run"))
    depends_on("libxsmm@1.17-pyfr+shared", when="@3: +libxsmm", type=("run"))

    # Explicitly add dependencies to environment variables
    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        deps = [
            ("metis", "metis"),
            ("scotch", "scotch"),
            ("kahip", "kahip"),
            ("tinytc", "tiny-tensor-compiler"),
            ("libxsmm", "libxsmm"),
            ("hip", "hip"),
            ("hip", "rocblas"),
        ]
        pyfr_library_path = []
        for variant, dep in deps:
            if "+{}".format(variant) in self.spec:
                if dep == "hip":
                    hip_libdir = str(self.spec[dep].prefix.lib)
                    if os.path.isdir(hip_libdir):
                        pyfr_library_path.append(hip_libdir)
                    continue
                pyfr_library_path.extend(self.spec[dep].libs.directories)
        env.set("PYFR_LIBRARY_PATH", ":".join(pyfr_library_path))

        # LD_LIBRARY_PATH needed for cuda
        if "+cuda" in self.spec:
            env.prepend_path("LD_LIBRARY_PATH", self.spec["cuda"].libs.directories[0])
