from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLeidenalg(PythonPackage):
    """This package implements the Leiden algorithm in C++ and exposes it to python"""

    homepage = "https://leidenalg.readthedocs.io/en/latest/"
    pypi = "leidenalg/leidenalg-0.10.0.tar.gz"

    version("0.10.0", sha256="a3829dceb3d9198a0489891d471f2abe8ffd5a3e8ddc8c298543d16caa8d7f19")

    depends_on("c", type=("build"))
    depends_on("cxx", type=("build"))

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@45:", type=("build"))
    depends_on("py-igraph@0.10", type=("build", "run"))
    depends_on("igraph@0.10", type=("build"))
    depends_on("py-setuptools-scm", type=("build"))

    # Add to this if new versions is released, they must amtch
    depends_on("libleidenalg@0.10.0", when="@0.10.0")

    def patch(self):
        filter_file(
            r"'build-deps/install/include'",
            f"'{self.spec['igraph'].prefix.include}', "
            f"'{self.spec['libleidenalg'].prefix.include}'",
            "setup.py",
            string=True,
        )
        filter_file(
            r"'build-deps/install/lib'",
            f"'{self.spec['igraph'].prefix.lib}', "
            f"'{self.spec['igraph'].prefix.lib64}', "
            f"'{self.spec['libleidenalg'].prefix.lib}', "
            f"'{self.spec['libleidenalg'].prefix.lib64}'",
            "setup.py",
            string=True,
        )
