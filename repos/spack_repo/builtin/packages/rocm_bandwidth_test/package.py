# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RocmBandwidthTest(CMakePackage):
    """Test to measure PciE bandwidth on ROCm platforms"""

    homepage = "https://github.com/ROCm/rocm_bandwidth_test"
    git = "https://github.com/ROCm/rocm_bandwidth_test.git"
    url = "https://github.com/ROCm/rocm_bandwidth_test/archive/rocm-6.4.3.tar.gz"
    tags = ["rocm"]

    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    version(
        "7.1.1",
        git="https://github.com/ROCm/rocm_bandwidth_test",
        tag="rocm-7.1.1",
        commit="bba00e25cc49f8cda357cfe0439f0e01ba8839bb",
        submodules=True,
    )
    version(
        "7.1.0",
        git="https://github.com/ROCm/rocm_bandwidth_test",
        tag="rocm-7.1.0",
        commit="9f0a001fa5cfcbe6ecdf2e96fd91eacb371a8a1e",
        submodules=True,
    )
    version(
        "7.0.2",
        git="https://github.com/ROCm/rocm_bandwidth_test",
        tag="rocm-7.0.2",
        commit="ae9cd3f755553027bf799f9bb71c11a6c556d366",
        submodules=True,
    )
    version(
        "7.0.0",
        git="https://github.com/ROCm/rocm_bandwidth_test",
        tag="rocm-7.0.0",
        commit="49a72abaaaadb9934d6bcc96ac70663d7cca02f3",
        submodules=True,
    )
    version("6.4.3", sha256="2b8d9eb16191e9d8dcfdc345615298b36b8e7d468f1b40d46638989301b03688")
    version("6.4.2", sha256="70cd7918dd07564241576e4ae8a4c5d007f87aa3d93589baded49022dc2cf27b")
    version("6.4.1", sha256="6910f52af9416802245d4fb6406274fd2bde6e9c287cc2d602adf682ecf98e4e")
    version("6.4.0", sha256="0a4c8aa32e041f0344eda448927d677b4a65835dda9736a7f2ab72b8e7f14d1c")
    version("6.3.3", sha256="d33f656eb6ba7db78b41c4bcf6d830b511dc97c6d645760e6d05edd07fcaefba")
    version("6.3.2", sha256="3754831244d7c4f6314fc25b3e929adf9abe44c9cb60621dd8ae5d1aa930ae55")
    version("6.3.1", sha256="98002e4104929a62a308114ed82fba530880359a17f90ebd62a2ca49c2baac78")
    version("6.3.0", sha256="6d1e444b962e7a40fb9f20c87631865d3e04e8c9027fd21b439bee9b62d0070c")
    version("6.2.4", sha256="4d25c62d81f60eba8042f57ca0905adc853a214333ffc70238d91e2f53606a79")
    version("6.2.1", sha256="042cfe3adc0f0ad0b8620e361b2846eb57c7b54837ed7a8c3a773e6fdc4e1af4")
    version("6.2.0", sha256="ca4caa4470c7ad0f1a4963072c1a25b0fd243844a72b26c83fcbca1e82091a41")
    version("6.1.2", sha256="4259d53350d6731613d36c03593750547f84f084569f8017783947486b8189da")
    version("6.1.1", sha256="01da756228f2bfb5e25ddb74b75a5939693b1b4f4559f37cfc85729e36a98450")
    version("6.1.0", sha256="b06522efbd1a55247412c8f535321058e2463eab4abd25505c37e8c67941ae26")
    version("6.0.2", sha256="af95fe84729701184aeb14917cee0d8d77ab1858ddcced01eb7380401e2134ae")
    version("6.0.0", sha256="9023401bd6a896059545b8e6263c6730afd89d7d45c0f5866261c300415532a6")
    version("5.7.1", sha256="7426ef1e317b8293e4d6389673cfa8c63efb3f7d061e2f50a6f0b1b706e2a2a7")
    version("5.7.0", sha256="fa95c28488ab4bb6d920b9f3c316554ca340f44c87ec2efb4cf8fa488e63ddd9")

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3:", type="build")
    depends_on("curl", when="@7.0:")
    depends_on("numactl", when="@7.0:")

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
    ]:
        depends_on(f"hsakmt-roct@{ver}", when=f"@{ver}")

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
    ]:
        depends_on(f"hsa-rocr-dev@{ver}", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    for ver in ["7.0.0", "7.0.2", "7.1.0", "7.1.1"]:
        depends_on(f"llvm-amdgpu@{ver}", when=f"@{ver}")
        depends_on(f"hip@{ver}", when=f"@{ver}")

    patch("add_numa_hsa.patch", when="@7.0.0")
    patch("modify_hsa_include.patch", when="@7.0.2:")

    # https://github.com/ROCm/rocm_bandwidth_test/issues/131
    # install doesnt honour CMAKE_INSTALL_PREFIX
    patch("change_install_path.patch", when="@7.0.0")
    patch("change_install_path_7.0.2.patch", when="@7.0.2:")

    @property
    def build_targets(self):
        targets = []
        if self.spec.satisfies("@:6.4.3"):
            targets.append("package")
        return targets

    def cmake_args(self):
        args = []
        if self.spec.satisfies("@7.0:"):
            args.append(
                self.define("CMAKE_C_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang")
            )
            args.append(
                self.define(
                    "CMAKE_CXX_COMPILER", f"{self.spec['llvm-amdgpu'].prefix}/bin/amdclang++"
                )
            )
            args.append(self.define("AMD_APP_STANDALONE_BUILD_PACKAGE", "ON"))
            args.append(self.define("NUMA_INCLUDE_DIR", self.spec["numactl"].prefix.include))
            args.append(self.define("HSA_INCLUDE_DIR", self.spec["hsa-rocr-dev"].prefix.include))
        return args
