# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


def plugin_validator(pkg_name, variant_name, values):
    if values == ("none",):
        return
    for v in values:
        if v not in SingularityEos.plugins:
            raise InstallError(f"Unknown Singularity-EOS plugin '{v}'")


class SingularityEos(CMakePackage, CudaPackage, ROCmPackage):
    """Singularity-EOS: A collection of closure models and tools useful for
    multiphysics codes."""

    homepage = "https://lanl.github.io/singularity-eos/main/index.html"
    git = "https://github.com/lanl/singularity-eos.git"
    url = "https://github.com/lanl/singularity-eos/archive/refs/tags/release-1.6.1.tar.gz"

    maintainers("rbberger", "Yurlungur")

    license("BSD-3-Clause")

    version("main", branch="main")
    version("1.12.0", commit="e32a25bed7b73baa7a5684c0183d2c369e16693c", tag="release-1.12.0")
    version("1.11.1", commit="7365053a5bd59839ac47e6133426620540aca7e3", tag="release-1.11.1")
    version("1.11.0", commit="c996f6505161618f9ca9663942e0beef738b0ecc", tag="release-1.11.0")
    version("1.10.0", commit="82df6cff9ca8b16f8468f20b9d1eaeff60ac53c7", tag="release-1.10.0")
    version("1.9.2", commit="9e7de3eccd610e0654e9a05d673ef7b24d32cf31", tag="release-1.9.2")
    version("1.9.1", commit="1be18426a2c9c26f969bc14a73b482d5beca0217", tag="release-1.9.1")
    version("1.9.0", commit="cfb7d4bf9fac557d53793a6717e52377b586d77a", tag="release-1.9.0")
    version("1.8.0", commit="4f363a371f4896f3304fdc1f5facd52d8a9718c1", tag="release-1.8.0")
    version("1.7.0", commit="b5d7d8cd5c8525cc9d51a71102a645b9c1df6d6e", tag="release-1.7.0")

    # build with kokkos, kokkos-kernels for offloading support
    variant("kokkos", default=False, description="Enable kokkos")
    variant(
        "kokkos-kernels", default=False, description="Enable kokkos-kernels for linear algebra"
    )

    # for compatibility with downstream projects
    variant("mpi", default=False, description="Build with MPI support")

    # build converters for sesame, stellarcollapse eos's
    variant(
        "build_extra",
        description="Build converters",
        values=any_combination_of("sesame", "stellarcollapse").with_default("none"),
    )

    # build the Fortran interface
    variant("fortran", default=True, description="Enable building fortran interface")

    # build the Python bindings
    variant("python", default=False, description="Enable building Python bindings")

    variant("eospac", default=True, description="Enable EOSPAC for table reads")

    variant("hdf5", default=False, description="Enable HDF5 support")

    variant("spiner", default=True, description="Use Spiner")

    variant("closure", default=True, description="Build closure module")
    variant("shared", default=False, description="Build shared libs")
    variant("vandv", default=True, description="Enable V&V EOSs in default Singularity::Variant")

    plugins = {"dust": ("self", "example/plugin")}

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    variant(
        "plugins",
        multi=True,
        default="none",
        validator=plugin_validator,
        description="list of plugins to build",
        when="@1.9.0:",
    )
    variant(
        "variant",
        default="default",
        description="include path used for variant header",
        when="@1.9.0:",
    )

    # building/testing/docs
    depends_on("cmake@3.19:", type="build")
    depends_on("python@3:", when="+python")
    depends_on("py-pybind11@2.9.1:", when="+python")
    depends_on("catch2@2.13.7", when="@:1.8.0", type="test")
    depends_on("catch2@3.0.1:", when="@1.9.0:", type="test")
    depends_on("py-numpy", type="test")

    # Require kokkos for device/offloading support
    requires("+kokkos", when="+cuda")
    requires("+kokkos", when="+rocm")

    # linear algebra when using closure models. Eigen without kokkos
    depends_on("eigen@3.3.8:", when="~kokkos-kernels+closure")
    requires("+kokkos-kernels", when="+kokkos+closure")

    # test_pte fails on AMD MI300 for versions of llvm < 19
    # rocm 6.4 is the first version of rocm that depends on llvm >= 19
    depends_on("hip@6.4:", when="+rocm")

    depends_on("eospac", when="+eospac")

    depends_on("ports-of-call@1.4.2,1.5.2:", when="@:1.7.0")
    depends_on("ports-of-call@1.5.2:", when="@1.7.1:")
    depends_on("ports-of-call@1.6.0:", when="@1.9.0:")
    depends_on("ports-of-call@2.0.0:", when="@1.11.0:")
    depends_on("ports-of-call@3.0.0:", when="@1.12.0:")
    depends_on("ports-of-call@main", when="@main")

    depends_on("spiner +kokkos", when="+kokkos+spiner")
    depends_on("spiner +hdf5", when="+hdf5+spiner")

    depends_on("spiner@:1.6.0", when="@:1.7.0 +spiner")
    depends_on("spiner@1.6.1:", when="@1.7.1:1.9.0 +spiner")
    depends_on("spiner@1.6.3:", when="@1.9.1: +spiner")
    depends_on("spiner@main", when="@main +spiner")

    depends_on("mpark-variant", when="@:1.10")
    depends_on(
        "mpark-variant",
        patches=patch(
            "https://raw.githubusercontent.com/lanl/singularity-eos/b6ae9bac37fca51854c8da7a699577c9932188e8/utils/gpu_compatibility.patch",
            sha256="592e64ceccd2822ec1cc7eb01ac3fcad620551940beab793003afb6b5366dad8",
        ),
        when="@:1.10 +cuda",
    )
    depends_on(
        "mpark-variant",
        patches=patch(
            "https://raw.githubusercontent.com/lanl/singularity-eos/b6ae9bac37fca51854c8da7a699577c9932188e8/utils/gpu_compatibility.patch",
            sha256="592e64ceccd2822ec1cc7eb01ac3fcad620551940beab793003afb6b5366dad8",
        ),
        when="@:1.10 +rocm",
    )
    depends_on("binutils@:2.39,2.42:+ld", when="build_type=Debug")
    depends_on("binutils@:2.39,2.42:+ld", when="build_type=RelWithDebInfo")

    for _myver, _kver in zip(("@:1.6.2", "@1.7.0:", "@1.12.0:"), ("@3.2:", "@3.3:", "@4.7:")):
        depends_on(f"kokkos{_kver}", when=f"{_myver}+kokkos")
        depends_on(f"kokkos-kernels{_kver}", when=f"{_myver}+kokkos-kernels")

    # set up kokkos offloading dependencies
    for _flag in ("~cuda", "+cuda", "~rocm", "+rocm"):
        depends_on("kokkos" + _flag, when="+kokkos" + _flag)

    for _flag in ("~cuda", "+cuda"):
        depends_on("kokkos-kernels" + _flag, when="+kokkos-kernels" + _flag)

    depends_on("kokkos+pic", when="+kokkos-kernels")
    depends_on("kokkos+cuda_lambda", when="+cuda+kokkos")

    for _flag in list(CudaPackage.cuda_arch_values):
        depends_on("kokkos cuda_arch=" + _flag, when="+cuda+kokkos cuda_arch=" + _flag)
        depends_on("kokkos-kernels cuda_arch=" + _flag, when="+cuda+kokkos cuda_arch=" + _flag)

    for _flag in ROCmPackage.amdgpu_targets:
        depends_on("kokkos amdgpu_target=" + _flag, when="+rocm+kokkos amdgpu_target=" + _flag)

    conflicts("cuda_arch=none", when="+cuda", msg="CUDA architecture is required")
    conflicts("amdgpu_target=none", when="+rocm", msg="ROCm architecture is required")

    # these are mirrored in the cmake configuration
    conflicts("+hdf5", when="~spiner")

    conflicts("+fortran", when="~closure")

    # NOTE: these are set so that dependencies in downstream projects share
    # common MPI dependence
    for _flag in ("~mpi", "+mpi"):
        depends_on("hdf5~cxx+hl" + _flag, when="+hdf5" + _flag)
        depends_on("py-h5py" + _flag, when="@:1.6.2 " + _flag)

    # can be removed once <1.8.0 versions have been removed
    def flag_handler(self, name, flags):
        if name == "fflags":
            if self.spec.satisfies("+fortran%cce"):
                # The Cray fortran compiler generates module files with
                # uppercase names by default, which is not handled by the
                # CMake scripts. The following flag forces the compiler to
                # produce module files with lowercase names.
                flags.append("-ef")
        return (flags, None, None)

    def cmake_args(self):
        args = [
            self.define("SINGULARITY_PATCH_MPARK_VARIANT", False),
            self.define_from_variant("SINGULARITY_USE_CUDA", "cuda"),
            self.define_from_variant("SINGULARITY_USE_KOKKOS", "kokkos"),
            self.define_from_variant("SINGULARITY_USE_KOKKOSKERNELS", "kokkos-kernels"),
            self.define_from_variant("SINGULARITY_USE_FORTRAN", "fortran"),
            self.define_from_variant("SINGULARITY_BUILD_CLOSURE", "closure"),
            self.define_from_variant("SINGULARITY_BUILD_PYTHON", "python"),
            self.define_from_variant("SINGULARITY_USE_SPINER", "spiner"),
            self.define_from_variant("SINGULARITY_USE_SPINER_WITH_HDF5", "hdf5"),
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("SINGULARITY_USE_V_AND_V_EOS", "vandv"),
            self.define("SINGULARITY_BUILD_TESTS", self.run_tests),
            self.define(
                "SINGULARITY_BUILD_SESAME2SPINER",
                "sesame" in self.spec.variants["build_extra"].value,
            ),
            self.define(
                "SINGULARITY_TEST_SESAME",
                ("sesame" in self.spec.variants["build_extra"].value and self.run_tests),
            ),
            self.define(
                "SINGULARITY_BUILD_STELLARCOLLAPSE2SPINER",
                "stellarcollapse" in self.spec.variants["build_extra"].value,
            ),
            self.define(
                "SINGULARITY_TEST_STELLAR_COLLAPSE",
                ("stellarcollapse" in self.spec.variants["build_extra"].value and self.run_tests),
            ),
            self.define("SINGULARITY_TEST_PYTHON", ("+python" in self.spec and self.run_tests)),
            self.define_from_variant("SINGULARITY_USE_HDF5", "hdf5"),
            self.define_from_variant("SINGULARITY_USE_EOSPAC", "eospac"),
        ]

        if self.spec.satisfies("@1.9.0:"):
            if "none" not in self.spec.variants["plugins"].value:
                pdirs = []
                for p in self.spec.variants["plugins"].value:
                    spackage, path = self.plugins[p]
                    if spackage == "self":
                        pdirs.append(join_path(self.stage.source_path, path))
                    else:
                        pdirs.append(join_path(self.spec[spackage].prefix, path))
                args.append(self.define("SINGULARITY_PLUGINS", ";".join(pdirs)))

            variant_path = self.spec.variants["variant"].value
            if variant_path != "default":
                parts = os.path.normpath("variant_path").split(os.sep)
                if parts[0] in self.plugins.keys():
                    spackage, path = self.plugins[parts[0]]
                    parts[0] = self.spec[spackage].prefix
                    variant_path = join_path(*parts)
                args.append(self.define("SINGULARITY_VARIANT", variant_path))

        if "+rocm" in self.spec:
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
            args.append(self.define("CMAKE_C_COMPILER", self.spec["hip"].hipcc))
        if "+kokkos+cuda" in self.spec:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        if "+kokkos" in self.spec:
            args.append(
                self.define("CMAKE_CXX_STANDARD", self.spec["kokkos"].variants["cxxstd"].value)
            )

        return args

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        if os.path.isdir(self.prefix.lib64):
            lib_dir = self.prefix.lib64
        else:
            lib_dir = self.prefix.lib

        if "+python" in self.spec:
            python_version = self.spec["python"].version.up_to(2)
            python_inst_dir = join_path(
                lib_dir, "python{0}".format(python_version), "site-packages"
            )
            env.prepend_path("PYTHONPATH", python_inst_dir)
