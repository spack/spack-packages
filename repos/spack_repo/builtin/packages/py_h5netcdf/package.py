# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyH5netcdf(PythonPackage):
    """A Python interface for the netCDF4 file-format that reads and writes local or
    remote HDF5 files directly via h5py or h5pyd, without relying on the Unidata netCDF
    library."""

    homepage = "https://github.com/h5netcdf/h5netcdf"
    pypi = "h5netcdf/h5netcdf-0.10.0.tar.gz"

    license("BSD-3-Clause")

    version("1.8.1", sha256="9b396a4cc346050fc1a4df8523bc1853681ec3544e0449027ae397cb953c7a16")
    version("1.6.1", sha256="7ef4ecd811374d94d29ac5e7f7db71ff59b55ef8eeefbe4ccc2c316853d31894")
    version("1.3.0", sha256="a171c027daeb34b24c24a3b6304195b8eabbb6f10c748256ed3cfe19806383cf")
    version("0.10.0", sha256="fc1cfec33bb9f730c412f87fcbc259167fd7620635679ccfc6e31971730dbd60")

    variant("h5py", default=False, description="Use h5py backend", when="@1.8:")

    with default_args(type="build"):
        depends_on("py-setuptools@42:", when="@1.3:", type="build")
        depends_on("py-setuptools", type="build")
        depends_on("py-setuptools-scm@7:+toml", when="@1.3:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-packaging", when="@1.3:")
        depends_on("py-numpy", when="@1.8.1:")
        depends_on("py-h5py", when="+h5py")
        depends_on("py-h5py", when="@:1.7")
