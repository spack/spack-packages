# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Sphexa(CMakePackage, CudaPackage, ROCmPackage):
    """SPH and N-body simulation framework"""

    homepage = "https://github.com/sphexa-org/sphexa"
    url = "https://github.com/sphexa-org/sphexa/archive/v0.0.0.tar.gz"
    git = "https://github.com/sphexa-org/sphexa.git"
    maintainers("sekelle")

    license("MIT")

    version("0.95", sha256="1007ffa97eb2085d50173676ec5e6387d1da7a8b78f204308223fbdbbecc60a1")
    version("0.93.1", sha256="95a93d0063ac8857b9be12c1aca24f5b2eef9dd4ffe8cf3f6b552a4dd54b940f")
    version("develop", branch="develop")

    variant("testing", default=True, description="Enable unit and integration tests")
    variant("analytical", default=True, description="Enable analytical tests")
    variant("grackle", default=False, description="Enable radiative cooling with GRACKLE")
    variant("disks", default=False, description="Enable disk physics and propagator")

    variant("hdf5", default=True, description="Enable support for HDF5 I/O")
    variant("gpu_aware_mpi", default=True, description="GPU aware MPI")

    depends_on("cmake@3.22:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("mpi")
    depends_on("cuda@12:", when="@0.95: +cuda")
    depends_on("cuda@11.2:", when="@0.93: +cuda")
    depends_on("hip", when="+rocm")
    depends_on("rocthrust", when="+rocm")
    depends_on("hipcub", when="+rocm")
    depends_on("hdf5 +mpi", when="+hdf5")
    depends_on("h5hut@master", when="@0.95: +hdf5")

    # Build MPI with GPU support when GPU aware MPI is requested.
    # For cray-mpich, the user is responsible to configure it for GPU aware MPI.
    with when("+gpu_aware_mpi"):
        depends_on("openmpi +cuda", when="+cuda ^[virtuals=mpi] openmpi")
        depends_on("mpich +cuda", when="+cuda ^[virtuals=mpi] mpich")
        depends_on("mvapich-plus +cuda", when="+cuda ^[virtuals=mpi] mvapich-plus")

        depends_on("mpich +rocm", when="+rocm ^[virtuals=mpi] mpich")

    conflicts("%gcc@:11", when="@0.95:")
    conflicts("%gcc@:10", when="@:0.93.1")
    conflicts("cuda_arch=none", when="+cuda", msg="CUDA architecture is required")
    conflicts("amdgpu_target=none", when="+rocm", msg="HIP architecture is required")
    conflicts("+cuda", when="+rocm", msg="CUDA and HIP cannot both be enabled")

    def cmake_args(self):
        spec = self.spec

        hdf5lib = "H5HUT"
        if self.spec.satisfies("@:0.94"):
            hdf5lib = "H5PART"

        args = [
            self.define_from_variant("SPH_EXA_WITH_" + hdf5lib, "hdf5"),
            self.define_from_variant("BUILD_TESTING", "testing"),
            self.define_from_variant("BUILD_ANALYTICAL", "analytical"),
            self.define_from_variant("SPH_EXA_WITH_GRACKLE", "grackle"),
            self.define_from_variant("SPH_EXA_WITH_DISKS", "disks"),
            self.define_from_variant("SPH_EXA_WITH_H5HUT", "hdf5"),
            self.define_from_variant("SPH_EXA_WITH_CUDA", "cuda"),
            self.define_from_variant("RYOANJI_WITH_CUDA", "cuda"),
            self.define_from_variant("CSTONE_WITH_CUDA", "cuda"),
            self.define_from_variant("SPH_EXA_WITH_HIP", "rocm"),
            self.define_from_variant("RYOANJI_WITH_HIP", "rocm"),
            self.define_from_variant("CSTONE_WITH_HIP", "rocm"),
        ]
        # args.append('-DCMAKE_C_COMPILER=mpicc')
        # args.append('-DCMAKE_CXX_COMPILER=mpicxx')

        if spec.satisfies("+rocm") or spec.satisfies("+cuda"):
            args.append(self.define_from_variant("CSTONE_WITH_GPU_AWARE_MPI", "gpu_aware_mpi"))

        if spec.satisfies("+rocm"):
            archs = spec.variants["amdgpu_target"].value
            arch_str = ";".join(archs)
            args.append(self.define("CMAKE_HIP_ARCHITECTURES", arch_str))

        if spec.satisfies("+cuda"):
            args.append(self.define("CMAKE_CUDA_FLAGS", "-ccbin={0}".format(spec["mpi"].mpicxx)))
            archs = spec.variants["cuda_arch"].value
            arch_str = ";".join(archs)
            args.append(self.define("CMAKE_CUDA_ARCHITECTURES", arch_str))

        return args
