# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPymatgen(PythonPackage):
    """Python Materials Genomics is a robust materials analysis code that
    defines core object representations for structures and molecules with
    support for many electronic structure codes. It is currently the core
    analysis code powering the Materials Project."""

    homepage = "http://www.pymatgen.org/"
    pypi = "pymatgen/pymatgen-4.7.2.tar.gz"
    git = "https://github.com/materialsproject/pymatgen.git"

    license("MIT")

    version("2026.9.24", sha256="eaefbf34e4bc0546543a1e7502efef1d96bce5ef26d882c302caa3fee4469f00")
    version("2022.9.8", sha256="2250e05b81af3313bc0fc70cb558c2f528ed4eefb32d943ed9bd7a9756f03652")
    version("2021.3.9", sha256="a6f22d69133a48b7801bfd5e6a2878b47b4b4b2ef1a377b87c6c573be14cbf16")
    version(
        "2020.12.31", sha256="5002490facd47c55d2dae42c35712e061c1f5d881180485c0543a899589856d6"
    )

    with default_args(type="build"):
        depends_on("py-cython@0.29.23:", when="@2022.1.7:")
        # https://github.com/materialsproject/pymatgen/commit/29b5b909e109cb04d4b118d0de5b3929819b9378
        depends_on("py-cython@:2", when="@:2023.7.16")

        depends_on("py-setuptools@77:", when="@2026.9.23:")
        depends_on("py-setuptools@43:")
        depends_on("py-setuptools-scm@8:", when="@2026.9.23:")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:", when="@2026.2.24:")
        depends_on("python@3.8:", when="@2022.1.8:")
        # to prevent: 'PyThreadState' {aka 'struct _ts'} has no member named
        # 'use_tracing'; did you mean 'tracing'?
        depends_on("python@:3.9", when="@:2021.3.9")

        depends_on("py-pymatgen-core@2026.9.23:", when="@2026.9.23:")

        # Historical dependencies
        with when("@:2022.9.8"):
            depends_on("py-numpy@1.20.1:", when="@2021.1.1:")
            depends_on("py-numpy@1.9:")
            depends_on("py-requests")
            depends_on("py-ruamel-yaml@0.17:", when="@2022.4.26:")
            depends_on("py-ruamel-yaml@0.15.6:", when="@2021.1.1:")
            depends_on("py-monty@3.0.2:", when="@2021.1.1:")
            depends_on("py-monty@0.9.6:")
            depends_on("py-scipy@1.5.0:", when="@2021.1.1:")
            depends_on("py-scipy@0.14:")
            depends_on("py-tabulate")
            depends_on("py-spglib@1.9.9.44:", when="@2021.1.1:")
            depends_on("py-spglib@1.9.8.7:")
            depends_on("py-networkx@2.2:", when="@2021.1.1:")
            depends_on("py-matplotlib@1.5:")
            depends_on("py-palettable@3.1.1:", when="@2021.1.1:")
            depends_on("py-palettable@2.1.1:")
            depends_on("py-sympy", when="@2021.1.1:")
            depends_on("py-pandas", when="@2021.1.1:")
            depends_on("py-plotly@4.5.0:", when="@2021.1.1:")
            depends_on("py-uncertainties@3.1.4:", when="@2021.1.1:")
            depends_on("py-pybtex", when="@2022.1.9:")
            depends_on("py-tqdm", when="@2022.1.9:")
