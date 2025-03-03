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

    version("3.4.1", sha256="68daa57504ff548340e54ff117bd86c1d2f784b21e0fb2689cf3272b8937b24b")
    version("2.2.2", sha256="dbc60163b27de21076c9a30d24b5b7b6fa05141d68cf2553fa9a77bf79a29136")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/s/sentence-transformers/{0}-{1}.tar.gz"
        if version == Version("2.2.2"):
            name = "sentence-transformers"
        else:
            name = "sentence_transformers"
        return url.format(name, version.dotted)

    depends_on("py-setuptools@42:", when="@3.4.1", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("python@3.9.0:", when="@3.4.1", type=("build", "run"))
    depends_on("python@3.6.0:", type=("build", "run"))
    depends_on("py-transformers@4.41.0:4", when="@3.4.1", type=("build", "run"))
    depends_on("py-transformers@4.6.0:4", when="@2.2.2", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-torch@1.11.0:", when="@3.4.1", type=("build", "run"))
    depends_on("py-torch@1.6.0:", when="@2.2.2", type=("build", "run"))
    depends_on("py-torchvision", type=("build", "run"))
    depends_on("py-numpy", when="@2.2.2", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-nltk", when="@2.2.2", type=("build", "run"))
    depends_on("py-sentencepiece", when="@2.2.2", type=("build", "run"))
    depends_on("py-huggingface-hub@0.20.0:", when="@3.4.1", type=("build", "run"))
    depends_on("py-huggingface-hub@0.4.0:", when="@2.2.2", type=("build", "run"))
    depends_on("py-pillow", when="@3.4.1", type=("build", "run"))
