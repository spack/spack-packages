# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyDask(PythonPackage):
    """Dask is a flexible parallel computing library for analytics."""

    homepage = "https://github.com/dask/dask/"
    pypi = "dask/dask-1.1.0.tar.gz"

    maintainers("Chrismarsh")

    license("BSD-3-Clause")

    version("2026.3.0", sha256="f7d96c8274e8a900d217c1ff6ea8d1bbf0b4c2c21e74a409644498d925eb8f85")
    version("2025.7.0", sha256="c3a0d4e78882e85ea81dbc71e6459713e45676e2d17e776c2f3f19848039e4cf")
    version("2025.3.0", sha256="322834f44ebc24abeb564c56ccb817c97d6e7af6be71ad0ad96b78b51f2e0e85")
    version("2024.12.1", sha256="bac809af21c2dd7eb06827bccbfc612504f3ee6435580e548af912828f823195")
    version("2024.7.1", sha256="dbaef2d50efee841a9d981a218cfeb50392fc9a95e0403b6d680450e4f50d531")
    version("2023.4.1", sha256="9dc72ebb509f58f3fe518c12dd5a488c67123fdd66ccb0b968b34fd11e512153")
    version("2022.10.2", sha256="42cb43f601709575fa46ce09e74bea83fdd464187024f56954e09d9b428ceaab")
    version("2021.6.2", sha256="8588fcd1a42224b7cfcd2ebc8ad616734abb6b1a4517efd52d89c7dd66eb91f8")
    version("2021.4.1", sha256="195e4eeb154222ea7a1c368119b5f321ee4ec9d78531471fe0145a527f744aa8")
    version("2020.12.0", sha256="43e745afd4b464e6c0113131e430a16dce6ac42460b06e24d799093d098f7ab0")

    variant("array", default=True, description="Install requirements for dask.array")
    variant(
        "bag", default=True, when="@:2021.3.0", description="Install requirements for dask.bag"
    )
    variant("dataframe", default=True, description="Install requirements for dask.dataframe")
    variant("distributed", default=True, description="Install requirements for dask.distributed")
    variant("diagnostics", default=False, description="Install requirements for dask.diagnostics")

    variant(
        "delayed",
        default=True,
        when="@:2021.3.0",
        description="Install requirements for dask.delayed (dask.imperative)",
    )

    conflicts("~array", when="@2023.8: +dataframe", msg="From 2023.8, +dataframe requires +array")

    with default_args(type="build"):
        depends_on("py-setuptools")
        depends_on("py-setuptools@80:", when="@2026.3.0:")
        depends_on("py-setuptools@62.6:", when="@2023.4.1:")

        depends_on("py-setuptools-scm@9:", when="@2026.3.0:")

        depends_on("py-versioneer@0.29+toml", when="@2023.10.1:2025.11.0")
        depends_on("py-versioneer@0.28+toml", when="@2023.4.1:2023.10.0")

        depends_on("py-packaging@20:", when="@2022.10.2:")

    with default_args(type=("build", "run")):
        # python@3.14 breaks py-dask@:2025.7.0
        depends_on("python@:3.13", when="@:2025.12")
        depends_on("python@3.10:", when="@2024.8.1:")
        depends_on("python@3.9:", when="@2024.7.1")
        depends_on("python@3.8:", when="@:2023.4.1")

        # Common requirements
        depends_on("py-click@8.1:", when="@2023.11.0:")
        depends_on("py-click@8.0:", when="@2023.4.1:")
        depends_on("py-click@7.0:", when="@2022.10.2:")

        depends_on("py-cloudpickle@3.0.0:", when="@2024.8.1:")
        depends_on("py-cloudpickle@1.5.0:", when="@2023.4.1:")
        depends_on("py-cloudpickle@1.1.1:", when="@2021.3.1:")

        depends_on("py-fsspec@2021.09.0:", when="@2023.4.1:")
        depends_on("py-fsspec@0.6.0:", when="@2021.3.1:")

        depends_on("py-packaging@20:", when="@2022.10.2:")

        depends_on("py-partd@1.4.0:", when="@2024.7.1:")
        depends_on("py-partd@1.2.0:", when="@2023.4.0:")
        depends_on("py-partd@0.3.10:", when="@2021.3.1:")

        depends_on("py-pyyaml")
        depends_on("py-pyyaml@5.3.1:", when="@2022.10.2:")

        depends_on("py-toolz@0.12.0:", when="@2026.3.0:")
        depends_on("py-toolz@0.10.0:", when="@2023.4.1:")
        depends_on("py-toolz@0.8.2:", when="@2021.3.1:")

        depends_on("py-importlib-metadata@4.13.0:", when="@2023.4.0:2024.2")
        depends_on("py-importlib-metadata@4.13.0:", when="@2024.3.0: ^python@:3.11")

        # Requirements for dask.array
        with when("+array"):
            depends_on("py-numpy@1.24.0:", when="@2024.8.2:")
            depends_on("py-numpy@1.21.0:", when="@2023.4.0:")
            depends_on("py-numpy@1.18.0:", when="@2022.10.2:")
            depends_on("py-numpy@1.16.0:", when="@2021.3.1:")
            depends_on("py-numpy@1.15.1:", when="@2020.12.0:")
            # https://github.com/dask/dask/issues/11066
            depends_on("py-numpy@:1", when="@:2024.5.0")
            # The dependency on py-toolz is non-optional starting version 2021.3.1
            depends_on("py-toolz@0.8.2:", when="@:2021.3.0")

        # Requirements for dask.bag
        with when("+bag"):
            # The dependency on py-cloudpickle is non-optional starting version 2021.3.1
            depends_on("py-cloudpickle@0.2.2:", when="@2.13.0:2021.3.0")
            depends_on("py-cloudpickle@0.2.1:", when="@0.8.2:")

            # The dependency on py-fsspec is non-optional starting version 2021.3.1
            depends_on("py-fsspec@0.6.0:", when="@:2021.3.0")
            # The dependency on py-toolz is non-optional starting version 2021.3.1
            depends_on("py-toolz@0.8.2:", when="@:2021.3.0")
            # The dependency on py-partd is non-optional starting version 2021.3.1
            depends_on("py-partd@0.3.10:", when="@:2021.3.0")

        # Requirements for dask.dataframe
        with when("+dataframe"):
            # +dataframe stopped requiring numpy from 2023.8.0:, but now requires dask[array]
            # see the conflict() at the top of package that ensures +dataframe +array
            depends_on("py-numpy@1.21.0:", when="@2023.4.0:2023.7.0")
            depends_on("py-numpy@1.18.0:", when="@2022.10.2:")
            depends_on("py-numpy@1.16.0:", when="@2021.3.1:")
            depends_on("py-numpy@1.15.1:", when="@2020.12.0:")
            # https://github.com/dask/dask/issues/11066
            depends_on("py-numpy@:1", when="@:2023.4.0")

            depends_on("py-pandas@2.0:", when="@2024.7.1:")
            depends_on("py-pandas@1.3:", when="@2023.4.0:")
            depends_on("py-pandas@1.0:", when="@2022.10.2:")
            depends_on("py-pandas@0.25.0:", when="@2020.12.0:")

            # https://github.com/dask/dask/issues/10164
            depends_on("py-pandas@:1", when="@:2023.1")

            # starting with 2025.7 needs py-arrow
            depends_on("py-pyarrow@16.0:", when="@2026.1.0:")
            depends_on("py-pyarrow@14.0.1:", when="@2025.1.0:2025")
            with when("@2025.1.0:"):
                depends_on("arrow+parquet")

            # The dependency on py-toolz is non-optional starting version 2021.3.1
            depends_on("py-toolz@0.8.2:", when="@:2021.3.0")
            # The dependency on py-partd is non-optional starting version 2021.3.1
            depends_on("py-partd@0.3.10:", when="@:2021.3.0")
            # The dependency on py-fsspec is non-optional starting version 2021.3.1
            depends_on("py-fsspec@0.6.0:", when="@:2021.3.0")
            # Starting with version 2024.3.0, dataframe requires a separate package py-dask-expr
            depends_on("py-dask-expr@1.1", when="@2024.7.1")

        # Requirements for dask.distributed
        with when("+distributed"):
            depends_on("py-distributed@2026.3.0:", when="@2026.3.0")
            depends_on("py-distributed@2025.7.0", when="@2025.7.0")
            depends_on("py-distributed@2025.3.0", when="@2025.3.0")
            depends_on("py-distributed@2024.7.1", when="@2024.7.1")
            depends_on("py-distributed@2024.12.1", when="@2024.12.1")
            depends_on("py-distributed@2023.4.1", when="@2023.4.1")
            depends_on("py-distributed@2022.10.2", when="@2022.10.2")
            depends_on("py-distributed@2021.6.2", when="@2021.6.2")
            depends_on("py-distributed@2020.12.0:2021.8.0", when="@:2021.6.1")

        # Requirements for dask.diagnostics
        with when("+diagnostics"):
            depends_on("py-bokeh@3.1.0:", when="@2024.9.0:")
            depends_on("py-bokeh@2.4.2:2", when="@2022.10.2:2023.3")
            depends_on("py-bokeh@2.4.2:", when="@2023.4.0:")
            depends_on("py-bokeh@1.0.0:1,2.0.1:")

            depends_on("py-jinja2@2.10.3:", when="@2023.4.0:")
            depends_on("py-jinja2", when="@2022.10.2:")

        with when("+delayed"):
            # Requirements for dask.delayed
            # The dependency on py-cloudpickle is non-optional starting version 2021.3.1
            depends_on("py-cloudpickle@0.2.2:", when="@:2021.3.0")
            # The dependency on py-toolz is non-optional starting version 2021.3.1
            depends_on("py-toolz@0.8.2:", when="@:2021.3.0")

    # https://github.com/dask/dask/pull/11035
    patch("dask_dataframe_accessor.patch", when="@:2024.1.0 ^python@3.11.9:3.11")

    @property
    def import_modules(self):
        modules = ["dask", "dask.bytes"]

        if "+array" in self.spec:
            modules.append("dask.array")

        if "+bag" in self.spec:
            modules.append("dask.bag")

        if "+dataframe" in self.spec:
            modules.extend(["dask.dataframe", "dask.dataframe.tseries", "dask.dataframe.io"])

        if "+diagnostics" in self.spec:
            modules.append("dask.diagnostics")

        return modules
