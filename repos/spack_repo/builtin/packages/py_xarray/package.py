# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXarray(PythonPackage):
    """N-D labeled arrays and datasets in Python"""

    homepage = "https://github.com/pydata/xarray"
    pypi = "xarray/xarray-0.9.1.tar.gz"

    # 'xarray.tests' requires 'pytest'. Leave out of 'import_modules' to avoid
    # unnecessary dependency.
    skip_modules = ["xarray.tests"]

    license("Apache-2.0")
    maintainers("Chrismarsh", "adamjstewart")

    version("2026.4.0", sha256="c4ac9a01a945d90d5b1628e2af045099a9d4943536d4f2ee3ae963c3b222d15b")
    version("2026.2.0", sha256="978b6acb018770554f8fd964af4eb02f9bcc165d4085dbb7326190d92aa74bcf")
    version("2025.7.1", sha256="2884bf5672b540fcc6ff8c20a3196bda0d78fbfb4d67398d60526e97c2faceef")
    version("2024.7.0", sha256="4cae512d121a8522d41e66d942fb06c526bc1fd32c2c181d5fe62fe65b671638")
    version("2023.7.0", sha256="dace2fdbf1b7ff185d9c1226a24bf83c2ae52f3253dbfe80e17d1162600d055c")
    version("2022.3.0", sha256="398344bf7d170477aaceff70210e11ebd69af6b156fe13978054d25c48729440")
    with default_args(deprecated=True):
        version(
            "0.18.2", sha256="5d2e72a228286fcf60f66e16876bd27629a1a70bf64822c565f16515c4d10284"
        )
        version(
            "0.17.0", sha256="9c2edad2a4e588f9117c666a4249920b9717fb75703b96998cf65fcd4f60551f"
        )
        version(
            "0.16.2", sha256="38e8439d6c91bcd5b7c0fca349daf8e0643ac68850c987262d53526e9d7d01e4"
        )
        version(
            "0.14.0", sha256="a8b93e1b0af27fa7de199a2d36933f1f5acc9854783646b0f1b37fed9b4da091"
        )
        version(
            "0.13.0", sha256="80e5746ffdebb96b997dba0430ff02d98028ef3828e6db6106cbbd6d62e32825"
        )
        version(
            "0.12.0", sha256="856fd062c55208a248ac3784cac8d3524b355585387043efc92a4188eede57f3"
        )
        version(
            "0.11.0", sha256="636964baccfca0e5d69220ac4ecb948d561addc76f47704064dcbe399e03a818"
        )
        version("0.9.1", sha256="89772ed0e23f0e71c3fb8323746374999ecbe79c113e3fadc7ae6374e6dc0525")

    variant("accel", default=False, when="@2025.7:", description="Accerlators, e.g., numba")
    variant("io", default=False, description="Build io backends")
    variant("etc", default=False, when="@2025.7:", description="Etc")
    variant("parallel", default=False, description="Build parallel backend")
    variant("viz", default=False, when="@2024.7:", description="Buid viz backends")

    with default_args(type="build"):
        depends_on("py-setuptools@77.0.3:", when="@2025.6:")
        depends_on("py-setuptools@42:", when="@0.17:")
        depends_on("py-setuptools@38.4:", when="@0.16:", type=("build", "run"))
        depends_on("py-setuptools")
        depends_on("py-setuptools-scm@8:", when="@2025.8:")
        depends_on("py-setuptools-scm@7:", when="@2023.7:")
        depends_on("py-setuptools-scm@3.4:+toml", when="@0.17:2022.3")
        depends_on("py-setuptools-scm", when="@0.15:")

        # Historical dependencies
        depends_on("py-setuptools-scm-git-archive", when="@0.17:2022.3")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:", when="@2025.7:")
        depends_on("py-numpy@1.26:", when="@2025.7:")
        depends_on("py-numpy@1.23:", when="@2024.7:")
        depends_on("py-numpy@1.21:", when="@2023.7:")
        depends_on("py-numpy@1.18:", when="@0.20:")
        depends_on("py-numpy@1.17:", when="@0.18:")
        depends_on("py-numpy@1.15:", when="@0.15:")
        depends_on("py-numpy@1.14:", when="@0.14.0")
        depends_on("py-numpy@1.12:", when="@0.11:0.13")
        depends_on("py-numpy@1.7:", when="@0.9.1")
        # https://github.com/pydata/xarray/releases/tag/v2024.06.0
        depends_on("py-numpy@:1", when="@:2024.5")
        depends_on("py-packaging@24.2:", when="@2026.4:")
        depends_on("py-packaging@24.1:", when="@2025.7:")
        depends_on("py-packaging@23.1:", when="@2024.7:")
        depends_on("py-packaging@21.3:", when="@2023.7:")
        depends_on("py-packaging@20:", when="@0.21:")
        depends_on("py-pandas@2.2:", when="@2025.7:")
        depends_on("py-pandas@2.0:2.1", when="@2024.7:")
        depends_on("py-pandas@1.4:2.1", when="@2023.7:")
        depends_on("py-pandas@1.1:", when="@0.20:")
        depends_on("py-pandas@1:", when="@0.18:")
        depends_on("py-pandas@0.25:", when="@0.15:")
        depends_on("py-pandas@0.24:", when="@0.14.0")
        depends_on("py-pandas@0.19.2:", when="@0.11:0.13")
        depends_on("py-pandas@0.15.0:", when="@0.9.1")

        # Historical dependencies
        # https://github.com/pydata/xarray/pull/5845
        depends_on("py-setuptools", when="@:0.19")

        with when("+accel"):
            depends_on("py-scipy@1.15:", when="@2026.4:")
            depends_on("py-scipy@1.13:")
            depends_on("py-bottleneck")
            depends_on("py-numbagg@0.9:", when="@2026.4:")
            depends_on("py-numbagg@0.8:")
            depends_on("py-numba@0.62:", when="@2026:")
            depends_on("py-numba@0.59:")
            depends_on("py-flox@0.10:", when="@2026.4:")
            depends_on("py-flox@0.9:")
            depends_on("py-opt-einsum")

        with when("+io"):
            depends_on("py-netcdf4@1.6:", when="@2025.7:")
            depends_on("py-netcdf4")
            depends_on("py-h5netcdf@1.5:+h5py", when="@2026.4:")
            depends_on("py-h5netcdf@1.4:", when="@2026:")
            depends_on("py-h5netcdf")
            depends_on("py-pydap")
            depends_on("py-scipy@1.15:", when="@2026.4:")
            depends_on("py-scipy@1.13:", when="@2025.7:")
            depends_on("py-scipy")
            depends_on("py-zarr@3:", when="@2026.4:")
            depends_on("py-zarr@2.18:", when="@2025.7:")
            depends_on("py-zarr")
            depends_on("py-fsspec")
            depends_on("py-cftime")
            depends_on("py-pooch")

            # Historical dependencies
            depends_on("py-rasterio", when="@:2022.3")
            depends_on("py-cfgrib", when="@:2022.3")

        with when("+etc"):
            depends_on("py-sparse@0.15:")

        with when("+parallel"):
            # xarray uses inline_array starting in v2022.6.0 which only exists
            # since dask 2021.1.0
            depends_on(
                # +delayed is :2021.3.0
                "py-dask@2022: +array+dataframe+distributed+diagnostics",
                when="@2022.6:",
            )
            depends_on(
                "py-dask@:2021 +array+dataframe+distributed+diagnostics+delayed", when="@:2022.5"
            )

        with when("+viz"):
            depends_on("py-cartopy@0.24:", when="@2026.4:")
            depends_on("py-cartopy@0.23:", when="@2025.7:")
            depends_on("py-matplotlib@3.10:", when="@2026.4:")
            depends_on("py-matplotlib@3.8:", when="@2026:")
            depends_on("py-matplotlib")
            depends_on("py-nc-time-axis")
            depends_on("py-seaborn")
