# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyXxhash(PythonPackage):
    """xxhash is a Python binding for the xxHash library by
    Yann Collet."""

    homepage = "https://github.com/ifduyue/python-xxhash"
    pypi = "xxhash/xxhash-2.0.2.tar.gz"

    license("BSD-2-Clause")

    version("3.6.0", sha256="f0162a78b13a0d7617b2845b90c763339d1f1d82bb04a4b07f4ab535cc5e05d6")
    version("3.5.0", sha256="84f2caddf951c9cbf8dc2e22a89d4ccf5d86391ac6418fe81e3c67d0cf60b45f")
    version("3.4.1", sha256="0379d6cf1ff987cd421609a264ce025e74f346e3e145dd106c0cc2e3ec3f99a9")
    version("3.3.0", sha256="c3f9e322b1ebeebd44e3d9d2d9b124e0c550c1ef41bd552afdcdd719516ee41a")
    version("3.2.0", sha256="1afd47af8955c5db730f630ad53ae798cf7fae0acb64cebb3cf94d35c47dd088")
    version("2.0.2", sha256="b7bead8cf6210eadf9cecf356e17af794f57c0939a3d420a00d87ea652f87b49")

    depends_on("c", type="build")  # generated

    depends_on("python@2.6:2,3.3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@45:", type="build", when="@3.2.0:")
    depends_on("py-setuptools-scm@6.2:", type="build", when="@3.2.0:")
    depends_on("xxhash@0.8:")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        env.set("XXHASH_LINK_SO", "1")
