# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyCurryreader(PythonPackage):
    """File reader for Compumedics Neuroscan data formats (.cdt, .dat)."""

    homepage = "https://github.com/mne-tools/curry-python-reader"
    pypi = "curryreader/curryreader-0.1.2.tar.gz"

    license("BSD-3-Clause")

    version("0.1.2", sha256="3f1f821e0e386ca7ad2a2422dcb699e3180daa153cc91d74796ccc9f1f83bf41")

    depends_on("python@3.7:", type=("build", "run"))

    with default_args(type="build"):
        depends_on("py-hatch-vcs")
        depends_on("py-hatchling")

    with default_args(type=("build", "run")):
        depends_on("py-certifi@2020.6.20:")
        depends_on("py-cycler@0.10:")
        depends_on("py-kiwisolver@1.2:")
        depends_on("py-matplotlib@3.3.2:")
        depends_on("py-numpy@1.19.2:")
        depends_on("pil@8.0.1:")
        depends_on("py-pip@21.0.1:")
        depends_on("py-pyparsing@2.4.7:")
        depends_on("py-python-dateutil@2.8.1:")
        depends_on("py-setuptools@50.3.2:")
        depends_on("py-six@1.15:")
