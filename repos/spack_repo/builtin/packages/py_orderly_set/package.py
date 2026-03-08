# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyOrderlySet(PythonPackage):
    """Orderly Set is a package containing multiple implementations of
    Ordered Set."""

    homepage = "https://github.com/seperman/orderly-set"
    pypi = "orderly_set/orderly_set-5.2.3.tar.gz"

    license("MIT", checked_by="wdconinc")

    version("5.5.0", sha256="e87185c8e4d8afa64e7f8160ee2c542a475b738bc891dc3f58102e654125e6ce")
    version("5.4.1", sha256="a1fb5a4fdc5e234e9e8d8e5c1bbdbc4540f4dfe50d12bf17c8bc5dbf1c9c878d")
    version("5.3.2", sha256="5fd6d917788d0e2196582f38a1c4b74591963d4df9be24ae5a51ba4cea2c987f")
    version("5.2.3", sha256="571ed97c5a5fca7ddeb6b2d26c19aca896b0ed91f334d9c109edd2f265fb3017")
    version("5.2.2", sha256="52a18b86aaf3f5d5a498bbdb27bf3253a4e5c57ab38e5b7a56fa00115cd28448")
    version("5.2.1", sha256="2adab28582db06f3fec29eaf1b31cc55358d2d9471a54e89a285cfa194258328")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build", when="@:5.4")
    depends_on("py-flit-core@3.2:3", type="build", when="@5.5:")
