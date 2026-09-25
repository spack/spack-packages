# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Swiftsim(AutotoolsPackage):
    """SPH With Inter-dependent Fine-grained Tasking (SWIFT) provides
    astrophysicists with a state of the art framework to perform
    particle based simulations.
    """

    homepage = "https://swift.strw.leidenuniv.nl"
    url = "https://github.com/SWIFTSIM/SWIFT/archive/refs/tags/v2026.04.tar.gz"
    git = "https://github.com/SWIFTSIM/SWIFT.git"

    license("GPL-3.0-only")

    version("master", branch="master")

    version("2026.04", sha256="0e183c53975de24306027789e3cf2ae9e6ee59403d516da8f3e03eaa2c1ff2c9")
    version("2026.01", sha256="5febdd40c3b129a907476960fc398ac5d1f65c5f8670f9cd605dd3ae52d8cd61")
    version("2025.01", sha256="c8353f4cfe0184e98e026f05a1754fed165509da572dbf8ad3eaface4b919253")
    version("1.0.0", sha256="d02c6d5616bae01725494c91ce25a37b18c6d6abb25b63b8e89e0a1f9b32ecca")
    version("0.9.0", sha256="11eab2dc48f94ad0774140b4090c74342cc614326ab20aa8aa492207235c402e")

    variant("mpi", default=True, description="Enable distributed memory parallelism")
    variant(
        "fftw", default=True, description="Enable FFTW support, used for perioodic gravity forces."
    )

    depends_on("c", type="build")  # generated

    # Build dependencies
    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    # link-time / run-time dependencies
    # gsl is optional, but strong compiler settings choke on function without retval:
    depends_on("gsl")
    depends_on("mpi", when="+mpi")
    depends_on("metis")
    depends_on("hdf5~mpi", when="~mpi")
    depends_on("hdf5+mpi", when="+mpi")
    depends_on("fftw-api@3.3:", when="+fftw")

    def configure_args(self):

        args = [
            "--with-metis={0}".format(self.spec["metis"].prefix),
            "--disable-dependency-tracking",
            "--enable-optimization",
            "--enable-compiler-warnings=yes",
        ]
        args.extend(self.enable_or_disable("mpi"))
        args.extend(
            self.with_or_without("fftw", activation_value=lambda x: self.spec["fftw-api"].prefix)
        )

        # Vector code doesnt support aarch64.
        if self.spec.satisfies("target=aarch64:"):
            args.append("--disable-vec")

        return args
