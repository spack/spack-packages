# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFsspecXrootd(PythonPackage):
    """An XRootD implementation for fsspec."""

    homepage = "https://coffeateam.github.io/fsspec-xrootd/"
    pypi = "fsspec_xrootd/fsspec_xrootd-0.4.0.tar.gz"

    maintainers("wdconinc")

    license("BSD-3-Clause", checked_by="wdconinc")

    version("0.5.1", sha256="76f2b3a0cfa58e2b26c2b67cf72769169f1eed44294ca98ec0648d19e45bfd85")  # FIXME
    version("0.5.0", sha256="ab3bb3afccc0a5833281ec1bdba3ad0961842fc3c12abd03235609e810595263")  # FIXME
    version("0.4.0", sha256="d7f124430d26ab9139d33bc50fa8abfde3624db5dcaa5c18f56af9bf17f16f13")

    depends_on("python@3.9:", type=("build", "run"), when="@0.5:")
    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-setuptools@42:", type="build")
    depends_on("py-setuptools-scm@3.4:+toml", type="build")

    depends_on("py-fsspec", type=("build", "run"))
