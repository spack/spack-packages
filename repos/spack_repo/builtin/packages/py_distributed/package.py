# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDistributed(PythonPackage):
    """Distributed scheduler for Dask"""

    homepage = "https://distributed.dask.org/"
    pypi = "distributed/distributed-2.10.0.tar.gz"

    # 'distributed.dashboard.components' requires 'bokeh', but 'bokeh' is not listed as
    # a dependency. Leave out of 'import_modules' list to avoid unnecessary dependency.
    import_modules = [
        "distributed",
        "distributed.deploy",
        "distributed.comm",
        "distributed.comm.tests",
        "distributed.protocol",
        "distributed.cli",
        "distributed.dashboard",
        "distributed.http",
        "distributed.http.tests",
        "distributed.http.scheduler",
        "distributed.http.scheduler.prometheus",
        "distributed.http.worker",
        "distributed.diagnostics",
    ]

    license("BSD-3-Clause")

    version("2026.3.0", sha256="4a8fc6102fededfbaae45288501276da2297a054d74eb6589f01b087c7f95c26")
    version("2025.7.0", sha256="5f8ec20d3cdfb286452831c6f9ebee84527e9323256c20dd2938d9c6e62c5c18")
    version("2025.3.0", sha256="84a68c91db2a106c752ca7845fba8cd92ad4f3545c0fb2d9b6dec0f44b225539")
    version("2024.12.1", sha256="438aa3ae48bfac9c2bb2ad03f9d47899286f9cb3db8a627b3b8c0de9e26f53dd")
    version("2024.7.1", sha256="7bce7fa745163b55bdd67fd632b3edf57b31827640390b92d0ee3f73436429d3")
    version("2023.4.1", sha256="0140376338efdcf8db1d03f7c1fdbb5eab2a337b03e955d927c116824ee94ac5")
    version("2022.10.2", sha256="53f0a5bf6efab9a5ab3345cd913f6d3f3d4ea444ee2edbea331c7fef96fd67d0")
    version("2022.2.1", sha256="fb62a75af8ef33bbe1aa80a68c01a33a93c1cd5a332dd017ab44955bf7ecf65b")
    version("2021.6.2", sha256="d7d112a86ab049dcefa3b21fd1baea4212a2c03d22c24bd55ad38d21a7f5d148")
    version("2021.4.1", sha256="4c1b189ec5aeaf770c473f730f4a3660dc655601abd22899e8a0662303662168")
    version("2020.12.0", sha256="2a0b6acc921cd4e0143a7c4383cdcbed7defbc4bd9dc3aab0c7f1c45f14f80e1")

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-setuptools@80:", when="@2026.3.0:")
        depends_on("py-setuptools@62.6:", when="@2023.4.1:")

        depends_on("py-setuptools-scm@9:", when="@2026.3.0:")

        depends_on("py-versioneer@0.29: +toml", when="@2023.10.1:2026.3.0")
        depends_on("py-versioneer@0.28: +toml", when="@2023.4.1:2023.10.0")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@2024.8.1:")
        # https://github.com/dask/distributed/pull/6605
        depends_on("python@:3.11", when="@:2022.6.0")
        depends_on("python@3.8:", when="@2022.2.1:")

        # In Spack py-dask+distributed depends on py-distributed, not the other way around.
        # Hence, no need for depends_on("py-dask", ...)
        depends_on("py-click@8.0:", when="@2023.4.1:")
        depends_on("py-click@6.6:")

        depends_on("py-cloudpickle@3.0.0:", when="@2024.8.2:")
        depends_on("py-cloudpickle@1.5.0:")

        depends_on("py-jinja2", when="@2022.2.1:")
        depends_on("py-jinja2@2.10.3:", when="@2023.4.1:")

        depends_on("py-locket@1:", when="@2022.2.1:")

        depends_on("py-msgpack@1.0.2:", when="@2024.8.1:")
        depends_on("py-msgpack@1.0.0:", when="@2023.4.1:")
        depends_on("py-msgpack@0.6.0:")

        depends_on("py-packaging@20.0:", when="@2022.2.1:")

        depends_on("py-psutil@5.8.0:", when="@2024.8.1:")
        depends_on("py-psutil@5.7.2:", when="@2024.7.1:")
        depends_on("py-psutil@5.7.0:", when="@2023.4.1:")
        depends_on("py-psutil@5.0:")

        depends_on("py-pyyaml")
        depends_on("py-pyyaml@5.4.1:", when="@2024.8.1:")
        depends_on("py-pyyaml@5.3.1:", when="@2023.4.1:")

        depends_on("py-sortedcontainers@2.0.5:", when="@2023.4.1:")
        depends_on("py-sortedcontainers@:1,2.0.2:")

        depends_on("py-tblib@1.6:")
        depends_on("py-tblib@1.6:3.1,3.2.2:", when="@2026.3.0")

        depends_on("py-toolz@0.12.0:", when="@2026.3.0")
        depends_on("py-toolz@0.11.2:", when="@2024.8.1:")
        # Note that the setup.py is wrong for py-toolz, when="@2022.10.2".
        # See https://github.com/dask/distributed/pull/7309
        depends_on("py-toolz@0.10.0:", when="@2022.10.2:")
        depends_on("py-toolz@0.8.2:")

        depends_on("py-tornado@6.2.0:", when="@2024.8.1:")
        depends_on("py-tornado@6.0.4:", when="@2024.7.1:")
        depends_on("py-tornado@6.0.3:6.1", when="@2022.10.2")
        depends_on("py-tornado@6.0.3:", when="^python@3.8:")
        depends_on("py-tornado@5:", when="^python@:3.7")

        depends_on("py-urllib3@1.26.5:", when="@2025.7.0:")
        depends_on("py-urllib3@1.24.3:", when="@2023.4.1:")
        depends_on("py-urllib3", when="@2022.10.2:")

        depends_on("py-zict@3.0.0:", when="@2024.7.1:")
        depends_on("py-zict@2.2.0:", when="@2023.4.1:")
        depends_on("py-zict@0.1.3:")

    def patch(self):
        if self.spec.satisfies("@:2023.3"):
            filter_file("^dask .*", "", "requirements.txt")
