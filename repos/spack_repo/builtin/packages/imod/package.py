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
    IMOD was developed primarily by David Mastronarde, Rick Gaudette, Sue Held,
    Jim Kremer, Quanren Xiong, Suraj Khochare, and John Heumann at the
    University of Colorado."""

    homepage = "https://bio3d.colorado.edu/imod/"
    hg = "http://bio3d.colorado.edu/imod/nightlyBuilds/IMOD"

    maintainers("Markus92")

    license("GPL-2", checked_by="Markus292")

    version("5.2.3", revision="b520a584fca2")

    variant("hdf5", default=False, description="Build with HDF5")
    variant("fftw", default=False, description="Use external FFTW")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("java@17:")

    depends_on("qt@5.12: +opengl")  # It SHOULD be compatible with 4.6+, upstream recommends 5.12+
    depends_on("cuda", when="+cuda")
    depends_on("libtiff@4:")
    depends_on("fftw@3: +shared", when="+fftw")
    depends_on("hdf5@:1.11", when="+hdf5")
    depends_on("jpeg")
    depends_on("glu")
    depends_on("tcsh")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+hdf5"):
            env.set("HDF5_DIR", self.spec["hdf5"].prefix)
        if self.spec.satisfies("+fftw"):
            env.set("FFTW3_DIR", self.spec["fftw"].prefix)

    def edit(self, spec, prefix):
        configure = Executable("./setup")
        configure_args = ["-inst", prefix]  # Set up prefix
        configure(*configure_args)

    # For GCC > 9, this flag is required to get it to compile
    def flag_handler(self, name: str, flags: List[str]):
        if name == "fflags":
            flags.append("-fallow-argument-mismatch")
        return (flags, None, None)

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.set("IMOD_DIR", self.prefix)
