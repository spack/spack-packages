from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMumps4py(PythonPackage):
    """Python wrapper for the MUMPS solver (MUMPS4PY)."""

    homepage = "https://github.com/imadki/mumps4py"
    url = "https://github.com/imadki/mumps4py/archive/refs/tags/1.0.0.tar.gz"

    maintainers = ["williampiat3"]

    version("1.0.0", sha256="634dd52a9942e88a430d6c8b519cbf6e50db77dd5f1be1cb04e5ab3f3e9da8ba")

    # Python requirements
    depends_on("python@3.5:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type="build")

    # Runtime and build deps
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython", type="build")
    depends_on("py-mpi4py", type=("build", "run"))

    # Optional/test deps
    depends_on("py-pytest", type="test")

    # External solver
    depends_on("mumps")
    depends_on("cmake", type="build")

    def build_args(self, spec, prefix):
        # Ensure MUMPS include/lib are passed if setup.py needs them
        mumps = spec["mumps"]
        args = [
            "--inplace",
            "MUMPS_INC={0}".format(mumps.prefix.include),
            "MUMPS_LIB={0}".format(mumps.prefix.lib),
        ]
        return args

    def test_all_solvers(self):
        """Function to run all mumps4py tests that assess whether all solvers can be used"""
        pytest = which("pytest")
        pytest("tests", "-v")
