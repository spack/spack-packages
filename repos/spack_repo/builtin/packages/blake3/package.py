# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Blake3(CMakePackage):
    """BLAKE3 is a cryptographic hash function that makes use of @b/{tree hashing}[1]
    to achieve parallelism without sacrificing collision resistance or indifferentiability.

    [1]: https://eprint.iacr.org/2009/210.pdf
    """

    homepage = "https://github.com/BLAKE3-team/BLAKE3"
    url = "https://github.com/BLAKE3-team/BLAKE3/archive/refs/tags/1.5.1.tar.gz"
    git = "https://github.com/BLAKE3-team/BLAKE3.git"

    root_cmakelists_dir = "c"

    maintainers("haampie", "cosmicexplorer")

    version("1.8.5", sha256="220bd81286e2a0585beac66d41ac3f4c2c33ae8a4e339fc88cf22d5e00514fe9")
    version("1.8.4", sha256="b5ee5f5c5e025eb2733ae3af8d4c0e53bb66dff35095decfd377f1083e8ac9be")
    version("1.8.0", sha256="b9f565adc6e2c8c813dafd6d5406a71382f7ac6aa3250b19e9d8a68c457fd769")
    version("1.7.0", sha256="59bb6f42ecf1bd136b40eaffe40232fc76488b03954ef25cb588404b8d66a7e0")
    version("1.6.0", sha256="cc6839962144126bc6cc1cde89a50c3bb000b42a93d7e5295b1414d9bdf70c12")
    version("1.5.1", sha256="822cd37f70152e5985433d2c50c8f6b2ec83aaf11aa31be9fe71486a91744f37")

    version("master", branch="master")
    version("1.8.1", tag="1.8.1",
            commit="ad639b126ef9b5f3b131093363cc3bb6bba4c3bf")

    # OpenMP would be more natural and potentially more performant than the work-stealing approach
    # of oneTBB, since the work is extremely regular and can be performed in a known finite amount
    # of memory:
    # https://github.com/BLAKE3-team/BLAKE3/pull/457#issuecomment-4229630358
    variant("tbb", when="@1.8.1:", default=True,
            description="build in the intel oneTBB parallelism library.")

    depends_on("c", type="build")  # generated

    depends_on("cmake@3.9:", type="build")
