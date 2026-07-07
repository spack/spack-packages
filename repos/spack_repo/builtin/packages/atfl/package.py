# Copyright Spack Project Developers. See COPYRIGHT file.
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from pathlib import Path
from typing import ClassVar, Dict

from spack_repo.builtin.build_systems.compiler import CompilerPackage
from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.packages.llvm.package import LlvmDetection

from spack.package import *

_VERSIONS = {
    "22.1.0": {
        "ubuntu22.04": (
            "c691180ffd64acd3aa68b04610283145702d66470ccb1de49b59141727e5da29",
            "https://developer.arm.com/packages/arm-toolchains/ubuntu/pool/arm-toolchain-for-linux_22.1-54~jammy_arm64.deb",
        ),
        "ubuntu24.04": (
            "c5183342da63c780ca0877a7cdebcee982dee86d617bed72518d9e62082a955a",
            "https://developer.arm.com/packages/arm-toolchains/ubuntu/pool/arm-toolchain-for-linux_22.1-54~noble_arm64.deb",
        ),
        "rhel8": (
            "030b4f7456c36cf956ecd82cd7d8b34210f501a9a3214acb9f3c660c1a931fe9",
            "https://developer.arm.com/packages/arm-toolchains/rhel/el8/aarch64/arm-toolchain-for-linux-22.1-54.el8.aarch64.rpm",
        ),
        "rhel9": (
            "596fd8468fe3d132de168e043ca8a29b6c6fead275d2254ee630f2da27d6b1ae",
            "https://developer.arm.com/packages/arm-toolchains/rhel/el9/aarch64/arm-toolchain-for-linux-22.1-54.el9.aarch64.rpm",
        ),
        "rhel10": (
            "89bd818d8d7b3e30f93a3ace60ab3d269a28c2b3b3e3ded31cd76d89877419ec",
            "https://developer.arm.com/packages/arm-toolchains/rhel/el10/aarch64/arm-toolchain-for-linux-22.1-54.el10.aarch64.rpm",
        ),
        "amzn2023": (
            "48c01cd0bd8063eb55709d1a968aa0fb2465f129558974cff7dbe80e0a3d7785",
            "https://developer.arm.com/packages/arm-toolchains/amazonlinux/al2023/aarch64/arm-toolchain-for-linux-22.1-54.al2023.aarch64.rpm",
        ),
        "sles15": (
            "83bab7739d8866453903ed4c9591e34a729e4414517ba290a7af269ed74d862c",
            "https://developer.arm.com/packages/arm-toolchains/sles/sles15/aarch64/arm-toolchain-for-linux-22.1-54.sles15.aarch64.rpm",
        ),
        "sles16": (
            "48225eb252ca6894c83dbe7b4e8adf93bf316b9e93216794defa198dc50b0cc7",
            "https://developer.arm.com/packages/arm-toolchains/sles/sles16/aarch64/arm-toolchain-for-linux-22.1-54.sles16.aarch64.rpm",
        ),
    },
    "21.1.1": {
        "ubuntu22.04": (
            "8132ef95e4671c20a5f2b21dbe2d7ad8ae16137ea634e3e11096a8b87a3ffeee",
            "https://developer.arm.com/packages/arm-toolchains%3Aubuntu-22/jammy/arm64/arm-toolchain-for-linux_21.1-81_arm64.deb",
        ),
        "ubuntu24.04": (
            "18f210fb04f27c50af932e1549deeda394a4ff351f9388957de0b096ab5f1db0",
            "https://developer.arm.com/packages/arm-toolchains%3Aubuntu-24/noble/arm64/arm-toolchain-for-linux_21.1-81_arm64.deb",
        ),
        "rhel8": (
            "c5f0c3f7a25e269160aa3d684cb14edc57252bc38643929c67cda892f1c28dda",
            "https://developer.arm.com/packages/arm-toolchains%3Arhel-8/el8/aarch64/arm-toolchain-for-linux-21.1-81.aarch64.rpm",
        ),
        "rhel9": (
            "3ead2888f8aa71b79a944270b1f7f723f56a7d161aeb2abaad14b3333f91f0e9",
            "https://developer.arm.com/packages/arm-toolchains%3Arhel-9/el9/aarch64/arm-toolchain-for-linux-21.1-81.aarch64.rpm",
        ),
        "rhel10": (
            "a2fc22f18b7ee764ca11af48e6215b43ab47597cc67ba63fcccf0e40f9859a76",
            "https://developer.arm.com/packages/arm-toolchains%3Arhel-10/el10/aarch64/arm-toolchain-for-linux-21.1-81.aarch64.rpm",
        ),
        "amzn2023": (
            "f7bc8c156aaa367dff1d6ced922e90581a04c8bac92e5675cc107eb3cd28428a",
            "https://developer.arm.com/packages/arm-toolchains%3Aamzn-2023/al2023/aarch64/arm-toolchain-for-linux-21.1-81.aarch64.rpm",
        ),
        "sles15": (
            "8de2e35511d7f59a933c40e2e20ed2e01d018f51caba36dc5e9e0c6da71a3619",
            "https://developer.arm.com/packages/arm-toolchains%3Asles-15/sl15/aarch64/arm-toolchain-for-linux-21.1-81.aarch64.rpm",
        ),
    },
    "20.1.0": {
        "ubuntu22.04": (
            "944cf6420fb7b49c52d6c3d6f139fbb4896073ad401204a0cdf609faea360e73",
            "https://developer.arm.com/packages/arm-toolchains%3Aubuntu-22/jammy/arm64/arm-toolchain-for-linux_20.1-65_arm64.deb",
        ),
        "ubuntu24.04": (
            "b9f7db08da8d579daad06999a65136e6b449b79c870a16264fbef1a7ab0cbe6b",
            "https://developer.arm.com/packages/arm-toolchains%3Aubuntu-24/noble/arm64/arm-toolchain-for-linux_20.1-65_arm64.deb",
        ),
        "rhel8": (
            "795e6b74b2b538cc8431ff164c145aa7920ad9394ccf1d544a06667663b70f01",
            "https://developer.arm.com/packages/arm-toolchains%3Arhel-8/el8/aarch64/arm-toolchain-for-linux-20.1-65.aarch64.rpm",
        ),
        "rhel9": (
            "453fc0f4d62968a833499f40a3d04deddbf292c9ff40fd3d246e84ba5b9d7d7a",
            "https://developer.arm.com/packages/arm-toolchains%3Arhel-9/el9/aarch64/arm-toolchain-for-linux-20.1-65.aarch64.rpm",
        ),
        "amzn2023": (
            "87b2031290b9a48b0f2c700aff5f38560f7d1cb7d7f0b0f537ce18965260a54a",
            "https://developer.arm.com/packages/arm-toolchains%3Aamzn-2023/al2023/aarch64/arm-toolchain-for-linux-20.1-65.aarch64.rpm",
        ),
        "sles15": (
            "506a9ddff6d7daf60e1d5b8cfed95f6f25e70db3cc9545d8ea3e9745056740f9",
            "https://developer.arm.com/packages/arm-toolchains%3Asles-15/sl15/aarch64/arm-toolchain-for-linux-20.1-65.aarch64.rpm",
        ),
    },
}


