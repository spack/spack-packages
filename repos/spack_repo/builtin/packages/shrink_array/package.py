# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


def _valid_chunk_size(x):
    """What the library accepts (is_valid_chunk_size): a power of two or a multiple of 64."""
    return x.isdigit() and int(x) > 0 and (int(x) % 64 == 0 or int(x) & (int(x) - 1) == 0)


class ShrinkArray(CMakePackage):
    """Compressed arrays for C++ HPC codes: used like a std::vector, they take
    less memory when large parts of them hold the same value -- zero, or a few
    repeated values. An array is cut into chunks of S elements; a uniform chunk
    keeps no buffer of its own. Arrays of 10^9 elements, written from OpenMP
    threads -- or, with threads=std, from std::threads or TBB.

    Installs one library per variant and chunk size, found with
    find_package(shrink_array): shrink_array::zero_<S>, shrink_array::zero_or_value_<S>,
    shrink_array::zero_any_<S> (static S), shrink_array::<variant>_dyn (runtime S),
    shrink_array::<variant> (the first static size). Up to 0.2.1 the package is
    find_package(chunk) and the targets chunk::chunk_<variant>_<S>; the later
    versions still provide these names, deprecated."""

    homepage = "https://github.com/cea-hpc/shrink-array"
    url = "https://github.com/cea-hpc/shrink-array/archive/refs/tags/v0.4.0.tar.gz"
    git = "https://github.com/cea-hpc/shrink-array.git"

    maintainers("phil12692")

    license("Apache-2.0")

    version("develop", branch="develop")
    version("0.4.0", sha256="0ce2504792d1a3bbd618ec3223a90036adf1d50548930482281f835b08b115cd")
    version("0.3.0", sha256="d223c1d83fc4ac339980f6883bb6ed170f9e84c14b048e655c657647cc33d16c")
    version("0.2.1", sha256="323fdc97caed6b1c59b589e73a7f92d0b68e20ac8657c36c4aad9109c9d60b6c")
    version("0.2.0", sha256="179938b68b55c8b74a6d01b1a2e8443902e798c5867b651a7576d86c2ab1fb5f")
    version("0.1.3", sha256="a06f94ae4b2580cbd8506e254563678514fa1627c51abd4a319f11fc988a4bfa")
    version("0.1.2", sha256="6c411397ed62cc23813aaef91c491f053ec29b0ea66b43c073b31e10ca1e2bf3")
    version("0.1.1", sha256="fdbc4b4d1a2104e022d96454b047d64475d6ae5d381da92fada41a905cf78e43")
    version("0.1.0", sha256="81d9b5c50ac4d1d437b5b3df80d6fb1b51ce3f8106ff9c662820ba6eee533ad9")

    variant(
        "threads",
        default="openmp",
        values=("openmp", "std", "serial"),
        multi=False,
        description="Threading backend of the libraries (CHUNK_THREADS): openmp; std, "
        "std::jthread workers of the library's own, for programs whose threads are "
        "std::threads or TBB; serial",
    )
    variant(
        "tbb",
        default=False,
        description="With +examples and threads=std: also the TBB bench and the TBB adaptor's "
        "validation (CHUNK_WITH_TBB). The libraries never link TBB: a TBB program includes "
        "chunk/tbb_adaptor.h and links TBB itself",
    )
    variant(
        "sizes",
        default="256,1024",
        values=_valid_chunk_size,
        multi=True,
        description="Static chunk sizes, each a power of two or a multiple of 64: one library "
        "per variant and size (shrink_array::zero_any_256, ...); "
        "the smallest is the one of the bare shrink_array::<variant> targets",
    )
    variant(
        "dyn",
        default=True,
        description="Also a runtime-size library per variant (shrink_array::<variant>_dyn): "
        "adaptive re-chunk",
    )
    variant(
        "fast_alloc",
        default=True,
        description="The fast_allocators slab allocator for the chunk buffers "
        "(off: the standard allocator)",
    )
    variant("stats", default=False, description="Collect compression statistics (CHUNK_STATS)")
    variant(
        "second_value_indexed",
        default=False,
        description="zero_any: second values as 4-byte identifiers "
        "(less memory, about +3% write time)",
    )
    variant(
        "checks",
        default=False,
        description="Runtime invariant checks in an optimised build (CHUNK_CHECK_OPTIM)",
    )
    variant(
        "examples",
        default=False,
        description="Also build the examples, benchmarks and validation harnesses (not installed)",
    )

    depends_on("cxx", type="build")
    # C: the reduced models of formal/, built with the tests only.
    depends_on("c", type="build")
    depends_on("cmake@3.20:", type="build")
    depends_on("tbb", when="+tbb")
    # shrink_bench compresses its reference data (find_package(BZip2 REQUIRED)).
    depends_on("bzip2", when="+examples")
    # The source checks registered as tests (scripts/check_*.py) and the scripts
    # the validation runs.
    depends_on("python@3.8:", type="test")
    # threads=openmp: the OpenMP runtime is the compiler's own (libgomp, libomp,
    # libiomp5), found by find_package(OpenMP). No package to depend on: a
    # Clang without libomp fails at configure, with CMake's message.

    # Linux only: membarrier, madvise, mincore, /proc.
    requires("platform=linux", msg="shrink-array relies on Linux system calls and /proc")

    # C++20 (GCC 13 and Clang 18 are the oldest tested).
    conflicts("%gcc@:12", msg="shrink-array needs GCC 13 or later")
    conflicts("%clang@:17", msg="shrink-array needs Clang 18 or later")
    # CHUNK_THREADS and CHUNK_WITH_TBB come with 0.2.0, CHUNK_STATS with 0.1.2:
    # an earlier version ignores the option and would install something else
    # than the spec says (serial libraries for threads=std, no statistics).
    conflicts("threads=std", when="@:0.1.3", msg="the std backend comes with 0.2.0")
    conflicts("+tbb", when="@:0.1.3", msg="the TBB examples come with 0.2.0")
    conflicts("+stats", when="@:0.1.1", msg="the statistics option comes with 0.1.2")
    conflicts("+tbb", when="~examples", msg="+tbb builds TBB examples only: add +examples")
    conflicts("+tbb", when="threads=openmp", msg="the TBB examples need threads=std")
    conflicts("+tbb", when="threads=serial", msg="the TBB examples need threads=std")

    def cmake_args(self):
        spec = self.spec
        sizes = sorted(spec.variants["sizes"].value, key=int)
        threads = spec.variants["threads"].value
        args = [
            # CHUNK_OPENMP for every version (see below for the versions up to
            # 0.2.1); CHUNK_THREADS (which sets it to match) only where the std
            # backend exists.
            self.define("CHUNK_OPENMP", threads == "openmp"),
            self.define("CHUNK_STATIC_SIZES", ";".join(sizes)),
            self.define("CHUNK_DEFAULT_SIZE", sizes[0]),
            self.define_from_variant("CHUNK_BUILD_DYN", "dyn"),
            self.define("CHUNK_STD_ALLOC", spec.satisfies("~fast_alloc")),
            self.define_from_variant("CHUNK_STATS", "stats"),
            self.define_from_variant("CHUNK_SECOND_VALUE_INDEXED", "second_value_indexed"),
            self.define_from_variant("CHUNK_CHECK_OPTIM", "checks"),
            self.define_from_variant("SHRINK_ARRAY_BUILD_EXAMPLES", "examples"),
            self.define("SHRINK_ARRAY_BUILD_TESTS", self.run_tests),
            # The target is the spec's: Spack's compiler wrapper passes its
            # -march=. Without this the project adds -march=native (-mcpu=native,
            # -tp=host) after it, and the package only runs on the build host's
            # CPU. Read by the versions after 0.2.1; the earlier ones ignore it
            # and stay tied to the build host.
            self.define("CHUNK_NATIVE_TUNING", False),
            # The compiler and standard library Spack chose: no libc++ switch
            # (the project's default with Clang up to 0.2.1), no mold, no Intel
            # libm.
            self.define("CHUNK_USE_LIBCXX", False),
            self.define("CHUNK_USE_MOLD", "OFF"),
            self.define("SHRINK_INTEL_LIBM", False),
        ]
        # Up to 0.2.1 these four options had no CHUNK_ prefix: those versions
        # ignore the names above and would take their defaults -- serial
        # libraries (OMP was OFF), libc++ with Clang (USE_LIBCXX was ON), mold
        # on AUTO, no checks.
        if spec.satisfies("@:0.2.1"):
            args += [
                self.define("OMP", threads == "openmp"),
                self.define("USE_LIBCXX", False),
                self.define("USE_MOLD", "OFF"),
                self.define_from_variant("CHECK_OPTIM", "checks"),
            ]
        if threads == "std":
            args.append(self.define("CHUNK_THREADS", "std"))
        if spec.satisfies("+tbb"):
            args.append(self.define("CHUNK_WITH_TBB", True))
        return args
