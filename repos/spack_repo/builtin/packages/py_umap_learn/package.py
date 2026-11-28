# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyUmapLearn(PythonPackage):
    """Uniform Manifold Approximation and Projection (UMAP) is a dimension
    reduction technique that can be used for visualisation similarly to t-SNE,
    but also for general non-linear dimension reduction."""

    homepage = "https://github.com/lmcinnes/umap"
    pypi = "umap-learn/umap_learn-0.6.0.tar.gz"

    license("BSD-3-Clause")

    version("0.6.0", sha256="2f56945fdf8470efc12dc79c91d8a091a33d1e03ea3251d76e019da8e3617c38")
    version(
        "0.5.3",
        sha256="dbd57cb181c2b66d238acb5635697526bf24c798082daed0cf9b87f6a3a6c0c7",
        url="https://files.pythonhosted.org/packages/source/u/umap-learn/umap-learn-0.5.3.tar.gz",
    )

    depends_on("py-setuptools@61:", type="build", when="@0.6:")
    depends_on("py-setuptools", type="build")
    # up to 0.5.4 umap imports pkg_resources, which setuptools 82 removed
    depends_on("py-setuptools@:81", type=("build", "run"), when="@:0.5.4")
    depends_on("python@3.10:", type=("build", "run"), when="@0.6:")
    depends_on("py-numpy@2:", type=("build", "run"), when="@0.6:")
    depends_on("py-numpy@1.17:", type=("build", "run"))
    depends_on("py-scikit-learn@1.6:", type=("build", "run"), when="@0.6:")
    depends_on("py-scikit-learn@0.22:", type=("build", "run"))
    depends_on("py-scipy@1.13:", type=("build", "run"), when="@0.6:")
    depends_on("py-scipy@1.0:", type=("build", "run"))
    depends_on("py-numba@0.60:", type=("build", "run"), when="@0.6:")
    depends_on("py-numba@0.49:", type=("build", "run"))
    depends_on("py-pynndescent@0.7:", type=("build", "run"), when="@0.6:")
    depends_on("py-pynndescent@0.5:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