class Atfl(Package, LlvmDetection, CompilerPackage):
    """Arm Toolchain for Linux (ATfL): LLVM-based AArch64 compilers.

    Installs the distro package (RPM/DEB) from Arm's repos, without root.
    """

    maintainers("pawosm-arm")
    homepage = "https://developer.arm.com/documentation/110477"

    _alias: ClassVar[Dict[str, str]] = {"rocky10": "rhel10", "rocky9": "rhel9", "rocky8": "rhel8"}
    for ver, per_os in _VERSIONS.items():
        pkg = per_os.get(_alias.get(host_platform().default_os, host_platform().default_os), None)
        if pkg:
            version(ver, sha256=pkg[0], url=pkg[1], expand=False)

    # Linux AArch64 only
    requires("platform=linux", msg="ATfL is only available on Linux")
    requires("target=aarch64:", msg="ATfL provides AArch64-native compilers")

    provides("c", "cxx")
    provides("fortran")

    # Optional: allow opt-in to lld via the spec. Default is GNU ld for
    # maximum compatibility; packages that prefer lld can request `%atfl+lld`.
    variant("lld", default=False, description="Use lld linker (adds -fuse-ld=lld)")

    # Arm Performance Libraries are required: ATfL's default configuration
    # links against ArmPL (e.g. -fveclib=ArmPL -> -lamath). Ensure it's
    # present and wired into the environment so linking always succeeds.
    depends_on("armpl-gcc~examples", type="run")

    compiler_languages = ["c", "cxx", "fortran"]
    compiler_version_regex = r"Arm Toolchain for Linux [\d\.]+ [cf]lang version ([\d\.]+)"
    c_names = ["armclang"]
    cxx_names = ["armclang++"]
    fortran_names = ["armflang"]
    compiler_wrapper_link_paths = {
        "c": join_path("arm", "armclang"),
        "cxx": join_path("arm", "armclang++"),
        "fortran": join_path("arm", "armflang"),
    }
    implicit_rpath_libs = ["libclang"]
    stdcxx_libs = ("-lstdc++",)

    debug_flags = [
        "-gcodeview",
        "-gdwarf-2",
        "-gdwarf-3",
        "-gdwarf-4",
        "-gdwarf-5",
        "-gline-tables-only",
        "-gmodules",
        "-g",
    ]

    opt_flags = ["-O0", "-O1", "-O2", "-O3", "-Ofast", "-Os", "-Oz", "-Og", "-O", "-O4"]

    def archspec_name(self) -> str:
        """Return the compiler name to use for archspec queries."""
        return "clang"

    def install(self, spec: Spec, prefix: Prefix) -> None:
        """Install the package."""
        archive = self.stage.archive_file
        extract_dir = join_path(self.stage.path, "extract")
        mkdir(extract_dir)
        if archive.endswith(".rpm"):
            Executable("bsdtar")("-xf", archive, "-C", str(extract_dir))
        elif archive.endswith(".deb"):
            Executable("dpkg-deb")("-x", archive, str(extract_dir))
        else:
            raise InstallError(f"Unknown archive type: {archive}")
        src_root = join_path(extract_dir, "opt", "arm", "arm-toolchain-for-linux")

        if not Path(src_root).is_dir():
            raise InstallError(f"Expected payload at {src_root}")

        # We must remove all of the libamath.* symlinks as they reach /opt
        for cand in Path(src_root).rglob("libamath.*"):
            if cand.is_symlink():
                cand.unlink()

        install_tree(str(src_root), prefix)

        with open(join_path(prefix, "bin", "atfl-performance.cfg"), "a") as f:
            # Enable lld if requested. Some system builds (e.g. ncurses with
            # version scripts) are stricter under lld; make this opt-in to
            # maximize compatibility.
            if self.spec.satisfies("+lld"):
                print("-fuse-ld=lld", file=f)

            # ArmPL's libamath must be visible to the compiler.
            # ArmPL directory layout: <prefix>/armpl_<version>_gcc/lib
            armpl_dir = join_path(
                self["armpl-gcc"].prefix, "armpl_" + str(self["armpl-gcc"].version) + "_gcc", "lib"
            )
            print(f"-L{armpl_dir} -Wl,-rpath={armpl_dir}", file=f)

            # Ensure ATfL's own Fortran runtime is available to dependents.
            # At first, Flang was using libFortranRuntime and libFortranDecimal;
            # later toolchains use libflang_rt.runtime. This avoids per-package
            # tweaks.
            fortran_runtime = ""
            fortran_runtime_paths = set()
            for cand in Path(prefix).rglob("libFortranRuntime.*"):
                fortran_runtime = "-lFortranRuntime -lFortranDecimal"
                fortran_runtime_paths.add(str(cand.parent))
            for cand in Path(prefix).rglob("libflang_rt.runtime.*"):
                fortran_runtime = "-lflang_rt.runtime"
                fortran_runtime_paths.add(str(cand.parent))
            for rt_path in fortran_runtime_paths:
                print(f"-L{rt_path} -Wl,-rpath,{rt_path}", file=f)
            print(f"-Wl,--push-state -Wl,--as-needed {fortran_runtime} -Wl,--pop-state", file=f)

    def _cc_path(self) -> str:
        return join_path(self.prefix, "bin", "armclang")

    def _cxx_path(self) -> str:
        return join_path(self.prefix, "bin", "armclang++")

    def _fortran_path(self) -> str:
        return join_path(self.prefix, "bin", "armflang")

    def _standard_flag(self, *, language: str, standard: str) -> str:
        flags = {
            "cxx": {"11": "-std=c++11", "14": "-std=c++14", "17": "-std=c++17"},
            "c": {"99": "-std=c99", "11": "-std=c11"},
        }
        return flags[language][standard]

    def setup_compiler_environment(self, env: EnvironmentModifications) -> None:
        """Set up the build environment for this compiler package."""

        # Prefer LLVM binutils (needed by LTO).
        env.set("AR", join_path(self.prefix, "bin", "llvm-ar"))
        env.set("NM", join_path(self.prefix, "bin", "llvm-nm"))
        env.set("RANLIB", join_path(self.prefix, "bin", "llvm-ranlib"))

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        """Set up the run environment for this package."""
        self.setup_compiler_environment(env)

    def setup_dependent_build_environment(self, env: EnvironmentModifications, _: Spec) -> None:
        """Set up the build environment for packages that depend on this one."""
        self.setup_run_environment(env)
