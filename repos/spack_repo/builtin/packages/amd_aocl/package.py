# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.bundle import BundlePackage

from spack.package import *


class AmdAocl(BundlePackage):
    """AMD Optimizing CPU Libraries (AOCL) - AOCL is a set of numerical
    libraries tuned specifically for AMD EPYC processor family. They have a
    simple interface to take advantage of the latest hardware innovations.
    The tuned implementations of industry standard math libraries enable
    fast development of scientific and high performance computing projects.

    Preferred FFT for this bundle is aocl-fftw (fftw-api). aocl-fftz is not
    included: aocl-fftz+wrappers also provides fftw-api and conflicts with
    aocl-fftw; install aocl-fftz separately. aocl-fftz~wrappers (native API
    only) may be installed alongside the bundle.

    LICENSING INFORMATION: By downloading, installing and using this software,
    you agree to the terms and conditions of the AMD AOCL license agreement.
    You may obtain a copy of this license agreement from
    https://www.amd.com/en/developer/aocl/aocl-eula.html
    https://www.amd.com/en/developer/aocl/eula/aocl-4-1-eula.html
    """

    homepage = "https://www.amd.com/en/developer/aocl.html"

    maintainers("amd-toolchain-support")

    version("6.0.0")
    version("5.3")
    version("5.2")
    version("5.1")
    version("5.0")
    version("4.2")
    version("4.1")
    version("4.0")
    version("3.2")
    version("3.1")
    version("3.0")
    version("2.2")

    variant("openmp", default=False, description="Enable OpenMP support.")
    variant(
        "python",
        default=False,
        when="@5:",
        description="Enable Python support for AOCL-DA.",
    )

    conflicts("+openmp", when="@:3", msg="OpenMP is not supported by aocl-lapack before 4.0")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("scalapack")
    depends_on("lapack")
    depends_on("blas")
    depends_on("fftw-api")

    requires("^[virtuals=scalapack] aocl-scalapack")
    requires("^[virtuals=lapack] aocl-lapack")
    requires("^[virtuals=blas] aocl-blas")
    requires(
        "^[virtuals=fftw-api] aocl-fftw",
        msg="amd-aocl uses aocl-fftw as its fftw-api provider",
    )

    with when("+openmp"):
        depends_on("aocl-dlp threads=openmp", when="@5.2:")
        depends_on("aocl-blas threads=openmp")
        depends_on("aocl-fftw +openmp")
        depends_on("aocl-lapack threads=openmp", when="@4:")
        depends_on("aocl-sparse +openmp", when="@4.2:")
        depends_on("aocl-da +openmp", when="@5:")
        depends_on("aocl-compression +openmp", when="@4.2:")

    with when("~openmp"):
        depends_on("aocl-dlp threads=none", when="@5.2:")
        depends_on("aocl-blas threads=none")
        depends_on("aocl-fftw ~openmp")
        depends_on("aocl-lapack threads=none")
        depends_on("aocl-sparse ~openmp", when="@4.2:")
        depends_on("aocl-da ~openmp", when="@5:")
        depends_on("aocl-compression ~openmp", when="@4.2:")

    with when("@5:"):
        depends_on("aocl-da +python", when="+python")
        depends_on("aocl-da ~python", when="~python")

    for vers in [
        "2.2",
        "3.0",
        "3.1",
        "3.2",
        "4.0",
        "4.1",
        "4.2",
        "5.0",
        "5.1",
        "5.2",
        "5.3",
        "6.0.0",
    ]:
        with when(f"@={vers}"):
            depends_on(f"aocl-blas@={vers}")
            depends_on(f"aocl-fftw@={vers}")
            depends_on(f"aocl-lapack@={vers}")
            depends_on(f"aocl-libm@={vers}")
            depends_on(f"aocl-scalapack@={vers}")
            depends_on(f"aocl-sparse@={vers}")
            if Version(vers) >= Version("4.2"):
                depends_on(f"aocl-compression@={vers}")
                depends_on(f"aocl-crypto@={vers}")
                depends_on(f"aocl-libmem@={vers}")
            if Version(vers) >= Version("5.0"):
                depends_on(f"aocl-da@={vers}")
            if Version(vers) >= Version("5.2"):
                depends_on(f"aocl-dlp@={vers}")
            if Version(vers) >= Version("6.0.0"):
                depends_on(f"aocl-openrng@={vers}")
