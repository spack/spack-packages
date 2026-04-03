# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os
import re
import shutil

from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.compiler import CompilerPackage
from spack_repo.builtin.packages.llvm.package import LlvmDetection

from spack.package import *


class LlvmAmdgpu(CMakePackage, LlvmDetection, CompilerPackage):
    """Toolkit for the construction of highly optimized compilers,
    optimizers, and run-time environments."""

    homepage = "https://github.com/ROCm/llvm-project"
    git = "https://github.com/ROCm/llvm-project.git"
    url = "https://github.com/ROCm/llvm-project/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm", "compiler"]
    executables = [
        r"amdclang",
        r"amdclang\+\+",
        r"amdflang",
        r"clang.*",
        r"flang.*",
        "llvm-.*",
        "amdldd",
    ]

    compiler_wrapper_link_paths = {
        "c": "rocmcc/amdclang",
        "cxx": "rocmcc/amdclang++",
        "fortran": "rocmcc/amdflang",
    }

    stdcxx_libs = ("-lstdc++",)

    generator("ninja")

    maintainers("srekolam", "renjithravindrankannath", "haampie", "afzpatel")

    license("Apache-2.0")
    version("7.2.0", sha256="e86138d2a63fbcbdf64668d55573b26ae944d0f0ae5a3f5bb59bf7bdb3124d3f")
    version("7.1.1", sha256="d76a16db4a56914383029e241823f7bc2a3d645f2967dd22230f11c11cfe189e")
    version("7.1.0", sha256="87f5532b8b653bd18541cdf6e59923cbd340b300d8ec5046d3e4288d9e5195c0")
    version("7.0.2", sha256="fd612fa750bebd0c3be0ea642b2cae8ff5c7e00a2280b22b9ea16ee86a11d763")
    version("7.0.0", sha256="3d479a2aa615b6bb35cd3521122fbff34188dc0cc52d8b0acda59f9f55198211")
    version("6.4.3", sha256="7a484b621d568eef000ee8c4d2d46d589e5682b950f1f410ce7215031f1f3ad7")
    version("6.4.2", sha256="9f42cb73d90bd4561686c0366f60f6e58cfd32ff24b094c69e8259fb5d177457")
    version("6.4.1", sha256="460ad28677092b9eb86ffdc49bcb4d01035e32b4f05161d85f90c9fa80239f50")
    version("6.4.0", sha256="dca1c145a23f05229d5d646241f9d1d3c5dbf1d745b338ae020eabe33beb965c")
    version("6.3.3", sha256="4df9aba24e574edf23844c0d2d9dda112811db5c2b08c9428604a21b819eb23d")
    version("6.3.2", sha256="1f52e45660ea508d3fe717a9903fe27020cee96de95a3541434838e0193a4827")
    version("6.3.1", sha256="e9c2481cccacdea72c1f8d3970956c447cec47e18dfb9712cbbba76a2820552c")
    version("6.3.0", sha256="79580508b039ca6c50dfdfd7c4f6fbcf489fe1931037ca51324818851eea0c1c")
    version("6.2.4", sha256="7af782bf5835fcd0928047dbf558f5000e7f0207ca39cf04570969343e789528")
    version("6.2.1", sha256="4840f109d8f267c28597e936c869c358de56b8ad6c3ed4881387cf531846e5a7")
    version("6.2.0", sha256="12ce17dc920ec6dac0c5484159b3eec00276e4a5b301ab1250488db3b2852200")
    version("6.1.2", sha256="300e9d6a137dcd91b18d5809a316fddb615e0e7f982dc7ef1bb56876dff6e097")
    version("6.1.1", sha256="f1a67efb49f76a9b262e9735d3f75ad21e3bd6a05338c9b15c01e6c625c4460d")
    version("6.1.0", sha256="6bd9912441de6caf6b26d1323e1c899ecd14ff2431874a2f5883d3bc5212db34")
    version("6.0.2", sha256="7d35acc84de1adee65406f92a369a30364703f84279241c444cd93a48c7eeb76")
    version("6.0.0", sha256="c673708d413d60ca8606ee75c77e9871b6953c59029c987b92f2f6e85f683626")
    version("5.7.1", sha256="6b54c422e45ad19c9bf5ab090ec21753e7f7d854ca78132c30eb146657b168eb")
    version("5.7.0", sha256="4abdf00b297a77c5886cedb37e63acda2ba11cb9f4c0a64e133b05800aadfcf0")

    provides("c", "cxx")
    provides("fortran", when="@7.0:")

    variant(
        "rocm-device-libs",
        default=True,
        description=(
            "Build ROCm device libs as external LLVM project instead of a "
            "standalone spack package."
        ),
    )
    variant(
        "llvm_dylib",
        default=False,
        description="Build LLVM shared library, containing all "
        "components in a single shared library",
    )
    variant(
        "link_llvm_dylib",
        default=False,
        description="Link LLVM tools against the LLVM shared library",
    )

    provides("libllvm@17", when="@5.7:6.1")
    provides("libllvm@18", when="@6.2:6.3")
    provides("libllvm@19", when="@6.4")
    provides("libllvm@20", when="@7.0:7.1")
    provides("libllvm@22", when="@7.2")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.13.4:", type="build")
    depends_on("python", type="build")
    depends_on("z3", type="link")
    depends_on("zlib-api", type="link")
    depends_on("ncurses+termlib", type="link")
    depends_on("libxml2", type="link")
    depends_on("pkgconfig", type="build")

    depends_on("numactl", when="@7.1:")
    depends_on("libdrm", when="@7.1:")
    depends_on("libelf", when="@7.1:")
    depends_on("xxd", when="@7.1:")

    # This flavour of LLVM doesn't work on MacOS, so we should ensure that it
    # isn't used to satisfy any of the libllvm dependencies on the Darwin
    # platform.
    conflicts("platform=darwin")

    patch("0001-update-HIP_PATH-deduction-for-5.7.0.patch", when="@:6.0")

    # Below patch is to set the flag -mcode-object-version=none until
    # the below fix is available in device-libs release code.
    # https://github.com/ROCm/ROCm-Device-Libs/commit/f0356159dbdc93ea9e545f9b61a7842f9c881fdf
    patch("patch-llvm-5.5.0.patch", when="@5.7 +rocm-device-libs")

    # i1 muls can sometimes happen after SCEV.
    # They resulted in ISel failures because we were missing the patterns for them.
    # This fix is targeting 6.1 rocm release.
    # Need patch until https://github.com/llvm/llvm-project/pull/67291 is merged.
    patch("001-Add-i1-mul-patterns-5.7.patch", when="@5.7")

    # fixes the libamdhip64.so not found in some ROCm math lib tests
    patch(
        "https://github.com/ROCm/llvm-project/commit/444d1d12bbc0269fed5451fb1a9110a049679ca5.patch?full_index=1",
        sha256="b4774ca19b030890d7b276d12c446400ccf8bc3aa724c7f2e9a73531a7400d69",
        when="@6",
    )
    patch("002-Add-rpath-to-hiprt.patch", when="@7.0:")

    # Fix for https://github.com/llvm/llvm-project/issues/78530
    # Patch from https://github.com/llvm/llvm-project/pull/80071
    patch(
        "https://github.com/ROCm/llvm-project/commit/c651b2b0d9d1393fb5191ac3acfe96e5ecc94bbc.patch?full_index=1",
        sha256="eaf700a5b51d53324a93e5c951bc08b6311ce2053c44c1edfff5119f472d8080",
        when="@:6.2",
    )

    patch(
        "https://github.com/ROCm/llvm-project/commit/97301a5390f841241e5ed88e26c218882e018cc4.patch?full_index=1",
        sha256="74471ee320c4d839a433c04b9d35db868f2a13c08183297d1a09ec580ca1d7e9",
        when="@7.2",
    )

    conflicts("^cmake@3.19.0")

    # https://github.com/spack/spack/issues/45746
    conflicts("^ninja@1.12:", when="@:6.0")

    root_cmakelists_dir = "llvm"
    install_targets = ["clang-tidy", "install"]

    # Add device libs sources so they can be an external LLVM project
    for d_version, d_shasum in [
        ("6.0.2", "c6d88b9b46e39d5d21bd5a0c1eba887ec473a370b1ed0cebd1d2e910eedc5837"),
        ("6.0.0", "198df4550d4560537ba60ac7af9bde31d59779c8ec5d6309627f77a43ab6ef6f"),
        ("5.7.1", "703de8403c0bd0d80f37c970a698f10f148daf144d34f982e4484d04f7c7bbef"),
        ("5.7.0", "0f8780b9098573f1c456bdc84358de924dcf00604330770a383983e1775bf61e"),
    ]:
        resource(
            name="rocm-device-libs",
            placement="rocm-device-libs",
            url=f"https://github.com/ROCm/ROCm-Device-Libs/archive/rocm-{d_version}.tar.gz",
            sha256=d_shasum,
            when=f"@{d_version} +rocm-device-libs",
        )

    for d_version, d_shasum in [
        ("7.1.1", "4c5b58afa1e11461954bd005a10ebf29941c120f1d6a7863954597f5eacfc605"),
        ("7.1.0", "383fa8e1776c3ee527cdddc9f9ac6f7134c3fcd8758eae9be8bd3a8b7fdca9b1"),
        ("7.0.2", "9c2020f7a42d60fe9775865ab58464078007926a3b01f1ca8128557c89e7a566"),
        ("7.0.0", "9ea2cbcf343f643ede6e16d82fbd0303771e1978759b2e546d0efc0df3263e4c"),
        ("6.4.3", "3b23bed04cbed72304d31d69901eb76afa2099c7ac37f055348dfcda2d25e41a"),
        ("6.4.2", "8ad5dbf7cb0f728b8e515f46a41db24ed3b99ca894ccdd9f4d9bac969e9e35bb"),
        ("6.4.1", "f72d100a46a2dd9f4c870cef156604777f1bdb1841df039d14bf37b19814b9da"),
        ("6.4.0", "ff740e8c8f2229c6dc47577363f707b1a44ea4254f8ad74f8f0a669998829535"),
        ("6.3.3", "aa2e30d3d68707d6df4840e954bb08cc13cd312cec1a98a64d97adbe07262f50"),
        ("6.3.2", "aaecaa7206b6fa1d5d7b8f7c1f7c5057a944327ba4779448980d7e7c7122b074"),
        ("6.3.1", "547ceeeda9a41cdffa21e57809dc5834f94938a0a2809c283aebcbcf01901df0"),
        ("6.3.0", "8fd6bcd6a5afd0ae5a59e33b786a525f575183d38c34049c2dab6b9270a1ca3b"),
        ("6.2.4", "b7aa0055855398d1228c39a6f4feb7d7be921af4f43d82855faf0b531394bb9b"),
        ("6.2.1", "dbe477b323df636f5e3221471780da156c938ec00dda4b50639aa8d7fb9248f4"),
        ("6.2.0", "c98090041fa56ca4a260709876e2666f85ab7464db9454b177a189e1f52e0b1a"),
        ("6.1.2", "6eb7a02e5f1e5e3499206b9e74c9ccdd644abaafa2609dea0993124637617866"),
        ("6.1.1", "72841f112f953c16619938273370eb8727ddf6c2e00312856c9fca54db583b99"),
        ("6.1.0", "50386ebcb7ff24449afa2a10c76a059597464f877225c582ba3e097632a43f9c"),
        ("6.0.2", "e7ff4d7ac35a2dd8aad1cb40b96511a77a9c23fe4d1607902328e53728e05c28"),
        ("6.0.0", "99e8fa1af52d0bf382f28468e1a345af1ff3452c35914a6a7b5eeaf69fc568db"),
        ("5.7.1", "655e9bfef4b0b6ad3f9b89c934dc0a8377273bb0bccbda6c399ac5d5d2c1c04c"),
        ("5.7.0", "2c56ec5c78a36f2b847afd4632cb25dbf6ecc58661eb2ae038c2552342e6ce23"),
    ]:
        resource(
            name="hsa-runtime",
            placement="hsa-runtime",
            url=f"https://github.com/ROCm/ROCR-Runtime/archive/rocm-{d_version}.tar.gz",
            sha256=d_shasum,
            when=f"@{d_version}",
        )

    for d_version, d_shasum in [
        ("7.2.0", "728ea7e9bf16e6ed217a0fd1a8c9afaba2dae2e7908fa4e27201e67c803c5638")
    ]:
        resource(
            name="rocm-systems",
            placement="rocm-systems",
            url=f"https://github.com/ROCm/rocm-systems/archive/rocm-{d_version}.tar.gz",
            sha256=d_shasum,
            when=f"@{d_version}",
        )

    for d_version, d_shasum in [
        ("7.1.0", "e6ef3e62eb0626765c55084c9de5fd19f9b216b11577e71ef36046c0081f1102"),
        ("7.1.1", "b02e7a2b38c408067f3713ff47fe620059a8fe5f47110ab343116448625b7448"),
        ("7.2.0", "b003b608df470d88ad0a636581e134b05b8aee586b0332c545280e6c6366d121"),
    ]:
        resource(
            name="spirv-llvm-translator",
            url=f"https://github.com/ROCm/SPIRV-LLVM-Translator/archive/refs/tags/rocm-{d_version}.tar.gz",
            sha256=d_shasum,
            expand=True,
            destination="llvm/projects",
            placement="spirv-llvm-translator",
            when=f"@{d_version}",
        )

    for d_version, d_shasum in [
        ("6.0.2", "737b110d9402509db200ee413fb139a78369cf517453395b96bda52d0aa362b9"),
        ("6.0.0", "04353d27a512642a5e5339532a39d0aabe44e0964985de37b150a2550385800a"),
        ("5.7.1", "3b9433b4a0527167c3e9dfc37a3c54e0550744b8d4a8e1be298c8d4bcedfee7c"),
        ("5.7.0", "e234bcb93d602377cfaaacb59aeac5796edcd842a618162867b7e670c3a2c42c"),
    ]:
        resource(
            name="comgr",
            placement="comgr",
            url=f"https://github.com/ROCm/ROCm-CompilerSupport/archive/rocm-{d_version}.tar.gz",
            sha256=d_shasum,
            when=f"@{d_version}",
        )

    def _standard_flag(self, *, language, standard):
        flags = {
            "cxx": {
                "11": "-std=c++11",
                "14": "-std=c++14",
                "17": "-std=c++17",
                "20": "-std=c++20",
            },
            "c": {"99": "-std=c99", "11": "-std=c1x"},
        }
        return flags[language][standard]

    def cmake_args(self):
        llvm_projects = ["clang", "lld", "clang-tools-extra", "compiler-rt"]
        llvm_runtimes = ["libcxx", "libcxxabi"]
        args = [
            self.define("LLVM_ENABLE_Z3_SOLVER", "OFF"),
            self.define("LLVM_ENABLE_ZLIB", "ON"),
            self.define("CLANG_DEFAULT_LINKER", "lld"),
            self.define("LIBCXXABI_INSTALL_STATIC_LIBRARY", "OFF"),
            self.define("LLVM_ENABLE_RTTI", "ON"),
            self.define("LLVM_AMDGPU_ALLOW_NPI_TARGETS", "ON"),
            self.define("PACKAGE_VENDOR", "AMD"),
            self.define("CLANG_ENABLE_AMDCLANG", "ON"),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            self.define("CLANG_DEFAULT_RTLIB", "compiler-rt"),
            self.define("CLANG_DEFAULT_UNWINDLIB", "libgcc"),
        ]

        if self.spec.target.family == "aarch64":
            args.append(self.define("LLVM_TARGETS_TO_BUILD", "AMDGPU;AArch64"))
        else:
            args.append(self.define("LLVM_TARGETS_TO_BUILD", "AMDGPU;X86"))

        # Enable rocm-device-libs as a external project
        if self.spec.satisfies("+rocm-device-libs"):
            if self.spec.satisfies("@:6.0"):
                dir = os.path.join(self.stage.source_path, "rocm-device-libs")
            elif self.spec.satisfies("@6.1:"):
                dir = os.path.join(self.stage.source_path, "amd/device-libs")

            if self.spec.satisfies("@:7.0"):
                args.extend(
                    [
                        self.define("LLVM_EXTERNAL_PROJECTS", "device-libs"),
                        self.define("LLVM_EXTERNAL_DEVICE_LIBS_SOURCE_DIR", dir),
                    ]
                )
            else:
                args.append(self.define("ROCM_DEVICE_LIBS_INSTALL_PREFIX_PATH", self.prefix))
                args.append(
                    self.define("ROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC", "lib/clang/20/lib/amdgcn")
                )

        if self.spec.satisfies("+llvm_dylib"):
            args.append(self.define("LLVM_BUILD_LLVM_DYLIB", True))

        if self.spec.satisfies("+link_llvm_dylib"):
            args.append(self.define("LLVM_LINK_LLVM_DYLIB", True))
            args.append(self.define("CLANG_LINK_CLANG_DYLIB", True))

        # Get the GCC prefix for LLVM.
        if self.compiler.name == "gcc" and self.spec.satisfies("@:6.3"):
            args.append(self.define("GCC_INSTALL_PREFIX", self.compiler.prefix))
        if self.spec.satisfies("@:6.0"):
            comgrinc_path = os.path.join(self.stage.source_path, "comgr/lib/comgr/include")
        elif self.spec.satisfies("@6.1:"):
            comgrinc_path = os.path.join(self.stage.source_path, "amd/comgr/include")

        if self.spec.satisfies("@7.2:"):
            hsa_path = os.path.join(self.stage.source_path, "rocm-systems/projects/rocr-runtime")
        else:
            hsa_path = os.path.join(self.stage.source_path, "hsa-runtime")

        if self.spec.satisfies("@:6.2"):
            hsainc_path = os.path.join(hsa_path, "src/inc")
        if self.spec.satisfies("@6.3:"):
            hsainc_path = os.path.join(hsa_path, "runtime/hsa-runtime/inc")
        args.append("-DSANITIZER_HSA_INCLUDE_PATH={0}".format(hsainc_path))
        args.append("-DSANITIZER_COMGR_INCLUDE_PATH={0}".format(comgrinc_path))
        args.append("-DSANITIZER_AMDGPU:Bool=ON")
        if self.spec.satisfies("@6.1:7.0"):
            args.append(self.define("LLVM_ENABLE_LIBCXX", "OFF"))
        if self.spec.satisfies("@6.1:"):
            llvm_projects.remove("compiler-rt")
            llvm_runtimes.extend(["compiler-rt", "libunwind"])
            args.append(self.define("CLANG_LINK_FLANG_LEGACY", True))
            args.append(self.define("CMAKE_CXX_STANDARD", 17))
            args.append(self.define("FLANG_INCLUDE_DOCS", False))
            args.append(self.define("LLVM_BUILD_DOCS", "ON"))
            args.append(self.define("CLANG_DEFAULT_PIE_ON_LINUX", "OFF"))
        if self.spec.satisfies("@7.0:"):
            llvm_projects.extend(["mlir", "flang"])
            args.append(self.define("LIBOMPTARGET_BUILD_DEVICE_FORTRT", "ON"))
            args.append(self.define("FLANG_RUNTIME_F128_MATH_LIB", "libquadmath"))
        if self.spec.satisfies("@:7.0"):
            args.append(self.define("LIBCXX_ENABLE_SHARED", "OFF"))
            args.append(self.define("LIBCXX_ENABLE_STATIC", "ON"))
            args.append(self.define("LIBCXX_INSTALL_LIBRARY", "OFF"))
            args.append(self.define("LIBCXX_INSTALL_HEADERS", "OFF"))
            args.append(self.define("LIBCXXABI_ENABLE_SHARED", "OFF"))
            args.append(self.define("LIBCXXABI_ENABLE_STATIC", "ON"))
        else:
            args.append(self.define("LIBCXX_ENABLE_SHARED", "ON"))
            args.append(self.define("LIBCXX_ENABLE_STATIC", "OFF"))
            args.append(self.define("LIBCXX_INSTALL_LIBRARY", "ON"))
            args.append(self.define("LIBCXX_INSTALL_HEADERS", "ON"))
            args.append(self.define("LIBCXXABI_ENABLE_SHARED", "ON"))
            args.append(self.define("LIBCXXABI_ENABLE_STATIC", "OFF"))
        if self.spec.satisfies("@7.1:"):
            llvm_runtimes.extend(["offload", "openmp"])
            args.append(self.define("LLVM_INSTALL_UTILS", "ON"))
            args.append(self.define("OPENMP_ENABLE_LIBOMPTARGET", "ON"))
            args.append(self.define("LLVM_ENABLE_LIBCXX", "ON"))
            args.append(self.define("LIBOMPTARGET_ENABLE_DEBUG", "ON"))
            args.append(self.define("LIBOMPTARGET_NO_SANITIZER_AMDGPU", "ON"))
            args.append(self.define("LIBOMPTARGET_EXTERNAL_PROJECT_HSA_PATH", hsa_path))
            args.append(self.define("OFFLOAD_EXTERNAL_PROJECT_UNIFIED_ROCR", "ON"))
            devlibs_dir = os.path.join(self.stage.source_path, "amd/device-libs")
            args.append(
                self.define("LIBOMPTARGET_EXTERNAL_PROJECT_ROCM_DEVICE_LIBS_PATH", devlibs_dir)
            )
        if self.spec.satisfies("@7.2:"):
            args.append(self.define("LLVM_RUNTIME_TARGETS", "default;amdgcn-amd-amdhsa"))
            args.append("-DRUNTIMES_amdgcn-amd-amdhsa_LLVM_ENABLE_RUNTIMES=openmp")
            args.append("-DRUNTIMES_amdgcn-amd-amdhsa_LLVM_ENABLE_PER_TARGET_RUNTIME_DIR=ON")
            spirv_dir = os.path.join(self.stage.source_path, "llvm/projects/spirv-llvm-translator")
            args.append(self.define("LLVM_EXTERNAL_SPIRV_LLVM_TRANSLATOR_SOURCE_DIR", spirv_dir))
        args.append(self.define("LLVM_ENABLE_PROJECTS", llvm_projects))
        args.append(self.define("LLVM_ENABLE_RUNTIMES", llvm_runtimes))

        # CMake args passed just to runtimes
        runtime_cmake_args = [self.define("CMAKE_INSTALL_RPATH_USE_LINK_PATH", True)]

        # When building runtimes, just-built clang has to know where GCC is.
        gcc_install_dir_flag = get_gcc_install_dir_flag(self.spec, self.compiler)
        if gcc_install_dir_flag:
            runtime_cmake_args.extend(
                [
                    self.define("CMAKE_C_FLAGS", gcc_install_dir_flag),
                    self.define("CMAKE_CXX_FLAGS", gcc_install_dir_flag),
                ]
            )

        args.append(self.define("RUNTIMES_CMAKE_ARGS", runtime_cmake_args))
        return args

    compiler_languages = ["c", "cxx", "fortran"]
    c_names = ["amdclang"]
    cxx_names = ["amdclang++"]
    fortran_names = ["amdflang"]
    compiler_version_argument = "--version"
    compiler_version_regex = r"roc-(\d+[._]\d+[._]\d+)"
    installed_dir_regex = r"InstalledDir:\s*(.+)"

    @classmethod
    def determine_version(cls, exe):
        try:
            compiler = Executable(exe)
            output = compiler(cls.compiler_version_argument, output=str, error=str)
            # Reject if the compiler is not under the InstalledDir
            # reported by --version (e.g. /usr/bin is not valid).
            installed_dir_match = re.search(cls.installed_dir_regex, output)
            if installed_dir_match:
                installed_dir = os.path.normpath(installed_dir_match.group(1).strip())
                exe_dir = os.path.normpath(os.path.dirname(os.path.abspath(str(exe))))
                if exe_dir != installed_dir:
                    return None
            else:
                return None
            match = re.search(cls.compiler_version_regex, output)
            if match:
                version_str = match.group(1)
                return version_str
        except ProcessError:
            pass
        except Exception as e:
            tty.debug(e)
        return None

    # Make sure that the compiler paths are in the LD_LIBRARY_PATH
    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)

    # Make sure that the compiler paths are in the LD_LIBRARY_PATH
    def setup_dependent_run_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        # Required for enabling asan on dependent packages
        for root, _, files in os.walk(self.prefix):
            if "libclang_rt.asan-x86_64.so" in files:
                env.prepend_path("LD_LIBRARY_PATH", root)
        env.prune_duplicate_paths("LD_LIBRARY_PATH")

    @run_after("install")
    def post_install(self):
        if self.spec.satisfies("@6.1:7.0 +rocm-device-libs"):
            exe = self.prefix.bin.join("llvm-config")
            output = Executable(exe)("--version", output=str, error=str)
            version = re.split("[.]", output)[0]
            mkdirp(join_path(self.prefix.lib.clang, version, "lib"), "amdgcn")
            install_tree(
                self.prefix.amdgcn, join_path(self.prefix.lib.clang, version, "lib", "amdgcn")
            )
            shutil.rmtree(self.prefix.amdgcn)
            symlink(
                join_path(self.prefix.lib.clang, version, "lib", "amdgcn"),
                os.path.join(self.prefix, "amdgcn"),
            )

        cfg_files = ["clang.cfg", "clang++.cfg"]
        if self.spec.satisfies("@7:"):
            cfg_files.append("flang.cfg")
        gcc_install_dir_flag = get_gcc_install_dir_flag(self.spec, self.compiler)
        if gcc_install_dir_flag:
            for cfg in cfg_files:
                with open(os.path.join(self.prefix.bin, cfg), "w") as f:
                    print(gcc_install_dir_flag, file=f)

    # Required for enabling asan on dependent packages
    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        for root, _, files in os.walk(self.prefix):
            if "libclang_rt.asan-x86_64.so" in files:
                env.prepend_path("LD_LIBRARY_PATH", root)
        env.prune_duplicate_paths("LD_LIBRARY_PATH")

    def _cc_path(self):
        return os.path.join(self.spec.prefix.bin, "amdclang")

    def _cxx_path(self):
        return os.path.join(self.spec.prefix.bin, "amdclang++")

    def _fortran_path(self):
        return os.path.join(self.spec.prefix.bin, "amdflang")


def get_gcc_install_dir_flag(spec: Spec, compiler) -> Optional[str]:
    """Get the --gcc-install-dir=... flag, so that clang does not do a system scan for GCC."""
    if not spec.satisfies("%gcc"):
        return None
    gcc = Executable(compiler.cc)
    libgcc_path = gcc("-print-file-name=libgcc.a", output=str, fail_on_error=False).strip()
    if not os.path.isabs(libgcc_path):
        return None
    libgcc_dir = os.path.dirname(libgcc_path)
    return f"--gcc-install-dir={libgcc_dir}" if os.path.exists(libgcc_dir) else None
