# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPymatgenCore(PythonPackage):
    """Python Materials Genomics is a robust materials analysis code that defines
    core object representations for structures and molecules with support for many
    electronic structure codes. It is currently the core analysis code powering the
    Materials Project (https://materialsproject.org). This repository is for
    pymatgen-core, which implements the core data structures and algorithms."""

    homepage = "https://pymatgen.org/"
    pypi = "pymatgen_core/pymatgen_core-2026.8.13.tar.gz"

    license("MIT")

    version("2026.8.13", sha256="b3966eab5bdb6fce83ac417e22e4bafe331f3380caef439cbb284c929cf9548c")

    depends_on("python@3.11:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-cython@0.29.23:")
        depends_on("py-setuptools@77:")
        depends_on("py-setuptools-scm@8:")

    with default_args(type=("build", "run")):
        depends_on("py-bibtexparser@1")
        depends_on("py-joblib@1.3.2:")
        depends_on("py-lxml@6.1:")
        depends_on("py-matplotlib@3.8:")
        depends_on("py-monty@2026.7.16:")
        depends_on("py-networkx@2.7:")
        depends_on("py-numpy@1.25.0:2", when="^python@:3.12")
        depends_on("py-numpy@2.1:2", when="^python@3.13:")
        depends_on("py-orjson@3.10:3")
        depends_on("py-palettable@3.3.3:")
        depends_on("py-pandas@2:")
        depends_on("py-plotly@5:")
        depends_on("py-requests@2.32.5:")
        depends_on("py-scipy@1.13:")
        depends_on("py-scipy@1.14.1:", when="platform=windows")
        depends_on("py-spglib@2.5:")
        depends_on("py-sympy@1.3:")
        depends_on("py-tabulate@0.9:")
        depends_on("py-tqdm@4.67.3:")
        depends_on("py-uncertainties@3.1:")
