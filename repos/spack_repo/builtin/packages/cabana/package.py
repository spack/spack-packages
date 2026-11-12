# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage
from spack_repo.builtin.packages.kokkos.package import Kokkos

from spack.package import *


class Cabana(CMakePackage, CudaPackage, ROCmPackage):
    """The Exascale Co-Design Center for Particle Applications Toolkit"""

    homepage = "https://github.com/ECP-copa/Cabana"
    git = "https://github.com/ECP-copa/Cabana.git"
    url = "https://github.com/ECP-copa/Cabana/archive/0.7.0.tar.gz"

    maintainers("junghans", "streeve", "sslattery")

    tags = ["e4s", "ecp"]

    version("master", branch="master")
    version("0.8.0", sha256="1399145d4fbfe5d4ac569540e97d3609053d333a12b3b3882dcb5dc488767907")
    version("0.7.0", sha256="3d46532144ea9a3f36429a65cccb7562d1244f1389dd8aff0d253708d1ec9838")
    version("0.6.1", sha256="fea381069fe707921831756550a665280da59032ea7914f7ce2a01ed467198bc")
    version("0.6.0", sha256="a88a3f80215998169cdbd37661c0c0af57e344af74306dcd2b61983d7c69e6e5")
    version("0.5.0", sha256="b7579d44e106d764d82b0539285385d28f7bbb911a572efd05c711b28b85d8b1")
    version("0.4.0", sha256="c347d23dc4a5204f9cc5906ccf3454f0b0b1612351bbe0d1c58b14cddde81e85")
    version("0.3.0", sha256="fb67ab9aaf254b103ae0eb5cc913ddae3bf3cd0cf6010e9686e577a2981ca84f")

    # Copy kokkos backends (cuda, openmp, serial, rocm, ...) as variants
    _kokkos_backends = Kokkos.devices_variants
    for _backend in _kokkos_backends:
        _deflt, _when, _descr = _kokkos_backends[_backend]
        if _when is not None:
            _when = f"^kokkos{_when}"
        variant(_backend.lower(), default=_deflt, description=_descr, when=_when)

    variant("shared", default=True, description="Build shared libraries")
    variant("mpi", default=True, description="Build with mpi support")
    variant("all", default=False, description="Build with ALL support")
    variant("arborx", default=False, description="Build with ArborX support")
    variant("heffte", default=False, description="Build with heFFTe support", when="@0.5:")
    variant("hypre", default=False, description="Build with HYPRE support")
    variant("silo", when="@0.4:", default=False, description="Build with SILO support")
    variant("hdf5", when="@0.6: +mpi", default=False, description="Build with HDF5 support")
    variant("cajita", when="@:0.5 +mpi", default=False, description="Build Cajita subpackage")
    variant("grid", when="@0.6: +mpi", default=False, description="Build Grid subpackage")
    variant("testing", default=False, description="Build unit tests")
    variant("examples", default=False, description="Build tutorial examples")
    variant("performance_testing", default=False, description="Build performance tests")

    depends_on("c", type="build", when="+mpi")
    depends_on("cxx", type="build")

    depends_on("cmake@3.9:", type="build", when="@:0.4.0")
    depends_on("cmake@3.16:", type="build", when="@0.5.0:")

    depends_on("googletest", type="build", when="+testing")

    depends_on("kokkos@3.1:4.6", when="@0.3")
    depends_on("kokkos@3.2:4.6", when="@0.4:0.5")
    depends_on("kokkos@3.7:4.6", when="@0.6:0.7")
    depends_on("kokkos@4.1:4.6", when="@0.8.0")
    depends_on("kokkos@4.1:", when="@0.8.1:")

    for _backend in _kokkos_backends:
        depends_on(f"kokkos~{_backend}", when=f"~{_backend}")
        depends_on(f"kokkos+{_backend}", when=f"+{_backend}")

    # Propagate cuda architectures down to Kokkos and optional submodules
    for _arch in CudaPackage.cuda_arch_values:
        cuda_dep = f"cuda_arch={_arch}"
        depends_on(f"kokkos {cuda_dep}", when=cuda_dep)
        depends_on(f"heffte {cuda_dep}", when=f"+heffte {cuda_dep}")
        depends_on(f"arborx {cuda_dep}", when=f"+arborx {cuda_dep}")
        depends_on(f"hypre {cuda_dep}", when=f"+hypre {cuda_dep}")

    for _arch in ROCmPackage.amdgpu_targets:
        rocm_dep = f"amdgpu_target={_arch}"
        depends_on(f"kokkos {rocm_dep}", when=rocm_dep)
        depends_on(f"heffte {rocm_dep}", when=f"+heffte {rocm_dep}")
        depends_on(f"arborx {rocm_dep}", when=f"+arborx {rocm_dep}")
        depends_on(f"hypre {rocm_dep}", when=f"+hypre {rocm_dep}")

    # https://github.com/ECP-copa/Cabana/releases/tag/0.7.0
    depends_on("kokkos@3.7: +cuda_lambda", when="@:0.6 +cuda")
    depends_on("kokkos@4.1: +cuda_lambda", when="@0.7: +cuda")

    # Dependencies for subpackages
    depends_on("all-library", when="@0.5.0:+all")
    depends_on("arborx", when="+arborx @0.8:")
    depends_on("arborx@1.7", when="+arborx @:0.7.0")
    depends_on("hypre-cmake@2.22.0:", when="@0.4.0 +hypre")
    depends_on("hypre-cmake@2.22.1:", when="@0.5.0:0.7.0 +hypre")
    depends_on("hypre@3.0.0:", when="@0.8.0:+hypre")
    depends_on("heffte@2.1.0", when="@0.5.0+heffte")
    depends_on("heffte@2.3.0:", when="@0.6.0:+heffte")
    depends_on("silo", when="@0.5.0:+silo")
    depends_on("hdf5", when="@0.6.0:+hdf5")
    depends_on("mpi", when="+mpi")

    # Hardware targets are required for GPU builds
    conflicts("+cuda", when="cuda_arch=none")
    conflicts("+rocm", when="amdgpu_target=none")

    # The +grid does not support gcc>=13 (missing iostream/cstdint includes):
    conflicts("+grid", when="@:0.6 %gcc@13:")

    # Conflict variants only available in newer versions of cabana
    conflicts("+sycl", when="@:0.3.0")

    # Hypre doesn't support rocm for older versions
    conflicts("+hypre +rocm", when="@:0.7.0")

    @when("+mpi")
    def patch(self):
        # CMakeLists.txt tries to enable C when MPI is requsted, but too late:
        filter_file("LANGUAGES CXX", "LANGUAGES C CXX", "CMakeLists.txt")

    def cmake_args(self):
        options = [self.define_from_variant("BUILD_SHARED_LIBS", "shared")]

        enable = ["TESTING", "EXAMPLES", "PERFORMANCE_TESTING"]
        require = ["ALL", "ARBORX", "HEFFTE", "HYPRE", "SILO", "HDF5"]

        # MPI was changed from ENABLE to REQUIRE in 0.4.0
        if self.spec.satisfies("@:0.3.0"):
            enable.append("MPI")
        else:
            require.append("MPI")

        # Cajita was renamed Grid in 0.6
        if self.spec.satisfies("@0.6.0:"):
            enable.append("GRID")
        else:
            enable.append("CAJITA")

        for category, cname in zip([enable, require], ["ENABLE", "REQUIRE"]):
            for var in category:
                cbn_option = f"Cabana_{cname}_{var}"
                options.append(self.define_from_variant(cbn_option, var.lower()))

        # Attempt to disable find_package() calls for disabled options(if option supports it):
        for var in require:
            if not self.spec.satisfies("+" + var.lower()):
                options.append(self.define("CMAKE_DISABLE_FIND_PACKAGE_" + var, "ON"))

        # Use hipcc for HIP.
        if self.spec.satisfies("+rocm"):
            options.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))

        return options
