# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (NVIDIA Software License Agreement)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *

import os

class CudaSamples(CMakePackage, MakefilePackage, CudaPackage):
    """Samples for CUDA Developers which demonstrates features in CUDA
    Toolkit."""

    homepage = "https://github.com/NVIDIA/cuda-samples"
    git = "https://github.com/NVIDIA/cuda-samples.git"
    url = "https://github.com/NVIDIA/cuda-samples/archive/refs/tags/v13.0.tar.gz"

    # Not sure if I can take the responsibility;
    # I just added it since running benchmarks on HPC need it now.
    #maintainers("guanyuming-he")

    # This is a proprietary license. See 
    # https://spack.readthedocs.io/en/latest/
    # packaging_guide_creation.html#proprietary-software
    license_required = True
    license_comment = "#"
    license_files = ["LICENSE"]
    license_vars = []
    license_url = (
        "https://www.nvidia.com/en-us/agreements/"
        "enterprise-software/nvidia-software-license-agreement/"
    )

    # Update this as CUDA is updated in Spack.
    # Can execute `spack checksum cuda-samples`
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
    for v,h in _ver_map.items():
        version(v, sha256=h)
        depends_on("cuda@"+v, when="@"+v)

    # Don't need this variant now as CUDA is always required.
    #variant("cuda", default=True, description="build using CUDA (required)")

	# Allows one to specify the compilers to use. Please do specify it
	# explicitly if the default is ambiguous.
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # cuda-samples changed build systems starting with 12.8
    build_system(
        conditional("cmake", when="@12.8:"),
        conditional("makefile", when="@:12.5"),
        default="cmake",
    )

    # After the change to CMake, the build defaults to all GPU arches
    # supported by the NVCC it depends on
    conflicts("cuda_arch=none", when="@:12.5+cuda", 
        msg="Please specify cuda_arch as variant for installation.\n"
            "You can query it with \n"
            "nvidia-smi --query-gpu=name,compute_cap --format=csv"
    )

    @when("@:12.5")
    def setup_build_environment(self, env):
        env.set("CUDA_PATH", self.spec["cuda"].prefix)
        env.set("SMS", self.spec.variants["cuda_arch"].value[0])

    @when("@12.8:")
    def cmake_args(self):
        args = ["-DCUDAToolkit_ROOT=" + self.spec["cuda"].prefix]
        return args

    # cuda-samples doesn't actually install the samples in the
    # CMAKE_INSTALL_PREFIX dir, so this copies them
    @when("@12.8:")
    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree(
            os.path.join(self.stage.source_path, "Samples"),
            prefix.bin
        )
        # Don't forget to install the common files!
        mkdir(prefix.common)
        install_tree(
            os.path.join(self.stage.source_path, "Common"),
            prefix.common
        )
        

    # Similar to the CMake version, the Make version doesn't have an install
    # phase but instead just creates binaries in a `bin` folder under the build
    # directory
    @when("@:12.5")
    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree("bin", prefix.bin)
        # Don't forget to install the common files!
        mkdir(prefix.common)
        install_tree(
            os.path.join(self.stage.source_path, "Common"),
            prefix.common
        )
        
