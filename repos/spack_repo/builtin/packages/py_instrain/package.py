# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyInstrain(PythonPackage):
    """inStrain is python program for analysis of co-occurring genome
    populations from metagenomes that allows highly accurate genome
    comparisons, analysis of coverage, microdiversity, and linkage, and
    sensitive SNP detection with gene localization and synonymous
    non-synonymous identification."""

    homepage = "https://github.com/MrOlm/instrain"
    pypi = "inStrain/inStrain-1.5.7.tar.gz"

    maintainers("MrOlm")

    variant("prodigal", default=False, description="Enables profiling on a gene by gene level")

    license("MIT")

    version("1.10.0", sha256="f40f1d439914ec85cec83ce4c3f2fbf2ce064132109be9f2d3bfd048899b5a8e")
    version("1.6.3", sha256="8cc4af185a41f860aa3a58dfacabfe635bf7b28535ac0bb4db67983f95dbd528")
    version("1.5.7", sha256="c5dcb01dae244927fe987b5f0695d895ccf521c9dfd87a2cb59057ad50bd9bfa")

    # Bio.codonalign.codonalphabet was removed in biopython 1.78; fixed upstream after 1.10.0
    # https://github.com/MrOlm/inStrain/pull/221
    patch(
        "https://github.com/MrOlm/inStrain/commit/260e022d7e0fd9ad31a1dfca47de38748cff2200.patch?full_index=1",
        sha256="482792f85248c55568551079a99d2e4b02a49e97148e57a15cc66fde57aabd6f",
        when="@:1.10.0",
    )

    depends_on("python@3.4.0:", type=("build", "run"))
    depends_on("py-setuptools", type=("build"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas@0.25:1.1.2,1.1.4:", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"), when="@:1.7.0")
    depends_on("py-pytest", type=("build"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-pysam@0.15:", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-lmfit", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"), when="@:1.7.0")
    # non-python dependencies
    # https://instrain.readthedocs.io/en/latest/installation.html#dependencies
    # Essential dependencies
    depends_on("samtools", type=("build", "run"))
    # Optional dependencies
    depends_on("prodigal", type=("build", "run"), when="+prodigal")
