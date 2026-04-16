# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.rocm import ROCmPackage
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


class RocmTensile(CMakePackage):
    """Radeon Open Compute Tensile library"""

    homepage = "https://github.com/ROCm/Tensile/"
    git = "https://github.com/ROCm/Tensile.git"
    url = "https://github.com/ROCm/Tensile/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    license("MIT")

    maintainers("srekolam", "renjithravindrankannath", "haampie", "afzpatel")
    version("7.2.1", sha256="9d7757997b09c80a450a81dc48046408433d79d78f72ba362ee0afd721788b2e")
    version("7.2.0", sha256="e09cfe77fc0b9198e3dd0530214599b1bf849a8bd36031a734f0e591aafb7caf")
    version("7.1.1", sha256="12e3b538efe2069ecd77dfd0bc9309d6f067eab002f153ddbf8b20896ee46ec3")
    version("7.1.0", sha256="853b92723750ee2249d8f7aedb1e367a97fb3b9fe4b3741d67e8c1bee7cd97cb")
    version("7.0.2", sha256="6c87c6a0795d54051aaad97c4467ee1a298ce24ddf450a287f9496df8ab3b6d3")
    version("7.0.0", sha256="1b825a8b79822adafb2d9747b1e4ff78ce14a71561b02048fe134eecf224714c")
    version("6.4.3", sha256="0190bfc7050c6ea73fb20ce4d35a056644e129f792f3b016b079ee6cc237a598")
    version("6.4.2", sha256="0c30d711ed09f53af9509e264addad9be25e897a7ad490752741cb848a2f31e6")
    version("6.4.1", sha256="f96fe39fbb0d43e39b258b21d66234abf3248f8cfa6954f922618d4bb7d04c74")
    version("6.4.0", sha256="cfe32aa31aa0dd79018d0cdd36e09df3a548159cb7b8e18d0ef6513d0febce90")
    version("6.3.3", sha256="5849fc3898e9cea05569c0ee102c13043c4df67079119572687bc42f274ae496")
    version("6.3.2", sha256="700e43a22d7e6309bf74624b18a42bb0132ef35716fccec897d3045a97759e6a")
    version("6.3.1", sha256="9882e8f949e1eb1d4b7dbd215370ecce643852dd2ce6e021d59cd49d32ba9dea")
    version("6.3.0", sha256="7ae90d1a513dc6f000a45f644b360305ef212ab3dff7b0217b6addabebf932e1")
    version("6.2.4", sha256="dd0721e4371c8752aa4b14362f75d7ebb7805f57dcb990e03ae08cef4a291383")
    version("6.2.1", sha256="29802dc65a7cea29f0e2608782c75db87e9c71eea8aeb485e856cf2861d83098")
    version("6.2.0", sha256="6f7d679bfffd1f723f2788b00fdcb1b4673b597f9f85c2cdaab3c2aa17afb33d")
    version("6.1.2", sha256="6a08190f6d9c8cc76764a68e2dd3e7af4759d4146ddc1c4b3370c7762a6f6d83")
    version("6.1.1", sha256="04fd76e6a0e9b7528e61df0721b03c0e977c145a2a1ea331d515c9167d7ac35f")
    version("6.1.0", sha256="69bfdc711d3a86e6651b1dcfb2c461c7d3ae574e6d884833d4e07d3e7ad06491")
    version("6.0.2", sha256="1d8a92422560c1e908fa25fd97a4aa07a96659528a543f77618408ffcfe1f307")
    version("6.0.0", sha256="5d90add62d1439b7daf0527316e950e454e5d8beefb4f723865fe9ab26c7aa42")
    version("5.7.1", sha256="9211a51b23c22b7a79e4e494e8ff3c31e90bf21adb8cce260acc57891fb2c917")
    version("5.7.0", sha256="fe2ae067c1c579f33d7a1e26da3fe6b4ed44befa08f9dfce2ceae586f184b816")

    amdgpu_targets = ROCmPackage.amdgpu_targets

    variant(
        "amdgpu_target",
        description="AMD GPU architecture",
        values=auto_or_any_combination_of(*amdgpu_targets),
        sticky=True,
    )

    tensile_architecture = (
        "all",
        "gfx906:xnack-",
        "gfx908:xnack-",
        "gfx90a:xnack-",
        "gfx1010",
        "gfx1011",
        "gfx1012",
        "gfx1030",
    )

    variant(
        "tensile_architecture",
        default="all",
        description="AMD GPU architecture",
        values=tensile_architecture,
        multi=True,
    )
    variant("openmp", default=True, description="Enable OpenMP")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3:", type="build")
    depends_on("msgpack-c@3:")
    depends_on("boost", type=("build", "link"))
    depends_on(Boost.with_default_variants)

    for ver in [
        "5.7.0",
        "5.7.1",
        "6.0.0",
        "6.0.2",
        "6.1.0",
        "6.1.1",
        "6.1.2",
        "6.2.0",
        "6.2.1",
        "6.2.4",
        "6.3.0",
        "6.3.1",
        "6.3.2",
        "6.3.3",
        "6.4.0",
        "6.4.1",
        "6.4.2",
        "6.4.3",
        "7.0.0",
        "7.0.2",
        "7.1.0",
        "7.1.1",
        "7.2.0",
        "7.2.1",
    ]:
        depends_on(f"rocm-cmake@{ver}", type="build", when=f"@{ver}")
        depends_on(f"hip@{ver}", when=f"@{ver}")
        depends_on(f"comgr@{ver}", when=f"@{ver}")
        depends_on(f"rocminfo@{ver}", type="build", when=f"@{ver}")
        depends_on(f"rocm-openmp-extras@{ver}", when=f"@{ver}")
        depends_on(f"rocm-smi-lib@{ver}", type="build", when=f"@{ver}")

    root_cmakelists_dir = "Tensile/Source"

    patch("0003-require-openmp-extras-when-tensile-use-openmp.patch")
    patch("0004-replace_rocm_smi.patch", when="@6.4:")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("@7.1:"):
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++")
        else:
            env.set("CXX", self.spec["hip"].hipcc)
        env.append_flags("LDFLAGS", "-pthread")

    def get_gpulist_for_tensile_support(self):
        arch = self.spec.variants["tensile_architecture"].value
        return self.tensile_architecture[1:] if arch[0] == "all" else arch

    def cmake_args(self):
        args = [
            self.define("amd_comgr_DIR", self.spec["comgr"].prefix),
            self.define("Tensile_COMPILER", "hipcc"),
            self.define("Tensile_LOGIC", "asm_full"),
            self.define("Tensile_CODE_OBJECT_VERSION", "V3"),
            self.define("Boost_USE_STATIC_LIBS", "OFF"),
            self.define_from_variant("TENSILE_USE_OPENMP", "openmp"),
            self.define("BUILD_WITH_TENSILE_HOST", True),
            self.define("Tensile_LIBRARY_FORMAT", "msgpack"),
            self.define("TENSILE_USE_OPENMP", True),
            self.define("ROCM_OPENMP_EXTRAS_DIR", self.spec["rocm-openmp-extras"].prefix),
        ]

        if self.spec.satisfies("^cmake@3.21.0:"):
            args.append(
                self.define("CMAKE_HIP_ARCHITECTURES", self.get_gpulist_for_tensile_support())
            )
        else:
            args.append(
                self.define("Tensile_ARCHITECTURE", self.get_gpulist_for_tensile_support())
            )

        if self.spec.satisfies("^cmake@3.21.0:3.21.2"):
            args.append(self.define("__skip_rocmclang", "ON"))

        if self.spec.satisfies("@7.1:"):
            args.append(
                self.define("CMAKE_MODULE_PATH", f"{self.stage.source_path}/next-cmake/cmake")
            )
        if "auto" not in self.spec.variants["amdgpu_target"]:
            args.append(self.define_from_variant("GPU_TARGETS", "amdgpu_target"))
        return args

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            install_tree("./client", prefix.client)
            install_tree("./lib", prefix.lib)
