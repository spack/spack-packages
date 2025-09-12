# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gdl(CMakePackage):
    """A free and open-source IDL/PV-WAVE compiler.

    GNU Data Language (GDL) is a free/libre/open source incremental compiler
    compatible with IDL and to some extent with PV-WAVE.
    """

    homepage = "https://github.com/gnudatalanguage/gdl"
    url = "https://github.com/gnudatalanguage/gdl/releases/download/v1.1.2_testing3/gdl-v1.1.2_testing3.tar.gz"
    git = "https://github.com/gnudatalanguage/gdl.git"

    maintainers("lbsny")

    version(
        "1.1.2_testing3", sha256="09f2c6dbfbd5b13e0c82cf608f04c48f7ec460b071781315721bd2a10b48bd25"
    )
    version(
        "1.1.2_testing2", sha256="00a5ece888e99a7391fea66188f322426e3f8b5daedb2d5c285ee75413a55043"
    )
    version(
        "1.1.2_testing", sha256="04fb26671218f38aea611ea4b41679dc9ea5125889d0367fad541b9eeed709d2"
    )
    version("1.1.1", sha256="744ed3abcdc5e1bbf31147a8a0c21c33662f200b6096ee3d3adedd160a3a9662")
    version("1.1", sha256="915b290af1fe21fe1307ecb3756b7841dd28fdeff541d4a36cf7b57371c3c9f3")
    version("1.0.6", sha256="b02a257d59ad608cd300471e9cac6c23b6dc75938f79eaba812e30c56aed4865")
    version("1.0.5", sha256="b1ea9ee700b3fead67e78877ac95dde84b6d0fa4e959dd17251c078673dd52ec")
    version("1.0.4", sha256="f248123c1c82710d070243e29b2dd445bc6fd378800f3bdaa4b8cb46962c5fb1")
    version("1.0.3", sha256="db72eeb84c54dba387d5474500ce005ff1dc605b070bd00f57a552d3bb6ab16c") 

    variant("graphicsmagick", default=False, description="Enable GraphicsMagick")
    variant("hdf4", default=False, description="Enable HDF4")
    variant("hdf5", default=True, description="Enable HDF5")
    variant("openmp", default=True, description="Enable OpenMP")
    variant("proj", default=True, description="Enable PROJ")
    variant("python", default=False, description="Build the GDL Python module")
    variant("wx", default=False, description="Enable WxWidgets")
    variant("x11", default=False, description="Enable X11")
    variant("mpi", default=False, description="Enable MPI")

    extends("python", when="+python")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    depends_on("cmake@3:", type="build")
    depends_on("graphicsmagick", when="+graphicsmagick")
    depends_on("hdf", when="+hdf4")
    depends_on("hdf5", when="+hdf5")
    depends_on("libx11", when="+x11")

    depends_on("plplot+wx", when="@:1.0.6 +wx")  # plplot dependency removed in v1.1
    depends_on("plplot+wx+wxold", when="@:1.0.6 +wx")
    depends_on("plplot~wx", when="@:1.0.6 ~wx")
    
    depends_on("proj@:8", when="+proj")
    depends_on("wxwidgets", when="+wx")
    depends_on("mpi", when="+mpi")

    depends_on("eigen")
    depends_on("fftw")
    depends_on("gsl")
    depends_on("jpeg")
    depends_on("libice")
    depends_on("libsm")
    depends_on("libxinerama")
    depends_on("libxxf86vm")
    depends_on("netcdf-c")
    depends_on("pslib")
    depends_on("readline")
    depends_on("libtirpc", type="link")
    depends_on("libgeotiff", type="link")
    depends_on("udunits")
    depends_on("eccodes")
    depends_on("shapelib")
    depends_on("expat")
    depends_on("glpk")
    depends_on("qhull")

    def cmake_args(self):
        args = []

        if self.spec.satisfies("+mpi"):
            args += ["-DMPI=ON"]
        else:
            args += ["-DMPI=OFF"]

        if self.spec.satisfies("+graphicsmagick"):
            args += ["-DGRAPHICSMAGICK=ON"]
        else:
            args += ["-DGRAPHICSMAGICK=OFF"]

        if self.spec.satisfies("+hdf4"):
            args += ["-DHDF=ON"]
        else:
            args += ["-DHDF=OFF"]

        if self.spec.satisfies("+hdf5"):
            args += ["-DHDF5=ON"]
        else:
            args += ["-DHDF5=OFF"]

        if self.spec.satisfies("+openmp"):
            args += ["-DOPENMP=ON"]
        else:
            args += ["-DOPENMP=OFF"]

        if self.spec.satisfies("+proj"):
            args += ["-DLIBPROJ=ON"]
        else:
            args += ["-DLIBPROJ=OFF"]

        if self.spec.satisfies("+python"):
            args += ["-DPYTHON_MODULE=ON"]
        else:
            args += ["-DPYTHON_MODULE=OFF"]
            args += ["-DPYTHON=OFF"]

        if self.spec.satisfies("+wx"):
            args += ["-DWXWIDGETS=ON"]
        else:
            args += ["-DWXWIDGETS=OFF"]

        if self.spec.satisfies("+x11"):
            args += ["-DX11=ON"]
        else:
            args += ["-DX11=OFF"]

        return args

    @run_after("install")
    def post_install(self):
        if self.spec.satisfies("+python"):
            # gdl installs the python module into prefix/lib/site-python
            # move it to the standard location
            src = os.path.join(self.spec.prefix.lib, "site-python")
            dst = python_platlib
            if os.path.isdir(src):
                if not os.path.isdir(dst):
                    mkdirp(dst)
                for f in os.listdir(src):
                    os.rename(os.path.join(src, f), os.path.join(dst, f))
