# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDaskMl(PythonPackage):
    """Scalable Machine Learning with Dask."""

    homepage = "https://ml.dask.org/"
    pypi = "dask-ml/dask-ml-1.8.0.tar.gz"

    license("BSD-3-Clause")

    version("2025.1.0", sha256="b31caeb5f603f9537ffa34bd247e0e1fcefda7c007631260f8abdee49f89b1e1")
    version("1.8.0", sha256="8fc4ac3ec1915e382fb8cae9ff1ec9b5ac1bee0b6f4c6975d6e6cb7191a4a815")

    variant("docs", default=False, description="Build HTML documentation", when="@:2024.3.20")
    variant("xgboost", default=False, description="Deploys XGBoost alongside Dask")

    depends_on("python@3.10:", when="@2025.1.0:", type=("build", "run"))
    depends_on("python@3.6:", type=("build", "run"))

    depends_on("py-hatchling", when="@2024.4.1:", type="build")
    depends_on("py-hatch-vcs", when="@2024.4.1:", type="build")
    depends_on("py-setuptools", when="@:2024.3.20", type="build")
    depends_on("py-setuptools-scm", when="@:2024.3.20", type="build")
    depends_on("gmake", type="build")

    depends_on("py-dask+array+dataframe@2025.1.0:", when="@2025.1.0:", type=("build", "run"))
    depends_on("py-dask+array+dataframe@2.4.0:", type=("build", "run"))
    depends_on("py-distributed@2025.1.0:", when="@2025.1.0:", type=("build", "run"))
    depends_on("py-distributed@2.4.0:", type=("build", "run"))
    depends_on("py-numba@0.51:", when="@1.9:", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-numpy@1.24:", when="@2025.1.0:", type=("build", "run"))
    # np.float removed in numpy@1.24
    depends_on("py-numpy@1.17.3:1.23", when="@1.8.0", type=("build", "run"))
    depends_on("py-pandas@2:", when="@2025.1.0:", type=("build", "run"))
    depends_on("py-pandas@0.24.2:", type=("build", "run"))
    depends_on("py-scikit-learn@1.6.1:", when="@2025.1.0:", type=("build", "run"))
    # if_delegate_has_method() method used in dask-ml@1.8.0 has been removed in scikit-learn@1.3
    # _check_param_grid() method used in dask-ml@1.8.0 has been removed in scikit-lean@1.1
    depends_on("py-scikit-learn@0.23:1.0", when="@1.8.0", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-dask-glm@0.2.0:", type=("build", "run"))
    depends_on("py-multipledispatch@0.4.9:", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))

    with when("+docs"):
        depends_on("py-nbsphinx", type=("build", "run"))
        depends_on("py-numpydoc", type=("build", "run"))
        depends_on("py-sphinx", type=("build", "run"))
        depends_on("py-sphinx-rtd-theme", type=("build", "run"))
        depends_on("py-sphinx-gallery", type=("build", "run"))
        # Some more dependencies in ci/environment-docs.yaml
        depends_on("py-graphviz", type=("build", "run"))
        depends_on("py-heapdict", type=("build", "run"))
        depends_on("py-ipykernel", type=("build", "run"))
        depends_on("py-ipython", type=("build", "run"))
        depends_on("py-nose", type=("build", "run"))
        depends_on("py-sortedcontainers", type=("build", "run"))
        depends_on("py-testpath", type=("build", "run"))
        depends_on("py-tornado", type=("build", "run"))
        depends_on("py-zict", type=("build", "run"))
        depends_on("py-dask-sphinx-theme@1.1.0:", type=("build", "run"))

    depends_on("py-xgboost+dask", type=("build", "run"), when="+docs")
    depends_on("py-xgboost+dask", type=("build", "run"), when="+xgboost")

    patch("xgboost_dependency_v2024.3.20.patch", when="@2024.3.20:")
    patch("xgboost_dependency.patch", when="@:2023.3.24")

    conflicts("+docs", when="target=aarch64: %gcc")

    def url_for_version(self, version):
        url = "https://files.pythonhosted.org/packages/source/d/dask-ml/dask{0}ml-{1}.tar.gz"
        if version > Version("2024.4.3"):
            sep = "_"
        else:
            sep = "-"
        return url.format(sep, version)

    @run_after("install")
    def install_docs(self):
        if "+docs" in self.spec:
            with working_dir("docs"):
                make("html")
            install_tree("docs", self.prefix.docs)
