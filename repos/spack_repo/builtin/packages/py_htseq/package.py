# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHtseq(PythonPackage):
    """HTSeq is a Python package that provides infrastructure to process
    data from high-throughput sequencing assays."""

    homepage = "https://htseq.readthedocs.io/en/master/index.html"
    pypi = "HTSeq/HTSeq-2.0.3.tar.gz"

    license("GPL-3.0-only")

    version("2.1.2", sha256="69d5a6b9a832ea85edf8a32fbac591a8af2e32bb961d1f3843c48c9d03a77a82")
    version("2.0.3", sha256="c7e7eb29bdc44e80d2d68e3599fa8a8f1d9d6475624dcf1b9644285a8a9c0fac")
    version("0.11.2", sha256="65c4c13968506c7df92e97124df96fdd041c4476c12a548d67350ba8b436bcfc")
    version("0.9.1", sha256="af5bba775e3fb45ed4cde64c691ebef36b0bf7a86efd35c884ad0734c27ad485")

    variant("qa", default=True, description="Quality assessment")
    variant("mtx", default=True, description="BigWig manipulation", when="@2:")
    variant("mtx", default=True, description="mtx output files", when="@2:")
    variant("h5ad", default=True, description="h5ad output files", when="@2:")
    variant("loom", default=True, description="loom output files", when="@2:")

    depends_on("python@3.8:3.12", when="@:0.11.2")
    depends_on("python@3.9:3.12", when="@2.0.3")
    depends_on("python@3.10:", when="@2.1.2:")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    # build-only dependencies
    depends_on("py-setuptools", type="build")
    depends_on("py-cython@0.29.5:", type="build")
    # run dependencies
    depends_on("py-numpy@1", type=("build", "run"), when="@:2.0.7")
    depends_on("py-numpy@2:", type=("build", "run"), when="@2.0.8:")
    depends_on("py-pysam", type=("build", "run"))
    # variant dependencies
    depends_on("py-matplotlib@1.4:", type=("build", "run"), when="+qa")
    depends_on("py-scipy@1.5.0:", type=("build", "run"), when="+mtx")
    depends_on("py-anndata", type=("build", "run"), when="+h5ad")
    depends_on("py-loompy", type=("build", "run"), when="+loom")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/h/{0}/{0}-{1}.tar.gz"
        if version >= Version("2.0.7"):
            name = "htseq"
        else:
            name = "HTSeq"
        return url.format(name, version)
