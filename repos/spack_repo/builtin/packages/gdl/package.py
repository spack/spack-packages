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

    version("1.1.2_testing3", sha256="09f2c6dbfbd5b13e0c82cf608f04c48f7ec460b071781315721bd2a10b48bd25")
    version("1.1.2_testing2", sha256="00a5ece888e99a7391fea66188f322426e3f8b5daedb2d5c285ee75413a55043")
    version("1.1.2_testing", sha256="04fb26671218f38aea611ea4b41679dc9ea5125889d0367fad541b9eeed709d2")
    version("1.1.1", sha256="744ed3abcdc5e1bbf31147a8a0c21c33662f200b6096ee3d3adedd160a3a9662")
    version("1.1", sha256="ece207ad463cb93be625a9f65ce94552a145f11ca0788b75f2761c2c6b4c094a")
    version("1.0.6", sha256="7623beeeca04fac85703b0bd6d9368d9be76e4c93a5ffe0ef638a9447aea4c1f")
    version("1.0.5", sha256="1929c5a905aa7cb1914d823ae08ab86c0e4cdc74e9a5233f8bad1435f0c4bf63")
    version("1.0.4", sha256="2b04c4319202ccd4ee73e8e771006b812d0db9f9e68428b85884c99bc66aa276")
    version("1.0.3", sha256="d2a4e205d4ef9157081cd467be3572ae5d2338f8e56fbc7ed20cf6f7213d7ae2")
    version("0.9.9", sha256="ad5de3fec095a5c58b46338dcc7367d2565c093794ab1bbcf180bba1a712cf14")
    version("0.9.8", sha256="0e22df7314feaf18a76ae39ee57eea2ac8c3633bc095acbc25e1e07277d7c98b")

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

    depends_on("plplot+wx", when="@:1.0.6 +wx")  #plplot dependency removed in v1.1
    depends_on("plplot+wx+wxold", when="@:1.0.6 +wx")
    depends_on("plplot~wx", when="@:1.0.6 ~wx")
    
    depends_on("proj@:8", when="+proj")
    depends_on("wxwidgets@3.2.8.1", when="+wx")
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

    # Building the Python module requires patches currently targetting 0.9.8
    # othwerwise asking for the Python module *only* builds the Python module
    conflicts("+python", when="@:0.9.7,0.9.9")

    # Allows building gdl as a shared library to in turn allow building
    # both the executable and the Python module
    patch(
        "https://sources.debian.org/data/main/g/gnudatalanguage/0.9.8-7/debian/patches/Create-a-shared-library.patch",
        sha256="bb380394c8ea2602404d8cd18047b93cf00fdb73b83d389f30100dd4b0e1a05c",
        when="@0.9.8",
    )
    patch(
        "Always-build-antlr-as-shared-library.patch",
        sha256="f40c06e8a8f1977780787f58885590affd7e382007cb677d2fb4723aaadd415c",
        when="@0.9.8",
    )

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
