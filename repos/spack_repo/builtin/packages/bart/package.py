# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack_repo.builtin.build_systems.python import PythonExtension

from spack.package import *


class Bart(MakefilePackage, CudaPackage, PythonExtension):
    """BART: Toolbox for Computational Magnetic Resonance Imaging"""

    homepage = "https://mrirecon.github.io/bart/"
    url = "https://github.com/mrirecon/bart/archive/v0.5.00.tar.gz"

    license("BSD-3-Clause")

    version("0.9.00", sha256="86668e4d56460a5f5def2d01fba2b5143830f34028f09cad42c099d862bd892d")
    version("0.7.00", sha256="a16afc4b632c703d95b5c34e47acd82fafc19f51f9aff442373eecfef08bfc41")
    version("0.6.00", sha256="dbbd33d1e3ed3324fe21f90a3b62cb51765fe369f21df100b46a32004928f18d")
    version("0.5.00", sha256="30eedcda0f0ef3808157542e0d67df5be49ee41e4f41487af5c850632788f643")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("gcc@11:", type="build", when="@0.9:")

    # patch to fix build with MKL
    patch(
        "https://github.com/mrirecon/bart/commit/b62ca4972d5ac41a44217a5c27123c15daae74db.patch?full_index=1",
        sha256="501ca985df2324fc02e32cc4ffb32ce5c235fe83a59f5b853eb78ad0f2d6629c",
        when="@0.5.00",
    )

    # patch to fix Makefile for openblas and cuda
    patch("Makefile.patch", when="@:0.6.00")
    patch("Makefile-0.7.00.patch", when="@0.7.00")
    patch("Makefile-0.9.00.patch", when="@0.9.00")

    # patch to set path to bart
    patch("bart_path-0.5.00.patch", when="@0.5.00")
    patch("bart_path-0.6.00.patch", when="@0.6.00:0.7")
    patch("bart_path-0.9.00.patch", when="@0.9.00")

    depends_on("libpng")
    depends_on("fftw")
    depends_on("blas")
    depends_on("lapack")
    depends_on("py-numpy", type="run")
    depends_on("py-matplotlib", type="run")
    extends("python")

    conflicts("^atlas", msg="BART does not currently support atlas")

    def setup_build_environment(self, env):
        env.set("PREFIX", self.prefix)
        env.set("FFTW_BASE", self.spec["fftw"].prefix)

        if self.spec["blas"].name == "openblas":
            env.set("OPENBLAS", "1")
            env.set("FORTRAN", "0")

        elif self.spec.satisfies("^[virtuals=blas] intel-oneapi-mkl"):
            env.set("MKL", "1")
            env.set("MKL_BASE", spec["mkl"].prefix.mkl)
        else:
            env.set("BLAS_BASE", spec["blas"].prefix)

        if self.spec.satisfies("@:0.7.00"):
            if "^netlib-lapack+lapacke" not in self.spec:
                env.set("NOLAPACKE", "1")

        if self.spec.satisfies("+cuda"):
            cuda_arch = self.spec.variants["cuda_arch"].value
            env.set("CUDA", "1")
            env.set("CUDA_BASE", spec["cuda"].prefix)
            env.set("GPUARCH_FLAGS", " ".join(self.cuda_flags(cuda_arch)))

    def install(self, spec, prefix):
        make("install")

        install_tree("scripts", prefix.scripts)
        install_tree("matlab", prefix.matlab)
        install("startup.m", prefix)

        os.makedirs(python_platlib, exist_ok=True)

        install("python/bart.py", python_platlib)
        install("python/cfl.py", python_platlib)
        install("python/wslsupport.py", python_platlib)

        if spec.satisfies("^python@3:"):
            install("python/bartview3.py", join_path(prefix.bin, "bartview"))
            filter_file(r"#!/usr/bin/python3", "#!/usr/bin/env python", prefix.bin.bartview)
        else:
            install("python/bartview.py", join_path(prefix.bin, "bartview"))
            filter_file(r"#!/usr/bin/python", "#!/usr/bin/env python", prefix.bin.bartview)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@0.9:"):
            env.set("BART_TOOLBOX_PATH", self.prefix)
        else:
            env.set("TOOLBOX_PATH", self.prefix)
