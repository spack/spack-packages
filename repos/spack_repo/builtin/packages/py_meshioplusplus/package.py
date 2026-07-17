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
    url = "https://github.com/loumalouomega/meshioplusplus/archive/refs/tags/v6.2.0.tar.gz"
    git = "https://github.com/loumalouomega/meshioplusplus.git"

    maintainers("loumalouomega")

    license("MIT", checked_by="loumalouomega")

    version("main", branch="main")
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

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.15:", type="build")
    depends_on("py-scikit-build-core@0.8:", type="build")
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
        }
