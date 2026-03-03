# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.cuda import CudaPackage

from spack.package import *


class Relion(CMakePackage, CudaPackage):
    """RELION (for REgularised LIkelihood OptimisatioN, pronounce rely-on) is a
    stand-alone computer program that employs an empirical Bayesian approach to
    refinement of (multiple) 3D reconstructions or 2D class averages in
    electron cryo-microscopy (cryo-EM)."""

    homepage = "https://www2.mrc-lmb.cam.ac.uk/relion"
    git = "https://github.com/3dem/relion.git"
    url = "https://github.com/3dem/relion/archive/4.0.0.zip"
    maintainers("dacolombo", "Markus92")

    license("GPL-2.0-only")

    version("5.0.1", sha256="3253230cd4b3d9633a5cac906937039b9971eb9430c3e2d838473777fb811f4c")
    version("4.0.1", sha256="7e0d56fd4068c99f943dc309ae533131d33870392b53a7c7aae7f65774f667be")
    version("4.0.0", sha256="0987e684e9d2dfd630f1ad26a6847493fe9fcd829ec251d8bc471d11701d51dd")

    # 3.1.4 latest release in 3.1 branch
    version("3.1.4", sha256="3bf3449bd2d71dc85d2cdbd342e772f5faf793d8fb3cda6414547cf34c98f34c")
    version("3.1.3", sha256="e67277200b54d1814045cfe02c678a58d88eb8f988091573453c8568bfde90fc")
    version("3.1.2", sha256="dcdf6f214f79a03d29f0fed2de58054efa35a9d8401543bdc52bfb177987931f")
    version("3.1.1", sha256="63e9b77e1ba9ec239375020ad6ff631424d1a5803cba5c608c09fd44d20b1618")
    version("3.1.0", sha256="8a7e751fa6ebcdf9f36046499b3d88e170c4da86d5ff9ad1914b5f3d178867a8")

    # 3.0.8 latest release in 3.0 branch
    version("3.0.8", sha256="18cdd58e3a612d32413eb37e473fe8fbf06262d2ed72e42da20356f459260973")
    version("3.0.7", sha256="a6d37248fc4d0bfc18f4badb7986dc1b6d6849baa2128b0b4dade13cb6991a99")

    # relion master contains development code
    # contains 3.0 branch code
    version("master")

    variant("gui", default=True, description="build the gui")
    variant("cuda", default=True, description="enable compute on gpu")
    variant("double", default=True, description="double precision (cpu) code")
    variant("double-gpu", default=False, description="double precision gpu")

    # if built with purpose=cluster then relion will link to gpfs libraries
    # if that's not desirable then use purpose=desktop
    variant(
        "purpose",
        default="cluster",
        values=("cluster", "desktop"),
        description="build relion for use in cluster or desktop",
    )

    variant(
        "build_type",
        default="RelWithDebInfo",
        description="The build type to build",
        values=("Debug", "Release", "RelWithDebInfo", "Profiling", "Benchmarking"),
    )

    # these new values were added in relion 3
    # do not seem to cause problems with < 3
    variant("mklfft", default=False, description="Use MKL rather than FFTW for FFT")
    variant(
        "allow_ctf_in_sagd",
        default=True,
        description=(
            "Allow CTF-modulation in SAGD, as specified in Claim 1 of patent US10,282,513B2"
        ),
        when="@3",
    )
    variant("altcpu", default=False, description="Use CPU acceleration", when="~cuda")

    variant(
        "external_motioncor2",
        default=False,
        description="Have external motioncor2 available in addition to Relion builtin",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("mpi")
    depends_on("cmake@3:", type="build")
    depends_on("binutils@2.32:", type="build")
    depends_on("fftw precision=float,double", when="~mklfft")

    # use the +xft variant so the interface is not so horrible looking
    depends_on("fltk+xft", when="+gui")

    depends_on("libtiff")
    depends_on("libpng", when="@4:")

    depends_on("cuda@9:", when="@3: +cuda")
    conflicts("cuda@13:", when="@:5.0.0 +cuda")
    depends_on("tbb", when="+altcpu")
    depends_on("mkl", when="+mklfft")
    depends_on("ctffind@4.1:4", type="run", when="@5")
    depends_on("ctffind@:4", type="run")
    depends_on("motioncor2", type="run", when="+external_motioncor2")

    depends_on("ghostscript", type="run", when="@4:")
    depends_on("pbzip2", type="run", when="@5:")
    depends_on("xz", type="run", when="@5:")
    depends_on("zstd", type="run", when="@5:")

    for arch in CudaPackage.cuda_arch_values:
        depends_on(
            f"py-relion@5.0.1 +cuda cuda_arch={arch}",
            type=("build", "run"),
            when=f"@5.0.1 +cuda cuda_arch={arch}",
        )
    depends_on("py-relion@5.0.1 ~cuda", type=("build", "run"), when="@5.0.1 ~cuda")

    patch("0002-Simple-patch-to-fix-intel-mkl-linking.patch", when="@:3.1.1 os=ubuntu18.04")
    patch(
        "https://github.com/3dem/relion/commit/2daa7447c1c871be062cce99109b6041955ec5e9.patch?full_index=1",
        sha256="4995b0d4bc24a1ec99042a4b73e9db84918eb6f622dacb308b718146bfb6a5ea",
        when="@4.0.0",
    )
    patch("cudarch-override.patch", when="@5: +cuda")

    def cmake_args(self):
        args = [
            "-DGUI=%s" % ("+gui" in self.spec),
            "-DDoublePrec_CPU=%s" % ("+double" in self.spec),
            "-DDoublePrec_GPU=%s" % ("+double-gpu" in self.spec),
            "-DALLOW_CTF_IN_SAGD=%s" % ("+allow_ctf_in_sagd" in self.spec),
            "-DMKLFFT=%s" % ("+mklfft" in self.spec),
            "-DALTCPU=%s" % ("+altcpu" in self.spec),
        ]
        if self.spec.satisfies("+gui"):
            incs = [f"-I{self.spec[lib].prefix.include}" for lib in ["libx11", "xproto"]]
            args += ["-DCMAKE_CXX_FLAGS=" + " ".join(incs)]

        if "+cuda" in self.spec:
            carch = self.spec.variants["cuda_arch"].value[0]

            # relion+cuda requires selecting cuda_arch
            if carch == "none":
                raise ValueError("Must select a value for cuda_arch")
            else:
                args += ["-DCUDA=ON", "-DCudaTexture=ON", "-DCUDA_ARCH=%s" % (carch)]

            if self.spec.satisfies("@5:"):
                cuda_flags = " ".join(
                    CudaPackage.cuda_flags(self.spec.variants["cuda_arch"].value)
                )
                args += [f"-DCUDARCH={cuda_flags}"]

        if self.spec.satisfies("@5: ~cuda"):
            # Relion 5 defaults to CUDA=ON so it has to be explicitly disabled.
            args.append("-DCUDA=OFF")

        if self.spec.satisfies("@5:"):
            args.append(f"-DPYTHON_EXE_PATH={self.spec['python'].command.path}")
            args.append("-DFETCH_WEIGHTS=OFF")

        return args

    def patch(self):
        # Remove flags not recognized by the NVIDIA compilers
        if self.spec.satisfies("%nvhpc"):
            filter_file("-std=c99", "-c99", "src/apps/CMakeLists.txt")

        # set up some defaults
        filter_file(
            r"(#define DEFAULTQSUBLOCATION).*",
            r'\1 "{0}"'.format(join_path(self.spec.prefix.bin, "relion_qsub.csh")),
            join_path("src", "pipeline_jobs.h"),
        )
        filter_file(
            r"(#define DEFAULTCTFFINDLOCATION).*",
            r'\1 "{0}"'.format(join_path(self.spec["ctffind"].prefix.bin, "ctffind")),
            join_path("src", "pipeline_jobs.h"),
        )

        if "+external_motioncor2" in self.spec:
            filter_file(
                r"(#define DEFAULTMOTIONCOR2LOCATION).*",
                r'\1 "{0}"'.format(join_path(self.spec["motioncor2"].prefix.bin, "MotionCor2")),
                join_path("src", "pipeline_jobs.h"),
            )

    def setup_run_environment(self, env):
        env.set("RELION_CTFFIND_EXECUTABLE", self.spec["ctffind"].prefix.bin.ctffind)
