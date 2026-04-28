# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re
import sys

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class RocmOpencl(CMakePackage):
    """OpenCL: Open Computing Language on ROCclr"""

    homepage = "https://github.com/ROCm/clr"
    url = "https://github.com/ROCm/clr/archive/refs/tags/rocm-6.4.3.tar.gz"
    git = "https://github.com/ROCm/clr.git"

    tags = ["rocm"]
    maintainers("srekolam", "renjithravindrankannath", "afzpatel")
    libraries = ["libamdocl64"]
    license("MIT")

    def url_for_version(self, version):
        if version <= Version("7.1.1"):
            url = "https://github.com/ROCm/clr/archive/rocm-{0}.tar.gz"
        else:
            url = "https://github.com/ROCm/rocm-systems/archive/rocm-{0}.tar.gz"
        return url.format(version)

    version("7.2.1", sha256="201f19174eafbace2f7abf0d1178ebb17db878191276aba6d23f0e1758b0e10f")
    version("7.2.0", sha256="728ea7e9bf16e6ed217a0fd1a8c9afaba2dae2e7908fa4e27201e67c803c5638")
    version("7.1.1", sha256="b09539ef53a775c03352f9843f3a346e4f2ad3941c1954e953d352e4984ee708")
    version("7.1.0", sha256="d53ee72dd430c934a53b1fe5c798ac34c53e8826589f8f9f214419512059ad2d")
    version("7.0.2", sha256="b49b1ccbf86ef78f4da5ff13ec3ee94f6133c55db3a95b823577b0808db5f2f1")
    version("7.0.0", sha256="cc417e73cda903511db5a72b77704fd41bf7b39204c5cacb2c64701b344b8c5d")
    version("6.4.3", sha256="aa7c9d9d7da3b5fc944b17ca7c032e8924a8dc327ec79eb8cb7f0c9df6fa76dc")
    version("6.4.2", sha256="6dca1ffff36dbf8665594a72b47b8dd0362f7ee446dea03961d8b5a639bf3ede")
    version("6.4.1", sha256="18ee75a04f6fc55e72f8b3fcad1e0d58eceb2ce0e0696ca76d9b3dfaf4bfd7ff")
    version("6.4.0", sha256="76fd0ad83da0dabf7c91ca4cff6c51f2be8ab259e08ad9743af47d1b3473c2ff")
    version("6.3.3", sha256="8e5adca8f8c2d99d4a4e49605dd6b56b7881b762ee8ce15b4a7000e3cd982fec")
    version("6.3.2", sha256="ec13dc4ffe212beee22171cb2825d2b16cdce103c835adddb482b9238cf4f050")
    version("6.3.1", sha256="bfb8a4a59e7bd958e2cd4bf6f14c6cdea601d9827ebf6dc7af053a90e963770f")
    version("6.3.0", sha256="829e61a5c54d0c8325d02b0191c0c8254b5740e63b8bfdb05eec9e03d48f7d2c")
    version("6.2.4", sha256="0a3164af7f997a4111ade634152957378861b95ee72d7060eb01c86c87208c54")
    version("6.2.1", sha256="e9cff3a8663defdbda833d49c9e7160171eca14dc285ffe4061378607d6c890d")
    version("6.2.0", sha256="620e4c6a7f05651cc7a170bc4700fef8cae002420307a667c638b981d00b25e8")
    version("6.1.2", sha256="1a1e21640035d957991559723cd093f0c7e202874423667d2ba0c7662b01fea4")
    version("6.1.1", sha256="2db02f335c9d6fa69befcf7c56278e5cecfe3db0b457eaaa41206c2585ef8256")
    version("6.1.0", sha256="49b23eef621f4e8e528bb4de8478a17436f42053a2f7fde21ff221aa683205c7")
    version("6.0.2", sha256="cb8ac610c8d4041b74fb3129c084f1e7b817ce1a5a9943feca1fa7531dc7bdcc")
    version("6.0.0", sha256="798b55b5b5fb90dd19db54f136d8d8e1da9ae1e408d5b12b896101d635f97e50")
    version("5.7.1", sha256="c78490335233a11b4d8a5426ace7417c555f5e2325de10422df06c0f0f00f7eb")
    version("5.7.0", sha256="bc2447cb6fd86dff6a333b04e77ce85755104d9011a14a044af53caf02449573")

    variant("asan", default=False, description="Build with address-sanitizer enabled or disabled")

    conflicts("+asan", when="os=rhel9")
    conflicts("+asan", when="os=centos7")
    conflicts("+asan", when="os=centos8")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("cmake@3:", type="build")
    depends_on("gl@4.5:", type="link")
    depends_on("numactl", type="link")
    depends_on("libx11", when="+asan")
    depends_on("xproto", when="+asan")
    depends_on("opencl-icd-loader@2024.05.08", when="@6.2:")

    # For avx build, the start address of values_ buffer in KernelParameters is not
    # correct as it is computed based on 16-byte alignment.
    patch(
        "https://github.com/ROCm/clr/commit/c4f773db0b4ccbbeed4e3d6c0f6bff299c2aa3f0.patch?full_index=1",
        sha256="5bb9b0e08888830ccf3a0a658529fe25f4ee62b5b8890f349bf2cc914236eb2f",
        when="@5.7:6.0",
    )
    patch(
        "https://github.com/ROCm/clr/commit/7868876db742fb4d44483892856a66d2993add03.patch?full_index=1",
        sha256="7668b2a710baf4cb063e6b00280fb75c4c3e0511575e8298a9c7ae5143f60b33",
        when="@5.7:6.0",
    )

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
        depends_on(f"comgr@{ver}", type="build", when=f"@{ver}")
        depends_on(f"hsa-rocr-dev@{ver}", type="link", when=f"@{ver}")
        depends_on(f"rocm-core@{ver}", when=f"@{ver}")

    for ver in [
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
    ]:
        depends_on(f"aqlprofile@{ver}", type="link", when=f"@{ver}")

    for ver in ["7.0.0", "7.0.2", "7.1.0", "7.1.1", "7.2.0", "7.2.1"]:
        depends_on(f"hsa-amd-aqlprofile@{ver}", type="link", when=f"@{ver}")

    @property
    def root_cmakelists_dir(self):
        if self.spec.satisfies("@7.2:"):
            return "projects/clr"
        else:
            return "."

    @classmethod
    def determine_version(cls, lib):
        match = re.search(r"lib\S*\.so\.\d+\.\d+\.(\d)(\d\d)(\d\d)", lib)
        if match:
            return "{0}.{1}.{2}".format(
                int(match.group(1)), int(match.group(2)), int(match.group(3))
            )
        else:
            ver = None
        return ver

    def cmake_args(self):
        args = ["-DUSE_COMGR_LIBRARY=yes", "-DBUILD_TESTS=ON"]
        args.append(self.define("CLR_BUILD_HIP", False))
        args.append(self.define("CLR_BUILD_OCL", True))
        if self.spec.satisfies("+asan"):
            args.append(
                self.define(
                    "CMAKE_CXX_FLAGS",
                    f"-I{self.spec['libx11'].prefix.include} "
                    f"-I{self.spec['mesa'].prefix.include} "
                    f"-I{self.spec['xproto'].prefix.include}",
                )
            )
        if self.spec.satisfies("@6.2:"):
            args.append(self.define("BUILD_ICD", False))
            args.append(self.define("AMD_ICD_LIBRARY_DIR", self.spec["opencl-icd-loader"].prefix))

        return args

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+asan"):
            env.set("CC", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang")
            env.set("CXX", f"{self.spec['llvm-amdgpu'].prefix}/bin/clang++")
            env.set("ASAN_OPTIONS", "detect_leaks=0")
            env.set("CFLAGS", "-fsanitize=address -shared-libasan")
            env.set("CXXFLAGS", "-fsanitize=address -shared-libasan")
            env.set("LDFLAGS", "-fuse-ld=lld")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.lib)
        env.set("OCL_ICD_VENDORS", self.prefix.vendors + "/")

    @run_after("install")
    def post_install(self):
        vendor_config_path = join_path(self.prefix + "/vendors")
        mkdirp(vendor_config_path)

        config_file_name = "amdocl64_30800.icd"
        with open(join_path(vendor_config_path, config_file_name), "w") as f:
            f.write("libamdocl64.so")

    def test_ocltst(self):
        """Run ocltst checks"""
        test_dir = "tests/ocltst" if sys.platform == "win32" else "share/opencl/ocltst"

        os.environ["LD_LIBRARY_PATH"] += os.pathsep + join_path(self.prefix, test_dir)

        ocltst = which(join_path(self.prefix, test_dir, "ocltst"), required=True)
        with test_part(self, "test_ocltst_runtime", purpose="check runtime"):
            ocltst("-m", "liboclruntime.so", "-A", "oclruntime.exclude")

        with test_part(self, "test_ocltst_perf", purpose="check perf"):
            ocltst("-m", "liboclperf.so", "-A", "oclperf.exclude")
