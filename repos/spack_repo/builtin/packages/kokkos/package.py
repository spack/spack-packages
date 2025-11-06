# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


class Kokkos(CMakePackage, CudaPackage, ROCmPackage):
    """Kokkos implements a programming model in C++ for writing performance
    portable applications targeting all major HPC platforms."""

    homepage = "https://github.com/kokkos/kokkos"
    git = "https://github.com/kokkos/kokkos.git"
    url = "https://github.com/kokkos/kokkos/releases/download/4.4.01/kokkos-4.4.01.tar.gz"

    tags = ["e4s"]

    test_requires_compiler = True

    maintainers("cedricchevalier19", "nmm0", "lucbv", "tpadioleau")

    license("Apache-2.0 WITH LLVM-exception")

    version("develop", branch="develop")

    version("4.7.01", sha256="404cf33e76159e83b8b4ad5d86f6899d442b5da4624820ab457412116cdcd201")
    version("4.7.00", sha256="126b774a24dde8c1085c4aede7564c0b7492d6a07d85380f2b387a712cea1ff5")
    version("4.6.02", sha256="baf1ebbe67abe2bbb8bb6aed81b4247d53ae98ab8475e516d9c87e87fa2422ce")
    version("4.6.01", sha256="b9d70e4653b87a06dbb48d63291bf248058c7c7db4bd91979676ad5609bb1a3a")
    version("4.6.00", sha256="be72cf7fc6ef6b99c614f29b945960013a2aaa23859bfe1a560d8d9aa526ec9c")
    version("4.5.01", sha256="52d003ffbbe05f30c89966e4009c017efb1662b02b2b73190670d3418719564c")
    version("4.5.00", sha256="cbfb742feeb9e649db9eca0394e6ca9a22aa017a1e6aab8576990772a0e3135b")
    version("4.4.01", sha256="3413f0cb39912128d91424ebd92e8832009e7eeaf6fa8da58e99b0d37860d972")
    version("4.4.00", sha256="0b46372f38c48aa088411ac1b7c173a5c90f0fdb69ab40271827688fc134f58b")

    version(
        "4.3.01",
        sha256="5998b7c732664d6b5e219ccc445cd3077f0e3968b4be480c29cd194b4f45ec70",
        url="https://github.com/kokkos/kokkos/archive/4.3.01.tar.gz",
    )
    version(
        "4.3.00",
        sha256="53cf30d3b44dade51d48efefdaee7a6cf109a091b702a443a2eda63992e5fe0d",
        url="https://github.com/kokkos/kokkos/archive/4.3.00.tar.gz",
    )
    version(
        "4.2.01",
        sha256="cbabbabba021d00923fb357d2e1b905dda3838bd03c885a6752062fe03c67964",
        url="https://github.com/kokkos/kokkos/archive/4.2.01.tar.gz",
    )
    version(
        "4.2.00",
        sha256="ac08765848a0a6ac584a0a46cd12803f66dd2a2c2db99bb17c06ffc589bf5be8",
        url="https://github.com/kokkos/kokkos/archive/4.2.00.tar.gz",
    )
    version(
        "4.1.00",
        sha256="cf725ea34ba766fdaf29c884cfe2daacfdc6dc2d6af84042d1c78d0f16866275",
        url="https://github.com/kokkos/kokkos/archive/4.1.00.tar.gz",
    )
    version(
        "4.0.01",
        sha256="bb942de8afdd519fd6d5d3974706bfc22b6585a62dd565c12e53bdb82cd154f0",
        url="https://github.com/kokkos/kokkos/archive/4.0.01.tar.gz",
    )
    version(
        "4.0.00",
        sha256="1829a423883d4b44223c7c3a53d3c51671145aad57d7d23e6a1a4bebf710dcf6",
        url="https://github.com/kokkos/kokkos/archive/4.0.00.tar.gz",
    )
    version(
        "3.7.02",
        sha256="5024979f06bc8da2fb696252a66297f3e0e67098595a0cc7345312b3b4aa0f54",
        url="https://github.com/kokkos/kokkos/archive/3.7.02.tar.gz",
    )

    depends_on("cxx", type="build")  # Kokkos requires a C++ compiler

    depends_on("cmake@3.16:", type="build")
    conflicts("^cmake@3.28", when="@:4.2.01 +cuda")
    conflicts("^cuda@13:", when="@:4.7.0")

    devices_variants = {
        "cuda": [False, "Whether to build CUDA backend"],
        "openmp": [False, "Whether to build OpenMP backend"],
        "threads": [False, "Whether to build the C++ threads backend"],
        "serial": [False, "Whether to build serial backend"],
        "rocm": [False, "Whether to build HIP backend"],
        "sycl": [False, "Whether to build the SYCL backend"],
        "openmptarget": [False, "Whether to build the OpenMPTarget backend"],
    }
    requires("+serial", when="~openmp ~threads", msg="Kokkos requires at least one host backend")

    tpls_variants = {
        "hpx": [False, "Whether to enable the HPX library"],
        "hwloc": [False, "Whether to enable the HWLOC library"],
        "numactl": [False, "Whether to enable the LIBNUMA library"],
        "memkind": [False, "Whether to enable the MEMKIND library"],
    }

    options_variants = {
        "aggressive_vectorization": [False, None, "Aggressively vectorize loops"],
        "compiler_warnings": [False, None, "Print all compiler warnings"],
        "complex_align": [True, None, "Align complex numbers"],
        "cuda_constexpr": [False, "+cuda", "Activate experimental constexpr features"],
        "cuda_lambda": [False, "+cuda", "Activate experimental lambda features"],
        "cuda_ldg_intrinsic": [False, "+cuda", "Use CUDA LDG intrinsics"],
        "cuda_relocatable_device_code": [False, "+cuda", "Enable RDC for CUDA"],
        "hip_relocatable_device_code": [False, None, "Enable RDC for HIP"],
        "sycl_relocatable_device_code": [False, "@4.5: +sycl", "Enable RDC for SYCL"],
        "cuda_uvm": [False, "+cuda", "Enable unified virtual memory (UVM) for CUDA"],
        "debug": [False, None, "Activate extra debug features - may increase compiletimes"],
        "debug_bounds_check": [False, None, "Use bounds checking - will increase runtime"],
        "debug_dualview_modify_check": [False, None, "Debug check on dual views"],
        "deprecated_code": [False, None, "Whether to enable deprecated code"],
        "examples": [False, None, "Whether to build examples"],
        "hpx_async_dispatch": [False, None, "Whether HPX supports asynchronous dispath"],
        "tuning": [False, None, "Create bindings for tuning tools"],
        "tests": [False, None, "Build for tests"],
    }

    conflicts("~debug_dualview_modify_check", when="@4.7:")  # always enable from 4.7.00

    spack_micro_arch_map = {
        "thunderx2": "THUNDERX2",
        "zen": "ZEN",
        "zen2": "ZEN2",
        "zen3": "ZEN3",
        "zen4": "ZEN4",
        "zen5": "ZEN5",
        "steamroller": "KAVERI",
        "excavator": "CARIZO",
        "power7": "POWER7",
        "power8": "POWER8",
        "power9": "POWER9",
        "power8le": "POWER8",
        "power9le": "POWER9",
        "sandybridge": "SNB",
        "haswell": "HSW",
        "mic_knl": "KNL",
        "cannonlake": "SKX",
        "cascadelake": "SKX",
        "westmere": "WSM",
        "ivybridge": "SNB",
        "broadwell": "BDW",
        "skylake": "SKL",
        "icelake": "ICL",
        "skylake_avx512": "SKX",
        "sapphirerapids": "SPR",
    }

    spack_cuda_arch_map = {
        "30": "kepler30",
        "32": "kepler32",
        "35": "kepler35",
        "37": "kepler37",
        "50": "maxwell50",
        "52": "maxwell52",
        "53": "maxwell53",
        "60": "pascal60",
        "61": "pascal61",
        "70": "volta70",
        "72": "volta72",
        "75": "turing75",
        "80": "ampere80",
        "86": "ampere86",
        "87": "ampere87",
        "89": "ada89",
        "90": "hopper90",
        "100": "blackwell100",
        "120": "blackwell120",
    }
    cuda_arches = spack_cuda_arch_map.values()
    conflicts("+cuda", when="cuda_arch=none")

    # Kokkos support only one cuda_arch at a time
    variant(
        "cuda_arch",
        description="CUDA architecture",
        values=("none",) + CudaPackage.cuda_arch_values,
        default="none",
        multi=False,
        sticky=True,
        when="+cuda",
    )

    # Since Kokkos supports only one amdgpu_target at a time, the multi-value property is disabled.
    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=("none",) + ROCmPackage.amdgpu_targets,
        default="none",
        multi=False,
        sticky=True,
        when="+rocm",
    )

    amdgpu_arch_map = {
        "gfx900": "vega900",
        "gfx906": "vega906",
        "gfx908": "vega908",
        "gfx90a": "vega90A",
        "gfx940": "amd_gfx940",
        "gfx942": "amd_gfx942",
        "gfx1030": "navi1030",
        "gfx1100": "navi1100",
    }
    amdgpu_apu_arch_map = {"gfx942": "amd_gfx942_apu"}
    amd_support_conflict_msg = (
        "{0} is not supported; "
        "Kokkos supports the following AMD GPU targets: " + ", ".join(amdgpu_arch_map.keys())
    )
    amd_apu_support_conflict_msg = (
        "{0} is not supported; "
        "Kokkos supports the following AMD GPU targets with unified memory: "
        + ", ".join(amdgpu_apu_arch_map.keys())
    )
    for arch in ROCmPackage.amdgpu_targets:
        if arch not in amdgpu_arch_map:
            conflicts(
                "+rocm", when=f"amdgpu_target={arch}", msg=amd_support_conflict_msg.format(arch)
            )
        if arch not in amdgpu_apu_arch_map:
            conflicts(
                "+rocm+apu",
                when=f"amdgpu_target={arch}",
                msg=amd_apu_support_conflict_msg.format(arch),
            )

    intel_gpu_arches = (
        "intel_gen",
        "intel_gen9",
        "intel_gen11",
        "intel_gen12lp",
        "intel_dg1",
        "intel_dg2",
        "intel_xehp",
        "intel_pvc",
    )
    variant(
        "intel_gpu_arch",
        default="none",
        values=("none",) + intel_gpu_arches,
        description="Intel GPU architecture",
    )
    variant("apu", default=False, description="Enable APU support", when="@4.5: +rocm")

    for dev, (dflt, desc) in devices_variants.items():
        variant(dev, default=dflt, description=desc)
    conflicts("+cuda", when="+rocm", msg="CUDA and ROCm are not compatible in Kokkos.")
    depends_on("intel-oneapi-dpl", when="+sycl")
    depends_on("rocthrust", when="@4.3: +rocm")

    for opt, (dflt, when, desc) in options_variants.items():
        variant(opt, default=dflt, description=desc, when=when)

    for tpl, (dflt, desc) in tpls_variants.items():
        variant(tpl, default=dflt, description=desc)
        depends_on(tpl, when="+%s" % tpl)

    variant("wrapper", default=False, description="Use nvcc-wrapper for CUDA build")
    variant("cmake_lang", default=False, description="Use CMake language support for CUDA/HIP")
    depends_on("kokkos-nvcc-wrapper", when="+wrapper")
    depends_on("kokkos-nvcc-wrapper@develop", when="@develop+wrapper")
    conflicts("+wrapper", when="~cuda")
    conflicts("+wrapper", when="+cmake_lang")

    cxxstds = ["11", "14", "17", "20"]
    variant("cxxstd", default="17", values=cxxstds, multi=False, description="C++ standard")
    variant("pic", default=False, description="Build position independent code")

    conflicts("cxxstd=11")
    conflicts("cxxstd=14", when="@4.0:")

    conflicts("+cuda", when="cxxstd=17 ^cuda@:10")
    conflicts("+cuda", when="cxxstd=20 ^cuda@:11")

    # Expose a way to disable CudaMallocAsync that can cause problems
    # with some MPI such as cray-mpich
    variant("alloc_async", default=False, description="Use CudaMallocAsync", when="@4.2: +cuda")

    # SYCL and OpenMPTarget require C++17 or higher
    for cxxstdver in cxxstds[: cxxstds.index("17")]:
        conflicts(
            "+sycl", when="cxxstd={0}".format(cxxstdver), msg="SYCL requires C++17 or higher"
        )
        conflicts(
            "+openmptarget",
            when="cxxstd={0}".format(cxxstdver),
            msg="OpenMPTarget requires C++17 or higher",
        )

    # HPX should use the same C++ standard
    for cxxstd in cxxstds:
        depends_on("hpx cxxstd={0}".format(cxxstd), when="+hpx cxxstd={0}".format(cxxstd))

    # HPX version constraints
    depends_on("hpx@1.7:", when="+hpx")

    # Patches
    patch("sycl_bhalft_test.patch", when="@4.2.00 +sycl")
    # adds amd_gfx940 support to Kokkos 4.2.00 (upstreamed in https://github.com/kokkos/kokkos/pull/6671)
    patch(
        "https://github.com/rbberger/kokkos/commit/293319c5844f4d8eea51eb9cd1457115a5016d3f.patch?full_index=1",
        sha256="145619e87dbf26b66ea23e76906576e2a854a3b09f2a2dd70363e61419fa6a6e",
        when="@4.2.00",
    )
    # Remove unnecessary C and C++ languages dependency in scripts/spack_test/CMakeLists.txt (upstreamed in https://github.com/kokkos/kokkos/pull/8357)
    patch(
        "https://github.com/kokkos/kokkos/commit/05d4901538251fff7ae6e58c84db670ad326b5c8.patch?full_index=1",
        sha256="89eb693ad4913c4fd06b25d786d56bfa631d7d612df80c0f5331852e358e0608",
        when="@:4.4",
    )

    variant("shared", default=True, description="Build shared libraries")
    for backend_name in ("cuda", "hip", "sycl"):
        conflicts("+shared", when=f"+{backend_name}_relocatable_device_code")

    # Filter spack-generated files that may include links to the
    # spack compiler wrappers
    filter_compiler_wrappers("kokkos_launch_compiler", relative_root="bin")
    filter_compiler_wrappers(
        "KokkosConfigCommon.cmake", relative_root=os.path.join("lib64", "cmake", "Kokkos")
    )

    # sanity check
    sanity_check_is_file = [
        join_path("include", "KokkosCore_config.h"),
        join_path("include", "Kokkos_Core.hpp"),
    ]
    sanity_check_is_dir = ["bin", "include"]

    @classmethod
    def get_microarch(cls, target):
        """Get the Kokkos microarch name for a Spack target (spec.target)."""
        smam = cls.spack_micro_arch_map

        # Find closest ancestor that has a known microarch optimization
        if target.name not in smam:
            for target in target.ancestors:
                if target.name in smam:
                    break
            else:
                # No known microarch optimizatinos
                return None

        return smam[target.name]

    def append_args(self, cmake_prefix, cmake_options, spack_options):
        variant_to_cmake_option = {"rocm": "hip"}
        for variant_name in cmake_options:
            opt = variant_to_cmake_option.get(variant_name, variant_name)
            optname = f"Kokkos_{cmake_prefix}_{opt.upper()}"
            # Explicitly enable or disable
            option = self.define_from_variant(optname, variant_name)
            if option:
                spack_options.append(option)

    @property
    def kokkos_cxx(self) -> str:
        if self.spec.satisfies("+wrapper"):
            return self["kokkos-nvcc-wrapper"].kokkos_cxx
        # Assumes build-time globals have been set already
        return spack_cxx

    def cmake_args(self):
        spec = self.spec
        from_variant = self.define_from_variant

        if spec.satisfies("~wrapper+cuda") and not (
            spec.satisfies("%clang") or spec.satisfies("%cce") or spec.satisfies("+cmake_lang")
        ):
            raise InstallError(
                "Kokkos requires +wrapper when using +cuda without %clang, %cce or +cmake_lang"
            )

        options = [
            from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
            from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            from_variant("BUILD_SHARED_LIBS", "shared"),
            from_variant("Kokkos_ENABLE_COMPILE_AS_CMAKE_LANGUAGE", "cmake_lang"),
        ]

        spack_microarches = []
        if spec.satisfies("+cuda"):
            cuda_arch = spec.variants["cuda_arch"].value
            if cuda_arch != "none":
                kokkos_arch_name = self.spack_cuda_arch_map[cuda_arch]
                spack_microarches.append(kokkos_arch_name)

        kokkos_microarch_name = self.get_microarch(spec.target)
        if kokkos_microarch_name:
            spack_microarches.append(kokkos_microarch_name)

        if spec.satisfies("+rocm"):
            amdgpu_target = spec.variants["amdgpu_target"].value
            if amdgpu_target != "none":
                if amdgpu_target in self.amdgpu_arch_map:
                    if spec.satisfies("+apu") and amdgpu_target in self.amdgpu_apu_arch_map:
                        spack_microarches.append(self.amdgpu_apu_arch_map[amdgpu_target])
                    else:
                        spack_microarches.append(self.amdgpu_arch_map[amdgpu_target])
                else:
                    # Note that conflict declarations should prevent
                    # choosing an unsupported AMD GPU target
                    raise SpackError("Unsupported target: {0}".format(amdgpu_target))

        if self.spec.variants["intel_gpu_arch"].value != "none":
            spack_microarches.append(self.spec.variants["intel_gpu_arch"].value)

        for arch in spack_microarches:
            options.append(self.define("Kokkos_ARCH_" + arch.upper(), True))

        self.append_args("ENABLE", self.devices_variants.keys(), options)
        self.append_args("ENABLE", self.options_variants.keys(), options)
        self.append_args("ENABLE", self.tpls_variants.keys(), options)

        for tpl in self.tpls_variants:
            if spec.variants[tpl].value:
                options.append(self.define(tpl + "_DIR", spec[tpl].prefix))

        if self.spec.satisfies("+wrapper"):
            options.append(self.define("CMAKE_CXX_COMPILER", self.kokkos_cxx))
        elif "+rocm" in self.spec:
            if "+cmake_lang" in self.spec:
                if self.spec.satisfies("%cxx=clang"):
                    options.append(self.define("CMAKE_HIP_COMPILER", self.compiler.cxx))
                else:
                    options.append(
                        self.define(
                            "CMAKE_HIP_COMPILER",
                            join_path(self.spec["llvm-amdgpu"].prefix.bin, "amdclang++"),
                        )
                    )
                options.append(from_variant("CMAKE_HIP_STANDARD", "cxxstd"))
                options.append(
                    self.define(
                        "CMAKE_HIP_ARCHITECTURES", self.spec.variants["amdgpu_target"].value
                    )
                )
                options.append(self.define("CMAKE_HIP_EXTENSIONS", False))
            else:
                options.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
            options.append(self.define("Kokkos_ENABLE_ROCTHRUST", True))
        elif "+cuda" in self.spec and "+cmake_lang" in self.spec:
            if self.spec.satisfies("%cxx=clang"):
                options.append(self.define("CMAKE_CUDA_COMPILER", self.compiler.cxx))
            else:
                options.append(
                    self.define(
                        "CMAKE_CUDA_COMPILER", join_path(self.spec["cuda"].prefix.bin, "nvcc")
                    )
                )
            options.append(
                self.define("CMAKE_CUDA_ARCHITECTURES", self.spec.variants["cuda_arch"].value)
            )
            options.append(from_variant("CMAKE_CUDA_STANDARD", "cxxstd"))
            options.append(self.define("CMAKE_CUDA_EXTENSIONS", False))

        if self.spec.satisfies("%oneapi") or self.spec.satisfies("%intel"):
            options.append(self.define("CMAKE_CXX_FLAGS", "-fp-model=precise"))

        options.append(
            self.define_from_variant("Kokkos_ENABLE_IMPL_CUDA_MALLOC_ASYNC", "alloc_async")
        )

        if self.version == Version("4.7.00"):
            options.append(self.define("Kokkos_ENABLE_IMPL_VIEW_LEGACY", True))

        # Remove duplicate options
        return dedupe(options)

    test_script_relative_path = join_path("scripts", "spack_test")

    @run_after("install")
    def setup_build_tests(self):
        # Skip if unsupported version
        cmake_source_path = join_path(self.stage.source_path, self.test_script_relative_path)
        if not os.path.exists(cmake_source_path):
            return
        # Copy test
        cmake_out_path = join_path(self.test_script_relative_path, "out")
        cmake_args = [
            cmake_source_path,
            "-DSPACK_PACKAGE_SOURCE_DIR:PATH={0}".format(self.stage.source_path),
            "-DSPACK_PACKAGE_TEST_ROOT_DIR:PATH={0}".format(
                join_path(install_test_root(self), cmake_out_path)
            ),
            "-DSPACK_PACKAGE_INSTALL_DIR:PATH={0}".format(self.prefix),
        ]
        cmake(*cmake_args)
        cache_extra_test_sources(self, cmake_out_path)

    def test_run(self):
        """Test if kokkos builds and runs"""
        cmake_path = join_path(
            self.test_suite.current_test_cache_dir, self.test_script_relative_path, "out"
        )

        if not os.path.exists(cmake_path):
            raise SkipTest(f"{cmake_path} is missing")

        cmake = self.spec["cmake"].command
        cmake_args = ["-DEXECUTABLE_OUTPUT_PATH=" + cmake_path]
        if self.spec.satisfies("+rocm"):
            prefix_paths = ";".join(get_cmake_prefix_path(self))
            cmake_args.append("-DCMAKE_PREFIX_PATH={0}".format(prefix_paths))

        cmake(cmake_path, *cmake_args)
        make = which("make")
        make()
        make(cmake_path, "test")
