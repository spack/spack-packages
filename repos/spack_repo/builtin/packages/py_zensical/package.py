# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyZensical(PythonPackage):
    """Zensical is a modern static site generator designed to simplify building
    and maintaining project documentation. It's built by the creators of Material
    for MkDocs and shares the same core design principles and philosophy –
    batteries included, easy to use, with powerful customization options."""

    homepage = "https://zensical.org"
    pypi = "zensical/zensical-0.0.29.tar.gz"

    license("MIT", checked_by="abhishek1297")

    version("0.0.29", sha256="0d6282be7cb551e12d5806badf5e94c54a5e2f2cf07057a3e36d1eaf97c33ada")

    # build-only dependencies
    depends_on("py-maturin@1.8:1", type="build")

    # build and runtime dependencies
    with default_args(type=("build", "run")):
        depends_on("python@3.10:")
        depends_on("py-click@8.1.8:")
        depends_on("py-deepmerge@2.0:")
        depends_on("py-markdown@3.7:")
        depends_on("py-pygments@2.16:")
        depends_on("py-pymdown-extensions@10.15:")
        depends_on("py-pyyaml@6.0.2:")
        # tomli only needed on Python < 3.11
        # (stdlib tomllib covers 3.11+)
        depends_on("py-tomli@2.0:", when="^python@:3.10")
