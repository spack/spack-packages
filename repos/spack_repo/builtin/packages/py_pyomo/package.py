# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyomo(PythonPackage):
    """Pyomo is a Python-based open-source software package that supports a
    diverse set of optimization capabilities for formulating and analyzing
    optimization models."""

    homepage = "https://www.pyomo.org/"
    pypi = "pyomo/pyomo-5.6.6.tar.gz"
    git = "https://github.com/Pyomo/pyomo.git"

    # Maintainer accurate as of 2026-02-20
    maintainers("mrmundt")

    license("BSD-3-Clause")

    version("6.10.0", sha256="672fac375e57e121ca935adcc16a1cd118be8afa1a3e5608161fb86220c3a577")
    version("6.9.5", sha256="0734020fcd5cc03ee200fd3f79d143fbfc14e6be116e0d16bab79f3f89609879")
    version("6.9.4", sha256="34ad22cd6bf9956de9c0d3842d01c1f92dee0515b25aa3e8f113b326549b1231")
    version("6.9.3", sha256="54ec698bb31f78460e1627cbfa90cb2741b629c1ecaca7035bd2e340351a47f7")
    version("6.9.2", sha256="81b2b14ea619244824e1c547cc12602fe9a6e19309cbf0742868c5b1ef37cb35")
    version("6.9.1", sha256="ccb85fa4b03450c32614a939c6830d073a7ce79461b12b0f1e7809db96ae86de")
    version("6.9.0", sha256="622323c9d24de09db9fb491847a9c371be24efa1cc2f38da4782e11850ec1e7d")
    version("6.8.2", sha256="40d8f7b216ad1602bb254f4296591608dd94fe2c961dc1e63ca6b84fb397bed6")
    version("6.8.1", sha256="dc3369193a915d6fa9a59382f1c02c17f6bf540584f641b9bd20d1f1a7f8ba8c")
    version("6.8.0", sha256="a204a78d8ed5fa7ad8fa94d3c8ed4f6da38b5c02a68b8fe446bc694f16c8d1ea")
    version("6.7.3", sha256="b7f0441c405af4f42f38527ae38826a5c0a4984dd7bea1fe07172789d8594770")
    version("6.7.2", sha256="53bef766854f7607ca1fcfe3f218594ab382f137a275cee3d925d2b2f96876bf")
    version("6.7.1", sha256="735b66c45937f1caa43f073d8218a4918b6de658914a699397d38d5b8c219a40")
    version("6.7.0", sha256="a245ec609ef2fd907269f0b8e0923f74d5bf868b2ec0e62bf2a30b3f253bd17b")
    version("6.6.2", sha256="c8ad55213ff8b1a2c4e469110db8079722d5a6f364c6c46a42e2f750fc9e4d26")
    version("6.6.1", sha256="3fb0aba7b0f4120e6ce0f242502c0e61478d61e326bc90b7dc392bbefd114b34")
    version("6.6.0", sha256="8766c08041b8d91fbc5166d220c9e723fed6057d18be1178bae3b6583376c65e")
    version("6.5.0", sha256="5a23e775bba9fdbad22698fa1a841e662482edc979f2dea41cc6c54b1bb4b968")
    version("6.4.4", sha256="922dd8e6e3e421550acf884bd27f74cab2fe6552cdde36715d116b0c8345c367")
    version("6.4.3", sha256="7f3f67f61a6e5c2dd9c4dd930356d3176bad1572f1abee780592e725d6445288")
    version("6.4.2", sha256="6f5a867e77bdd6ac2ba0da5d4a251e38543ae05eba5a0c5cf8ab39e7fa8e1ea9")
    version("6.4.1", sha256="a636a3a1c8314b8be85899cb6fac5d6a9a78fc75c6d58b74d3ec106ae5ed8f59")
    version("6.4.0", sha256="b548825301b6bd4073a0620a8265d956153d53c12fca37cc7184fa54fce96222")
    version("6.3.0", sha256="b4df6305438a2b6ec75bd2e1588b919feb97089ed179a944b334432723781f81")
    version("6.2", sha256="89bc69a9a0afe10f5d229abe508b04ebbd3d2e213aa6c8ec2db2562798fa0400")
    version("6.1.2", sha256="f2a58977c3c72e706aef7ab7d016bdf66df85df8ea5b25cc0ba387e2cef880bb")
    version("6.1.1", sha256="32f378fda748ff299b4492b12b04ed1d8b11c857117fa0e5e6b609aa322fcade")
    version("6.1", sha256="7d087b186a43b2ffd032bc4db87cdbcf2fdc187607211f3e6cdc0f54b6f516f4")
    version("6.0.1", sha256="4b27bc917b12a6011e7eb3442a54619f0f42f1087d4defa14b903dd985fdbe7c")
    version("6.0", sha256="3dbfb1c7a8ef76dfd99d82c211845cdba9bf31a179269b57b6b28ad635ae34f9")
    version("5.7.3", sha256="2c4697107477a1b9cc9dad534d8f9c2dc6ee397c47ad44113e257732b83cfc8f")
    version("5.7.2", sha256="f10ada18ade84b16225dc519ef1788dd6d5f22cb22d0ea44db64c96d14cb7bb0")
    version("5.7.1", sha256="1228204d7eb4cdd217fed6323a7434de68e89a2aaa74085ea47f1b42fb64d8cd")
    version("5.7", sha256="27e3a3c8411de9bc52e5e6aa88e9a0de0dd7369126bc905996e23057775905d7")

    variant("cython", default=False, description="Enable cythonization of Pyomo.")
    variant("tests", default=False, description="Install testing dependencies.", when="@6.1:")
    variant(
        "docs", default=False, description="Install docs generation dependencies.", when="@6.1:"
    )
    variant("optional", default=False, description="Install optional dependencies.", when="@6.1:")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    ############################
    # UPDATE THESE AS REQUIRED
    ############################

    # python_requires
    depends_on("python@3.10:3.14", when="@6.10", type=("build", "run"))
    depends_on("python@3.9:3.14", when="@6.9.5", type=("build", "run"))
    depends_on("python@3.9:3.13", when="@6.9", type=("build", "run"))
    depends_on("python@3.8:3.13", when="@6.8.1:6.8.2", type=("build", "run"))
    depends_on("python@3.8:3.12", when="@6.7:6.8.0", type=("build", "run"))
    depends_on("python@3.7:3.11", when="@6.4:6.6", type=("build", "run"))
    depends_on("python@3.6:3.10", when="@6.3", type=("build", "run"))
    depends_on("python@3.6:3.9", when="@6.0:6.2", type=("build", "run"))
    depends_on("python@2.7:2.8,3.4:3.9", when="@5.7", type=("build", "run"))

    # universally required
    depends_on("py-setuptools@77:", type="build")
    # ply was removed as a required dependency in 6.10.0
    depends_on("py-ply", when="@:6.9.5", type=("build", "run"))

    # required for pre-6 series
    depends_on("py-pyutilib@6.0.0", when="@5", type=("build", "run"))
    depends_on("py-six@1.4:", when="@5", type=("build", "run"))
    depends_on("py-appdirs", when="@5.6:5.7.0", type=("build", "run"))

    # when cython is requested
    depends_on("py-cython", when="+cython", type="build")

    # when tests is requested
    depends_on("py-coverage", when="@6.1:+tests", type=("run"))
    depends_on("py-nose", when="@6.1:6.2+tests", type=("run"))
    depends_on("py-parameterized", when="@6.1:+tests", type=("run"))
    depends_on("py-pybind11", when="@6.1:+tests", type=("run"))
    depends_on("py-pytest", when="@6.3:+tests", type=("run"))
    depends_on("py-pytest-parallel", when="@6.3:+tests", type=("run"))

    # when docs is requested
    depends_on("py-sphinx@3:", when="@:6.6+docs", type=("run"))
    depends_on("py-sphinx@5:8.1,8.2.1:", when="@6.7:+docs", type=("run"))
    depends_on("py-sphinx-copybutton", when="@6.1:+docs", type=("run"))
    depends_on("py-sphinx-rtd-theme@0.6:", when="@6.1:+docs", type=("run"))
    depends_on("py-sphinxcontrib-jsmath", when="@6.1:+docs", type=("run"))
    depends_on("py-sphinxcontrib-napoleon", when="@6.1:+docs", type=("run"))
    depends_on("py-sphinx-toolbox@2.16:", when="@6.7.1:6.9.2+docs", type=("run"))
    depends_on("py-sphinx-jinja2-compat@0.1.1:", when="@6.7.1:6.9.2+docs", type=("run"))
    depends_on("py-enum-tools", when="@6.7.1:6.8.0+docs", type=("run"))
    depends_on("py-numpy@1", when="@6.1:6.7+docs", type=("run"))
    depends_on("py-numpy", when="@6.8:+docs", type=("run"))
    depends_on("py-scipy", when="@6.4.2:+docs", type=("run"))

    # when optional is requested
    depends_on("py-dill", when="@6.1:+optional", type=("run"))
    depends_on("py-ipython", when="@6.1:+optional", type=("run"))
    depends_on("py-linear-tree", when="@6.8:+optional ^python@:3.13", type=("run"))
    depends_on("py-matplotlib@:3.6.0,3.6.2:", when="@6.1:+optional", type=("run"))
    depends_on("py-networkx", when="@6.1:+optional", type=("run"))
    depends_on("py-numpy@1", when="@6.1:6.7+optional", type=("run"))
    depends_on("py-numpy", when="@6.8:+optional", type=("run"))
    depends_on("py-openpyxl", when="@6.1:+optional", type=("run"))
    depends_on("py-pint", when="@6.1:+optional", type=("run"))
    depends_on("py-plotly", when="@6.6:+optional", type=("run"))
    depends_on("py-python-louvain", when="@6.1:+optional", type=("run"))
    depends_on("py-pyyaml", when="@6.1:+optional", type=("run"))
    depends_on("py-qtconsole", when="@6.7.1:+optional", type=("run"))
    depends_on("py-scikit-learn@:1.7", when="@6.8:+optional", type=("run"))
    depends_on("py-scipy", when="@6.1:+optional", type=("run"))
    depends_on("py-sympy", when="@6.1:+optional", type=("run"))
    depends_on("py-xlrd", when="@6.1:+optional", type=("run"))
    depends_on("py-z3-solver", when="@6.1:+optional", type=("run"))
    depends_on("py-pywin32", when="@6.1:+optional platform=windows", type=("run"))
    depends_on("py-casadi", when="@6.1:+optional", type=("run"))
    depends_on("py-numdifftools", when="@6.1:+optional", type=("run"))
    depends_on("py-pandas", when="@6.1:+optional", type=("run"))
    depends_on("py-seaborn", when="@6.1:+optional", type=("run"))

    @when("^py-pip@23.1:")
    def config_settings(self, spec, prefix):
        if "+cython" in self.spec:
            return {"--global-option": "--with-cython"}
        return {}

    @when("^py-pip@:23.0")
    def global_options(self, spec, prefix):
        options = []
        if "+cython" in self.spec:
            options.append("--with-cython")
        return options
