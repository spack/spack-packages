# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Melissa(CMakePackage):
    """Melissa is a file-avoiding, adaptive, fault-tolerant and elastic
    framework, to run large-scale sensitivity analysis on supercomputers.

    **Note:** This package is now unified as `py-melissa-online` from version 3+.
    """

    homepage = "https://gitlab.inria.fr/melissa/melissa"
    git = "https://gitlab.inria.fr/melissa/melissa.git"
    url = "https://gitlab.inria.fr/melissa/melissa/-/archive/v2.0.0/melissa-v2.0.0.tar.gz"
    # attention: Git**Hub**.com accounts
    maintainers("abhishek1297", "raffino")

    version(
        "2.4.1",
        sha256="92a8c7f823ef79c8a5eb05b67120e130c9b03bf7fecd635b4ae9501eb32b2fd7",
        deprecated=True,
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")  # generated
    depends_on("pkgconfig", type="build")

    with when("@:2.1.0"):
        depends_on("cmake@3.15:", type="build")
        depends_on("python@3.9:3.12", type=("build", "run"))

    with when("@2.1.1:"):
        depends_on("cmake@3.22:", type="build")
        depends_on("python@3.11:3.12", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("libzmq@4.2:4")
        depends_on("mpi")

    def cmake_args(self):
        args = []

        if self.spec.satisfies("@:2.0.0"):
            # embed runtime library search paths
            rpaths = [self.spec["libzmq"].prefix.lib, self.spec["mpi"].prefix.lib]
            joined_rpaths = ";".join(rpaths)

            args.append(f"-DCMAKE_INSTALL_RPATH={joined_rpaths}")
            args.append("-DCMAKE_INSTALL_RPATH_USE_LINK_PATH=ON")
        return args

    def setup_run_environment(self, env):
        python = self.spec["python"]
        python_version = python.version.up_to(2)
        # This path points to the python client API scripts installed in $CMAKE_INSTALL_PREFIX/lib
        melissa_api_site_packages = f"{self.prefix.lib}/python{python_version}/site-packages"
        env.prepend_path("PYTHONPATH", melissa_api_site_packages)
