# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.scons import SConsPackage
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


def submodules(package):
    submodules = []
    if package is not None and package.spec.satisfies("~external-eigen"):
        submodules.append("ext/eigen")
    if package is not None and package.spec.satisfies("~external-fmt"):
        submodules.append("ext/fmt")
    if package is not None and package.spec.satisfies("~external-googletest"):
        submodules.append("ext/googletest")
    if package is not None and package.spec.satisfies("~external-sundials"):
        submodules.append("ext/sundials")
    if (
        package is not None
        and package.spec.satisfies("~external-highfive")
        and package.spec.satisfies("@3.0.0:")
    ):
        submodules.append("ext/HighFive")
    if (
        package is not None
        and package.spec.satisfies("~external-yamlcpp")
        and package.spec.satisfies("@2.5.1:")
    ):
        submodules.append("ext/yaml-cpp")
    return submodules


class Cantera(SConsPackage):
    """Cantera is an open-source suite of tools for problems involving
    chemical kinetics, thermodynamics, and transport processes."""

    homepage = "https://www.cantera.org/docs/sphinx/html/index.html"
    url = "https://github.com/Cantera/cantera/archive/v2.5.1.tar.gz"
    git = "https://github.com/Cantera/cantera.git"

    version(
        "3.2.0",
        tag="v3.2.0",
        commit="4a8358eb80cfeb50474386b5f9ec0b3a83519889",
        submodules=submodules,
    )
    version(
        "3.1.0",
        tag="v3.1.0",
        commit="6e0027548cf295bd478b8acfe34816f2db6dd58b",
        submodules=submodules,
    )
    version(
        "3.0.0",
        tag="v3.0.0",
        commit="806842dacc59203cfe98b8467a27a6b386cd5ece",
        submodules=submodules,
    )

    version(
        "2.6.0",
        tag="v2.6.0",
        commit="9573e6b1e1097dca3bf86da37726333ab62663bb",
        submodules=submodules,
    )

    version(
        "2.5.1",
        tag="v2.5.1",
        commit="b0bace78223959cd3e5a15317734cacff7b0b0a2",
        submodules=submodules,
    )

    version(
        "2.4.0",
        tag="v2.4.0",
        commit="8f2468da525ca7ab96a0fabf96c493b429fd522d",
        submodules=submodules,
    )

    version(
        "2.3.0",
        tag="v2.3.0",
        commit="8329edf45fc4a3e0b1a93e882be77ef2fbf9c9c5",
        submodules=submodules,
        deprecated=True,  # python 2.7 required, unsupported
    )

    version(
        "2.2.1",
        tag="v2.2.1",
        commit="92d17b5feb98107ac104a7e4deb43fd35748288d",
        deprecated=True,  # python 2.7 required, unsupported
    )

    variant(
        "blas-lapack",
        default=False,
        description=(
            "Use external blas and lapack installation. "
            "Otherwise, linear algebra is done with Eigen."
        ),
    )
    variant("debug", default=True, description="With compiler debugging symbols")

    variant("hdf5", default=False, description="With HDF5 support")
    conflicts("+hdf5", when="@:2.4.0")

    variant(
        "legacy-clib",
        default=False,
        description="Build the legacy CLib instead of the generated CLib.",
    )
    conflicts("+legacy-clib", when="@:2.6")

    variant("python", default=False, description="With the cantera python module")

    variant("external-eigen", default=False, description="Use external eigen installation")
    conflicts("+external-eigen", when="@:2.2.1")

    variant("external-fmt", default=False, description="Use external fmt installation")
    conflicts("+external-fmt", when="@:2.2.1")

    variant(
        "external-googletest", default=False, description="Use external googletest installation"
    )
    conflicts("+external-googletest", when="@:2.2.1")

    variant("external-highfive", default=False, description="Use external highfive installation")
    conflicts("+external-highfive", when="@:2.6.0")

    variant("external-sundials", default=False, description="Use external sundials installation")

    variant("external-yamlcpp", default=False, description="Use external yaml-cpp installation")
    conflicts("+external-yamlcpp", when="@2.4.0:")

    variant(
        "matlab",
        default=False,
        description="Build the Cantera legacy Matlab toolbox (vesion <= 3.0)",
    )
    conflicts("+matlab", when="@3.1.0:")

    variant(
        "libdirname",
        default="lib",
        description="Directory name where Cantera is installed",
        values=("lib", "lib64", "libx32"),
        multi=False,
    )

    # Required dependencies
    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    # build dependencies
    depends_on("py-packaging", type="build")
    depends_on("python@3.10:", when="@3.0.0:", type="build")
    depends_on("python@:3.10", when="@2.4.0:2.6.0", type="build")

    # additional dependencies for version >= 3.2.0
    depends_on("doxygen@1.8:", when="@3.2.0:", type="build")
    depends_on("py-ruamel-yaml@0.17.16:", when="@3.2.0:", type="build")
    depends_on("py-jinja2@2.10:", when="@3.2.0:", type="build")

    # optional external dependencies
    # otherwise versions included as submodules are used
    depends_on("eigen", when="+external-eigen")
    depends_on("fmt@3.0.0:3.0.2", when="+external-fmt")
    depends_on("googletest+gmock", when="+external-googletest")
    depends_on("hdf5", when="+hdf5")
    depends_on("highfive", when="@3.0.0: +external-highfive")
    depends_on("yaml-cpp", when="+external-yamlcpp")
    depends_on("sundials@7:", when="@3.1.0: +external-sundials")
    depends_on("sundials@:6", when="@3.0.0 +external-sundials")
    depends_on("sundials@:5", when="@:2.6.0 +external-sundials")
    depends_on("blas", when="+blas-lapack")
    depends_on("lapack", when="+blas-lapack")

    # TODO: replace this with an explicit list of components of Boost,
    # for instance depends_on('boost +filesystem')
    # See https://github.com/spack/spack/pull/22303 for reference
    depends_on(Boost.with_default_variants)

    # Python module dependencies
    extends("python", when="+python")
    depends_on("py-cython", when="+python", type="build")
    depends_on("py-numpy", when="+python", type=("build", "run"))
    depends_on("py-scipy", when="+python", type=("build", "run"))
    depends_on("py-3to2", when="+python", type=("build", "run"))
    depends_on("py-pip", when="+python", type=("build", "run"))
    depends_on("py-matplotlib", when="+python", type=("build", "run"))
    depends_on("py-ruamel-yaml@0.17.16:", when="+python", type=("build", "run"))

    # Matlab toolbox dependencies
    extends("matlab", when="+matlab")

    def build_args(self, spec, prefix):
        # Valid args can be found by running `scons help`
        # Required args
        args = [
            "build",
            "prefix={0}".format(prefix),
            "CC={0}".format(spack_cc),
            "CXX={0}".format(spack_cxx),
            "FORTRAN={0}".format(spack_fc),
            # Allow Spack environment variables to propagate through to SCons
            "env_vars=all",
        ]

        if spec.satisfies("@2.5.1:"):
            args.extend(
                [
                    "libdirname={0}".format(spec.variants["libdirname"].value),
                    "cc_flags={0}".format(self.compiler.cc_pic_flag),
                ]
            )
        else:
            # enable build of versions <= 2.4.0 with modern compilers
            args.append("cc_flags={0} -fcommon".format(self.compiler.cc_pic_flag))

        if spec.satisfies("@:2.5.1"):
            args.append("VERBOSE=yes")

        if spec.satisfies("@:2.2.1"):
            args.append("F77={0}".format(spack_f77))

        # Use external fmt installation
        if spec.satisfies("+external-fmt"):
            args.append("system_fmt=y")

        # Use external googletest installation
        if spec.satisfies("+external-googletest"):
            args.append("system_googletest=y")

        # Use external eigen installation
        if spec.satisfies("+external-eigen"):
            args.extend(
                [
                    "system_eigen=y",
                    "extra_inc_dirs={0}".format(
                        join_path(
                            spec["eigen"].prefix.include,
                            "eigen{0}".format(spec["eigen"].version.up_to(1)),
                        )
                    ),
                ]
            )

        # HDF5 support
        if spec.satisfies("+hdf5"):
            args.extend(
                [
                    "hdf_support=y",
                    "hdf_include={0}".format(spec["hdf5"].prefix.include),
                    "hdf_libdir={0}".format(spec["hdf5"].prefix.libs),
                ]
            )

        # Use external highfive installation
        if spec.satisfies("+external-highfive") and spec.satisfies("@3.0.0:"):
            args.extend(
                ["system_highfive=y", "extra_inc_dirs={0}".format(spec["highfive"].prefix.include)]
            )

        # Use external yaml-cpp installation
        if spec.satisfies("+external-yamlcpp"):
            args.extend(
                [
                    "system_yamlcpp=y",
                    "extra_inc_dirs={0}".format(spec["yaml-cpp"].prefix.include),
                    "extra_lib_dirs={0}".format(spec["yaml-cpp"].prefix.libs),
                ]
            )

        # Use external sundials installation
        if spec.satisfies("+external-sundials"):
            args.extend(
                [
                    "system_sundials=y",
                    "sundials_include={0}".format(spec["sundials"].prefix.include),
                    "sundials_libdir={0}".format(spec["sundials"].prefix.libs),
                ]
            )

        # Use external BLAS/LAPACK installations
        if spec.satisfies("+blaslapack"):
            lapack_blas = spec["lapack"].libs + spec["blas"].libs
            args.extend(
                [
                    "blas_lapack_libs={0}".format(",".join(lapack_blas.names)),
                    "blas_lapack_dir={0}".format(spec["lapack"].prefix.lib),
                ]
            )

        # Enable debugging symbols
        if spec.satisfies("+debug"):
            args.append("debug=yes")
        else:
            args.append("debug=no")

        # legacy CLib
        if spec.satisfies("+legacy-clib"):
            args.append("clib_legacy=yes")

        # Boost support
        if spec.satisfies("@2.3.0:"):
            args.append("boost_inc_dir={0}".format(spec["boost"].prefix.include))
        else:
            args.extend(
                [
                    "build_thread_safe=yes",
                    "boost_inc_dir={0}".format(spec["boost"].prefix.include),
                    "boost_lib_dir={0}".format(spec["boost"].prefix.lib),
                ]
            )

        # Python module
        if spec.satisfies("+python"):
            if spec.satisfies("@:2.5.1"):
                args.extend(["python_package=full", "python_cmd={0}".format(python.path)])
                if spec["python"].satisfies("@3:"):
                    args.extend(["python3_package=y", "python3_cmd={0}".format(python.path)])
                else:
                    args.append("python3_package=n")
            else:
                args.extend(["python_package=y", "python_cmd={0}".format(python.path)])
        else:
            if spec.satisfies("@:2.5.1"):
                args.append("python_package=none")
                args.append("python3_package=n")
            else:
                args.append("python_package=n")

        # Matlab toolbox
        if spec.satisfies("+matlab") and spec.satisfies("@:3.1.0"):
            args.extend(["matlab_toolbox=y", "matlab_path={0}".format(spec["matlab"].prefix)])
        elif spec.satisfies("@:2.5.1"):
            args.append("matlab_toolbox=n")

        return args

    def build_test(self):
        if self.spec.satisfies("+python"):
            # Tests will always fail if Python dependencies aren't built
            # In addition, 3 of the tests fail when run in parallel
            scons("test", parallel=False)

    @run_after("install")
    def filter_compilers(self):
        """Run after install to tell the Makefile and SConstruct files to use
        the compilers that Spack built the package with.

        If this isn't done, they'll have CC, CXX, F77, and FC set to Spack's
        generic cc, c++, f77, and f90. We want them to be bound to whatever
        compiler they were built with."""

        kwargs = {"ignore_absent": True, "backup": False, "string": True}
        dirname = os.path.join(self.prefix, "share/cantera/samples")

        cc_files = [
            "cxx/rankine/Makefile",
            "cxx/NASA_coeffs/Makefile",
            "cxx/kinetics1/Makefile",
            "cxx/flamespeed/Makefile",
            "cxx/combustor/Makefile",
            "f77/SConstruct",
        ]

        cxx_files = [
            "cxx/rankine/Makefile",
            "cxx/NASA_coeffs/Makefile",
            "cxx/kinetics1/Makefile",
            "cxx/flamespeed/Makefile",
            "cxx/combustor/Makefile",
        ]

        f77_files = ["f77/Makefile", "f77/SConstruct"]

        fc_files = ["f90/Makefile", "f90/SConstruct"]

        for filename in cc_files:
            filter_file(
                os.environ["CC"], self.compiler.cc, os.path.join(dirname, filename), **kwargs
            )

        for filename in cxx_files:
            filter_file(
                os.environ["CXX"], self.compiler.cxx, os.path.join(dirname, filename), **kwargs
            )

        for filename in f77_files:
            filter_file(
                os.environ["F77"], self.compiler.f77, os.path.join(dirname, filename), **kwargs
            )

        for filename in fc_files:
            filter_file(
                os.environ["FC"], self.compiler.fc, os.path.join(dirname, filename), **kwargs
            )
