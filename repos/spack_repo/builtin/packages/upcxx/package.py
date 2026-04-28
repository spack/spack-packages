# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.generic import Package
from spack_repo.builtin.build_systems.rocm import ROCmPackage

from spack.package import *


@memoized
def is_CrayXC():
    return host_platform().name == "linux" and (os.environ.get("CRAYPE_NETWORK_TARGET") == "aries")


@memoized
def is_CrayEX():
    if host_platform().name == "linux":
        target = os.environ.get("CRAYPE_NETWORK_TARGET")
        if target in ["ofi", "ucx"]:  # normal case
            return True
        elif target is None:  # but some systems lack Cray PrgEnv
            fi_info = which("fi_info")
            if (
                fi_info
                and fi_info("-l", output=str, error=str, fail_on_error=False).find("cxi") >= 0
            ):
                return True
    return False


@memoized
def cross_detect():
    if is_CrayXC():
        if which("srun"):
            return "cray-aries-slurm"
        if which("aprun"):
            return "cray-aries-alps"
    return "none"


class Upcxx(Package, CudaPackage, ROCmPackage):
    """UPC++ is a C++ library that supports Partitioned Global Address Space
    (PGAS) programming, and is designed to interoperate smoothly and
    efficiently with MPI, OpenMP, CUDA, ROCm/HIP and AMTs. It leverages GASNet-EX to
    deliver low-overhead, fine-grained communication, including Remote Memory
    Access (RMA) and Remote Procedure Call (RPC)."""

    homepage = "https://upcxx.lbl.gov"
    maintainers("bonachea")
    url = "https://bitbucket.org/berkeleylab/upcxx/downloads/upcxx-2021.3.0.tar.gz"
    git = "https://bitbucket.org/berkeleylab/upcxx.git"

    tags = ["e4s", "ecp"]

    license("BSD-3-Clause-LBNL")

    version("develop", branch="develop")
    version("master", branch="master")

    version("2025.10.0", sha256="bb43348d351777b7462e6bbadda358b426cd150e138ac08ee74649b91bba32ec")
    version("2023.9.0", sha256="6bad2976b4bfc0263b497daa967f448159c3c2259827c8376bc96c9bf9171a83")
    with default_args(deprecated=True):
        version(
            "2023.3.0", sha256="382af3c093decdb51f0533e19efb4cc7536b6617067b2dd89431e323704a1009"
        )
        version(
            "2022.9.0", sha256="dbf15fd9ba38bfe2491f556b55640343d6303048a117c4e84877ceddb64e4c7c"
        )
        version(
            "2022.3.0", sha256="72bccfc9dfab5c2351ee964232b3754957ecfdbe6b4de640e1b1387d45019496"
        )
    # Do NOT add older versions here.
    # UPC++ releases over 2 years old are not supported.
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("gmake", type="build")

    patch("fix_configure_ldflags.patch", when="@:2023.9.0")

    variant("mpi", default=False, description="Enables MPI-based spawners and mpi-conduit")

    variant(
        "cuda",
        default=False,
        description="Enables UPC++ support for the CUDA memory kind on NVIDIA GPUs.\n"
        + "NOTE: Requires CUDA Driver library be present on the build system",
    )

    variant(
        "rocm",
        default=False,
        description="Enables UPC++ support for the ROCm/HIP memory kind on AMD GPUs",
    )

    variant(
        "level_zero",
        default=False,
        description="Enables UPC++ support for the Level Zero memory kind on Intel GPUs",
    )

    variant(
        "cross",
        default=cross_detect(),
        description="UPC++ cross-compile target (autodetect by default)",
    )

    conflicts(
        "cross=none",
        when=is_CrayXC(),
        msg='cross=none is unacceptable on Cray XC. Please specify an appropriate "cross" value',
    )
    conflicts(
        "@2025.10.0:", when=is_CrayXC(), msg="Cray XC support was removed in upcxx@2025.10.0"
    )

    # UPC++ always relies on GASNet-EX.
    # This variant allows overriding with a particular version of GASNet-EX sources,
    # although this is not officially supported and some combinations might be rejected.
    # Original default was to use the embedded version of GASNet-EX,
    # but currently there are newer versions in Spack so we default to that instead.
    variant("gasnet", default=True, description="Override embedded GASNet-EX with Spack's")
    depends_on("gasnet conduits=none", when="+gasnet")

    depends_on("mpi", when="+mpi")
    depends_on("python@2.7.5:", type=("build", "run"))

    depends_on("libfabric", when=is_CrayEX())

    conflicts("^hip@:4.4.0", when="+rocm")

    depends_on("oneapi-level-zero@1.8.0:", when="+level_zero")

    # All flags should be passed to the build-env in autoconf-like vars
    flag_handler = env_flags

    def set_variables(self, env):
        env.set("UPCXX_INSTALL", self.prefix)
        env.set("UPCXX", self.prefix.bin.upcxx)
        if is_CrayXC():
            env.set("UPCXX_NETWORK", "aries")
        elif is_CrayEX():
            env.set("UPCXX_NETWORK", "ofi")
            env.set("GASNET_SPAWN_CONTROL", "pmi")

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        self.set_variables(env)

    def setup_dependent_build_environment(
        self, env: EnvironmentModifications, dependent_spec: Spec
    ) -> None:
        self.set_variables(env)

    def setup_dependent_package(self, module, dependent_spec):
        dependent_spec.upcxx = self.prefix.bin.upcxx

    def install(self, spec, prefix):
        env = os.environ
        if env.get("GASNET_CONFIGURE_ARGS") is None:
            env["GASNET_CONFIGURE_ARGS"] = ""
        # UPC++ follows autoconf naming convention for LDLIBS, which is 'LIBS'
        if env.get("LDLIBS"):
            env["LIBS"] = env["LDLIBS"]

        if spec.satisfies("%oneapi@2025:"):
            env["CXXFLAGS"] = (
                "-Wno-error=missing-template-arg-list-after-template-kw "
                "-Wno-missing-template-arg-list-after-template-kw"
            )

        options = ["--prefix=%s" % prefix]

        if "cross=none" in spec:
            options.append("--without-cross")
        else:
            options.append("--with-cross=" + spec.variants["cross"].value)

        if (is_CrayXC() or is_CrayEX()) and env.get("CRAYPE_DIR"):
            # Undo spack compiler wrappers:
            # the C/C++ compilers must work post-install
            real_cc = join_path(env["CRAYPE_DIR"], "bin", "cc")
            real_cxx = join_path(env["CRAYPE_DIR"], "bin", "CC")
            if "+mpi" in spec:
                env["GASNET_CONFIGURE_ARGS"] += " --with-mpicc=" + real_cc
        else:
            real_cc = self.compiler.cc
            real_cxx = self.compiler.cxx
            if "+mpi" in spec:
                real_cxx = spec["mpi"].mpicxx

        options.append("--with-cc=" + real_cc)
        options.append("--with-cxx=" + real_cxx)

        if is_CrayEX():
            # Probe to find the right libfabric provider (SlingShot 10 vs 11)
            fi_info = which(spec["libfabric"].prefix.bin.fi_info) or which("fi_info")
            if fi_info is None or fi_info("-l", output=str).find("cxi") >= 0:
                provider = "cxi"
            else:
                provider = "verbs;ofi_rxm"

            # Append the recommended options for Cray Shasta
            if which("srun"):
                options.append("--with-pmi-runcmd=srun -n %N -- %C")
            elif which("aprun"):
                options.append("--with-pmi-runcmd=aprun -n %N %C")
            options.append("--with-default-network=ofi")
            options.append("--with-ofi-provider=" + provider)

        if "+gasnet" in spec:
            options.append("--with-gasnet=" + spec["gasnet"].prefix.src)

        options.append("--with-python=" + spec["python"].command.path)

        if "+mpi" in spec:
            options.append("--enable-mpi")
            options.append("--enable-mpi-compat")
        else:
            options.append("--without-mpicc")

        if "+cuda" in spec:
            options.append("--enable-cuda")
            options.append("--with-cuda-home=" + spec["cuda"].prefix)
            options.append("--with-nvcc=" + spec["cuda"].prefix.bin.nvcc)
            options.append(
                "--with-ldflags=" + self.compiler.cc_rpath_arg + spec["cuda"].prefix.lib64
            )

        if "+rocm" in spec:
            options.append("--enable-hip")
            options.append("--with-hip-home=" + spec["hip"].prefix)
            options.append("--with-ldflags=" + self.compiler.cc_rpath_arg + spec["hip"].prefix.lib)

        if "+level_zero" in spec:
            options.append("--enable-ze")
            options.append("--with-ze-home=" + spec["oneapi-level-zero"].prefix)

        env["GASNET_CONFIGURE_ARGS"] = "--enable-rpath " + env["GASNET_CONFIGURE_ARGS"]

        configure(*options)

        make()

        make("install")

        install_tree("example", prefix.example)

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def check_install(self):
        # enable testing of unofficial conduits (mpi)
        test_networks = "NETWORKS=$(CONDUITS)"
        # build hello world against installed tree in all configurations
        make("test_install", test_networks)
        make("tests-clean")  # cleanup
        # build all tests for all networks in debug mode
        make("tests", test_networks)
        if "cross=none" in self.spec:
            make("run-tests", "NETWORKS=smp")  # runs tests for smp backend
        make("tests-clean")  # cleanup

    def test_upcxx_install(self):
        """checking UPC++ compile+link for all installed backends"""
        test_install = join_path(self.prefix.bin, "test-upcxx-install.sh")
        test_upcxx_install = which(test_install, required=True)
        out = test_upcxx_install(output=str.split, error=str.split)
        assert "SUCCESS" in out

    # `spack external find` support
    executables = ["^upcxx$"]

    @classmethod
    def determine_version(cls, exe):
        """Return either the version of the executable passed as argument
        or ``None`` if the version cannot be determined.
        exe (str): absolute path to the executable being examined
        """
        output = Executable(exe)("--version", output=str, error=str)
        match = re.search(r"UPC\+\+ version\s+(\S+)\s+(?:upcxx-(\S+))?", output)
        if match is None:
            return None
        elif match.group(2):  # Git snapshot
            return match.group(2)
        else:  # official release
            return match.group(1)

    @classmethod
    def determine_variants(cls, exes, version_str):
        meta = exes[0] + "-meta"  # find upcxx-meta
        output = Executable(meta)("CPPFLAGS", output=str, error=str)
        variants = ""
        if re.search(r"-DUPCXXI_CUDA_ENABLED=1", output):
            variants += "+cuda"
        else:
            variants += "~cuda"
        if re.search(r"-DUPCXXI_HIP_ENABLED=1", output):
            variants += "+rocm"
        else:
            variants += "~rocm"
        if re.search(r"-DUPCXXI_ZE_ENABLED=1", output):
            variants += "+level_zero"
        else:
            variants += "~level_zero"
        return variants
