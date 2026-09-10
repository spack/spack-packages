# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPybv(PythonPackage):
    """A lightweight I/O utility for the BrainVision data format."""

    homepage = "https://github.com/bids-standard/pybv"
    pypi = "pybv/pybv-0.7.5.tar.gz"
    git = "https://github.com/bids-standard/pybv.git"

    license("BSD-3-Clause")

    version("0.7.6", sha256="518dac9bf151601c45787bf0ddcc5e37afd61033058eb734067825f8ae46d51b")
    version("0.7.5", sha256="57bb09305c1255b11dd5c6a75d0e6b3c81675cf0469d6a757b148ac332ac05d5")

    depends_on("python@3.9:", type=("build", "run"), when="@0.7.6:")
    depends_on("python@3.7:3", type=("build", "run"), when="@:0.7.5")
    depends_on("py-hatch-vcs", type="build", when="@0.7.6:")
    depends_on("py-hatchling", type="build", when="@0.7.6:")

    depends_on("py-numpy@1.18.1:", type=("build", "run"))

    # Historical dependencies
    depends_on("py-setuptools@46.4:", type="build", when="@:0.7.5")
