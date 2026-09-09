# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class CudaSamples(CMakePackage, MakefilePackage, CudaPackage):
    """Samples for CUDA Developers to demonstrate features of the CUDA Toolkit."""

    homepage = "https://github.com/NVIDIA/cuda-samples"
    git = "https://github.com/NVIDIA/cuda-samples.git"
    url = "https://github.com/NVIDIA/cuda-samples/archive/refs/tags/v13.0.tar.gz"

    maintainers("guanyuming-he")

    license_required = True
    license_files = ["LICENSE"]
    license_url = (
        "https://www.nvidia.com/en-us/agreements/"
        "enterprise-software/nvidia-software-license-agreement/"
    )

    build_system(
        conditional("cmake", when="@12.8:"),
        conditional("makefile", when="@:12.5"),
        default="cmake",
    )

    _ver_map = {
        "13.3": "fab59f405d6c0b87395ce6fc1d46d3f559c380c9a2704ab14d6dc0d3ce1cff16",
        "13.2update": "057e68d22bd02e41d60c9826e7622ac1b88de0f1dbe25ed49bd995f768306f9d",
        "13.2": "c7d8da987a43fd6ed7c2641df204dfc639768adbae070bc22f9df0e03005f7de",
        "13.1": "03d7748a773fcd2350c2de88f2d167252c78ea90a52e229e7eb2a6922e3ba350",
        "13.0": "63cc9d5d8280c87df3c1f4e2276234a0f42cc497c52b40dd5bdda2836607db79",
        "12.9": "2e67e1f6bdb15bf11b21e07e988e2f9f60fb054eff51ef01cebdd47229788015",
        "12.8": "fe82484f9a87334075498f4e023a304cc70f240a285c11678f720f0a1e54a89d",
        "12.5": "5c40cc096706045b067ec5897f039403014aa7a39b970905698466a2d029b972",
        "12.4.1": "01bb311cc8f802a0d243700e4abe6a2d402132c9d97ecf2c64f3fbb1006c304c",
        "12.4": "aa28fa2227768dd31ebbf9cd48b265a0c8810fae03e02c6079c0fa71bbea7319",
    }
    for v, h in _ver_map.items():
        version(v, sha256=h)

    # freeimage is deprecated. Use --deprecated for cuda-samples+freeimage
    variant("freeimage", default=False, description="add samples using freeimage")
    variant("freeglut", default=False, description="add samples using freeglut")

    with default_args(type="build"):
        depends_on("c")
        depends_on("cxx")
        depends_on("cmake@3.10:")

    depends_on("gl")
    depends_on("mesa-glu")
    depends_on("freeglut", when="+freeglut")
    depends_on("freeimage", when="+freeimage")
    for v, _ in _ver_map.items():
        depends_on("cuda@" + v, when="@" + v)

    conflicts("%gcc@15:", when="@:12", msg="GCC 15 is not supported for CUDA <= 12")
    conflicts("%gcc@16:", when="@:13.3", msg="GCC 16 is not supported for CUDA <= 13.3")
    conflicts(
        "cuda_arch=none",
        when="@:12.5+cuda",
        msg="Please specify cuda_arch as variant for installation.\n"
        "cuda_arch is the compute_cap you desire, which can be queried via \n"
        "nvidia-smi --query-gpu=name,compute_cap --format=csv",
    )

    @when("@:12.5")
    def setup_build_environment(self, env):
        spec = self.spec
        glu = sepc["mesa-glu"]
        env.append_flags("CPPFLAGS", f"-I{glu.prefix.include}")
        env.append_flags("LDFLAGS", f"-L{glu.prefix.lib}")
        gl_headers = [
            spec["gl"].headers.directories, glu.headers.directories
        ]
        if spec.satisfies("^libx11"):
            gl_headers += spec['libx11'].headers.directories[0]
            gl_headers += spec['xproto'].headers.directories[0]
        for h in gl_headers:
            env.append_flags("CPPFLAGS", f"-I{h}")
        if sepc.satisfies("+freeglut"):
            freeglut = sepc["freeglut"]
            env.append_flags("CPPFLAGS", f"-I{freeglut.prefix.include}")
            env.append_flags("LDFLAGS", f"-L{freeglut.prefix.lib}")
        if sepc.satisfies("+freeimage"):
            freeimg = sepc["freeimage"]
            env.append_flags("CPPFLAGS", f"-I{freeimg.prefix.include}")
            env.append_flags("LDFLAGS", f"-L{freeimg.prefix.lib}")
        env.set("CUDA_PATH", sepc["cuda"].prefix)
        env.set("SMS", sepc.variants["cuda_arch"].value[0])

    @when("@12.8:")
    def cmake_args(self):
        spec = self.spec
        glu = spec["mesa-glu"]
        gl_headers = ";".join(spec["gl"].headers.directories + glu.headers.directories)
        if spec.satisfies("^libx11"):
            gl_headers += f";{spec['libx11'].headers.directories[0]}"
            gl_headers += f";{spec['xproto'].headers.directories[0]}"
        args = [
            self.define("CUDAToolkit_ROOT", spec["cuda"].prefix),
            self.define("GLU_INCLUDE_DIR", glu.prefix.include),
            self.define("GLU_LIBRARY", glu.libs[0]),
            self.define("OPENGL_INCLUDE_DIR", gl_headers),
            self.define("OPENGL_glu_LIBRARY", glu.libs[0]),
        ]
        if spec.satisfies("+freeglut"):
            freeglut = spec["freeglut"]
            args += [
                self.define("GLUT_INCLUDE_DIR", freeglut.prefix.include),
                self.define("GLUT_freeglut_LIBRARY", freeglut.libs[0]),
            ]
        if spec.satisfies("+freeimage"):
            freeimg = spec["freeimage"]
            args += [
                self.define("FreeImage_INCLUDE_DIR", freeimg.prefix.include),
                self.define("FreeImage_LIBRARY", freeimg.libs[0]),
            ]
        return args

    # Below 13.1, installation is not handled by CMake or the Makefile.
    @when("@12.8:13.0")
    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree(os.path.join(self.build_directory, "Samples"), prefix.bin)
        mkdir(prefix.common)
        install_tree(os.path.join(self.stage.source_path, "Common"), prefix.common)

    @when("@:12.5")
    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree(os.path.join(self.build_directory, "bin"), prefix.bin)
        mkdir(prefix.common)
        install_tree(os.path.join(self.stage.source_path, "Common"), prefix.common)
