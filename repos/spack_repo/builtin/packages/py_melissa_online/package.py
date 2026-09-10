# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMelissaOnline(PythonPackage):
    """Melissa: file-avoiding, adaptive, fault-tolerant and elastic
    framework for large-scale sensitivity analysis or deep-surrogate training."""

    homepage = "https://gitlab.inria.fr/melissa/melissa"
    git = "https://gitlab.inria.fr/melissa/melissa.git"
    url = "https://gitlab.inria.fr/melissa/melissa/-/archive/v3.0.0/melissa-v3.0.0.tar.gz"

    maintainers("abhishek1297", "raffino")

    license("BSD-3-Clause")

    version("develop", branch="develop", preferred=True)
    version("3.0.0", sha256="9146ac9eff2ae029a189a0fc944b1857f3fd9230000e151a693e73e10943486c")

    variant(
        "launcher_only",
        default=False,
        description="Installs only pure Python launcher components",
    )
    variant(
        "metric_logger",
        values=["tensorboard", "wandb"],
        default="tensorboard",
        description="Metric logger to use for DL logging.",
    )
    variant(
        "torch",
        default=True,
        when="~launcher_only",
        description="Enable PyTorch framework.",
    )
    requires("platform=linux", msg="Melissa is only supported on Linux Systems.")

    depends_on("python@3.11:3.14", type=("build", "run"))

    # basic build-time dependencies
    with default_args(type="build"):
        depends_on("py-pip@23.1:")
        depends_on("py-scikit-build-core@0.11:")
        depends_on("cmake@3.24:")
        depends_on("ninja")

    # basic runtime dependencies
    with default_args(type="run"):
        depends_on("py-typing-extensions")
        depends_on("py-psutil@5.4:")
        depends_on("py-jsonschema@4.5:")
        depends_on("py-python-rapidjson@1.8:")

        # monitoring dependencies
        depends_on("py-requests@2.32:")
        depends_on("py-rich@14:")

    with when("~launcher_only"):
        # ======================================================
        #                client-api dependencies
        # ======================================================
        with default_args(type="build"):
            depends_on("c")
            depends_on("cxx")
            depends_on("fortran")
            depends_on("py-pybind11@3:")

        with default_args(type=("build", "run")):
            depends_on("mpi")
            depends_on("py-mpi4py@3.1.6:")
            depends_on("conduit@0.9.7:+mpi+python+fortran+shared~hdf5~examples")
            depends_on("libzmq@4.2:4")
        # ======================================================

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #                server-side dependencies
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        with default_args(type="run"):
            depends_on("py-pyzmq@22.3.0:")
            depends_on("py-numpy@1.21:")
            depends_on("py-cloudpickle@2.2.0:")
            depends_on("py-iterative-stats@0.1.2:")
            depends_on("py-scipy@1.10.0:")
            depends_on("py-matplotlib")
            depends_on("py-tensorboardx@2.6:", when="metric_logger=tensorboard")
            depends_on("py-wandb@0.15:", when="metric_logger=wandb")

            with when("+torch"):
                depends_on("py-torch@2:+distributed+mpi")
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # end when("~launcher_only")

    def config_settings(self, spec, _):
        """Pass variants to scikit-build-core/CMake."""
        settings = {}
        settings["cmake.define.LAUNCHER_ONLY"] = "ON" if "+launcher_only" in spec else "OFF"
        settings["cmake.define.INSTALL_ZMQ"] = "OFF"
        settings["cmake.define.INSTALL_CONDUIT"] = "OFF"
        return settings

    def setup_dependent_build_environment(self, env, _):
        """Prepend MelissaConfig.cmake path to CMAKE_PREFIX_PATH."""
        python_version = self.spec["python"].version.up_to(2)
        # location inside the installation prefix where MelissaConfig.cmake resides
        config_path = join_path(
            self.prefix,
            "lib",
            f"python{python_version}",
            "site-packages",
            "melissa",
            "share",
            "cmake",
            "Melissa",
        )
        env.prepend_path("CMAKE_PREFIX_PATH", config_path)

    @run_before("install")
    def warn_about_variants(self):
        """Warns user"""

        if "^py-torch%gcc@13:" in self.spec:
            tty.warn(
                "\n**********************************************************************"
                "\n\t PyTorch builds may fail on recent GCC versions."
                "\n\t It is recommended to use `%gcc@11:12`."
                "\n**********************************************************************"
            )

        if "+launcher_only" in self.spec:
            tty.warn(
                "\n**********************************************************************"
                "\n\tYou are building Melissa with launcher only mode."
                "\n\tOther set variants will be ignored."
                "\n**********************************************************************"
            )
