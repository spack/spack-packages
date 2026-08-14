# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPsims(PythonPackage):
    """A declarative API for writing XML documents for HUPO PSI-MS mzML and mzIdentML."""

    homepage = "https://mobiusklein.github.io/psims"
    pypi = "psims/psims-1.3.6.tar.gz"

    license("Apache-2.0")

    version("1.3.6", sha256="f63d5d7659a3cd87c2c604d0bb460f18c20816653747e355426e35ce91989447")

    variant("numpress", default=False, description="Support numpressed mzML format")
    variant("mzmlb", default=False, description="Support bzMLb format")
    variant("pyteomics", default=False, description="Optional to avoid circular dependency")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-lxml")
    depends_on("py-numpy")
    depends_on("py-six")
    depends_on("py-sqlalchemy")

    depends_on("py-pynumpress", when="+numpress")

    depends_on("py-h5py", when="+mzmlb")
    depends_on("py-hdf5plugin", when="+mzmlb")

    depends_on("py-pyteomics@4.0.1:", when="+pyteomics")
