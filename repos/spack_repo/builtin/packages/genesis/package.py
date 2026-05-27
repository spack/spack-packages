# Copyright Spack Project Developers. See COPYRIGHT file for details.  #
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Genesis(AutotoolsPackage, CudaPackage):
    """GENESIS is a Molecular dynamics and modeling software
    for bimolecular systems such as proteins, lipids, glycans,
    and their complexes.
    """

    homepage = "https://mdgenesis.org/"
    url = "https://github.com/genesis-release-r-ccs/genesis/archive/refs/tags/v2.1.6.1.tar.gz"

    license("LGPL-3.0-or-later", checked_by="chig")

    version("2.1.6.1", sha256="fdc0e889590f198e2261105901c27718268a18a1cd32300e2232b457a7ba6761")
    version("2.1.5", sha256="622e6dc0bf9db54b2d18165f098044146abbf20837cb6209af2015856469afbf")
    version("2.1.4", sha256="8a6ae1b5a775a41e6d6c398759d78c513a87537bb6832ebda9ea7d426c2408af")
    version("2.1.3", sha256="24b0e407d4d6d54f570f3153d78773ffce79877fbf02f4d6c8bc68675caafecf")
    version("2.1.2", sha256="cce6834f429d28a0f26450c8b92bab24e86b8c03bf7f2dc3868b74b65bf3f7f0")
    version("2.1.1", sha256="0092822ce1a477dd2c4dc6b6035ccfeb0506d78e27b345e4f40bc844efe7a08d")
    version("2.1.0", sha256="b348377875b99a62cb93a834047dedeb28cc2a1c615d0bcf0eecadaa1376020c")
    version("2.0.3", sha256="a389ed869e6b04dd05a194c0f8577d5e1839f8bcd453fde5b30428a428405830")
    version("2.0.2", sha256="8e80d7a1601bf6b12adf3e4ddcbec55aee27a3431784fbc0a46c784eb092f230")
    version("2.0.0", sha256="87f097754cb36b1d532ca4952843e60b5115d1eb28e6c2c0fee77c8c720bd958")


    variant("openmp", default=True, description="Enable OpenMP.")
    variant("single", default=False, description="Enable single precision.")
    variant("mixed",  default=False, description="Enable mixed precision.", when="@2.0.0:")
    variant("hmdisk", default=False, description="Enable huge molecule on hard disk.")

    # Fix NVTX include path for CUDA 12 on Arm sbsa-linux platforms
    # (e.g., GH200). nvToolsExt.h is located under
    # targets/sbsa-linux/include/nvtx3.
    patch("fix-nvtx-include.patch", when="+cuda")
    patch("fix-nvtx-include.patch", when="+gpu")
    # The original configure logic only supports Fujitsu cross-compilation targets.
    # This patch enables native Fujitsu compiler builds on A64FX systems.
    patch("fj_compiler_2.0.0.patch", when="@2.0.0:2.1.3 %fj")
    patch("fj_compiler_2.1.4.patch", when="@2.1.4: %fj")

    conflicts("%apple-clang", when="+openmp")

    # GitHub-generated source archives are not produced by `make dist`.
    # Since the bundled configure script is not guaranteed to match the
    # current configure.ac, regenerate the autotools files before configure.
    force_autoreconf = True

    depends_on("mpi", type=("build", "run"))
    depends_on("lapack")
<<<<<<< HEAD
    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
=======
    depends_on("c", type="build")  # generated
    depends_on("fortran", type="build")  # generated
>>>>>>> 6b622f1392 (Fix for autoreconf in genseis)

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("python", type=("build", "run"))

    parallel = False

    def configure_args(self):
        spec = self.spec
        options = []
        options.extend(self.enable_or_disable("openmp"))
        options.extend(self.enable_or_disable("single"))
        options.extend(self.enable_or_disable("mixed"))
        options.extend(self.enable_or_disable("hmdisk"))
        if spec.satisfies("+cuda"):
            options.append("--enable-gpu")
            options.append("--with-cuda=%s" % spec["cuda"].prefix)
        else:
            options.append("--disable-gpu")
        if spec.target == "a64fx":
            options.append("--host=Fugaku")
        return options

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("FC", self.spec["mpi"].mpifc, force=True)
        env.set("F77", self.spec["mpi"].mpif77, force=True)
        env.set("CC", self.spec["mpi"].mpicc, force=True)
        env.set("CXX", self.spec["mpi"].mpicxx, force=True)
        env.set("LAPACK_LIBS", self.spec["lapack"].libs.ld_flags)
        if self.spec.satisfies("+cuda"):
            cuda_arch = self.spec.variants["cuda_arch"].value
            cuda_gencode = " ".join(self.cuda_flags(cuda_arch))
            env.set("NVCCFLAGS", cuda_gencode)

    def install(self, spec, prefix):
        make("install")
        install_tree("doc", prefix.share.doc)

    @property
    def cached_tests_work_dir(self):
        """The working directory for cached test sources."""
        return join_path(self.test_suite.current_test_cache_dir, "tests")

    @run_after("install")
    def cache_test_sources(self):
        cache_extra_test_sources(self, ["tests"])

    def test(self):
        import os

        os.environ["OMP_NUM_THREADS"] = "1"

        exe_name = self.spec["python"].command.path
        test_name = join_path(
            self.install_test_root, "tests", "regression_test", "test.py"
        )
        bin_name = join_path(self.prefix.bin, "spdyn")

        mpirun = self.spec["mpi"].mpirun

        opts = [
            test_name,
            f"{mpirun} -np 8 {bin_name}",
        ]

        self.run_test(exe_name, options=opts, expected="Passed  61 / 61")
