# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMeshioplusplus(PythonPackage):
    """meshio++: I/O for many mesh formats. A C++20 core (pybind11) with a
    pure-Python fallback for every format, so behavior and file compatibility
    are identical whether or not the native libraries are present."""

    homepage = "https://github.com/loumalouomega/meshioplusplus"
    # 6.0.0 has no PyPI sdist, so build every version from the GitHub archive
    # (scikit-build-core builds fine from the source tree) for a uniform source.
    url = "https://github.com/loumalouomega/meshioplusplus/archive/refs/tags/v9.10.0.tar.gz"
    git = "https://github.com/loumalouomega/meshioplusplus.git"

    maintainers("loumalouomega")

    license("MIT", checked_by="loumalouomega")

    # Upstream's default branch moved from main to master at v7.0.0.
    version("master", branch="master")
    version("9.10.0", sha256="6006148e1afb57f6d9426209775c2c6b008d8e10bd3d80ff7c676af9a99fd5fa")
    version("9.4.1", sha256="dc57060303b90a18128e259c5266d48d4a80e68d535ac028467b3ac8d518d772")
    version("9.0.0", sha256="8d7fdab4763a2174291e40c5da503bbb6d37b36591a54f7c0b1fa869eef54798")
    version("8.7.0", sha256="d8721aa4ed82ef2f7fe49062910826a7012f6823eb22d5290690c298eafe68ec")
    # v8.0.0: the WebAssembly build gained every core format; no change to the
    # Python wheel this package builds.
    version("8.0.0", sha256="ba0434950e9e2ef165ff9d50043ee6bb3e4359e7bc72ba77108553b7aad4b83f")
    version("7.0.0", sha256="797809b8c645d4712de9160ea375b0dc301b593844c475ca5bdbeb6490446c9a")
    version("6.6.1", sha256="327c1b146fefa3eb19404e2b422b5cf789fe81b8f402fea9694124d50b13e88b")
    version("6.6.0", sha256="a585a7b932a9a893b17710f68ed64a04b492d12abfe74c5744812fb44599cbae")
    version("6.5.0", sha256="f0ebdb7a547097ae338b2295eaa2cb08fe728a7d32c408f4109511ded3196779")
    version("6.4.0", sha256="d969bb081ac5bb9b43ce0fa32d3c6a5a8fc53a9f4ad086b03d7ebb40368a01fb")
    version("6.3.0", sha256="ead9fd2264ba809903c91347b7cbd1e526ac78373b2935590c967cad20aacf59")
    version("6.2.0", sha256="275c1a938845a416040b1517fb8f9c1c008e86ad888b432d0852eba0fac83126")
    version("6.1.0", sha256="0061d9b3ff20b65f6bb66dc4787b4c8f5c9f3abc9567b0b9e60fab28a8774afa")
    version("6.0.0", sha256="c5edd1c3f961a6282f08a76205e060ed3cb985401381313beb02788bc537ba94")

    variant("hdf5", default=True, description="C++ HDF5-backed formats and the h5py fallback")
    variant(
        "netcdf",
        default=True,
        description="C++ netCDF-backed format (Exodus) and the netCDF4 fallback",
    )
    variant("zlib", default=True, description="C++ VTU zlib compression path")
    variant(
        "zstd",
        default=False,
        description="C++ VTK XML zstd compression codec and the zstandard fallback",
        when="@7.3:",
    )
    variant(
        "lz4",
        default=False,
        description="C++ VTK XML lz4 compression codec and the lz4 fallback",
        when="@7.3:",
    )
    variant(
        "kahip",
        default=False,
        description="KaHIP-backed mesh partitioning quality",
        when="@7.6:",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.15:", type="build")
    # +pyproject: py-scikit-build-core@:0.8 only pulls in py-pyproject-metadata
    # / py-pathspec (needed to parse our PEP 621 pyproject.toml) when this
    # variant is set; without it, the concretizer can pick @0.8~pyproject and
    # the build fails at "Preparing metadata (pyproject.toml)".
    depends_on("py-scikit-build-core@0.8: +pyproject", type="build")
    depends_on("py-pybind11@2.11:", type="build")

    depends_on("python@3.8:", type=("build", "link", "run"))
    depends_on("py-numpy@1.20:", type=("build", "run"))
    depends_on("py-rich", type="run")

    depends_on("hdf5", when="+hdf5")
    # Some HDF5 formats (e.g. MED) always run the Python implementation.
    depends_on("py-h5py", when="+hdf5", type="run")
    depends_on("netcdf-c", when="+netcdf")
    depends_on("py-netcdf4", when="+netcdf", type="run")
    depends_on("zlib-api", when="+zlib")
    depends_on("zstd", when="+zstd")
    depends_on("py-zstandard", when="+zstd", type="run")
    depends_on("lz4", when="+lz4")
    depends_on("py-lz4", when="+lz4", type="run")
    # KaHIP has no PyPI/Spack Python fallback package; +kahip only wires up
    # the native accelerator.
    depends_on("kahip", when="+kahip")

    # meshio++ requires a C++20 toolchain for the native core.
    conflicts("%gcc@:9", msg="meshio++ needs GCC >= 10 for C++20")

    def config_settings(self, spec, prefix):
        # scikit-build-core forwards these to the CMake configure. The pybind11
        # extension requires the MESHIO mesh backend, which is the CMake default.
        def onoff(variant):
            return "ON" if spec.satisfies(variant) else "OFF"

        return {
            "cmake.define.MESHIOPLUSPLUS_WITH_HDF5": onoff("+hdf5"),
            "cmake.define.MESHIOPLUSPLUS_WITH_NETCDF": onoff("+netcdf"),
            "cmake.define.MESHIOPLUSPLUS_WITH_ZLIB": onoff("+zlib"),
            "cmake.define.MESHIOPLUSPLUS_WITH_ZSTD": onoff("+zstd"),
            "cmake.define.MESHIOPLUSPLUS_WITH_LZ4": onoff("+lz4"),
            "cmake.define.MESHIOPLUSPLUS_WITH_KAHIP": onoff("+kahip"),
        }
