# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PySentenceTransformers(PythonPackage):
    """This framework provides an easy method to compute dense vector representations
    for sentences, paragraphs, and images. The models are based on transformer
    networks like BERT / RoBERTa / XLM-RoBERTa etc. and achieve state-of-the-art
    performance in various task. Text is embedding in vector space such that similar
    text is close and can efficiently be found using cosine similarity."""

    homepage = "https://github.com/UKPLab/sentence-transformers"
    pypi = "sentence-transformers/sentence-transformers-2.2.2.tar.gz"

    maintainers("meyersbs")

    version("2.2.2", sha256="dbc60163b27de21076c9a30d24b5b7b6fa05141d68cf2553fa9a77bf79a29136")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.6.0:", type=("build", "run"))
    depends_on("py-transformers@4.6.0:4", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-torch@1.6.0:", type=("build", "run"))
    depends_on("py-torchvision", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-nltk", type=("build", "run"))
    depends_on("py-sentencepiece", type=("build", "run"))
    depends_on("py-huggingface-hub@0.4.0:", type=("build", "run"))
