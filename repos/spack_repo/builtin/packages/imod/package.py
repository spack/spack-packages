# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Imod(MakefilePackage, CudaPackage):
    """IMOD is a set of image processing, modeling and display programs used
    for tomographic reconstruction and for 3D reconstruction of EM serial
    sections and optical sections. The package contains tools for assembling
    and aligning data within multiple types and sizes of image stacks, viewing
    3-D data from any orientation, and modeling and display of the image files.
    """

    homepage = "https://bio3d.colorado.edu/imod/"
    hg = "http://bio3d.colorado.edu/imod/nightlyBuilds/IMOD"

    maintainers("Markus92")

    license("GPL-2", checked_by="Markus292")

    version("5.2.3", revision="b520a584fca2")

    variant("fftw", default=False, description="Use external FFTW?")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("java@17:")

    depends_on("qt@5.12:")  # Can do with 4.6:, but they themselves recommend 5.12+
    depends_on("cuda", when="+cuda")
    depends_on("libtiff@4:")
    depends_on("fftw@3:", when="+fftw")
    depends_on("hdf5")
    depends_on("jpeg")
    depends_on("glu")
    depends_on("tcsh", type=("build", "run"))
    depends_on("python", type=("run"))

    def edit(self, spec, prefix):
        configure = Executable("./setup")
        configure_args = ["-inst", prefix]  # Set up prefix
        configure(*configure_args)

        if self.spec.satisfies("+cuda"):
            cuda_flags = " ".join(self.cuda_flags(self.spec.variants["cuda_arch"].value))
            filter_file(r"-arch sm_\d{2}", cuda_flags, "configure")

    def flag_handler(self, name: str, flags: List[str]):
        if name == "fflags":
            flags.append("-fallow-argument-mismatch")
        return (flags, None, None)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+fftw"):
            env.set("FFTW3_DIR", self.spec["fftw"].prefix)
        if self.spec.satisfies("+cuda"):
            env.set("CUDA_DIR", self.spec["cuda"].prefix)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("IMOD_DIR", self.prefix)
