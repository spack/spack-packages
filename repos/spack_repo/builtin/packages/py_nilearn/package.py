# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNilearn(PythonPackage):
    """Statistical learning for neuroimaging in Python."""

    homepage = "https://nilearn.github.io/"
    pypi = "nilearn/nilearn-0.7.1.tar.gz"
    git = "https://github.com/nilearn/nilearn"

    maintainers("ChristopherChristofi")

    license("BSD")

    version("0.12.1", sha256="a08bbfae94d0fac5ba0aebbbcd864b7f91d1ef5725d1c309ce643dd64b2391b9")
    version("0.10.3", sha256="77819331314c4ca5c15c07634f69f855fafdf9add051b1882e3a600ad52757d8")
    version("0.10.1", sha256="928a364e7ed77d15d02b7f227197ea7c78f44f2fe780feb555d6d7cf9232f846")
    version("0.10.0", sha256="cc7f1068e038076527ead1bd363436f88f5e8d21e8bb57b323b30b926fc7553a")
    version("0.9.2", sha256="8da8d3835d92cd7b8a6cc92455a489d7e7f5994cf64fc71bce653e362773b9e4")
    version("0.9.0", sha256="f9c8e30adef51489910aec7724b5699de178427d3ae63873dad9b23dd321fe76")
    version("0.8.1", sha256="a0489940855130f35bbc4cac0750479a6f82025215ea7b1d778faca064219298")
    version("0.8.0", sha256="f2d3dc81005f829f3a183efa6c90d698ea6818c06264d2e3f03e805c4340febb")
    version("0.7.1", sha256="8b1409a5e1f0f6d1a1f02555c2f11115a2364f45f1e57bcb5fb3c9ea11f346fa")

    variant("plotting", default=False, description="Enable plotting functionalities")

    depends_on("python@3.9:", when="@0.11:", type=("build", "run"))
    depends_on("python@3.8:", when="@0.10.3:", type=("build", "run"))
    depends_on("python@3.7:", when="@0.10:", type=("build", "run"))
    depends_on("py-hatchling", when="@0.10.1:", type="build")
    depends_on("py-hatch-vcs", when="@0.10.1:", type="build")

    depends_on("py-joblib@1.2:", when="@0.11:", type=("build", "run"))
    depends_on("py-joblib@1:", when="@0.10:", type=("build", "run"))
    depends_on("py-joblib@0.15:", when="@0.9.1:", type=("build", "run"))
    depends_on("py-joblib@0.12:", when="@0.7:", type=("build", "run"))
    depends_on("py-lxml", when="@0.9.1:", type=("build", "run"))
    depends_on("py-nibabel@5.2:", when="@0.11:", type=("build", "run"))
    depends_on("py-nibabel@4:", when="@0.10.3:", type=("build", "run"))
    depends_on("py-nibabel@3.2:", when="@0.10:", type=("build", "run"))
    depends_on("py-nibabel@3:", when="@0.9.1:", type=("build", "run"))
    depends_on("py-nibabel@2.5:", when="@0.8:", type=("build", "run"))
    depends_on("py-nibabel@2.0.2:", type=("build", "run"))
    depends_on("py-numpy@1.22.4:", when="@0.11:", type=("build", "run"))
    depends_on("py-numpy@1.19:", when="@0.10:", type=("build", "run"))
    depends_on("py-numpy@1.18:", when="@0.9.1:", type=("build", "run"))
    depends_on("py-numpy@1.16:", when="@0.8:", type=("build", "run"))
    depends_on("py-numpy@1.11:", when="@0.5:", type=("build", "run"))
    depends_on("py-numpy@1.6.1:", type=("build", "run"))
    depends_on("py-pandas@2.2:", when="@0.11:", type=("build", "run"))
    depends_on("py-pandas@1.1.5:", when="@0.10:", type=("build", "run"))
    depends_on("py-pandas@1:", when="@0.9.1:", type=("build", "run"))
    depends_on("py-pandas@0.24.0:", when="@0.8:", type=("build", "run"))
    depends_on("py-pandas@0.18.0:", when="@0.7:", type=("build", "run"))
    depends_on("py-requests@2.25:", when="@0.10:", type=("build", "run"))
    depends_on("py-requests@2:", when="@0.7:", type=("build", "run"))
    depends_on("py-scikit-learn@1.4:", when="@0.11:", type=("build", "run"))
    depends_on("py-scikit-learn@1:", when="@0.10:", type=("build", "run"))
    depends_on("py-scikit-learn@0.22:", when="@0.9.1:", type=("build", "run"))
    depends_on("py-scikit-learn@0.21:", when="@0.8:", type=("build", "run"))
    depends_on("py-scikit-learn@0.19:", when="@0.7:", type=("build", "run"))
    depends_on("py-scipy@1.8:", when="@0.10.3:", type=("build", "run"))
    depends_on("py-scipy@1.6:", when="@0.10:", type=("build", "run"))
    depends_on("py-scipy@1.5:", when="@0.9.1:", type=("build", "run"))
    depends_on("py-scipy@1.2:", when="@0.8:", type=("build", "run"))
    depends_on("py-scipy@0.19:", when="@0.6:", type=("build", "run"))
    depends_on("py-packaging", when="@0.10.1:", type=("build", "run"))

    with when("+plotting"):
        depends_on("py-matplotlib@3.3:", when="@0.10:", type=("build", "run"))
        depends_on("py-matplotlib@3:", when="@0.9.1:", type=("build", "run"))
        depends_on("py-matplotlib@2:", when="@0.6:", type=("build", "run"))
        depends_on("py-plotly@5:", when="@0.12:", type=("build", "run"))
        depends_on("py-plotly", when="@0.10.3:", type=("build", "run"))
        depends_on("py-kaleido", when="@0.10.3:", type=("build", "run"))

    conflicts("py-setuptools-scm@9.0.0")
    conflicts("py-plotly@6.1.0")

    # Historical dependencies
    depends_on("py-setuptools", when="@:0.10.0", type="build")

    @property
    def skip_modules(self):
        modules = []

        if self.spec.satisfies("~plotting"):
            modules.append("nilearn.plotting")
            if self.spec.satisfies("@0.7:"):
                modules.append("nilearn.reporting")

        return modules
