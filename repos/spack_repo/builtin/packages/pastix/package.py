# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Pastix(CMakePackage, CudaPackage):
    """a high performance parallel solver for very large sparse linear systems
    based on direct methods"""

    homepage = "https://gitlab.inria.fr/solverstack/pastix/blob/master/README.md"
    url = "https://files.inria.fr/pastix/releases/v6/pastix-6.4.0.tar.gz"
    git = "https://gitlab.inria.fr/solverstack/pastix.git"
    maintainers("fpruvost", "mfaverge", "ramet")

    version("master", branch="master", submodules=True)
    version("6.4.0", sha256="891d426188eed56c1075fb34d2d80132593a1536ffc05cf333567f68a4811e55")
    version("6.3.2", sha256="c4da8802d1933eecf8c09d7e63c014c81ccf353fe623142e9f5c5fc65ed82ee0")
    version("6.3.1", sha256="290464d73b7d43356e4735a29932bf6f23a88e94ec7139ba7744c21e42c52681")
    version("6.3.0", sha256="a6bfec32a3279d7b24c5fc05885c6632d177e467f1584707c6fd7c42a8703c3e")
    version("6.2.2", sha256="cce9a1fe4678b5733c9f1a5a52f77b040eadc3e254418c6fb03d8ab37dede508")
    version("6.2.1", sha256="b680cbfc265df8cba18d3a7093fcc02e260198c4a2d6a86d1e684bb291e309dd")

    # cmake's specific
    variant("shared", default=True, description="Build Pastix as a shared library")

    # pastix's specific
    variant("doc", default=False, description="Enable documentation")
    variant("int64", default=False, description="To use 64 bits integers")
    variant("metis", default=False, description="Enable Metis")
    variant("scotch", default=True, description="Enable Scotch")
    variant(
        "runtime",
        default="none",
        description="Runtime support",
        values=("none", "starpu"),
        multi=False,
    )
    variant("cuda", default=False, when="runtime=starpu", description="Enable CUDA")
    variant("mpi", default=False, description="Enable MPI")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    # Dependencies
    depends_on("pkgconfig", type="build")
    depends_on("hwloc")
    depends_on("lapack")
    # ensure openblas use threads=openmp to be thread-safe
    depends_on("openblas threads=openmp", when="^[virtuals=lapack] openblas")
    with when("+metis"):
        depends_on("metis@5.1:")
        depends_on("metis@5.1:+int64", when="+int64")
    depends_on("scotch~int64", when="@=6.4.0~int64+scotch+cuda runtime=starpu")
    with when("+scotch"):
        depends_on("scotch~metis")
        depends_on("scotch~metis+int64", when="+int64")
        depends_on("scotch~metis~mpi", when="~mpi")
    with when("runtime=starpu"):
        depends_on("starpu")
        depends_on("starpu~mpi", when="~mpi")
        depends_on("starpu+mpi", when="+mpi")
        depends_on("starpu~cuda", when="~cuda")
        depends_on("starpu+cuda", when="+cuda")
        depends_on("cuda", when="+cuda")
    depends_on("mpi", when="+mpi")

    def cmake_args(self):
        spec = self.spec

        args = [
            "-Wno-dev",
            self.define("CMAKE_COLOR_MAKEFILE", "ON"),
            self.define("CMAKE_VERBOSE_MAKEFILE", "ON"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("PASTIX_INT64", "int64"),
            self.define_from_variant("PASTIX_ORDERING_METIS", "metis"),
            self.define_from_variant("PASTIX_ORDERING_SCOTCH", "scotch"),
            self.define("PASTIX_WITH_PARSEC", "OFF"),
            self.define_from_variant("PASTIX_WITH_MPI", "mpi"),
        ]

        if spec.satisfies("runtime=starpu"):
            args.extend([self.define("PASTIX_WITH_STARPU", "ON")])
            args.extend([self.define_from_variant("PASTIX_WITH_CUDA", "cuda")])

        if spec.satisfies("^[virtuals=lapack] intel-oneapi-mkl"):
            args.extend([self.define("BLA_VENDOR", "Intel10_64lp_seq")])
        elif spec.satisfies("^[virtuals=lapack] netlib-lapack"):
            args.extend([self.define("BLA_VENDOR", "Generic")])
        elif spec.satisfies("^[virtuals=lapack] openblas"):
            args.extend([self.define("BLA_VENDOR", "OpenBLAS")])

        if spec.satisfies("+mpi"):
            args.extend(
                [
                    self.define("MPI_C_COMPILER", self.spec["mpi"].mpicc),
                    self.define("MPI_CXX_COMPILER", self.spec["mpi"].mpicxx),
                    self.define("MPI_Fortran_COMPILER", self.spec["mpi"].mpifc),
                ]
            )

        if spec.satisfies("@=6.4.0~int64+cuda runtime=starpu ^openblas~ilp64"):
            blas = spec["openblas"].prefix
            args.extend(
                [
                    self.define("BLA_SIZEOF_INTEGER", 4),
                    self.define("BLA_PREFER_PKGCONFIG", True),
                    self.define("BLA_PKGCONFIG_BLAS", "openblas"),
                    self.define("BLA_PKGCONFIG_LAPACK", "openblas"),
                    self.define("CBLAS_DIR", blas),
                    self.define("LAPACKE_DIR", blas),
                ]
            )
            flags = [
                f"-gencode=arch=compute_{arch},code=sm_{arch}"
                for arch in spec.variants["cuda_arch"].value
                if arch != "none"
            ]
            # FindCUDA's separate device link also produces a shared-library host object.
            args.append(self.define("CUDA_NVCC_FLAGS", flags + ["-Xcompiler=-fPIC"]))
        return args
