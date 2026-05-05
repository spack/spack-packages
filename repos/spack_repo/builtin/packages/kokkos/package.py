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

    version("5.1.1", sha256="8bdbee0f0ac383436743ad8a9e3e928705b34b31a25a92dc5179c52a3aa98519")
    version("5.1.0", sha256="7bdbdfc88033ed7d940c7940ed8919e1f2b78a9656c69276beb76ad45c41ec4e")
    version("5.0.2", sha256="188817bb452ca805ee8701f1c5adbbb4fb83dc8d1c50624566a18a719ba0fa5e")
    version("5.0.1", sha256="cf7d8515ca993229929be9f051aecd8f93cde325adac8a4f82ed6848adace218")
    version("5.0.0", sha256="c45f3e19c3eb71fc8b7210cb04cac658015fc1839e7cc0571f7406588ff9bcef")
    version("4.7.04", sha256="4213b248c39e112299fa94ee08817e51126fc02996ed6e2ab56aec4cdb80ee1f")
    version("4.7.03", sha256="969e7933b9426219b220f08036e489b3226e6d8cd24eecf2c5b80df8c37443c0")
    version("4.7.02", sha256="a81826ac0a167933d13506bc2a986fb5517038df9abb780fe9bb2c1d4e80803b")
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
        deprecated=True,
    )

    depends_on("cxx", type="build")  # Kokkos requires a C++ compiler

    # TODO new major: any new major needs to update this
    with when("@5:"):
        conflicts("%gcc@:10.3")
        conflicts("%llvm@:13")
        conflicts("%llvm@:14", when="+cuda ~wrapper")
        conflicts("%apple-clang@:7")
        conflicts("%oneapi@:2021")
        conflicts("%oneapi@:2024", when="+sycl")
        depends_on("cuda@12.2:", when="+cuda")
        depends_on("hip@6.2:", when="+rocm")
        conflicts("%nvhpc@:22.2")
        conflicts("%msvc@:19.2")
        conflicts("%arm@:20")

    # TODO any new version: depending on the changes in Kokkos' build system,
    # there might be special requirements on the cmake version.
    depends_on("cmake@3.16:", type="build")
    depends_on("cmake@3.22:", type="build", when="@5:")
    depends_on("cmake@3.25.2:", type="build", when="@5: +cuda +cmake_lang")
    conflicts("^cmake@3.28", when="@:4.2.01 +cuda")
    conflicts("^cuda@13:", when="@:4.7.0")

    # device : (default value, when clause, description)
    devices_variants = {
        "cuda": [False, None, "Whether to build CUDA backend"],
        "openmp": [False, None, "Whether to build OpenMP backend"],
        "threads": [False, None, "Whether to build the C++ threads backend"],
        "serial": [False, None, "Whether to build serial backend"],
        "rocm": [False, None, "Whether to build HIP backend"],
        "sycl": [False, None, "Whether to build the SYCL backend"],
        "openmptarget": [False, "@:5.0", "Whether to build the OpenMPTarget backend"],
    }
    requires(
        "+serial", when="~hpx ~openmp ~threads", msg="Kokkos requires at least one host backend"
    )

    tpls_variants = {
        "hpx": [False, None, "Whether to enable the HPX library"],
        "hwloc": [False, None, "Whether to enable the HWLOC library"],
        "numactl": [False, "@:4", "Whether to enable the LIBNUMA library"],
        "memkind": [False, "@:4", "Whether to enable the MEMKIND library"],
    }

    # TODO any new version: check if all these options still exist
    options_variants = {
        "aggressive_vectorization": [False, None, "Aggressively vectorize loops"],
        "atomics_bypass": [
            False,
            "@4.6: +serial~threads~cuda~rocm~hpx~openmp~sycl~openmptarget",
            "Make atomics non-atomic for non-threaded MPI-only use cases",
        ],
        "compiler_warnings": [False, "@:4", "Print all compiler warnings"],
        "complex_align": [True, None, "Align complex numbers"],
        "cuda_constexpr": [False, "+cuda", "Activate experimental constexpr features"],
        "cuda_lambda": [False, "@:4 +cuda", "Activate experimental lambda features"],
        "cuda_ldg_intrinsic": [False, "@:4 +cuda", "Use CUDA LDG intrinsics"],
        "cuda_relocatable_device_code": [False, "+cuda", "Enable RDC for CUDA"],
        "hip_relocatable_device_code": [False, None, "Enable RDC for HIP"],
        "sycl_relocatable_device_code": [False, "@4.5: +sycl", "Enable RDC for SYCL"],
        "cuda_uvm": [False, "@:4 +cuda", "Enable unified virtual memory (UVM) for CUDA"],
        "debug": [False, None, "Activate extra debug features - may increase compiletimes"],
        "debug_bounds_check": [False, None, "Use bounds checking - will increase runtime"],
        "debug_dualview_modify_check": [False, "@:4", "Debug check on dual views"],
        "deprecated_code": [False, "@:4", "Whether to enable deprecated code"],
        "hpx_async_dispatch": [False, "@:4", "Whether HPX supports asynchronous dispath"],
        "tuning": [False, None, "Create bindings for tuning tools"],
        "tests": [False, None, "Build for tests"],
    }

    conflicts("~debug_dualview_modify_check", when="@4.7:")  # always enable from 4.7.00

    # archspec target : (cmake_arch_option, condition)
    spack_micro_arch_map = {
        "armv8.1a": ("ARMV81", None),
        "armv8.4a": ("ARMV84", "@4.7.00:"),
        "neoverse_v2": ("ARMV9_GRACE", "@4.7.04:4,5.1:"),
        "u74mc": ("RISCV_U74MC", "@4.7.00:"),
        "a64fx": ("A64FX", None),
        "thunderx2": ("ARMV8_THUNDERX2", None),
        "zen": ("ZEN", None),
        "zen2": ("ZEN2", None),
        "zen3": ("ZEN3", None),
        "zen4": ("ZEN4", "@4.6.00:"),
        "zen5": ("ZEN5", "@4.7.00:"),
        "power7": ("POWER7", "@:4.2.01"),
        "power8": ("POWER8", None),
        "power9": ("POWER9", None),
        "power8le": ("POWER8", None),
        "power9le": ("POWER9", None),
        "sandybridge": ("SNB", None),
        "haswell": ("HSW", None),
        "mic_knl": ("KNL", None),
        "cannonlake": ("SKX", None),  # fallback
        "cascadelake": ("SKX", None),  # fallback
        "westmere": ("WSM", "@:4.2.01"),
        "ivybridge": ("SNB", None),  # fallback
        "broadwell": ("BDW", None),
        "skylake": ("SKL", None),
        "icelake": ("ICL", None),
        "skylake_avx512": ("SKX", None),
        "sapphirerapids": ("SPR", None),
    }

    # unmapped Kokkos arches
    # ("AMDAVX", None),       # Generic AMD chip
    # ("ICX", None),          # Ice Lake Xeon Server (AVX512)
    # ("KNC", None),          # Knights Corner Xeon Phi
    # ("BGQ", "@:4.2.01"),    # IBM Blue Gene/Q
    # ("RISCV_SG2042", "@4.3.00:"), # Sophgo SG2042 (64-core RISC-V)
    # ("RISCV_RVA22V", "@4.5.00:"), # RVA22V profile (RISC-V vector extension)
    # ("ARMV80", None),       # ARMv8.0 Compatible CPU
    # ("ARMV84_SVE", "@4.7.00:"),   # ARMv8.4 with SVE (Scalable Vector Extension)
    # ("ARMV8_THUNDERX", None),  # Cavium ThunderX

    # cuda_arch : (cmake_arch_option, condition)
    spack_cuda_arch_map = {
        "30": ("kepler30", "@:4"),
        "32": ("kepler32", "@:4"),
        "35": ("kepler35", "@:4"),
        "37": ("kepler37", "@:4"),
        "50": ("maxwell50", None),
        "52": ("maxwell52", None),
        "53": ("maxwell53", None),
        "60": ("pascal60", None),
        "61": ("pascal61", None),
        "70": ("volta70", None),
        "72": ("volta72", None),
        "75": ("turing75", None),
        "80": ("ampere80", None),
        "86": ("ampere86", None),
        "87": ("ampere87", "@4.7.00:"),
        "89": ("ada89", "@4.0.01:"),
        "90": ("hopper90", None),
        "100": ("blackwell100", "@4.7.00:"),
        "103": ("blackwell103", "@5.1.0:"),
        "120": ("blackwell120", "@4.7.00:"),
        "121": ("blackwell121", "@5.1.0:"),
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

    # amdgpu_target : (cmake_arch_option, condition)
    amdgpu_arch_map = {
        "gfx900": ("vega900", None),
        "gfx906": ("vega906", None),
        "gfx908": ("vega908", None),
        "gfx90a": ("vega90A", None),
        "gfx940": ("amd_gfx940", "@4.3.00:"),
        "gfx942": ("amd_gfx942", "@4.2.00:"),
        "gfx950": ("amd_gfx950", "@5.1.0:"),
        "gfx1030": ("navi1030", None),
        "gfx1100": ("navi1100", "@4.1.00:"),
        "gfx1103": ("amd_gfx1103", "@4.5.00:"),
        "gfx1201": ("amd_gfx1201", "@5.0.0:"),
    }
    amdgpu_apu_arch_map = {"gfx942": ("amd_gfx942_apu", "@4.5.00:")}
    amd_support_conflict_msg = (
        "{0} is not supported; "
        "Kokkos supports the following AMD GPU targets: " + ", ".join(amdgpu_arch_map.keys())
    )
    # FIXME we should revisit this. More archs have unified memory via HMM,
    # only the APU has unified physical memory
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

    # cmake_arch_option : condition
    intel_gpu_arches = {
        "intel_gen": None,
        "intel_gen9": None,
        "intel_gen11": None,
        "intel_gen12lp": None,
        "intel_dg1": None,
        "intel_dg2": "@4.7.00:",
        "intel_xehp": None,
        "intel_pvc": None,
    }
    variant(
        "intel_gpu_arch",
        default="none",
        values=("none",) + tuple(intel_gpu_arches.keys()),
        description="Intel GPU architecture",
    )
    # FIXME this should move to the apu part
    variant("apu", default=False, description="Enable APU support", when="@4.5: +rocm")

    for dev, (dflt, when, desc) in devices_variants.items():
        variant(dev, default=dflt, description=desc, when=when)
    conflicts("+cuda", when="+rocm", msg="CUDA and ROCm are not compatible in Kokkos.")
    depends_on("intel-oneapi-dpl", when="+sycl")
    depends_on("rocthrust", when="@4.3: +rocm")

    for opt, (dflt, when, desc) in options_variants.items():
        variant(opt, default=dflt, description=desc, when=when)

    for tpl, (dflt, when, desc) in tpls_variants.items():
        variant(tpl, default=dflt, description=desc, when=when)
        depends_on(tpl, when="+%s" % tpl)

    # FIXME we should reorder variants and conflicts
    variant("wrapper", default=False, description="Use nvcc-wrapper for CUDA build")
    variant("cmake_lang", default=False, description="Use CMake language support for CUDA/HIP")
    depends_on("kokkos-nvcc-wrapper", when="+wrapper")
    depends_on("kokkos-nvcc-wrapper@develop", when="@develop+wrapper")
    conflicts("+wrapper", when="~cuda")
    conflicts("+wrapper", when="+cmake_lang")

    # TODO new major: update c++ std
    with default_args(multi=False, description="C++ standard"):
        variant("cxxstd", default="17", values=("14", "17", "20"), when="@3")
        variant("cxxstd", default="17", values=("17", "20", "23"), when="@4")
        variant("cxxstd", default="20", values=("20", "23"), when="@5:")

    # FIXME regroup variants and conflicts
    variant(
        "deprecated_code",
        default=True,
        when="@5:",
        description="Whether to enable deprecated code",
    )

    variant("pic", default=False, description="Build position independent code")

    conflicts("+cuda", when="cxxstd=17 ^cuda@:10")
    conflicts("+cuda", when="cxxstd=20 ^cuda@:11")

    # Expose a way to disable CudaMallocAsync that can cause problems
    # with some MPI such as cray-mpich
    variant("alloc_async", default=False, description="Use CudaMallocAsync", when="@4.2: +cuda")

    # TODO deprecation of v3: this can be removed
    # SYCL and OpenMPTarget require C++17 or higher
    conflicts("+sycl", when="cxxstd=14", msg="SYCL requires C++17 or higher")
    conflicts("+openmptarget", when="cxxstd=14", msg="OpenMPTarget requires C++17 or higher")

    # TODO new major: add new standard version here
    # HPX should use the same C++ standard
    for cxxstd in ["14", "17", "20", "23"]:
        depends_on(f"hpx cxxstd={cxxstd}", when=f"+hpx cxxstd={cxxstd}")

    # HPX version constraints
    depends_on("hpx@1.7:", when="+hpx")

    # TODO deprecation of some versions in 4: remove
    # Patches
    patch("sycl_bhalft_test.patch", when="@4.2.00 +sycl")
    # adds amd_gfx940 support to Kokkos 4.2.00 (upstreamed in https://github.com/kokkos/kokkos/pull/6671)
    patch(
        "https://github.com/rbberger/kokkos/commit/293319c5844f4d8eea51eb9cd1457115a5016d3f.patch?full_index=1",
        sha256="145619e87dbf26b66ea23e76906576e2a854a3b09f2a2dd70363e61419fa6a6e",
        when="@4.2.00",
    )
    # Remove unnecessary C and C++ languages dependency in scripts/spack_test/CMakeLists.txt
    # (upstreamed in https://github.com/kokkos/kokkos/pull/8357)
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
    def get_microarch(cls, target, kokkos_spec=None):
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

        microarch, cond = smam[target.name]
        if cond and kokkos_spec and not kokkos_spec.satisfies(cond):
            return None
        return microarch

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

        # TODO new major: update this
        if spec.satisfies("@5:"):
            if spec.version == Version("develop"):
                highest = max(v for v in self.versions if not v.isdevelop())
                major_version = int(str(highest.up_to(1)))
            else:
                major_version = int(str(spec.version.up_to(1)))
            options.append(
                from_variant(f"Kokkos_ENABLE_DEPRECATED_CODE_{major_version}", "deprecated_code")
            )

        spack_microarches = []
        if spec.satisfies("+cuda"):
            cuda_arch = spec.variants["cuda_arch"].value
            if cuda_arch != "none":
                kokkos_arch_name, cond = self.spack_cuda_arch_map[cuda_arch]

                if cond and not self.spec.satisfies(cond):
                    raise SpackError(f"Unsupported CUDA arch: {cuda_arch}")

                spack_microarches.append(kokkos_arch_name)

        kokkos_microarch_name = self.get_microarch(spec.target, spec)
        if kokkos_microarch_name:
            spack_microarches.append(kokkos_microarch_name)

        if spec.satisfies("+rocm"):
            amdgpu_target = spec.variants["amdgpu_target"].value
            if amdgpu_target != "none":
                if amdgpu_target in self.amdgpu_arch_map:
                    if spec.satisfies("+apu") and amdgpu_target in self.amdgpu_apu_arch_map:
                        kokkos_arch_name, cond = self.amdgpu_apu_arch_map[amdgpu_target]
                    else:
                        kokkos_arch_name, cond = self.amdgpu_arch_map[amdgpu_target]

                    if cond and not self.spec.satisfies(cond):
                        raise SpackError(f"Unsupported AMD GPU target: {amdgpu_target}")

                    spack_microarches.append(kokkos_arch_name)
                else:
                    # Note that conflict declarations should prevent
                    # choosing an unsupported AMD GPU target
                    raise SpackError(f"Unsupported AMD GPU target: {amdgpu_target}")

        if self.spec.variants["intel_gpu_arch"].value != "none":
            intel_gpu_arch = self.spec.variants["intel_gpu_arch"].value
            cond = self.intel_gpu_arches[intel_gpu_arch]

            if cond and not self.spec.satisfies(cond):
                raise SpackError(f"Unsupported Intel GPU target: {intel_gpu_arch}")

            spack_microarches.append(intel_gpu_arch)

        for arch in spack_microarches:
            options.append(self.define("Kokkos_ARCH_" + arch.upper(), True))

        self.append_args("ENABLE", self.devices_variants.keys(), options)
        self.append_args("ENABLE", self.options_variants.keys(), options)
        self.append_args("ENABLE", self.tpls_variants.keys(), options)

        for tpl in self.tpls_variants:
            if spec.satisfies(f"+{tpl}"):
                options.append(self.define(tpl + "_DIR", spec[tpl].prefix))

        if self.spec.satisfies("+wrapper"):
            options.append(self.define("CMAKE_CXX_COMPILER", self.kokkos_cxx))
        elif "+rocm" in self.spec:
            if "+cmake_lang" in self.spec:
                if self.spec.satisfies("%cxx=clang") or self.spec.satisfies("%cxx=rocmcc"):
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
            elif not (self.spec.satisfies("%cxx=clang") or self.spec.satisfies("%cxx=rocmcc")):
                options.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
            options.append(self.define("Kokkos_ENABLE_ROCTHRUST", True))

            # TODO deprecation of v4: remove partially
            # Using Kokkos_ENABLE_IMPL_HIP_MALLOC_ASYNC is problematic with ROCm 7
            # Newer Kokkos versions disable this by default
            if self.spec.satisfies("@4.5:5.0.0 %hip@7:"):
                options.append(self.define("Kokkos_ENABLE_IMPL_HIP_MALLOC_ASYNC", False))
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

        # TODO deprecation v4: remove
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
            self.define("SPACK_PACKAGE_SOURCE_DIR", self.stage.source_path),
            self.define(
                "SPACK_PACKAGE_TEST_ROOT_DIR", join_path(install_test_root(self), cmake_out_path)
            ),
            self.define("SPACK_PACKAGE_INSTALL_DIR", self.prefix),
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
        cmake_args = []
        if self.spec.satisfies("+rocm"):
            prefix_paths = ";".join(get_cmake_prefix_path(self))
            cmake_args.append(self.define("CMAKE_PREFIX_PATH", prefix_paths))

        if self.spec.satisfies("+wrapper"):
            cmake_args.append(
                self.define("CMAKE_CXX_COMPILER", self["kokkos-nvcc-wrapper"].kokkos_cxx)
            )
        else:
            cmake_args.append(self.define("CMAKE_CXX_COMPILER", self["cxx"].cxx))

        cmake(cmake_path, *cmake_args)
        cmake("--build", ".")
        cmake("--build", ".", "--target", "test")
