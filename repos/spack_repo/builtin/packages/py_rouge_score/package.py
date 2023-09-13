# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyRougeScore(PythonPackage):
    """This is a native python implementation of ROUGE, designed to replicate
    results from the original perl package."""

    homepage = "https://github.com/google-research/google-research/tree/master/rouge"
    pypi = "rouge_score/rouge_score-0.1.2.tar.gz"

    maintainers("meyersbs")

    version("0.1.2", sha256="c7d4da2683e68c9abf0135ef915d63a46643666f848e558a1b9f7ead17ff0f04")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-absl-py", type=("build", "run"))
    depends_on("py-nltk", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-six@1.14.0:", type=("build", "run"))
