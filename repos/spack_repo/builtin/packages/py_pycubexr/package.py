# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPycubexr(PythonPackage):
    """pyCubexR is a Python package for reading the Cube4 file format."""

    homepage = "https://github.com/extra-p/pycubexr"
    pypi = "pycubexr/pycubexr-2.0.0.tar.gz"

    license("BSD-3-Clause")

    maintainers("pearzt")

    version("2.1.0", sha256="c09ea0d3a13465f38ce1302eb980f8e0cd1293f9d1dc5d21eb5bd47c19f8fe0d")
    version("2.0.1", sha256="699643c076b603fb1140564da6c4589b73ec9efd3b9112cd3d957f5bee646915")
    version("2.0.0", sha256="03504fbbc9cbd514943e8aeb57919ad49731fe264bdbab86711bf10851276924")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.18:2", type=("build", "run"))
