# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPeakutils(PythonPackage):
    """Peak detection utilities for 1D data."""

    homepage = "https://bitbucket.org/lucashnegri/peakutils"
    pypi = "peakutils/peakutils-1.3.5.tar.gz"

    license("MIT")

    version("1.3.5", sha256="4ff2e7f3330b93024fe8da1ee04e00389e26bcb2ef79bd2f9cf86ccd4962e114")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
