from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyAdios4dolfinx(PythonPackage):
    """Python interface for IO for py-fenics-dolfinx using adios2"""

    homepage = "https://www.jsdokken.com/adios4dolfinx"

    url = "https://github.com/jorgensd/adios4dolfinx/archive/v0.9.4.tar.gz"
    git = "https://github.com/jorgensd/adios4dolfinx.git"

    maintainers("jorgensd")

    license("MIT", checked_by="jorgensd")

    version("main", branch="main")
    version("0.9.4", sha256="1d75d4f45f28c64821ad023df3273d933f1d4752c0e53b62f41030dca06bd627")
    version("0.9.3", sha256="0928f48dcc2ffaf5c97d3b2fedde6c4d79b2cbc5a3e2dbe0a0d50572c02590f5")
    version("0.9.2", sha256="a1b111a586ba8af6776e05d001850fdfc196cbc173eb501c8c1659ade993f49c")
    version(
        "0.9.1.post0", sha256="91a957bc967c1a3b0a454a5b8658600c38a38535c90b0c8b31bc0f52841c07fd"
    )
    version("0.9.1", sha256="4dfd8ea3d8d21566adc40a3615830e5613d215e774e7f30de6d8c88b2078b549")
    version("0.9.0", sha256="5a72a8bc111d848b56d6eb776d7ca5963fe41e4126a3d875304224f80f15b8f6")

    depends_on("py-packaging", type="run")

    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-scikit-build-core+pyproject@0.10:", type="build")
    depends_on("py-setuptools@42:", type="build")

    depends_on("py-fenics-dolfinx@main", when="@main")
    depends_on("py-fenics-dolfinx@0.9.0", when="@0.9")

    depends_on("adios2+python+hdf5+mpi", type="run")

    depends_on("py-pytest", type="test")
    depends_on("py-ipyparallel", type="test")
