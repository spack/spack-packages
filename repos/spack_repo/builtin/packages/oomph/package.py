# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Oomph(CMakePackage):
    """Oomph is a library for enabling high performance point-to-point,
    asynchronous communication over different fabrics"""

    homepage = "https://github.com/ghex-org/oomph"
    url = "https://github.com/ghex-org/oomph/archive/refs/tags/v0.0.0.tar.gz"
    git = "https://github.com/ghex-org/oomph.git"

    maintainers("boeschf", "msimberg")

    license("BSD-3-Clause", checked_by="msimberg")

    version("main", branch="main")
    version("0.5.0", sha256="4c79ff50d14efcde7ce4d14122714efb16443ccff437ab60973cf1db1032fc3d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran-bindings")

    generator("ninja")

    depends_on("ninja", type="build")

    variant("cuda", default=False, description="Enable CUDA support")
    variant("rocm", default=False, description="Enable ROCm support")

    backends = ("mpi", "ucx", "libfabric")
    variant(
        "backend", default="mpi", description="Transport backend", values=backends, multi=False
    )

    variant("fortran-bindings", default=False, description="Build Fortran bindings")
    with when("+fortran-bindings"):
        variant(
            "fortran-fp",
            default="float",
            description="Floating point type",
            values=("float", "double"),
            multi=False,
        )
        variant("fortran-openmp", default=True, description="Compile with OpenMP")

    variant(
        "enable-barrier",
        default=True,
        description="Enable thread barrier (disable for task based runtime)",
    )

    depends_on("cmake@3.17:", type="build")
    depends_on("googletest", type="test")
    depends_on("hwmalloc")
    depends_on("hwmalloc+cuda", when="+cuda")
    depends_on("hwmalloc+rocm", when="+rocm")
    depends_on("hwmalloc~rocm~cuda", when="~rocm~cuda")
    depends_on("cuda", when="+cuda")
    depends_on("hip", when="+rocm")

    conflicts("+cuda +rocm", msg="CUDA and ROCm support are mutually exclusive")

    with when("backend=ucx"):
        depends_on("ucx+thread_multiple")
        depends_on("ucx+cuda", when="+cuda")
        depends_on("ucx+rocm", when="+rocm")
        variant("use-pmix", default="False", description="Use PMIx to establish out-of-band setup")
        variant("use-spin-lock", default="False", description="Use pthread spin locks")
        depends_on("pmix", when="+use-pmix")

    libfabric_providers = ("cxi", "efa", "gni", "psm2", "tcp", "verbs")
    with when("backend=libfabric"):
        variant(
            "libfabric-provider",
            default="tcp",
            description="fabric",
            values=libfabric_providers,
            multi=False,
        )
        for provider in libfabric_providers:
            depends_on(f"libfabric fabrics={provider}", when=f"libfabric-provider={provider}")

    depends_on("mpi")
    depends_on("boost+thread")

    def cmake_args(self):
        args = [
            self.define_from_variant("OOMPH_BUILD_FORTRAN", "fortran-bindings"),
            self.define_from_variant("OOMPH_FORTRAN_OPENMP", "fortran-openmp"),
            self.define_from_variant("OOMPH_UCX_USE_PMI", "use-pmix"),
            self.define_from_variant("OOMPH_UCX_USE_SPIN_LOCK", "use-spin-lock"),
            self.define_from_variant("OOMPH_ENABLE_BARRIER", "enable-barrier"),
            self.define("OOMPH_WITH_TESTING", self.run_tests),
            self.define("OOMPH_GIT_SUBMODULE", False),
            self.define("OOMPH_USE_BUNDLED_LIBS", False),
        ]

        if self.run_tests and self.spec.satisfies("^mpi=openmpi"):
            args.append(self.define("MPIEXEC_PREFLAGS", "--oversubscribe"))

        if self.spec.satisfies("+fortran-bindings"):
            args.append(self.define("OOMPH_FORTRAN_FP", self.spec.variants["fortran-fp"].value))

        for backend in self.backends:
            args.append(
                self.define(
                    f"OOMPH_WITH_{backend.upper()}", self.spec.variants["backend"].value == backend
                )
            )

        if self.spec.satisfies("backend=libfabric"):
            args.append(
                self.define(
                    "OOMPH_LIBFABRIC_PROVIDER", self.spec.variants["libfabric-provider"].value
                )
            )

        return args
