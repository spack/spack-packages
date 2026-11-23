# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyLazyImporter(PythonPackage):
    """A context manager for portable, opt-in lazy imports."""

    homepage = "https://github.com/pganssle/lazy_importer"
    pypi = "lazy_importer/lazy_importer-0.1.0.tar.gz"

    license("Apache-2.0")

    version("0.1.0", sha256="b2e296716ce015c0cd80e57b940e52727c5b934b34b8656d5ce06bdd0ee5fbdd")

    with default_args(type="build"):
        depends_on("py-flit-core@3.12:3")

    with default_args(type=("build", "run")):
        depends_on("python@3.11:")
