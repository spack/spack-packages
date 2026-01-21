# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Arkouda(MakefilePackage):
    """Arkouda is a NumPy-like library for distributed data with a focus on
    large-scale data science applications."""

    homepage = "https://github.com/Bears-R-Us/arkouda"

    # Arkouda does not have a current PyPI package, so we use the GitHub tarball
    list_url = "https://github.com/Bears-R-Us/arkouda/tags"
    url = "https://github.com/Bears-R-Us/arkouda/archive/refs/tags/v2025.08.20.tar.gz"
    git = "https://github.com/Bears-R-Us/arkouda.git"

    # See https://spdx.org/licenses/ for a list.
    license("MIT")

    # A list of GitHub accounts to notify when the package is updated.
    maintainers("1RyanK", "ajpotts", "arezaii", "drculhane", "jaketrookman")

    version("main", branch="main")

    version(
        "2025.12.16", sha256="72638e9d8aa1889b6bafa76c6e8060e0c8aab0871be2693f8fb10f57cd4acbfa"
    )
    version(
        "2025.09.30", sha256="10f488a3ff3482b66f1b1e8a4235d72e91ad07acb932eca85d1e695f0f6155a2"
    )
    version(
        "2025.08.20", sha256="3e305930905397ff3a7a28a5d8cc2c9adca4194ca7f6ee51f749f427a2dea92c"
    )
    version(
        "2025.07.03", sha256="eb888fac7b0eec6b4f3bfa0bfe14e5c8f15b449286e84c45ba95c44d8cd3917a"
    )
    version(
        "2024.10.02",
        sha256="00671a89a08be57ff90a94052f69bfc6fe793f7b50cf9195dd7ee794d6d13f23",
        deprecated=True,
    )
    version(
        "2024.06.21",
        sha256="ab7f753befb3a0b8e27a3d28f3c83332d2c6ae49678877a7456f0fcfe42df51c",
        deprecated=True,
    )

    variant(
        "distributed",
        default=False,
        description="Build Arkouda for multi-locale execution on a cluster or supercomputer",
    )

    variant(
        "array_nd_max",
        default="1",
        values=("1", "2", "3"),
        multi=False,
        description="Set ARRAY_ND_MAX used by Arkouda build",
    )

    variant(
        "slurm-gasnet_ibv", default=False, description="Configure Chapel for Slurm + GASNet (ibv)"
    )

    depends_on(
        "chapel@2.0:2.4 +hdf5 +zmq",
        when="@2025.07.03:2025.08.20",
        type=("build", "link", "run", "test"),
    )
    depends_on(
        "chapel@2.0:2.5 +hdf5 +zmq", when="@2025.09.30:", type=("build", "link", "run", "test")
    )
    depends_on(
        "chapel@2.1: +hdf5 +zmq", when="@:2025.01.13", type=("build", "link", "run", "test")
    )

    depends_on("cmake@3.13.4:", type="build")
    depends_on("python@3.9:3.12.3", type=("build", "link", "run", "test"), when="@:2025.01.13")
    depends_on(
        "python@3.9:3.13", type=("build", "link", "run", "test"), when="@2025.07.03:2025.08.20"
    )
    depends_on("python@3.10:3.13", type=("build", "link", "run", "test"), when="@2025.09.30:")
    depends_on("libzmq@4.2.5:", type=("build", "link", "run", "test"))
    depends_on("hdf5+hl~mpi", type=("build", "link", "run", "test"))
    depends_on("libiconv", type=("build", "link", "run", "test"))
    depends_on("libidn2", type=("build", "link", "run", "test"))
    depends_on(
        "arrow+brotli+bz2+lz4+parquet+snappy+zlib+zstd",
        type=("build", "link", "run"),
        when="@2025.12.16:",
    )
    depends_on(
        "arrow@:19+brotli+bz2+lz4+parquet+snappy+zlib+zstd",
        type=("build", "link", "run"),
        when="@:2025.01.13",
    )
    depends_on(
        "arrow@15:19+brotli+bz2+lz4+parquet+snappy+zlib+zstd",
        type=("build", "link", "run"),
        when="@2025.07.03:",
    )

    # force lz4 to use cmake (add as a direct dep to control its variant)
    depends_on("lz4 build_system=cmake", type="build")

    requires("^chapel comm=none", when="~distributed")
    requires("^chapel +python-bindings", when="@2024.10.02:")
    requires(
        "^chapel comm=gasnet",
        "^chapel comm=ugni",
        "^chapel comm=ofi",
        policy="one_of",
        when="+distributed",
    )

    # Convenience integration: if the user selects Arkouda's slurm-gasnet_ibv,
    # force Chapel into a compatible comm/launcher configuration.
    requires(
        "+distributed",
        when="+slurm-gasnet_ibv",
        msg="slurm-gasnet_ibv requires a distributed Arkouda build (+distributed)",
    )
    requires(
        "^chapel comm=gasnet comm_substrate=ibv launcher=slurm-gasnetrun_ibv",
        when="+slurm-gasnet_ibv",
    )

    # Some systems need explicit -fPIC flag when building the Arrow functions
    patch("makefile-fpic-2024.06.21.patch", when="@2024.06.21")
    patch("makefile-fpic-2024.10.02.patch", when="@2024.10.02:2025.09.30")
    patch("makefile-fpic-2025.12.16.patch", when="@2025.12.16")

    sanity_check_is_file = [join_path("bin", "arkouda_server")]

    def check(self):
        # skip b/c we need the python client
        pass

    # override the default edit method to apply the patch
    def edit(self, spec, prefix):
        self.update_makefile_paths(spec, prefix)

    def update_makefile_paths(self, spec, prefix):
        # add to the Makefile.paths file for all of the dependencies installed by spack
        # in the form $(eval $(call add-path,<path-to-dep-aka-prefix>))
        with open("Makefile.paths", "w") as f:
            f.write("$(eval $(call add-path,{0}))\n".format(spec["hdf5"].prefix))
            f.write("$(eval $(call add-path,{0}))\n".format(spec["libzmq"].prefix))
            f.write("$(eval $(call add-path,{0}))\n".format(spec["arrow"].prefix))
            f.write("$(eval $(call add-path,{0}))\n".format(spec["libiconv"].prefix))
            f.write("$(eval $(call add-path,{0}))\n".format(spec["libidn2"].prefix))

    def build(self, spec, prefix):
        nd = spec.variants["array_nd_max"].value
        make_args = [f"ARRAY_ND_MAX={nd}"]

        # Detect distributed builds and skip the dependency checks built into
        # the Arkouda Makefile. These checks will try to spawn multiple jobs which may
        # cause the build to fail in situations where the user is constrained
        # to a limited number of simultaneous jobs.
        if spec.satisfies("+distributed"):
            with set_env(ARKOUDA_SKIP_CHECK_DEPS="1"):
                tty.warn("Distributed build detected. Skipping dependency checks")
                make(*make_args)
        else:
            make(*make_args)

    # Arkouda does not have an install target in its Makefile
    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("arkouda_server", prefix.bin)
        # Arkouda can have two executables depending on if Chapel is compiled in
        # single-locale or multi-locale mode
        if spec.satisfies("+distributed"):
            install("arkouda_server_real", prefix.bin)
