# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Pacman(CMakePackage, CudaPackage, ROCmPackage):
    """PACMAN is a performance-portable field transfer library for interpolating
    large-scale scientific data sets, built on Kokkos, Kokkos Kernels and ArborX."""

    homepage = "https://gitlab.com/drti/pacman"
    git = "https://gitlab.com/drti/pacman.git"
    url = "https://gitlab.com/drti/pacman/-/archive/v0.1.2/pacman-v0.1.2.tar.gz"

    maintainers("messahelramzi")

    license("BSD-3-Clause")

    version("0.1.2", sha256="8da7c647fcdae42cecf8846d9fc4f872c21aa0f989dbb869a850df8e1642d2e9")

    variant("sycl", default=False, description="Build the SYCL device Backend")
    variant("python", default=True, description="Build the Python interface")
    variant("fortran", default=False, description="Build the Fortran interface")
    variant("tests", default=False, description="Build the test suite")

    # A build carries at most one device Backend
    for _a, _b in (("cuda", "rocm"), ("cuda", "sycl"), ("rocm", "sycl")):
        conflicts(
            f"+{_a} +{_b}",
            msg=f"+{_a} and +{_b} are mutually exclusive: PACMAN builds at most one device "
            "Backend (pick one of +cuda, +rocm, +sycl)",
        )

    conflicts("+cuda", when="cuda_arch=none", msg="+cuda requires a cuda_arch value")

    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    depends_on("cmake@3.31:", type="build")

    depends_on("kokkos@5:")
    depends_on("kokkos-kernels@5:")
    depends_on("arborx@2.1:~mpi")

    # The device Backend of PACMAN is the one of Kokkos, kokkos-kernels and ArborX
    for _backend in ("cuda", "rocm", "sycl"):
        depends_on(f"kokkos~{_backend}", when=f"~{_backend}")
        depends_on(f"arborx~{_backend}", when=f"~{_backend}")
    depends_on("kokkos-kernels~cuda", when="~cuda")

    for _arch in CudaPackage.cuda_arch_values:
        _cuda_dep = f"+cuda cuda_arch={_arch}"
        depends_on(f"kokkos {_cuda_dep}", when=_cuda_dep)
        depends_on(f"kokkos-kernels {_cuda_dep}", when=_cuda_dep)
        depends_on(f"arborx {_cuda_dep}", when=_cuda_dep)

    # kokkos-kernels has no ROCm or SYCL variant: it follows the Kokkos it is built on
    for _arch in ROCmPackage.amdgpu_targets:
        _rocm_dep = f"+rocm amdgpu_target={_arch}"
        depends_on(f"kokkos {_rocm_dep}", when=_rocm_dep)
        depends_on(f"arborx {_rocm_dep}", when=_rocm_dep)

    depends_on("kokkos+sycl", when="+sycl")
    depends_on("arborx+sycl", when="+sycl")

    with when("+python"):
        extends("python")
        depends_on("py-pybind11", type="build")
        depends_on("py-numpy", type=("build", "run"))

    def cmake_args(self):
        if self.spec.satisfies("+rocm"):
            cxx = self.spec["hip"].hipcc
        else:
            cxx = self["kokkos"].kokkos_cxx

        args = [
            self.define("CMAKE_CXX_COMPILER", cxx),
            self.define_from_variant("BUILD_PYTHON_INTERFACE", "python"),
            self.define_from_variant("BUILD_FORTRAN_INTERFACE", "fortran"),
            self.define_from_variant("BUILD_TESTS", "tests"),
        ]

        if self.spec.satisfies("+python"):
            python = self.spec["python"].command.path
            args.append(self.define("Python_EXECUTABLE", python))

        # CMake drops the CUDA library directory from the RPATH as an nvcc implicit link
        # directory, so the CUDA libraries kokkos-kernels links would not be found at run
        # time. Linker flags reach every target, in the build tree and once installed.
        if self.spec.satisfies("+cuda"):
            rpath = " ".join(f"-Wl,-rpath,{d}" for d in self.spec["cuda"].libs.directories)
            for kind in ("EXE", "SHARED", "MODULE"):
                args.append(self.define(f"CMAKE_{kind}_LINKER_FLAGS", rpath))

        return args
