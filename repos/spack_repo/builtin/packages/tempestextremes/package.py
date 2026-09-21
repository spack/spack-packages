# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Tempestextremes(CMakePackage):
    """TempestExtremes is a growing collection of detection and
    characterization algorithms for large climate datasets, leveraging C++ for
    rapid throughput and a command line interface that maximizes flexibility
    of each kernel. The tracking kernels in this package have been already
    used for tracking and characterizing tropical cyclones (TCs), extratropical
    cyclones (ETCs), monsoonal depressions, atmospheric blocks, atmospheric
    rivers, and mesoscale convective systems (MCSs). By considering multiple
    extremes within the same framework, we can study the joint characteristics
    of extremes while minimizing the total data burden.
    """

    homepage = "https://github.com/ClimateGlobalChange/tempestextremes"
    url = "https://github.com/ClimateGlobalChange/tempestextremes/archive/refs/tags/v2.3.tar.gz"

    maintainers("andrewdnolan", "paullric", "xylar")

    license("BSD-2-Clause", checked_by="andrewdnolan")

    version("2.4.2", sha256="a370faadfe3958ed0db7bfab8ca0fcd50bbc91b11aeba3dff8728d0fb0f94267")
    version("2.4.1", sha256="c586739a62e3a8d8cc41cd2f17130825806b8bd618df25e9ac26a0ce0bd72016")
    version("2.4", sha256="c1be592ae5e1975c64f65025149d9c3f7b83474fcfe67ef3d5bb7206e63b4b6a")
    version("2.3.1", sha256="eff3564a99b0711335bd4f08e3a7dcec401c56d58fe6ef2d1ae778d7f7bf04e0")
    version("2.3", sha256="1194a3825ce7754bda6bdfc97da5390c8e37895f2a41fb2f22a480df0b777564")

    variant("mpi", default=True, description="Build with MPI support")

    depends_on("cxx", type="build")

    # Required dependencies
    depends_on("cmake@3.12:", type="build")
    depends_on("netcdf-c")

    # Optional dependencies
    depends_on("mpi", when="+mpi")

    def cmake_args(self):
        args = [self.define_from_variant("ENABLE_MPI", "mpi")]
        return args
