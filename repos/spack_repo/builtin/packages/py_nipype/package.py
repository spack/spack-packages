# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNipype(PythonPackage):
    """Neuroimaging in Python: Pipelines and Interfaces."""

    homepage = "https://github.com/nipy/nipype"
    pypi = "nipype/nipype-1.6.0.tar.gz"

    license("Apache-2.0")

    version("1.11.0", sha256="6707ec4c3cf8e1983aef7f8eea79627ee7b7ab4aa49649991550e129c165b7a7")
    version("1.10.0", sha256="19e5d6cefa70997198f78bc665ef4d3d3cb53325b5b98a72e51aefadaf6b3e0e")
    version("1.8.6", sha256="977b1315e8f70f94163ec07e31e5571be83f2add6023141c5a06ac700126f8d1")
    version("1.8.5", sha256="e3842743fb660464dd29de73dcfc9ef66d273be10bcc64059ff21cd5ef1e9655")
    version("1.7.0", sha256="e689fe2e5049598c9cd3708e8df1cac732fa1a88696f283e3bc0a70fecb8ab51")
    version("1.6.1", sha256="8428cfc633d8e3b8c5650e241e9eedcf637b7969bcd40f3423334d4c6b0992b5")
    version("1.6.0", sha256="bc56ce63f74c9a9a23c6edeaf77631377e8ad2bea928c898cc89527a47f101cf")
    version("1.4.2", sha256="069dcbb0217f13af6ee5a7f1e58424b9061290a3e10d7027d73bf44e26f820db")

    depends_on("python@3.10:", type=("build", "run"), when="@1.11:")
    depends_on("python@3.9:", type=("build", "run"), when="@1.9:")
    depends_on("python@3.7:", type=("build", "run"), when="@1.8:")

    with default_args(type="build"):
        depends_on("py-hatchling", when="@1.11:")
        depends_on("py-hatch-vcs", when="@1.11:")

        # Historical dependencies
        depends_on("py-setuptools@30.3:", when="@1.7.1:1.10")
        depends_on("py-setuptools", when="@:1.10")

    # dependencies are listed in nipype/info.py
    with default_args(type=("build", "run")):
        depends_on("py-click@6.6:")
        depends_on("py-networkx@2.5:", when="@1.9.1:")
        depends_on("py-networkx@2:", when="@1.6:")
        depends_on("py-networkx@1.9:")
        depends_on("py-nibabel@3:", when="@1.9.1:")
        depends_on("py-nibabel@2.1:")
        depends_on("py-numpy@1.21:", when="@1.9.1:")
        depends_on("py-numpy@1.17:", when="@1.8:")
        depends_on("py-numpy@1.15.3:", when="^python@3.7:")
        depends_on("py-packaging@21:", when="@1.11:")
        depends_on("py-packaging")
        depends_on("py-prov@1.5.2:")
        depends_on("py-pydot@1.2.3:")
        depends_on("py-python-dateutil@2.2:")
        depends_on("py-rdflib@5:", when="@1.5:")
        depends_on("py-scipy@1.8:", when="@1.9.1:")
        depends_on("py-scipy@0.14:")
        depends_on("py-simplejson@3.8:")
        depends_on("py-traits@6.2:", when="@1.9.1:")
        depends_on("py-traits@4.6:4,5.1:6.3", when="@1.8.4")
        depends_on("py-traits@4.6:4,5.1:", when="@:1.8.3")
        depends_on("py-filelock@3:")
        depends_on("py-acres@0.3:", when="@1.11:")
        depends_on("py-acres", when="@1.9.1:")
        depends_on("py-etelemetry@0.3.1:", when="@1.9.1:")
        depends_on("py-etelemetry@0.2:", when="@1.5:")
        depends_on("py-etelemetry")
        depends_on("py-looseversion@1.0.1:", when="@1.11:")
        depends_on("py-looseversion", when="@1.8.1:")
        depends_on("py-lxml@4.9.1:", when="@1.11:")
        depends_on("py-puremagic@1.15:", when="@1.11:")
        depends_on("py-puremagic", when="@1.9:")

        # Historical dependencies
        depends_on("py-pydotplus", when="@:1.5")

    conflicts("py-looseversion@1.2")

    skip_modules = ["nipype.sphinxext.apidoc"]
