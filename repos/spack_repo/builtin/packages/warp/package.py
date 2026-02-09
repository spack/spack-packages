# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# from spack_repo.builtin.build_systems.package import Package
import shlex
import shutil

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Warp(CMakePackage, CudaPackage):
    """Warp is a set of tools for cryo-EM and cryo-ET data processing
    including, among other tools: Warp, M, WarpTools, MTools, MCore, and
    Noise2Map."""

    homepage = "https://warpem.github.io/"
    url = "https://github.com/warpem/warp/archive/refs/tags/v2.0.0dev36.tar.gz"

    maintainers("Markus92")

    license("GPL-3", checked_by="Markus92")

    version(
        "2.0.0dev36", sha256="a50b019bbe2143d3709c4782db3e689455b94eb7162b5f8dd955996e9710a291"
    )

    # The source is riddled with calls to avx intrinsics, so make sure target supports it
    conflicts("target=:k10")  # last AMD processor not to support avx
    conflicts("target=:westmere")  # last Intel processor not to support avx
    conflicts("target=:x86_64_v2")  # last generic architecture not to support avx
    requires("target=x86_64:")  # Block non-x86_64 targets

    variant("cuda", default=True, description="Build with CUDA")
    conflicts("~cuda", msg="Cuda is required.")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.18:", type="build")
    depends_on("gmake", type="build")
    depends_on("patchelf", type=("build", "link"))
    depends_on("dotnet-core-sdk", type=("build"))

    depends_on("cuda@11.8:11", type=("build", "link"))
    depends_on("fftw@3 ~mpi precision=float", type=("build", "link"))
    depends_on("libtiff +shared")
    depends_on("python@3.11")
    depends_on("cudnn@8.7.0")
    depends_on("py-torch@2.0.1 +cuda")

    # Link dependencies for libSkiaSharp.so
    depends_on("fontconfig@2:", type="link")
    depends_on("freetype@2.10: +shared", type="link")
    depends_on("libxml2@2.9.13: +shared", type="link")
    depends_on("bzip2 +shared", type="link")
    depends_on("libpng libs=shared", type="link")
    depends_on("zlib +shared", type="link")
    depends_on("harfbuzz@2.7.4: default_library=shared", type="link")
    depends_on("brotli", type="link")
    depends_on("xz libs=shared", type="link")
    depends_on("glib@2: default_library=shared", type="link")
    depends_on("graphite2@1.3.14:", type="link")
    depends_on("pcre +shared", type="link")

    # Patch adds install target and creates a project-wide CMakeLists.txt
    patch("cmakelists.patch")
    patch(
        "https://github.com/warpem/warp/commit/f41372135e97e2d5cab1e4b66bc9b44cfcda23f6.patch?full_index=1",
        sha256="0309fd44d125f3f212381e99ab10e5a28d8630347a88d73341b983dfba972f9a",
    )

    @run_before("cmake")
    def set_cuda_archs(self) -> None:
        cuda_targets = ";".join(self.spec.variants["cuda_arch"].value)
        filter_file(
            r"^set_target_properties\(NativeAcceleration PROPERTIES CUDA_ARCHITECTURES"
            + r'\d+(?:;\d+)*"\)$',
            "set_target_properties(NativeAcceleration"
            + f'PROPERTIES CUDA_ARCHITECTURES "{cuda_targets}")',
            "NativeAcceleration/CMakeLists.txt",
        )

    def cmake_args(self):
        spec = self.spec
        args = []
        args.append(f"-DTorch_DIR=f{join_path(self['py-torch'].cmake_prefix_paths[0], 'Torch')}")
        return args

    @property
    def cuda_arch(self):
        cuda_arch = ";".join(self.spec.variants["cuda_arch"].value)
        if cuda_arch == "none":
            raise InstallError("Must select at least one value for cuda_arch")
        return cuda_arch

    # Build the .NET source code
    @run_before("build")
    def build_dotnet(self) -> None:
        dotnet = Executable("dotnet")
        for tool in [
            "Noise2Map/Noise2Map.csproj",
            "Noise2Mic/Noise2Mic.csproj",
            "Noise2Tomo/Noise2Tomo.csproj",
            "Noise2Half/Noise2Half.csproj",
            "EstimateWeights/EstimateWeights.csproj",
            "Frankenmap/Frankenmap.csproj",
            "MrcConverter/MrcConverter.csproj",
            "WarpWorker/WarpWorker.csproj",
            "WarpTools/WarpTools.csproj",
            "MTools/MTools.csproj",
            "MCore/MCore.csproj",
        ]:
            dotnet(
                "publish",
                "-nowarn:CS0219,CS0162,CS0168,CS0649,CS0067,CS0414,"
                + "CS0661,CS0659,CS0169,CS0618,CS1998,MSB3270,SYSLIB0011",
                "--configuration",
                "Release",
                "--framework",
                "net8.0",
                "--self-contained",
                "true",
                "/p:PublishSingleFile=true",
                "/p:DebugType=None",
                "-o",
                self.spec.prefix.bin,
                tool,
            )

    @run_after("install")
    def ensure_rpaths(self):
        # Patch the .NET rpath
        patchelf = Executable("patchelf")
        with working_dir(self.spec.prefix.bin):
            for tool in [
                "EstimateWeights",
                "Frankenmap",
                "MCore",
                "MrcConverter",
                "MTools",
                "Noise2Half",
                "Noise2Map",
                "Noise2Mic",
                "Noise2Tomo",
                "WarpTools",
                "WarpWorker",
            ]:
                patchelf("--add-rpath", self.spec.prefix.lib, tool)

        # .NET stores one of the libs in the output bin
        shutil.move(join_path(self.spec.prefix.bin, "libSkiaSharp.so"), self.spec.prefix.lib)

        skia_libs = [
            "fontconfig",
            "freetype",
            "libxml2",
            "bzip2",
            "libpng",
            "zlib",
            "harfbuzz",
            "xz",
            "glib",
            "graphite2",
            "pcre",
        ]
        for dependency in skia_libs:
            for libdir in self.spec[dependency].libs.directories:
                patchelf(
                    "--add-rpath",
                    shlex.quote(libdir),
                    join_path(self.spec.prefix.lib, "libSkiaSharp.so"),
                )
        # Brotli complains it cannot find library dir
        patchelf(
            "--add-rpath",
            shlex.quote(self.spec["brotli"].prefix.lib64),
            join_path(self.spec.prefix.lib, "libSkiaSharp.so"),
        )
