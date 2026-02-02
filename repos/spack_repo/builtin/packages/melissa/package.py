# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Melissa(CMakePackage):
    """Melissa is a file-avoiding, adaptive, fault-tolerant and elastic
    framework, to run large-scale sensitivity analysis on supercomputers.
    """

    homepage = "https://gitlab.inria.fr/melissa/melissa"
    git = "https://gitlab.inria.fr/melissa/melissa.git"
    url = "https://gitlab.inria.fr/melissa/melissa/-/archive/v2.0.0/melissa-v2.0.0.tar.gz"
    # attention: Git**Hub**.com accounts
    maintainers("abhishek1297", "raffino")

    version("develop", branch="develop", preferred=True)
    version("2.3.0", sha256="f356e05082e4bb26a210cd11ccfa78a783ebe07be2bd75d5e51ed10da3b58997")
    version("2.2.0", sha256="e805c9ac08de5aa666768d5d92bfc680f064bd9108415a911dfd08ad7b0a3cf3")
    version("2.1.1", sha256="6b92852429f13b144860edc37c7914723addabb0ec0bd108929ff567334d3f71")
    version("2.1.0", sha256="cf0f105ed5b1da260cc7476aec23df084470b50a61df997c0e457c38948bed93")
    version("2.0.1", sha256="a7ff4df75ea09af435b0c28c3fa3cab9335c1c76e1c48757facce36786b4962c")
    version("2.0.0", sha256="75957d1933cd9c228a6e8643bc855587162c31f3b0ca94c3f5e0e380d01775dd")

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

    def setup_build_environment(self, env):
        zmq_pkgconfig_path = self.spec["libzmq"].prefix.lib.pkgconfig
        env.prepend_path("PKG_CONFIG_PATH", zmq_pkgconfig_path)

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
