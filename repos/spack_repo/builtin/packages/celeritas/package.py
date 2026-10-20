# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Celeritas(CMakePackage, CudaPackage, ROCmPackage):
    """Celeritas is a new Monte Carlo transport code designed for
    high-performance (GPU-targeted) simulation of high-energy physics
    detectors.
    """

    homepage = "https://github.com/celeritas-project/celeritas"
    git = "https://github.com/celeritas-project/celeritas.git"
    url = "https://github.com/celeritas-project/celeritas/releases/download/v0.1.0/celeritas-0.1.0.tar.gz"

    maintainers("sethrj", "drbenmorgan")

    license("Apache-2.0")

    sanity_check_is_file = ["bin/celer-sim"]

    version("develop", branch="develop", get_full_repo=True)

    version("0.7.0", sha256="e48cf616bf662afede88951306c5806c97b1d1acb2be2cce91ddccc9ef076c4f")
    version("0.6.3", sha256="c87910acd0bb9dc85c53e2e4d9958f36d3bb1e5975f0e08fe7274b332a2ccf27")
    version("0.6.2", sha256="efca5a7f4797cd29d2b4e0b2251896b9fe4253ed95ff5c18f4d0476d4c34b48d")
    version("0.6.1", sha256="fe97cdb87e579559c29a0366058327243945bf2a0e25aac4d562c8fe0c672c2a")
    version("0.6.0", sha256="c776dee357ecff42f85ed02c328f24b092400af28e67af2c0e195ce8f67613b0")
    version("0.5.3", sha256="4d1fe1f34e899c3599898fb6d44686d2582a41b0872784514aa8c562597b3ee6")
    version("0.5.2", sha256="46311c096b271d0331b82c02485ac6bf650d5b0f7bd948fb01aef5058f8824e3")
    version("0.5.1", sha256="182d5466fbd98ba9400b343b55f6a06e03b77daed4de1dd16f632ac0a3620249")
    version(
        "0.5.0",
        sha256="4a8834224d96fd01897e5872ac109f60d91ef0bd7b63fac05a73dcdb61a5530e",
        deprecated=True,
    )
    version(
        "0.4.4",
        sha256="8b5ae63aa2d50c2ecf48d752424e4a33c50c07d9f0f5ca5448246de3286fd836",
        deprecated=True,
    )

    _cxxstd_values = ("17", "20")

    # Note: cuda and rocm variants are defined by mixin classes
    variant(
        "cxxstd",
        default="17",
        values=_cxxstd_values,
        multi=False,
        description="C++ standard version",
    )
    variant("covfie", default=True, when="@0.6:", description="Enable covfie magnetic fields")
    variant("debug", default=False, description="Enable runtime debug assertions")
    variant("dd4hep", default=False, when="@0.7:", description="Enable dd4hep plugin")
    variant("doc", default=False, description="Build and install documentation")
    variant("geant4", default=True, description="Enable Geant4 integration")
    variant("hepmc3", default=True, description="Use HepMC3 I/O interfaces")
    variant("openmp", default=False, description="Use OpenMP multithreading")
    variant("perfetto", default=False, when="@0.5:", description="Use Perfetto profiling")
    variant("root", default=False, description="Use ROOT I/O")
    variant("shared", default=True, description="Build shared libraries")
    variant("swig", default=False, when="@:0.4", description="Generate SWIG Python bindings")
    variant("vecgeom", default=True, description="Use VecGeom geometry")

    depends_on("cxx", type="build")

    depends_on("cmake@3.22:", type="build")
    depends_on("cmake@3.27:", type="build", when="+covfie")

    # FIXME: precompiled required due to IWYU errors from transitive includes
    depends_on("cli11~precompiled", when="@0.6:")
    depends_on("nlohmann-json")
    depends_on("covfie@0.13:", when="+covfie")
    depends_on("dd4hep +ddg4", when="+dd4hep")
    depends_on("g4vg@1.0.2:", when="@0.6: +geant4 +vecgeom")
    depends_on("hepmc3", when="+hepmc3")
    depends_on("root@6.28:", when="+root")
    depends_on("swig@4.1:", when="+swig")

    depends_on("python", when="@:0.5", type="build")
    depends_on("python", type="test")

    with default_args(when="+doc", type="build"):
        depends_on("doxygen")
        depends_on("python")
        depends_on("py-breathe")
        depends_on("py-sphinx")

    with when("+cuda"):
        depends_on("thrust")
        depends_on("cub", when="@0.7:")

    with when("+rocm"):
        depends_on("hiprand")
        depends_on("hipcub", when="@0.7:")
        depends_on("rocprim")
        depends_on("rocrand")
        depends_on("rocthrust")

    with when("+geant4"):
        depends_on("geant4@10.5:", when="@0.7:")
        depends_on("geant4@10.5:11.3", when="@0.5:0.6")
        depends_on("geant4@10.5:11.2", when="@0.4.2:0.4")

    with when("+vecgeom"):
        depends_on("vecgeom@1.2:1,2.2:", when="@0.7:")
        depends_on("vecgeom@1.2:1", when="@:0.6")

    # Ensure consistent C++ standards
    for _std in _cxxstd_values:
        for _pkg in ["geant4", "root", "vecgeom"]:
            depends_on(f"{_pkg} cxxstd={_std}", when=f"+{_pkg} cxxstd={_std}")
        # NOTE: as a private dependency, covfie cxxstd can differ from the
        # celeritas "public" standard

    # Ensure consistent CUDA architectures
    conflicts("cuda_arch=none", when="+cuda", msg="Accelerator hardware choice is required")
    for _pkg in ["covfie", "vecgeom"]:
        depends_on(f"{_pkg} ~cuda", when=f"+{_pkg} ~cuda")  # May be technically too strict
        depends_on(f"{_pkg} +cuda", when=f"+{_pkg} +cuda")
        for _arch in CudaPackage.cuda_arch_values:
            depends_on(f"{_pkg} cuda_arch={_arch}", when=f"+{_pkg} cuda_arch={_arch}")

    conflicts("+rocm ^hip@:5", when="@0.7:", msg="HIP API inconsistency: to be patched shortly")
    conflicts("+rocm", when="+cuda", msg="AMD and NVIDIA accelerators are incompatible")
    conflicts("+rocm", when="+vecgeom", msg="HIP support is only available with ORANGE")
    for _arch in ["cuda", "rocm"]:
        conflicts("+perfetto", when=f"+{_arch}", msg="Perfetto is only used for CPU profiling")

    # geant4@11.3.0 now returns const G4Element::GetElementTable()
    patch(
        "https://github.com/celeritas-project/celeritas/commit/3c8ed9614fc695fba35e8a058bedb7bc1556f71c.patch?full_index=1",
        sha256="1161c4f1166860d35d2a3f103236a63acd6a35aee2d2c27561cb929941d1c170",
        when="@0.5.0 +geant4 ^geant4@11.3.0:",
    )
    # CUDA 13 API change: removed clockRate and memoryClockRate
    patch(
        "https://github.com/celeritas-project/celeritas/commit/71221336cc3fc4232eda4b5b96fc5079a4193d86.patch?full_index=1",
        sha256="cc44c5d6d8fb371ff3d42e13521eb0752780715e9d070b46699633ca3cd7e995",
        when="@:0.6.2 +cuda ^cuda@13:",
    )

    def celeritas_use_list(self) -> List[str]:
        """This is extensible so that downstream subclasses (FNAL spack) can add
        other packages that mainstream Spack does not know about.
        """
        return [
            "covfie",
            "CUDA",
            "DD4hep",
            "Geant4",
            "HepMC3",
            "OpenMP",
            "Perfetto",
            "ROOT",
            "SWIG",
            "VecGeom",
        ]

    def cmake_args(self):
        define = self.define
        from_variant = self.define_from_variant
        args = [
            from_variant("BUILD_SHARED_LIBS", "shared"),
            from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            from_variant("CELERITAS_DEBUG", "debug"),
            from_variant("CELERITAS_BUILD_DOCS", "doc"),
            define("CELERITAS_BUILD_TESTS", False),
            from_variant("CELERITAS_USE_HIP", "rocm"),
            define("CELERITAS_USE_MPI", False),
        ]

        # NOTE: package names are stylized like the dependency asks: Find{pkg}.cmake
        for pkg in self.celeritas_use_list():
            args.append(from_variant("CELERITAS_USE_" + pkg, pkg.lower()))

        if self.spec.satisfies("+cuda"):
            args.append(CMakeBuilder.define_cuda_architectures(self))
        if self.spec.satisfies("+rocm"):
            args.append(CMakeBuilder.define_hip_architectures(self))
            # TODO: update celeritas CMakeLists to link to these if found
            rocm_pkg_list = ["hiprand", "rocprim", "rocrand", "rocthrust"]
            if self.spec.satisfies("@0.7:"):
                rocm_pkg_list.append("hipcub")
            args.append(
                define(
                    "CMAKE_HIP_FLAGS",
                    " ".join([f"-I{self.spec[p].prefix.include}" for p in rocm_pkg_list]),
                )
            )

        if self.spec.satisfies("@:0.4"):
            # Explicitly activate JSON for older versions
            args.append(define("CELERITAS_USE_JSON", True))

        if self.spec.satisfies("@:0.6"):
            args.extend(
                [
                    define("CELERITAS_BUILD_DEMOS", False),
                    define("CELERITAS_USE_Python", True),
                ]
            )

        if self.spec.satisfies("@0.6:"):
            # Protect against accidentally using vendored instead of spack
            args.extend(
                define(f"CELERITAS_BUILTIN_{pkg}", False)
                for pkg in ["covfie", "CLI11", "GTest", "nlohmann_json", "G4VG"]
            )
            # NOTE: Perfetto is always vendored!

        return args

    @when("+dd4hep")
    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("Celeritas_ROOT", self.prefix)
        env.prepend_path(
            self.spec["dd4hep"].package.plugin_path_var, self.spec["celeritas"].libs.directories[0]
        )
