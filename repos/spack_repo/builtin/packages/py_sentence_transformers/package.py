# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySentenceTransformers(PythonPackage):
    """This framework provides an easy method to compute dense vector representations
    for sentences, paragraphs, and images. The models are based on transformer
    networks like BERT / RoBERTa / XLM-RoBERTa etc. and achieve state-of-the-art
    performance in various task. Text is embedding in vector space such that similar
    text is close and can efficiently be found using cosine similarity."""

    homepage = "https://github.com/UKPLab/sentence-transformers"
    pypi = "sentence-transformers/sentence_transformers-5.1.2.tar.gz"

    maintainers("meyersbs")

    license("Apache-2.0")

    version("5.1.2", sha256="0f6c8bd916a78dc65b366feb8d22fd885efdb37432e7630020d113233af2b856")
    version("3.4.1", sha256="68daa57504ff548340e54ff117bd86c1d2f784b21e0fb2689cf3272b8937b24b")
    version("2.2.2", sha256="dbc60163b27de21076c9a30d24b5b7b6fa05141d68cf2553fa9a77bf79a29136")

    def url_for_version(self, version):
        url = (
            "https://files.pythonhosted.org/packages/source/s/sentence-transformers/{0}-{1}.tar.gz"
        )
        if version == Version("2.2.2"):
            name = "sentence-transformers"
        else:
            name = "sentence_transformers"
        return url.format(name, version.dotted)

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.9:", when="@3.4.1:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@42:", when="@3.4.1:", type="build")

    depends_on("py-transformers@4.6:4", when="@2.2.2", type=("build", "run"))
    depends_on("py-transformers@4.41:4", when="@3.4.1:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-torch@1.6:", when="@2.2.2", type=("build", "run"))
    depends_on("py-torch@1.11:", when="@3.4.1:", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-huggingface-hub@0.4:", when="@2.2.2", type=("build", "run"))
    depends_on("py-huggingface-hub@0.20:", when="@3.4.1:", type=("build", "run"))
    depends_on("pil", when="@3.4.1:", type=("build", "run"))
    depends_on("py-typing-extensions@4.5:", when="@5.1.2:", type=("build", "run"))

    # Historical
    depends_on("py-sentencepiece", when="@2.2.2", type=("build", "run"))
    depends_on("py-torchvision", when="@2.2.2", type=("build", "run"))
    depends_on("py-numpy", when="@2.2.2", type=("build", "run"))
    depends_on("py-nltk", when="@2.2.2", type=("build", "run"))
