from spack_repo.builtin.build_systems.python import PythonPackage, PythonPipBuilder

from spack.package import *


class PyMumps4py(PythonPackage):
    """Python wrapper for the MUMPS solver (MUMPS4PY)."""

    homepage = "https://github.com/imadki/mumps4py"
    url = "https://github.com/imadki/mumps4py/archive/refs/tags/1.0.0.tar.gz"

    maintainers = ["williampiat3"]

    version("1.0.0", sha256="634dd52a9942e88a430d6c8b519cbf6e50db77dd5f1be1cb04e5ab3f3e9da8ba")

    # build dependencies
    with default_args(type="build"):
        depends_on("cmake")
        depends_on("py-setuptools")
        depends_on("py-cython")

    # Python dependencies
    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        depends_on("py-mpi4py")

    # Optional/test deps
    depends_on("py-pytest", type="test")

    # External solver
    depends_on("mumps+float+complex+double")

    def build_args(self, spec, prefix):
        # Ensure MUMPS include/lib are passed if setup.py needs them
        mumps = spec["mumps"]
        args = [
            "MUMPS_INC={0}".format(mumps.prefix.include),
            "MUMPS_LIB={0}".format(mumps.prefix.lib),
        ]
        return args

    def install(self, spec: Spec, prefix: Prefix) -> None:
        """Install everything from build directory."""
        pip = spec["python"].command
        pip.add_default_arg("-m", "pip")

        args = PythonPipBuilder.std_args(self) + [f"--prefix={prefix}"]

        config_settings = self.config_settings(spec, prefix)
        for setting in config_settings:
            if isinstance(config_settings[setting], list):
                for value in config_settings[setting]:
                    args.append(f"--config-settings={setting}={value}")
            else:
                args.append(f"--config-settings={setting}={config_settings[setting]}")
        for option in self.install_options(spec, prefix):
            args.append(f"--install-option={option}")

        if self.stage.archive_file and self.stage.archive_file.endswith(".whl"):
            args.append(self.stage.archive_file)
        else:
            args.append(".")

        with working_dir(self.build_directory):
            pip(*args)

    def config_settings(self, spec, prefix):
        return {"--build-option": ["build_ext", "--inplace"]}

    def setup_build_environment(self, env):
        # Required by mumps4py to specify which MUMPS solvers to use
        env.set("MUMPS_SOLVERS", "dmumps,cmumps,zmumps,smumps")
        env.set("MUMPS_INC", join_path(self.spec["mumps"].prefix, "include"))
        env.set("MUMPS_LIB", join_path(self.spec["mumps"].prefix, "lib"))

    def setup_run_environment(self, env):
        # Required by mumps4py to specify which MUMPS solvers to use
        env.set("MUMPS_SOLVERS", "dmumps,cmumps,zmumps,smumps")
        env.set("MUMPS_INC", join_path(self.spec["mumps"].prefix, "include"))
        env.set("MUMPS_LIB", join_path(self.spec["mumps"].prefix, "lib"))

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def run_source_tests(self):
        """Test if all solvers are working"""
        with working_dir("spack-test", create=True):
            python(
                "-c",
                ";".join(
                    [
                        "from mumps4py.mumps_solver import MumpsSolver",
                        "MumpsSolver(verbose=False,system='complex64')",
                        "MumpsSolver(verbose=False, system='complex128')",
                        "MumpsSolver(verbose=False, system='double')",
                        "MumpsSolver(verbose=False, system='single')",
                    ]
                ),
            )
