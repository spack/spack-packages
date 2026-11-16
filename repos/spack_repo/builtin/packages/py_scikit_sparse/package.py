# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScikitSparse(PythonPackage):
    """Sparse matrix tools extending scipy.sparse, but with incompatible licenses"""

    homepage = "https://github.com/scikit-sparse/scikit-sparse"
    pypi = "scikit-sparse/scikit_sparse-0.4.16.tar.gz"
    git = "https://github.com/scikit-sparse/scikit-sparse.git"

    maintainers("cgcgcg")

    license("BSD-2-Clause")

    version("0.5.1", sha256="4adece3f378ac9185d17ba93482ea19ba87e55b1088d385f0c24bca8984afc08")
    version("0.4.16", sha256="3baf49ac98ae8cc4357005af49a0df93a6a53f4e61708705da2942ea4fa61a56")
    version("0.4.12", sha256="e6502fea9ba561cfa5491eb222ed2c81c16263d8182a293950db20509c941166")
    version("0.4.11", sha256="64c61a8777b7c7ba8e1f2bf76bc767f740e6426f1cce2d90f1324b177618e1ca")
    version("0.4.8", sha256="2a224c60da3ef951975242ea777478583d3265efc72db5cfb7861686521a4009")

    depends_on("c", type="build")

    depends_on("python@3.10:", when="@0.5:", type=("build", "link", "run"))
    depends_on("python@3.6:3.11", when="@0.4.11:0.4.12", type=("build", "link", "run"))
    depends_on("python@3.6:3.10", when="@0.4.8", type=("build", "link", "run"))
    depends_on("py-setuptools@61:", when="@0.5:", type="build")
    depends_on("py-setuptools@40.8:", type="build")
    depends_on("py-cython@3:", when="@0.5:", type="build")
    depends_on("py-cython@0.22:", when="@0.4.12:", type="build")
    depends_on("py-cython@0.22:0.29", when="@:0.4.11", type="build")
    depends_on("py-numpy@2:", when="@0.4.15:", type=("build", "link", "run"))
    depends_on("py-numpy@1.13.3:", type=("build", "link", "run"))
    # https://github.com/scikit-sparse/scikit-sparse/issues/120
    depends_on("py-numpy@:1", when="@:0.4.12", type=("build", "link", "run"))
    depends_on("py-scipy@1.14:", when="@0.5:", type="run")
    depends_on("py-scipy@0.19:", type="run")
    depends_on("py-packaging", when="@0.5:", type="run")
    depends_on("suite-sparse", type=("build", "link", "run"))

    import_modules = ["sksparse"]

    def url_for_version(self, version):
        # the source distribution is named scikit_sparse from 0.4.15 on
        name = "scikit_sparse" if version >= Version("0.4.15") else "scikit-sparse"
        url = "https://files.pythonhosted.org/packages/source/s/scikit-sparse/{0}-{1}.tar.gz"
        return url.format(name, version)

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        # setup.py looks here before the directories of conda, homebrew and the system
        suitesparse = self.spec["suite-sparse"]
        env.set("SUITESPARSE_INCLUDE_DIR", suitesparse.headers.directories[0])
        env.set("SUITESPARSE_LIBRARY_DIR", suitesparse.libs.directories[0])

    def test_cholesky(self):
        """factorize a sparse matrix with CHOLMOD and solve a system"""
        code = (
            "import numpy as np, scipy.sparse as sp, sksparse.cholmod as cholmod\n"
            "A = sp.diags([-1.0, 2.5, -1.0], [-1, 0, 1], shape=(100, 100), format='csc')\n"
            "b = np.ones(100)\n"
            "if hasattr(cholmod, 'cho_factor'):\n"  # the interface of 0.5
            "    x = cholmod.cho_factor(A).solve(b)\n"
            "else:\n"
            "    x = cholmod.cholesky(A)(b)\n"
            "assert np.allclose(A @ x, b)\n"
        )
        python = self.module.python
        python("-c", code)
