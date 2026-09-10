# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyteomics(PythonPackage):
    """A collection of tools that simplify reading, writing, and manipulating proteomics
    and mass-spectrometry data formats."""

    homepage = "http://pyteomics.readthedocs.io"
    pypi = "pyteomics/pyteomics-5.0.tar.gz"

    license("Apache-2.0")

    version("5.0", sha256="234a4d361d1a144247caa6b5fc35836eb3a40153bcd6f575c5b95c3bd49de21d")
    version("4.7.5", sha256="382aeaa8b921bdd2a7e5b4aa9fe46c6184bb43701205a845b4b861ee3e88f46a")

    variant("xml", default=False, description="Support XML-based formats")
    variant("tda", default=False, description="Target-Decoy Analysis (TDA)")
    variant("matplotlib", default=False, description="Plotting helpers")
    variant("pandas", default=False, description="Results as dataframes")
    variant("unimod", default=False, description="Unimod database interface")
    variant("numpress", default=False, description="Reading of numpressed mzML")
    variant("mzmlb", default=False, description="Reading of mzMLb format")
    variant("proforma", default=False, description="Parsing of chemical modifications")
    variant("spectrum_utils", default=False, description="Spectrum annotation")
    variant("scikit_learn", default=False, description="MAE regression")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-lxml", when="@5: +xml")
    depends_on("py-lxml@:5.3", when="@:4 +xml")
    depends_on("py-numpy", when="+xml")
    depends_on("py-psims", when="+xml")

    depends_on("py-numpy", when="+tda")

    depends_on("py-matplotlib", when="+matplotlib")

    depends_on("py-pandas@0.17:", when="+pandas")

    depends_on("py-lxml", when="@5: +unimod")
    depends_on("py-lxml@:5.3", when="@:4 +unimod")
    depends_on("py-sqlalchemy@1.4:", when="+unimod")

    depends_on("py-pynumpress", when="+numpress")

    depends_on("py-h5py", when="+mzmlb")
    depends_on("py-hdf5plugin", when="+mzmlb")

    depends_on("py-psims@0.1.43:", when="+proforma")

    depends_on("py-spectrum-utils", when="+spectrum_utils")

    depends_on("py-scikit-learn", when="+scikit_learn")
