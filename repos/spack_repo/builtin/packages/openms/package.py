# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import shutil

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.build_systems.python import PythonExtension

from spack.package import *


class Openms(CMakePackage, PythonExtension):
    """LC/MS data management, analysis and visualization."""

    homepage = "https://www.openms.de"
    url = "https://github.com/OpenMS/OpenMS/archive/refs/tags/release/3.5.0.tar.gz"
    git = "https://github.com/OpenMS/OpenMS.git"

    maintainers("w8jcik")

    version("3.5.0", sha256="550edea8ec9e468e0cdb3dc45677a193cb4b425e52d4ed84547addacd0445c2e")
    version("3.4.1", sha256="fa878fc4efb27151f475dbf59bb3d6a301891bf8c8eb7968934c92e3f2157909")
    version("3.3.0", sha256="9d79c7caffa4589010581d9c6b9e7a38bf501297290ca7c441f95d29879c76e6")
    version("3.2.0", sha256="5ff3ad30ac7f532f5fe0bc2c7ac28508e559848f8070399e2854302923e0ab25")

    version(
        "3.1.0",
        url="https://github.com/OpenMS/OpenMS/releases/download/Release3.1.0/OpenMS-3.1.0-src.tar.gz",
        sha256="0fd13edeaf5eaca014c13560bbcce0ec2abe9de6bb323289b38a3b3943b3d98b",
    )

    variant("gui", default=False, description="Build OpenMS GUI (TOPPView and TOPP utilities)")
    variant("pyopenms", default=False, description="Build pyOpenMS Python package")
    variant("hdf5", default=False, description="Enable HDF5 I/O")
    variant("coinor", default=True, description="Use COIN-OR CoinMP solver (otherwise GLPK)")
    conflicts("@:3.3~hdf5", msg="HDF5 is not optional with older OpenMS")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.21:", type="build")

    conflicts("@3.6 %gcc@:11", msg="OpenMS 3.6 needs GCC >= 12")
    conflicts("@3.4:3.5 %gcc@:9", msg="OpenMS 3.4 and 3.5 need GCC >= 10")

    depends_on("boost+regex+iostreams+date_time+math+pic")
    depends_on("boost@1.81:", when="@3.6:")
    depends_on("boost@1.74:", when="@3.5")
    depends_on("boost@1.74:1.88", when="@3.2:3.4")
    depends_on("boost@1.48:1.88", when="@3.1")

    depends_on("coinmp", when="+coinor")
    depends_on("clp", when="+coinor")
    depends_on("osi", when="+coinor")
    depends_on("coinutils", when="+coinor")
    depends_on("glpk", when="~coinor")

    depends_on("arrow@23:+parquet", when="@3.5:")
    depends_on("bzip2")
    depends_on("curl", when="@3.6:")
    depends_on("eigen@3.4:5", when="@3.6:")
    depends_on("eigen@3.3.4:5", when="@3.5")
    depends_on("eigen@3.3.4:4", when="@:3.4")
    depends_on("libsvm@2.91:")
    depends_on("libzip", when="@3.6.0:")
    depends_on("xerces-c")
    depends_on("zlib", when="@3.5.0:")

    depends_on("hdf5+cxx", when="+hdf5")

    depends_on("python", type=("build", "run"), when="+pyopenms")
    depends_on("py-uv", type=("build", "run"), when="@3.6:+pyopenms")
    depends_on("py-numpy@2:", type=("run"), when="@3.6:+pyopenms")
    depends_on("py-matplotlib@3.5:", type=("run"), when="@3.6:+pyopenms")
    extends("python", when="+pyopenms")

    # One would need to package 'autowrap' to enable pyOpenMS with OpenMS <= 3.5
    #
    #   depends_on("py-cython@:3.1", type="build", when="@3.5+pyopenms")
    #   depends_on("py-cython@:3", type="build", when="@:3.4+pyopenms")
    #   depends_on("py-packaging", type="build", when="@:3.5+pyopenms")
    #   depends_on("py-pip", type="build", when="@:3.5")
    #
    # OpenMS >= 3.6 no longer needs 'autowrap' to build the Python API.

    conflicts(
        "@:3.5+pyopenms",
        msg="Building of pyOpenMS from older OpenMS would require packaging of https://github.com/OpenMS/autowrap",
    )

    # Older releases of OpenMS require GUI-enabled Qt even when the main GUI is not built
    depends_on("qt-base@6.1:+gui+opengl", when="@3.6:+gui")
    depends_on("qt-base@6.1:+gui+opengl+network", when="@3.3:3.5")
    depends_on("qt-svg", when="+gui")
    depends_on("qt-svg", when="@3.4:3.5")

    depends_on("qt@5.6:", when="@:3.2")

    def cmake_args(self):
        args = [
            self.define_from_variant("WITH_GUI", "gui"),
            self.define_from_variant("WITH_HDF5", "hdf5"),
            self.define_from_variant("PYOPENMS", "pyopenms"),
            self.define("MT_ENABLE_OPENMP", True),
            self.define("ENABLE_DOCS", False),
            self.define("HAS_XSERVER", False),
        ]

        if self.spec.satisfies("@3.6:"):
            # The corresponding binary requires .NET runtime which Spack might be able
            # to provide but it is currently not implemented by this recipe.
            args.append(self.define("WITH_THERMO_RAW", False))

        if "+coinor" in self.spec:
            cxx_flags = {
                f"-I{self.spec['clp'].prefix.include}/coin",
                f"-I{self.spec['osi'].prefix.include}/coin",
                f"-I{self.spec['coinutils'].prefix.include}/coin",
            }

            args.append(self.define("CMAKE_CXX_FLAGS", " ".join(cxx_flags)))

        if self.spec.satisfies("~coinor"):
            # tests/class_tests/../LPWrapper_test fails with GLPK
            args.append(self.define("ENABLE_CLASS_TESTING", False))

        return args

    def install(self, spec, prefix):
        if self.spec.satisfies("+pyopenms"):
            python_packages_dir = join_path(
                self.prefix.lib, f"python{self.spec['python'].version.up_to(2)}", "site-packages"
            )

            shutil.move(
                join_path(self.build_directory, "pyOpenMS", "pyopenms"),
                join_path(python_packages_dir, "pyopenms"),
            )

        super().install(spec, prefix)
