# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyHstspreload(PythonPackage):
    """Chromium HSTS Preload list as a Python package and updated daily"""

    homepage = "https://github.com/sethmlarson/hstspreload"
    pypi = "hstspreload/hstspreload-2020.9.23.tar.gz"

    license("BSD-3-Clause")

    version("2025.1.1", sha256="346552a807b3a1762376de8ecce097544e7fcd64fb64231b4652da52f86fa6f1")
    version("2020.9.23", sha256="35822733ba67cfb4efc6cd7d1230b509f0bd42c90eeb329faf2fe679f801e40f")

    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
