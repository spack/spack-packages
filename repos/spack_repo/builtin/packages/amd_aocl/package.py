# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.bundle import BundlePackage

from spack.package import *


class AmdAocl(BundlePackage):
    """AMD Optimizing CPU Libraries (AOCL) - AOCL is a set of numerical
    libraries tuned specifically for AMD EPYC processor family. They have a
    simple interface to take advantage of the latest hardware innovations.
    The tuned implementations of industry standard  math libraries enable
    fast development of scientific and high performance computing projects

    LICENSING INFORMATION: By downloading, installing and using this software,
    you agree to the terms and conditions of the AMD AOCL license agreement.
    You may obtain a copy of this license agreement from
    https://www.amd.com/en/developer/aocl/aocl-eula.html
    https://www.amd.com/en/developer/aocl/eula/aocl-4-1-eula.html
    """

    homepage = "https://www.amd.com/en/developer/aocl.html"

    maintainers("amd-toolchain-support")

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

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")
    depends_on("scalapack")
    depends_on("lapack")
    depends_on("blas")

    requires("^[virtuals=scalapack] aocl-scalapack")
    requires("^[virtuals=lapack] aocl-lapack")
    requires("^[virtuals=blas] aocl-blas")
    # These are deprecated aliases of aocl-blas and aocl-lapack. Requesting one
    # alongside the canonical dependency installs two copies of the same library.
    conflicts(
        "^amdblis",
        when="^aocl-blas",
        msg="use aocl-blas; amdblis is a deprecated alias",
    )
    conflicts(
        "^amdlibflame",
        when="^aocl-lapack",
        msg="use aocl-lapack; amdlibflame is a deprecated alias",
    )

    with when("+openmp"):
        depends_on("aocl-blas threads=openmp")
        depends_on("aocl-fftw +openmp")
        depends_on("aocl-lapack threads=openmp")
        depends_on("aocl-sparse +openmp")
        depends_on("aocl-da +openmp")
        depends_on("aocl-compression +openmp")

    with when("~openmp"):
        depends_on("aocl-blas threads=none")
        depends_on("aocl-fftw ~openmp")
        depends_on("aocl-lapack threads=none")
        depends_on("aocl-sparse ~openmp")
        depends_on("aocl-da ~openmp")
        depends_on("aocl-compression ~openmp")

    for vers in ["2.2", "3.0", "3.1", "3.2", "4.0", "4.1", "4.2", "5.0", "5.1", "5.2", "5.3"]:
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
